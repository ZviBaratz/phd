(labbing:intro)=
# Introduction

<hr>

Centralized data collection and distribution efforts are key to the advancement of neuroscientific research {cite}`milhamAssessmentImpactShared2018, lairdLargeOpenDatasets2021, vanhornItTimeReprioritize2009`. Larger publicly available samples enable the detection and study of phenomena with smaller effect sizes more rapidly, by more people, and with more confidence {cite}`smithStatisticalChallengesBig2018, lairdLargeOpenDatasets2021, madanScanOnceAnalyse2021`. Data sharing enhances the reproducibility of findings, reduces time and costs for new research, promotes transparency, and encourages collaboration across fields {cite}`marHowProducePersonality2013a, poldrackMakingBigData2014, madanAdvancesStudyingBrain2017, milhamAssessmentImpactShared2018`. In recent years, such public datasets have become more numerous and increasingly accessible {cite}`borghiDataManagementSharing2018, lairdLargeOpenDatasets2021, horienHitchhikerGuideWorking2021`.

This unprecedented scale and availability of data has a proven impact on the field of neuroimaging {cite}`milhamAssessmentImpactShared2018`. However, there are still practical issues that hinder the ability of researchers to fully leverage these assets to optimize the quantity and quality of their scientific findings, individually or in collaboration {cite}`borghiDataManagementSharing2018, routierClinicaOpenSourceSoftware2021`. The management of subject information and both raw and packaged {{MRI}} data (i.e. converted to {{NIfTI}} and organized to conform with the {{BIDS}} standard) along with preprocessing results and any other, non-{{MRI}} data, in scale, can quickly prove to be a more complicated task than often anticipated. In one report, it is estimated that it generally takes two or three researchers working on a project based on data from public datasets roughly 6 to 9 months to download, process, and prepare the data for analysis {cite}`horienHitchhikerGuideWorking2021`. This period of time is also fertile ground for the introduction of more degrees of freedom to the analytical workflow (as well as human error), severely undermining the reproducibility of the results {cite}`botvinik-nezerVariabilityAnalysisSingle2020`. To better facilitate large-scale neuroimaging research, dedicated data and analysis management solutions are required.

The pipeline and methods presented in this thesis are based on the following requirements:
  1. General research information management
  2. Raw {{DICOM}} metadata extraction and database management
  3. Data conversion and standardization
  4. Efficient querying and distribution functionality
  5. Analysis workflow registration and orchestration

See the supplementary material ({ref}`labbing:supp:rdm`) for a more detailed overview.

## Free and Open-source Software (FOSS) and Collaborative Science

The benefit of {{FOSS}} and collaborative software development on scientific research in general {cite}`fortunatoCaseFreeOpen2021` and neuroscientific research in particular {cite}`gleesonCommitmentOpenSource2017, whiteFutureOpenOpenSource2019, halchenkoOpenNotEnough2012` has become a central topic of discussion in recent years. Working with and collaborating on open-source code repositories, including version control, testing, documentation, continuous integration ({{CI}}), and much more, is rapidly becoming a fundamental part of the technical capability expected from researchers in the field {cite}`mullerPythonNeuroscience2015`. Relevant educational content has become effectively ubiquitous in workshops and other educational programs, and an increasing number of contemporary initiatives are embracing the community-oriented philosophy and standards. This shift in the zeitgeist is largely owed to the widespread adoption of Python and the general-purpose programming language tools and paradigms it offers and encourages.

For the purposes of this thesis, the desired {{RDM}} solution is one that is entirely free and open-source, and is designed as a collaborative, community-oriented software development project. Because most researchers are not experienced with commonplace web development technologies (e.g. NodeJS, {{PHP}}, Java, etc.), as much of the codebase should be written in Python as possible. This will encourage user involvement, foster awareness to infrastructural details and processing decisions, and ultimately serve to support the credibility and reproducibility of the derived findings.

## Existing Solutions

A number of neuroimaging {{RDM}} systems have been developed to support particular research centers and collaborations across the world. Some of the most notable examples are the Extensible Neuroimaging Archive Toolkit ({{XNAT}}, see https://www.xnat.org/) {cite}`marcusExtensibleNeuroimagingArchive2007, herrickXNATCentralOpen2016`, Longitudinal Online Research and Imaging System ({{LORIS}}, see https://loris.ca/) {cite}`dasLORISWebbasedData2012`, and the newest addition, [brainlife.io](https://brainlife.io). All three are open-source and in active development, however, none offered both the required functionality and the means to create a sustainable, independent deployment of the application without specialized expertise at the time of writing. {numref}`existing-rdms` offers a summary of the technological stacks and {{DICOM}} or {{BIDS}}-related functionality provided by these applications.

```{list-table} A summary of existing open-source neuroimaging {{RDM}} applications' technological stacks and the required {{DICOM}} or {{BIDS}}-related functionality. All information was independently gathered from openly accessibly project websites, documentation, or code repositories.<br><span style="font-size: 0.8rem;">* <span>brainlife.io</span> has a new and exciting semi-automated web-based {{DICOM}} to {{BIDS}} conversion tool, *ezBIDS*, currently in development and approaching a stable release.</span><br><span style="font-size: 0.7rem;">[1] https://traefik.io/ [2] https://www.postgresql.org/ [3] https://tomcat.apache.org/ [4] https://httpd.apache.org/ [5] https://www.mysql.com/ [6] https://php.net/ [7] https://reactjs.org/</span>
:header-rows: 1
:name: existing-rdms

* - Name
  - Technological Stack
  - {{DICOM}} Import
  - {{DICOM}} to {{BIDS}} Conversion
  - {{BIDS}} Import
  - Deployment Documentation
  - Source Code
* - {{XNAT}}
  - + Linux
    + <span class="muted-ref">[Traefik](https://traefik.io/)</span><sup>[1]</sup>
    + {{PostgreSQL}}<sup>[2]</sup>
    + <span class="muted-ref">[Apache Tomcat](https://tomcat.apache.org/)</span><sup>[3]</sup>
  - {{ greenCheckmark }}
  - {{ redCross }}
  - {{ redCross }}
  - {{ greenCheckmark }}
  - [bitbucket.org/xnatdev](https://bitbucket.org/xnatdev/)
* - {{LORIS}}
  - + Linux
    + <span class="muted-ref">[Apache HTTP Server](https://httpd.apache.org/)</span><sup>[4]</sup>
    + <span class="muted-ref">[MySQL](https://www.mysql.com/)</span><sup>[5]</sup>
    + <span class="muted-ref">[PHP](https://php.net/)</span><sup>[6]</sup>
    + <span class="muted-ref">[React](https://reactjs.org/)</span><sup>[7]</sup>
  - {{ greenCheckmark }}
  - {{ redCross }}
  - {{ redCross }}
  - {{ greenCheckmark }}
  - [github.com/aces](https://github.com/aces)
* - <span>brainlife.io</span>
  - + Mixed microservice architecture
    + {{VueJS}}
  - {{ redCross }}
  - {{ greenCheckmarkStarred }}
  - {{ greenCheckmark }}
  - {{ redCross }}
  - [github.com/brainlife](https://github.com/brainlife)
```

The ability to manage a large {{DICOM}} dataset combined with external {{BIDS}} datasets and fluently associate the included or provided research information is a core requirement of this thesis which is not yet properly handled by existing tools. In addition, none of the applications' technological stacks are Python-based, making it significantly less likely for most researchers to be able to actively participate in their development.

To overcome this technical difficulty, the first part of this thesis introduces a dedicated, Python-based, open-source and community-oriented {{RDM}} application.