<h1>Introduction</h1>
The self-descriptions are single entries in a Federated Catalogue. The Federated Catalogue is basically a central repository of self-descriptions enabling the discovery and selection of providers, their service offerings and their assets. Self-descriptions are standardised, machine comprehensible metadata. A more detailed description about the role of self-descriptions within the Gaia-X ecosystem can be found in this Whitepaper (https://gaia-x.eu/wp-content/uploads/2022/08/SSI_Self_Description_EN_V3.pdf). Additional information about the Gaia-X architecture can be found in the Gaia-X Architecture Framework documents (https://docs.gaia-x.eu/).

**NOTE**: Metadata and Data Quality are defined as two different things, which is also reflected in the ISO standard documents being split into “ISO 19115 - Geographic Information – Metadata” and “ISO 19157 - Geographic Information – Data Quality”. Metadata and Data Quality could be defined as
- Metadata: Facts about the data
- Data Quality: Interpretation of the facts and the contained data. Data Quality depends on the specific goals the user likes to achieve with the data.

<h1>Schema Self-Descriptions in Marispace-X</h1>
All self-descriptions required for the Federated Catalogue in Marispace-X are collected here. The self-descriptions are in a draft phase and are steadily evaluated, updated and extended during the Marispace-X project

The self-descriptions are sorted into the following folders according to the respective entity (see Figure 1).
- Participants (e.g., legal persons, companies, ...)
- Service Offerings (e.g., platform, software, infrastructure, ...)
- Resources (e.g., data, sensor devices, infrastructure, ...)
  - Sensors (e.g., multibeam, ctd, camera, ...)

Resources and Sensors are separated into different entities in Marispace-X due to the complexity and large amount of different sensor types that exist (see Figure 1). The separation of "Sensors" is an extension to the Gaia-X framework. The resource self-descriptions "GeoData Resource" is the general self-descriptions of geospatial data resources. This self-description makes the data resource findable and accessible (**FA**IR principles - https://www.go-fair.org/fair-principles/) as they can be searched by geolocation, time, sensor type, theme. The "Sensor" self-description is a more detailed self-description of the specific sensor data, like "multibeam", "ctd", "camera" . This self-description makes the data interoperable and reusable (FA**IR** principles - https://www.go-fair.org/fair-principles/) as they contain attributes about sensor characteristics, sensor settings, and processing information. Technically, "Sensor" should be implemented as a child of a "GeoData Resource" (using the "aggregationOf" attribute from the Gaia-X ontologies).

![alt TEST](figures/Marispace-X-Concept_self_descriptions.jpg)
*Figure 1: Concept for self-descriptions of different entities in the federated catalogue in Marispace-X*

Each self-description can have the three following data files. Only the verified JSON-LD will be stored in the Federated Catalogue. All entities that already have a SHACL, JSON-LD, and/or a verified JSON-LD file can be found in the respective folders in this repository (selfdescriptions/)
- SHACL (template of the self-description that can be filled out using the SD Creation Wizard - https://sd-creation-wizard.gxfs.dev/)
- JSON-LD (self-description file created from the SHACL template using the SD Creation Wizard)
- verified JSON-LD (the self-description needs to be verified, "wrapped" into a verifiable paragraph)

For the self-descriptions of the entities "Participant", "Service Offering" ("Software", "Platform", "Infrastructure"), and "Resource" templates from Gaia-X exist that can also be used in Marispace-X. For the more specific descriptions of data and software resources, adaptions need to be made in Marispace-X. Therefore, these adaptions for the self-descriptions "GeoData Resource", "Sensor", and "Software  Resource" are described in the following.

<h2>GeoData Resource/Sensor Self-Descriptions</h2>
First SHACL files need to be created as templates for each self-description required in Marispace-X. These SHACL files are based on existing standards/ontologies as good as possible.
The current concept for data resources is a follows (see Figure 2):

- general resource self-description "geoDataResourceShape.ttl" (based on GeoDCAT-AP ontologie - https://semiceu.github.io/GeoDCAT-AP/drafts/latest/ - and Gaia-X ontologies - https://gaia-x.gitlab.io/technical-committee/federation-services/data-exchange/dewg/#data-product) - "GeoDCAT-AP provides an RDF vocabulary and the corresponding RDF syntax binding for the union of metadata elements of the core profile of ISO 19115:2003 and those defined in the framework of the INSPIRE Directive."
  - the "Sensor" self-descriptions are divided into different SHACL files, from sensor-generic to survey- and sensor-specific descriptions. These SHACL files should be merged to a single json-LD self-description for the "Sensor", denoted as "*filename.json", where filename is replace by the name of the respective data file (e.g., 20201023_101523_0001.json). Hence, for each data file a "Sensor" self-description can exist. Based on the technical feasibility, the three "Sensor" SHACL files are either first merged into one SHACL file, then filled out and converted to a JSON-LD, or the three SHACL files are first filled out, then converted to JSON-LDs and afterwards merged into one JOSN-LD, or the "sensor**Shape.ttl" and linked to the other two JSON-LD files. The benefit of the last solution is that the "sensorGeneralInformationShape.ttl" and "sensorSurveyInformation.ttl" files only need to be filled out once.
    - general sensor information self-description "sensorGeneralInformationShape.ttl" (based on MMI Device Ontology - https://mmisw.org/ont/mmi/device - and Gaia-X ontologies - https://gaia-x.gitlab.io/technical-committee/federation-services/data-exchange/dewg/#data-product) - "Contains generic sensor attributes like sensor name, sensor manufacturer, sensor id, serial number, ..."
    - survey specific information self-description "sensorSurveyInformation.ttl" (based on MMI Device Ontology - https://mmisw.org/ont/mmi/device - and GeoDCAT-AP ontologie - https://semiceu.github.io/GeoDCAT-AP/drafts/latest/ - and Gaia-x ontology - https://gaia-x.gitlab.io/technical-committee/federation-services/data-exchange/dewg/#data-product) - "Contains generic survey information about the sensor file like contact of surveyor, start date, end date, location, ..."
    - detailed sensor information self-description with the file naming convention "sensor**Shape.ttl" where * is replaced with the sensor name, e.g., "sensorSideScanSonarShape.ttl", "sensorCTDShape.ttl", "sensorCameraShape.ttl", "sensorSatelliteRadarShape.ttl" (this can be based on very specific ontologies for the respectivce sensor type, e.g., OGC SSN - https://www.w3.org/TR/vocab-ssn/, OGC EO - https://docs.ogc.org/is/10-157r4/10-157r4.html ; as many attributes are so specific that no ontolgies already exist, the current idea is to extend the MMI Device Ontology) - "Contains detailed sensor settings and sensor-specific attributes like frequency, sampling rate, ..."
   
![alt TEST](figures/Marispace-X-Concept_self_descriptions_2.jpg)
*Figure 2: Concept for self-descriptions of gesopatial data resources and corresponding sensor data in the federated catalogue in Marispace-X*


<h2>Software Resource Self-Descriptions</h2>
First SHACL files need to be created as templates for each self-description required in Marispace-X. These SHACL files are based on existing standards/ontologies as good as possible.
The current concept for data services is a follows:

- the software service self-description template "softwareOfferingShape.ttl" from Gaia-X is adapated to the needs for geospatial data services (based on GeoDCAT-AP ontologie - https://semiceu.github.io/GeoDCAT-AP/drafts/latest/ - and Gaia-X ontologies - https://gaia-x.gitlab.io/technical-committee/federation-services/data-exchange/dewg/#data-product) - "GeoDCAT-AP provides an RDF vocabulary and the corresponding RDF syntax binding for the union of metadata elements of the core profile of ISO 19115:2003 and those defined in the framework of the INSPIRE Directive.". The corresponding JSON-LD file is named "softwareOffering-servicename" where servicename is replaced with the respective title of the software service (e.g., softwareOffering-TrackPlanner_MBES.json)

<h1>Examples Self-Descriptions in Marispace-X</h1>
Example files for different applications are given in the repository, which are the JSON-LD self-descriptions filled from the SHACL template files. An overview of the different examples is given below.

<h2>Example GeoData Resource/Sensor</h2>

<h2>Example Software/Platform Offering</h2>
Examples for a software and platform offering are illustrated in Figure 4. The software service offering can consist of multiple software resources (software tools) the are part of the offering, but it could also be only a single software offering where the link to additional software resources might not be necessary. This is the case for the platform offering where only a single self-descriptions exist to describe the service offering.

![alt TEST](figures/Marispace-X-Self_description_example_software_service.jpg)
*Figure 4: Example for a software service offering and a platfrom service offering. The corresponding JSON-LD files can be found in the respective subfolder of the selfdescriptions/ folder*

<h2>Example Physical Resource</h2>
Examples for a physical resources are illustrated in Figure 5. The service offering is a rental of different survey equipment. So the service offering is linked to differnt physical resources like "Multibeam Echosounder Rental" and "Side Scan Sonar Rental". These physical resources can make use of the sensorGeneralInformation self-descriptions. If the self-description of the offered sensor already exists in the federated catalgoue, the physical resource can link to this sensor and so automatically adds the general information about the sensor.

![alt TEST](figures/Marispace-X-Self-description_example_physical_resource.jpg)
*Figure 5: Examples for physical resources offered via a service. The corresponding JSON-LD files can be found in the respective subfolder of the selfdescriptions/ folder*
