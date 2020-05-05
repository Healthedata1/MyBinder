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