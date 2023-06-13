# selfdescriptions

All self-descriptions required for the Federated Catalogue in Marispace-X are collected here. The self-descriptions are in a draft phase and are steadily evaluated, updated and extended during the Marispace-X project

The self-descriptions are sorted into the following folders according to the respective entity (see Figure 1)  
- Participants (e.g., legal persons, companies, ...)
- Services (e.g., platform, software, infrastructure, ...)
- Resources (e.g., data, sensor devices, infrastructure, ...)
- Sensors (e.g., multibeam, ctd, camera, ...)

Resources and Sensors are separated into different entities in Marispace-X due to the complexity and large amount of different sensor types that exist (see Figure 1). Resource self-descriptions like "dataResource", "geoDataResource" are general self-descriptions of geospatial data resources. These self-descriptions make the data resource findable and accessible as they can be searched by geolocation, time, sensor type, theme. The Sensors like "multibeam", "ctd", "camera" are more detailed self-descriptions of sensor data. These self-descriptions make the data interoperable and reusable as they contain attributes about sensor characteristics, sensor settings, and processing information. Technically, Sensors should be implemented as a child of a geoDataResource (using the "aggregationOf" attribute from the Gaia-X ontologies).

![alt TEST](figures/Marispace-X-Concept_self_descriptions.jpg)
*Figure 1: Concept for self-descriptions of different entities in the federated catalogue in Marispace-X*

Each self-description can have the three following data files.
- SHACL (template of the self-description that can be filled out using the SD Creation Wizard - https://sd-creation-wizard.gxfs.dev/)
- JSON-LD (self-description file created from the SHACL template using the SD Creation Wizard)
- verified JSON-LD (the self-description needs to be verified, "wrapped" into a verifiable paragraph)

First SHACL files need to be created for each self-description required in Marispace-X. These SHACL files are based on existing standards/ontologies as good as possible.

The current concept is a follows:
- general resource self-description "geoDataResource.ttl" (based on GeoDCAT-AP ontologie - https://semiceu.github.io/GeoDCAT-AP/drafts/latest/) - "GeoDCAT-AP provides an RDF vocabulary and the corresponding RDF syntax binding for the union of metadata elements of the core profile of ISO 19115:2003 and those defined in the framework of the INSPIRE Directive."
  - general sensor information self-description "sensorGeneralInformation.ttl" (based on MMI Device Ontology - https://mmisw.org/ont/mmi/device) - "Generic sensor attributes like sensor name, sensor manufacturer, sensor id, point of contact, ..."
    - detialed sensor information self-description with the file naming convention "sensor*.ttl" where * is replaced with the sensor name, e.g., "sensorSideScanSonar", "sensorCTD", "sensorCamera", "sensorSatelliteRadar" (this can be based on very specific ontologies for the respectivce sensor type, e.g., OGC SSN - https://www.w3.org/TR/vocab-ssn/, OGC EO - https://docs.ogc.org/is/10-157r4/10-157r4.html) - "Detailed sensor-specific attributes like sensor settings, sensor properties, ..."
