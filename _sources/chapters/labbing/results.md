(labbing:results)=
# Results

<hr>

The following section will detail the components of the {{Django}} and {{VueJS}} web application developed for the purposes of this thesis, all available under the dedicated {{GitHub}} organization's page at https://www.github.com/TheLabbingProject.

(labbing:results:project)=
## General Research Management Application

Even though it is built to support neuroimaging-based academic research, the core of the application is entirely domain-agnostic. Elementary research entities, such as subjects, studies, and experimental procedures, are managed independently of any particular data model.

(labbing:results:project:pylabber)=
### *pylabber*

{{pylabber}} (see https://www.github.com/TheLabbingProject/pylabber) is the base project repository (see {ref}`labbing:methods:backend:django` section in {ref}`labbing:methods`) for the complete web application. In addition to centralizing configurations and resources, it includes two general-purpose research apps:

* *accounts*: Manages laboratory and researcher information, as well as data distribution. Administrators can register new laboratories and users (researchers), and users can provide {{SSH}} credentials to remote machines to configure export destinations.
* *research*: Manages general research-related entities. Relies on external apps to associate models representing data acquisitions (such as an {{MRI}} session) to the appropriate subject, and models representing data instances (such as an {{MRI}} scan) to study groups. The decision to move group association from subjects to data instances was made in order to allow for flexible association of any part of the acquired data to any number of study groups. Each study may be assigned a number of study groups, as well as a number of experimental procedures. An experimental procedure consists of an ordered sequence of steps which may be categorized as either tasks or data acquisitions (see the *research* container nested within the *pylabber* container and highlighted in purple in {numref}`labbing-schema`).

```{figure} ./assets/labbing_schema.png
---
name: labbing-schema
alt: Web application's entity-relationship diagram.
width: 750px
---
[Crow's foot](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model#Crow's_foot_notation) Entity-Relationship ({{ER}}) diagram illustrating the database tables managed by the application and relationships between them.
```

(labbing:results:apps)=
## Reusable Django Apps

The integration of references to files and database access to metadata information is handled using reusable {{Django}} apps and conforms with the {{Django}} framework's general design philosophy. Other than reusability, encapsulation of domain-specific logic also contributes to both the maintainability and extensibility of the code-base.

(labbing:results:apps:django-analyses)=
### *django_analyses*

{{djangoanalyses}} provides database-driven analysis registration and execution management (see the {{djangoanalyses}} container, highlighted in red in {numref}`labbing-schema`).

(labbing:results:apps:django-analyses:analysis)=
#### Analysis Integration

Analysis interfaces (i.e. Python classes or functions used to initialize the execution of an analysis) are registered with a particular analysis version, which represents it in the database and holds references to the appropriate input and output specifications. When an analysis version is executed, a new run instance is created to combine the information about the analysis version with the provided inputs and eventually outputs (or traceback information, if an exception was raised).

Node instances are used as execution templates and provide a constant reference to runs of a specific analysis version with a particular configuration. Controlled execution of analyses with {{Celery}} is handled by providing nodes with input data and returning the created (or existing) run instances.

(labbing:results:apps:django-analyses:pipeline)=
#### Pipeline Integration

Pipelines, or workflows, may be registered in the database as a sequence of pipes. Each pipe describes the flow of data from one node's output to another node's input specification. A dedicated "pipeline runner" class is provided by the app to control the ordered execution of nodes according to the dependecies outlined by the pipes.

For more information about {{djangoanalyses}} and complete usage examples, see the app's <span class="muted-ref">[documentation site](https://django-analyses.readthedocs.io/)</span> (available at https://django-analyses.readthedocs.io/).

(labbing:results:apps:django-dicom)=
### *django_dicom*

{{djangodicom}} is used to import *.dcm* files, extract metadata from the headers, and keep an organized archive of the included {{DICOM}} entities (see [Part 3 Section A.1.2](https://dicom.nema.org/dicom/2013/output/chtml/part03/chapter_A.html) of the {{DICOM}} Standard as well as the {{djangodicom}} container, highlighted in yellow in {numref}`labbing-schema`). All attributes associated with each information entity included in a {{DICOM}} header are serialized to the database together with principal acquisition parameters (e.g. {{TE}}, {{TI}}, {{TR}}, etc.).

(labbing:results:apps:django-dicom:dicom-parser)=
#### *dicom_parser*

Header information is read using {{dicomparser}} (see https://www.github.com/open-dicom/dicom_parser), a wrapper around {{pydicom}} (see https://pydicom.github.io/) developed specifically for the purposes of the app. While {{pydicom}} focuses on low-level header parsing in compliance with the {{DICOM}} Standard, {{dicomparser}} provides a higher-level {{API}} to facilitate type conversion and vendor-specific metadata extraction methods. In addition, {{dicomparser}} includes a "sequence detection" utility, enabling the configuration of commonplace heuristics for automated categorization of the scanning protocol (e.g. {{MPRAGE}}, {{FLAIR}}, {{fMRI}}, {{dMRI}}, etc.).

(labbing:results:apps:django-mri)=
### *django_mri*

{{djangomri}} provides an abstraction layer which is ultimately meant to keep the users practically agnostic of file-format and metadata extraction processes (see the {{djangomri}} container, highlighted in orange in {numref}`labbing-schema`). It uses {{djangodicom}} alongside a supplementary {{NIfTI}} database table to simplify interaction with {{MRI}} data by providing abstract "scan" and "session" representations. The scan data model keeps a reference to source files and automates whatever possible to allow shifting the focus from infrastructure and technical details to processing and results.

In terms of file management, {{dicomparser}}'s sequence detection functionality provides information which is essential for automated {{BIDS}}-compliant organization. By taking advantage of the configured heuristics, {{djangomri}} maintains a "global" {{BIDS}} dataset, which holds the combined datasets of multiple studies. All research information is maintained in the database and any available {{BIDS}} app may be applied (see https://bids-apps.neuroimaging.io/).

Finally, {{djangomri}} makes extensive use of {{djangoanalyses}} and {{nipype}} {cite}`gorgolewskiNipypeFlexibleLightweight2011` to provide the specifications and analysis interfaces (see {ref}`labbing:results:apps:django-analyses:analysis`) for numerous neuroimaging processing tools, including {{fmriprep}} {cite}`estebanFMRIPrepRobustPreprocessing2019`, {{freesurfer}} {cite}`fischlFreeSurfer2012`, {{qsiprep}} {cite}`cieslakQSIPrepIntegrativePlatform2021`, {{CAT}} (see http://www.neuro.uni-jena.de/cat/), and more.

(labbing:results:front-end)=
## Front-end Application

(labbing:results:front-end:vuelabber)=
### *vuelabber*

