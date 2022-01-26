(labbing:intro)=
# Introduction

<hr>

Working with a large and diverse neuroimaging dataset is a challenging task not particular to this thesis {cite}`horienHitchhikerGuideWorking2021, borghiDataManagementSharing2018`. The following section will provide a quick overview of existing public datasets and explore how they are shared and what tools are most commonly utilized by researchers to use them to produce scientific findings.

## Public Large-scale Neuroimaging Datasets

Centralized data collection and distribution efforts are key to the advancement of neuroscientific research {cite}`milhamAssessmentImpactShared2018, lairdLargeOpenDatasets2021`. Larger publicly available samples enable the detection and study of phenomena with smaller effect sizes more rapidly, by more people, and with more confidence {cite}`smithStatisticalChallengesBig2018, lairdLargeOpenDatasets2021, madanScanOnceAnalyse2021`. Data sharing enhances the reporoducibility of findings, reduces time and costs for new research, promotes transparency, and encourages collaboration across fields {cite}`marHowProducePersonality2013a, poldrackMakingBigData2014, madanAdvancesStudyingBrain2017, milhamAssessmentImpactShared2018`. In recent years, such public datsets have become more numerous and increasingly accessible {cite}`borghiDataManagementSharing2018, lairdLargeOpenDatasets2021, horienHitchhikerGuideWorking2021`. The following table, taken from a practical guide to end-users (researchers interested in using public neuroimaging datasets) published in *Nature Human Behaviour* (https://www.nature.com/nathumbehav/) {cite}`horienHitchhikerGuideWorking2021`, offers a summary of currently available datasets, including sample size, modalities, processing stages, and access policy:

```{figure-md} markdown-fig
<img src="https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41562-020-01005-4/MediaObjects/41562_2020_1005_Fig1_HTML.png?as=webp" alt="Neuroimaging Datasets Summary" class="bg-primary mb-1" width="750px">

**Reprinted from "A hitchhiker’s guide to working with large, open-source neuroimaging   datasets" {cite}`horienHitchhikerGuideWorking2021`.**<br />**a**, For each dataset listed in the leftmost column, sample size is indicated, along with the type of data included (‘Data modalities’). ‘Data level’ refers to the level of preprocessing: white circle, raw data; grey circle, some level of preprocessed data; black, processed data (for example, statistical maps, connectivity matrices, etc.). **b**, For each open repository (i.e., a collection of open datasets) listed in the leftmost column, an estimate of the number of open datasets is listed. Datasets of particular interest are highlighted (‘Featured large datasets’). Sample sizes and the number of open datasets are current as of October 2020. Users are encouraged to visit the website associated with each dataset before use, as sample sizes, access conditions, etc. may change.
```

This unprecedented scale and availability of data has proven impact on the field of neuroimaging {cite}`milhamAssessmentImpactShared2018`. However, there are still practical issues that hinder the ability of researchers to fully leverage these assets to optimize the quantity and quality of their scientific findings, individually or in collaboration {cite}`borghiDataManagementSharing2018`. The management of subject information and both raw and packaged {{MRI}} data (i.e. converted to {{NIfTI}} and organized to conform with the {{BIDS}} standard) along with preprocessing results and any other, non-MRI data, in scale, can quickly prove to be a more complicated task than often anticipated. In one report, it is estimated that it generally takes two or three researchers working on a project based on data from public datasets roughly 6 to 9 months to download, process, and prepare the data for analysis {cite}`horienHitchhikerGuideWorking2021`. This period of time is also fertile ground for the introduction of more degrees of freedom to the analytical workflow (as well as human error), severly undermining the reproducibility of the results {cite}`botvinik-nezerVariabilityAnalysisSingle2020`. To better facilitate large-scale neuroimaging research, dedicated data and analysis management solutions are required.

## Neuroimaging Research Data Management

### Requirements

A complete neuroimaging Research Data Management ({{RDM}}) solution would be one that enables researchers to seamlessly integrate raw, independently acquired data, processing workflows, and results, with publicly shared datasets and their corresponding derivatives. For the purposes of this thesis, a neuroimaging data acquisition is assumed to be an {{MRI}} session originally encoded in the {{DICOM}} format, but most commonly converted to {{NIfTI}} and packaged as part of a {{BIDS}}-compliant dataset. The fundamental requirements from an {{RDM}} system would include:

1. **General research information management.** Collected data needs to be associated with a particular study group (e.g. general population, control, task, etc.), and studies should be assigned collaborators (researchers), thereby granting access. The entities and relationships required to adequately model the research process may be conceptualized and illustrated in a great number of ways, {numref}`research-entities-schema` proposes one such conceptual model.
    ```{figure} ./assets/research_entities.png
    ---
    name: research-entities-schema
    alt: A schematic representation of research data entities and       relationships.
    width: 750px
    ---
    Proposed conceptual [crow's foot](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model#Crow's_foot_notation) Entity-Relationship ({{ER}}) diagram illustrating research data management entities and their relationships.
    ```
2. **Raw {{DICOM}} metadata extraction and database management.** Independently resourced data is assumed to be encoded in the {{DICOM}} format, and therefore raw data files include a header section containing study and subject-relevant information. The ability to import *.dcm* files and maintain a database of the associated {{DICOM}} entities (see [Part 3 Section A.1.2](https://dicom.nema.org/dicom/2013/output/chtml/part03/chapter_A.html) of the DICOM Standard) is core to the workflow of the great majority of neuroimaging laboratories. Even after metadata extraction and conversion, {{DICOM}} files must be archived and made efficiently queryable for future inspection. Other than the general best-practice of never deleting raw data, information about the influence of acquisition parameters on derived measurements is constantly being updated {cite}`mcnabbIntersliceLeakageIntraslice2020,   riskImpactsSimultaneousMultislice2018, toddEvaluation2DMultiband2016`, along with metadata sharing standards and even conversion methods.
3. **Data conversion and standardization.** As established, raw {{DICOM}} data aggregated in *.dcm* files needs to be converted to {{NIfTI}} and packaged to comply with the {{BIDS}} standard. *dcm2niix* {cite}`liFirstStepNeuroimaging2016` (https://github.com/rordenlab/dcm2niix) provides exceptionally reliable format-conversion functionality, including {{JSON}}-sidecar generation (as specified in the {{BIDS}} standard). Once converted, the generated *.nii* and *.json* files must remain indefinitely associated with their original represenation as a {{DICOM}} series. Organization of the files as a {{BIDS}}-compliant dataset, however, is still only partially automated. While several tools offering semi-automated configurable workflows (e.g. *HeuDiConv*, *Dcm2Bids*) or interactive {{GUI}}s (e.g. *ezbids* {cite}`avesaniOpenDiffusionData2019`) are in continuous development, a completely automated solution has yet to emerge. In addition, the {{RDM}} would need to be able to reorganize and validate the standardization of data "pulled" from external repositories. For {{BIDS}}-compliant datasets, this can be handled relatively easily by serialization of the encoded metadata to the database alongside minor reorganization or renaming of the source directories. Other cases, however, such as the {{HCP}}, would require more involved and customized translation methods.
4. **Efficient querying and distribution functionality.** Once archived and packaged, the data must become accessible to the appropriate researchers. The application must provide comprehensive querying capabilities, covering both research entity relations and raw acquisition metadata. In addition, once a queryset has been curated, some method of distribution is required in order to dependably export the data to remote servers or workstations.
    ```{figure} ./assets/data_flow.png
    ---
    name: data-flow-diagram
    alt: A schematic representation of the fundamental requirements from a neuroimaging RDM system.
    width: 750px
    ---
    Schematic representation of the fundamental requirements from a       neuroimaging {{RDM}} system. Numbers circled in green correspond to the numbers of the requirements as listed above. Blue user represents an admin or laboratory manager providing general research information.
    ```

There is also an additional requirement, which is not strictly in the scope of an {{RDM}}, but would also be necessary for collaborating on a large-scale dataset:

* **Analysis workflow registration and orchestration.**

### Existing Solutions

#### LORIS

#### XNAT

#### Brainlife.io

## Collaborative Open-source Software Development