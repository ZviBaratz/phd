(labbing:results)=
# Results

<hr>

The following section will detail the components of the {{Django}} and {{VueJS}} web application developed for the purposes of this thesis, all available under the dedicated {{GitHub}} organization's page at https://www.github.com/TheLabbingProject.

## General Research Management Application

Even though it is built to support neuroimaging-based academic research, the core of the application is entirely domain-agnostic. Elementary research entities, such as subjects, studies, and experimental procedures, are managed independently of any particular data model.

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
## Reusable Django Apps

The integration of references to files and database access to metadata information is handled using reusable {{Django}} apps and conforms with the {{Django}} framework's general design philosophy. Other than reusability, encapsulation of domain-specific logic also contributes to both the maintainability and extensibility of the code-base.

### *django_dicom*

{{djangodicom}} is used to import *.dcm* files, extract metadata from the headers, and keep an organized archive of the included {{DICOM}} entities (see [Part 3 Section A.1.2](https://dicom.nema.org/dicom/2013/output/chtml/part03/chapter_A.html) of the {{DICOM}} Standard as well as the {{djangodicom}} container, highlighted in yellow in {numref}`labbing-schema`). All attributes associated with each information entity included in a {{DICOM}} header are serialized to the database together with principal acquisition parameters (e.g. {{TE}}, {{TI}}, {{TR}}, etc).

### *django_mri*

### *django_analyses*

## Front-end Application

### *vuelabber*

