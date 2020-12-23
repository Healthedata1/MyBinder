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
    "lastUpdated": "2020-12-22T21:43:46-08:00",
    "source": "Health_eData_Inc",
    "versionId": "1",
    "tag": [
      {
        "code": "2020-Sep"
      },
      {
        "code": "2021-Jan"
      }
    ]
  },
  "questionnaire": "http://www.fhir.org/guides/argonaut/patient-list/Questionniare/argo-pl-q2",
  "status": "completed",
  "subject": {
    "reference": "Patient/12345",
    "display": "Patient Name"
  },
  "authored": "2020-09-25T00:11:54.322Z",
  "item": [
    {
      "linkId": "q1",
      "text": "COVID Contact",
      "answer": [
        {
          "valueBoolean": False
        }
      ]
    },
    {
      "linkId": "q2",
      "text": "Age/Legal Sex",
      "answer": [
        {
          "valueString": "56/Male"
        }
      ]
    },
    {
      "linkId": "q3",
      "text": "SAPS II Score",
      "answer": [
        {
          "valueInteger": 80
        }
      ]
    },
    {
      "linkId": "q4",
      "text": "SAPS II Score change",
      "answer": [
        {
          "valueInteger": 12
        }
      ]
    },
    {
      "linkId": "q5",
      "text": "SOFA Score",
      "answer": [
        {
          "valueInteger": 12
        }
      ]
    },
    {
      "linkId": "q6",
      "text": "Unit",
      "answer": [
        {
          "valueString": "ICU"
        }
      ]
    }
  ]
}

appt_template = {
  "resourceType" : "Appointment",
  "id" : "pl-appt",
  "status" : "booked",
  "serviceType" : [
    {
      "coding" : [
        {
          "system" : "http://fhir.org/guides/argonaut-scheduling/CodeSystem/visit-type",
          "code" : "117",
          "display" : "Emergency Medical"
        }
      ],
      "text" : "Emergency Medical"
    }
  ],
  "specialty" : [
    {
      "coding" : [
        {
          "system" : "http://snomed.info/sct",
          "code" : "408478003",
          "display" : "Critical care medicine"
        }
      ],
      "text" : "Critical care medicine"
    }
  ],
  "appointmentType" : {
    "coding" : [
      {
        "system" : "http://terminology.hl7.org/CodeSystem/v2-0276",
        "code" : "EMERGENCY"
      }
    ],
    "text" : "Routine"
  },
  "start" : "2020-12-21T14:30:00-08:00",
  "end" : "2020-12-21T15:00:00-08:00",
  "participant" : [
        {
      "actor" : {
        "display" : "Patient X"
      },
      "required" : "required",
      "status" : "accepted"
    },
    {
      "actor" : {
        "display" : "Dr Y"
      },
      "required" : "required",
      "status" : "accepted"
    },
    {
      "actor" : {
        "display" : "Napa Office"
      },
      "required" : "required",
      "status" : "accepted"
    }
  ]
}
my_q = {'id': 'argo-pl-q2',
 'meta': {'lastUpdated': '2020-05-20T15:46:00.964+00:00',
  'source': '#eddpbEX0FzlvCJ4u',
  'versionId': '1',
  'profile': ['http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire'],
  'tag': [{'code': '2020-Sep'}, {'code': '2021-Jan'}]},
 'date': '2016-04-14',
 'item': [{'linkId': 'q1',
   'repeats': False,
   'required': False,
   'text': 'COVID Contact',
   'type': 'boolean'},
  {'linkId': 'q2',
   'repeats': False,
   'required': True,
   'text': 'Age/Legal Sex',
   'type': 'string'},
  {'linkId': 'q3',
   'repeats': False,
   'required': False,
   'text': 'SAPS II Score',
   'type': 'integer'},
  {'linkId': 'q4',
   'repeats': False,
   'required': False,
   'text': 'SAPS II Score change',
   'type': 'integer'},
  {'linkId': 'q5',
   'repeats': False,
   'required': False,
   'text': 'SOFA Score',
   'type': 'integer'},
  {'linkId': 'q6',
   'repeats': False,
   'required': False,
   'text': 'Unit',
   'type': 'string'}],
 'name': 'Patient-List-columns',
 'status': 'draft',
 'subjectType': ['Patient'],
 'title': 'Patient List columns',
 'url': 'Questionnaire/patient-list-columns',
 'resourceType': 'Questionnaire'}