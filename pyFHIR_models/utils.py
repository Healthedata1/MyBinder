#!/usr/bin/env python
# coding: utf-8

# ## Transaction Bundler utility
# 
# - inputs = resource as pyfhir model to append to bundle and existing bundle as pyfhir model to append to.
# 

# In[29]:


from fhir_model_generator.model import bundle, organization
from datetime import datetime, date, timedelta
import uuid
import FHIR_templates as f
from json import dumps
from requests import get, put, post
from IPython.display import display, HTML, Markdown



def to_json(r):
    return(dumps(r.as_json(), indent=2))


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
                timestamp = datetime.now().isoformat(),
                entry = [],
            )
        )
    fhir_bundle.entry.append(e)
    return(fhir_bundle)


# In[43]:

def validate_me(r_fhir): 
    '''
    input a fhir resource as dict and validate using a reference server
    '''
    
    # ref_server = 'http://test.fhir.org/r4'
    ref_server ='http://hapi.fhir.org/baseR4'
    headers = {
        'Accept':'application/fhir+json',
        'Content-Type':'application/fhir+json'
        }
    params = dict(
          )
    print('validating ...')
    r = post(f'{ref_server}/{r_fhir["resourceType"]}/$validate', params=params, headers=headers, data=dumps(r_fhir))
    try:
        display(HTML(
            '<h1>Validation output</h1>'
            f'<h3>Status Code = {r.status_code}</h3><br />'
            f'<h4>Response</h4><br />'
            f'{r.json()["text"]["div"]}'
            ))

    except KeyError:
        display(HTML(
            '<h1>Validation output</h1>'
            f'<h3>Status Code = {r.status_code}</h3><br />'
            f'<h4>Response</h4><br />'
            f'<pre>{dumps(r.json(),indent=4)}</pre>'
            ))  


if __name__ == "__main__": 
    org = organization.Organization(f.example_org)
    tbundle = bundle_me(org)
    print(dumps(tbundle.as_json(),indent=2))
 






