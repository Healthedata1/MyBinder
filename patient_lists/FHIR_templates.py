example_org = {
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

qr_template = {
  "resourceType": "QuestionnaireResponse",
  "meta": {
    "source": "Health_eData_Inc",
    "tag": [
      {
        "code": "2020-Sep"
      },
      {
        "code": "lformsVersion: 25.1.2"
      }
    ]
  },
  "questionnaire": "http://registry.fhir.org/argonaut/Questionniare/argo-pl-q1",
  "status": "completed",
  "subject": {
    "reference": "Patient/12345",
    "display": "Patient Name"
  },
  "authored": "2020-09-25T00:11:54.322Z",
  "item": [
    {
      "linkId": "dob",
      "text": "DOB",
      "answer": [
        {
          "valueString": "6/19/1964"
        }
      ]
    },
    {
      "linkId": "sex",
      "text": "Sex",
      "answer": [
        {
          "valueString": "M"
        }
      ]
    },
    {
      "linkId": "admit-date",
      "text": "Admission Datejson",
      "answer": [
        {
          "valueString": "09/24/2020"
        }
      ]
    },
    {
      "linkId": "rel-encounter-id",
      "text": "elated Encounter (e.g. admission Enounter) as id only",
      "answer": [
        {
          "valueString": "1234"
        }
      ]
    },
    {
      "linkId": "rel-encounter-ref",
      "text": "Related Encounter (e.g. admission Enounter) as FHIR reference",
      "answer": [
        {
          "valueReference": {
            "reference": "Encounter/foo",
            "display": "Related Encounter (e.g. admission Enounter) as FHIR reference"
          }
        }
      ]
    },
    {
      "linkId": "rel-encounter-uri",
      "text": "Related Encounter (e.g. admission Encounter) as uri",
      "answer": [
        {
          "valueUri": "http://example.org/data/1234"
        }
      ]
    }
  ]
}
