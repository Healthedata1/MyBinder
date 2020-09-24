example_organization_2 = {
  "resourceType" : "Organization",
  "id" : "example-organization-2",
  "meta" : {
    "profile" : [
      "http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization"
    ]
  },
  "identifier" : [
    {
      "system" : "http://hl7.org.fhir/sid/us-npi",
      "value" : "1407071236"
    },
    {
      "system" : "http://example.org/fhir/sid/us-tin",
      "value" : "121111111"
    }
  ],
  "active" : True,
  "type" : [
    {
      "coding" : [
        {
          "system" : "http://terminology.hl7.org/CodeSystem/organization-type",
          "code" : "prov",
          "display" : "Healthcare Provider"
        }
      ]
    }
  ],
  "name" : "Acme Clinic",
  "telecom" : [
    {
      "system" : "phone",
      "value" : "(+1) 734-677-7777"
    },
    {
      "system" : "email",
      "value" : "customer-service@acme-clinic.org"
    }
  ],
  "address" : [
    {
      "line" : [
        "3300 Washtenaw Avenue, Suite 227"
      ],
      "city" : "Amherst",
      "state" : "MA",
      "postalCode" : "01002",
      "country" : "USA"
    }
  ]
}

leung = {
  "resourceType": "Practitioner",
  "id": "argo-pl-leung",
  "meta": {
    "profile": [
      "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner"
    ]
  },
  "identifier": [
    {
      "system": "http://hl7.org.fhir/sid/us-npi",
      "value": "9941339108"
    },
    {
      "system": "http://www.example.org/fhir/identifiers",
      "value": "25456"
    }
  ],
  "name": [
    {
      "family": "Leung",
      "given": [
        "Alan"
      ],
      "prefix": [
        "Dr"
      ]
    }
  ]
}

jones = {
  "resourceType": "Practitioner",
  "id": "argo-pl-smith",
  "meta": {
    "profile": [
      "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner"
    ]
  },
  "identifier": [
    {
      "system": "http://hl7.org.fhir/sid/us-npi",
      "value": "9941339108"
    },
    {
      "system": "http://www.example.org/fhir/identifiers",
      "value": "25456"
    }
  ],
  "name": [
    {
      "family": "Leung",
      "given": [
        "Alan"
      ],
      "prefix": [
        "Dr"
      ]
    }
  ]
}

st_helena = {
  "resourceType": "Location",
  "id": "argo-pl-st-helena",
  "meta": {
    "profile": [
      "http://hl7.org/fhir/us/core/StructureDefinition/us-core-location"
    ]
  },
  "identifier": [
    {
      "system": "http://example.org/fhir/identifiers",
      "value": "30"
    }
  ],
  "status": "active",
  "name": "St Helena Hospital",
  "description": "St Helena Hospital",
  "telecom": [
    {
      "system": "phone",
      "value": "(+1) 707-555-5555"
    }
  ],
  "address": {
    "line": [
      "100 Woodland Rd"
    ],
    "city": "St Helena",
    "state": "CA",
    "postalCode": "94575",
    "country": "USA"
  },
  "managingOrganization": {
    "display": "St Joseph's Healthcare"
  }
}

queen = {
  "resourceType": "Location",
  "id": "argo-pl-queen",
  "meta": {
    "profile": [
      "http://hl7.org/fhir/us/core/StructureDefinition/us-core-location"
    ]
  },
  "identifier": [
    {
      "system": "http://example.org/fhir/identifiers",
      "value": "29"
    }
  ],
  "status": "active",
  "name": "Queen of the Valley Hospital",
  "description": "Queen of the Valley Hospital",
  "telecom": [
    {
      "system": "phone",
      "value": "(+1) 707-555-5555"
    }
  ],
  "address": {
    "line": [
      "100 Soscol"
    ],
    "city": "Napa",
    "state": "CA",
    "postalCode": "94559",
    "country": "USA"
  },
  "managingOrganization": {
    "display": "St Joseph's Healthcare"
  }
}

patient_template = {
  "resourceType": "Patient",
  "id": "my_id",
  "meta": {
    "profile": [
      "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"
    ]
  },
  "extension": [
    {
      "extension": [
        {
          "url": "ombCategory",
          "valueCoding": {
            "system": "urn:oid:2.16.840.1.113883.6.238",
            "code": "2028-9",
            "display": "Asian"
          }
        },
        {
          "url": "text",
          "valueString": "Asian"
        }
      ],
      "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race"
    },
    {
      "extension": [
        {
          "url": "ombCategory",
          "valueCoding": {
            "system": "urn:oid:2.16.840.1.113883.6.238",
            "code": "2186-5",
            "display": "Not Hispanic or Latino"
          }
        },
        {
          "url": "text",
          "valueString": "Not Hispanic or Latino"
        }
      ],
      "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity"
    },
    {
      "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
      "valueCode": "M"
    }
  ],
  "identifier": [
    {
      "use": "usual",
      "type": {
        "coding": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
            "code": "MR",
            "display": "Medical Record Number"
          }
        ],
        "text": "Medical Record Number"
      },
      "system": "http://hospital.smarthealthit.org",
      "value": "my_identifier"
    }
  ],
  "active": True,
  "name": [
    {
      "family": "my_lname",
      "given": [
        "my_fname"
      ]
    }
  ],
  "telecom": [
    {
      "system": "phone",
      "value": "555-555-5555",
      "use": "home"
    }
  ],
  "gender": "my_gender",
  "birthDate": "my_dob",
  "address": [
    {
      "line": [
        "49 Meadow St"
      ],
      "city": "Mounds",
      "state": "OK",
      "postalCode": "74047",
      "country": "US"
    }
  ]
}

careteam_template = {
  "resourceType": "CareTeam",
  "id": "proctology",
  "meta": {
    "profile": [
      "http://hl7.org/fhir/us/core/StructureDefinition/us-core-careteam"
    ]
  },
  "status": "active",
  "name": "Argo PL proctology",
  "subject": {
    "reference": "Patient/example"
  },
  "participant": [
    {
      "role": [
        {
          "coding": {
            "display": "Proctology"
          }
        }
      ],
      "member": {
        "display": "Ronald Bone, MD"
      }
    },
    {
      "role": {
        "display": "Urology"
      },
      "member": {
        "display": "Kathy Fielding, MD"
      }
    },
    {
      "role": [
        {
          "coding": {
            "display": "Proctology"
          }
        }
      ],
      "member": {
        "display": "Viet Chu, MD"
      }
    }
  ]
}


if __name__ == "__main__":
    print(example_organization_2)
    print(patient_template)
    print(st_helena)
    print(queen)
    print(careteam_template)
    print(leung)
    print(jones)
