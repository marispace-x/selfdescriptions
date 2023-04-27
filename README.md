# selfdescriptions

All self-descriptions required for the Federated Catalogue in Marispace-X are collected here. The self-descriptions are in a draft phase and are steadily evaluated, updated and extended during the Marispace-X project

The self-descriptions are sorted into the following folders according to the respective entity  
- Participants (e.g., legal persons, companies, ...)
- Services (e.g., platform, software, infrastructure, ...)
- Resources (e.g., data, sensor devices, infrastructure, ...)
- Sensors (e.g., multibeam, ctd, camera, ...)

Resources and Sensors are separated into different entities in Marispace-X due to the complexity and large amount of different sensor types that exist. Resource self-descriptions like "dataResource", "geoDataResource" are general self-descriptions of geospatial data resources. These self-descriptions make the data resource findable and accessible as they can be searched by geolocation, time, sensor type, theme. The Sensors like "multibeam", "ctd", "camera" are more detailed self-descriptions of sensor data. These self-descriptions make the data interoperable and reusable as they contain attributes about sensor characteristics, sensor settings, and processing information. Technically, Sensors should be implemented as a child of a geoDataResource.

Each self-description has the three following data files.
- SHACL (template of the self-description that can be filled out using the SD Creation Wizard - https://sd-creation-wizard.gxfs.dev/)
- JSON-LD (self-description file created from the SHACL template using the SD Creation Wizard)
- verified JSON-LD (the self-description needs to be verified, "wrapped" into a verifiable paragraph)

First SHACL files need to be created for each self-description required in Marispace-X. These SHACL files are based on existing standards/ontologies as good as possible.

![Alt text](figures/'Marispace-X - Structure of Self-descriptions and Metadata of Geospatial Sensor Data.jpg' "Concept for self-descriptions of different entities in the federated catalogue in Marispace-X")
