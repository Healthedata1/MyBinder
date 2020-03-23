#!/usr/bin/env python
# coding: utf-8

# ## Function to create PyFHIR Class instances
# 
# - use hs_model in local Jupyter folder 
# - function parameters for PyFHIR
#     - input is resource(or datatype) instance as key value pairs
#     - requires 'ResourceType' parameter for fhir ResourceType
#     - optionally 'BackboneElement' parameter for instantiating BackboneElement
#     - optionally other resource elements as parameters
#     - output is fhirclient class instance

# In[17]:


from importlib import import_module


# In[18]:


def pyfhir(ResourceType, BackboneElement=None, **kwargs):
    '''
    input is resource(or datatype) instance as key value pairs
    requires 'ResourceType' parameter for fhir ResourceType
    optionally 'BackboneElement' parameter for instantiating BackboneElement
    optionally other resource elements as parameters
    output is fhirclient class instance
    '''
    try:
        MyClass = getattr(import_module(
        f"fhir_model_generator.model.{ResourceType.lower()}"),BackboneElement
        )
    except TypeError:
            MyClass = getattr(import_module(
        f"fhir_model_generator.model.{ResourceType.lower()}"),ResourceType
        )    
    # Instantiate the class (pass arguments to the constructor, if needed)
    instance = MyClass(dict(kwargs), strict=False)
    return(instance)


# ### Some examples...

# In[22]:


def main():
    py_res1 = pyfhir(
    ResourceType ='Bundle',
    type = 'message',
    foo = 'bar',
    BackboneElement = 'BundleEntry'
    )
    
    py_res2 = pyfhir(
    ResourceType ='CodeableConcept',
    text = 'example',
    foo = 'bar',
    coding = [
        pyfhir(ResourceType ='Coding',
                    code = 'foo',
                    system = 'bar',
                   ).as_json()
             ],
       )
    
    [py_res1.as_json(),py_res2.as_json()]


# In[23]:


if __name__== "__main__":
  main()

