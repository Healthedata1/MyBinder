#!/usr/bin/env python
# coding: utf-8

# ## Transaction Bundler utility
# 
# - inputs = resource as pyfhir model to append to bundle and existing bundle as pyfhir model to append to.
# 

# In[29]:
import os, sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
# This allows you to import the desired function from the module hierarchy:
from pyFHIR_models.fhir_model_generator.model import bundle, organization
from datetime import datetime, date, timedelta
import uuid
import FHIR_templates as f
from json import dumps
from yaml import dump as y_dump
from requests import get, post, put
from IPython.display import display as Display, HTML, Markdown

headers = {
    'Accept':'application/fhir+json',
    'Content-Type':'application/fhir+json'
    }

def to_json(r):
    return(dumps(r.as_json(), indent=2))

def to_yaml(r):
    '''serialize defaultdict, dict or pyfhir object to yaml'''
    try:
        r_dict = dict(r.as_json())
    except AttributeError:
        try:
            r_dict = dict(r)
        except TypeError:
            r_dict = r
    return(y_dump(r_dict, sort_keys=False))

def get_id(ref):
    '''get id from FHIR Reference or URN for pyfhir or dict'''
    try:
        return(ref.reference.split(':')[-1].split('/')[-1])
    except AttributeError:
        return(ref['reference'].split(':')[-1].split('/')[-1])


def bundle_me(fhir_server, pyfhir_res, fhir_bundle=None):
    file_ts = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    if not pyfhir_res.id:
        new_urn = uuid.uuid1().urn # new urn for resource
        pyfhir_res.id = new_urn[9:]
    e = bundle.BundleEntry()
    e.fullUrl = f'{fhir_server}/{pyfhir_res.id}'
    e.resource = pyfhir_res
    e.request = bundle.BundleEntryRequest()
    #e.request.method = 'POST'
    e.request.method = 'PUT'
    e.request.url = f'{pyfhir_res.resource_type}/{pyfhir_res.id}'
    if fhir_bundle: #add entry
        pass
    else:  # create transaction bundle
        bundle_type = 'transaction'
        bundle_id = f'transaction-bundle-{file_ts}'   
        fhir_bundle = bundle.Bundle(
            dict(
                id = bundle_id,
                type = bundle_type,
                timestamp = f'{datetime.now().isoformat()}Z',
                entry = [],
            )
        )
    fhir_bundle.entry.append(e)
    return(fhir_bundle)

def validate(pyfhir_data):
    #val_server = 'http://test.fhir.org/r4'
    val_server = 'http://hapi.fhir.org/baseR4'
    params = dict(
      # profile = 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient' # The official URL for this profile is: http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient
        )
    r = post(f'{val_server}/{pyfhir_data.resource_type}/$validate', params = params, headers = headers, data = to_json(pyfhir_data))
    return r

def load_transaction(pyfhir_data):   
    '''PUT FHIR transaction bundle to test_server as json object'''
    #test_server = 'http://test.fhir.org/r4'
    test_server = 'http://hapi.fhir.org/baseR4'  
    display(HTML(f'&#9203...POSTing transaction bundle to {test_server}... ')) 
    params = dict(
      # profile = 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient' # The official URL for this profile is: http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient
        )  
    r = post(f'{test_server}', params = params, headers = headers, data = to_json(pyfhir_data))
    return r 

def fetch_r(type, id):
    '''Fetch resource and return dict'''
    #test_server = 'http://test.fhir.org/r4'
    test_server = 'http://hapi.fhir.org/baseR4'  
    display(HTML(f'&#9203...GETting {type} resource with id = {id} from {test_server}... ')) 
    params = dict(
      # profile = 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient' # The official URL for this profile is: http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient
        )  
    r = get(f'{test_server}/{type}/{id}', params = params, headers = headers)
    if r.status_code < 300:
        return r.json()
    else:
        display(HTML(f'{r.status_code}...{test_server}/{type}/{id} not found... '))


# In[43]:


if __name__ == "__main__": 
    test_server = 'http://test.fhir.org/r4'
    org = organization.Organization(f.example_org)
    tbundle = bundle_me(test_server,org)
    print(dumps(tbundle.as_json(),indent=2))
    print(to_json(org))
    print(to_yaml(org))
 






