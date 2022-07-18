(labbing:supp)=
# Supplementary Material

<hr>

(labbing:supp:rdm)=
## {{RDM}} Concept and Requirements

A complete neuroimaging research data management ({{RDM}}) solution would be one that enables researchers to seamlessly integrate raw, independently acquired data, processing workflows, and results, with publicly shared datasets and their corresponding derivatives. Generally, a neuroimaging data acquisition is assumed to be an {{MRI}} session originally encoded in the {{DICOM}} format, but most commonly converted to {{NIfTI}} and packaged as part of a {{BIDS}}-compliant dataset. The fundamental requirements from an {{RDM}} system would include:

1. **General research information management.** Collected data needs to be associated with a particular study group (e.g. general population, control, task, etc.), and studies should be assigned collaborators (researchers), thereby granting access. The entities and relationships required to adequately model the research process may be conceptualized and illustrated in a great number of ways, {numref}`research-entities-schema` proposes one such conceptual model.
    ```{figure} ./assets/research_entities.png
    ---
    name: research-entities-schema
    alt: A schematic representation of research data entities and       relationships.
    width: 750px
    ---
    Proposed conceptual [crow's foot](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model#Crow's_foot_notation) Entity-Relationship ({{ER}}) diagram illustrating research data management entities and their relationships.
    ```
2. **Raw {{DICOM}} metadata extraction and database management.** Independently resourced data is assumed to be encoded in the {{DICOM}} format, and therefore raw data files include a header section containing study and subject-relevant information. The ability to import *.dcm* files and maintain a database of the associated {{DICOM}} entities (see [Part 3 Section A.1.2](https://dicom.nema.org/dicom/2013/output/chtml/part03/chapter_A.html) of the {{DICOM}} Standard) is core to the workflow of the great majority of neuroimaging laboratories. Even after metadata extraction and conversion, {{DICOM}} files must be archived and made efficiently queryable for future inspection. Other than the general best-practice of never deleting raw data, information about the influence of acquisition parameters on derived measurements is constantly being updated {cite}`mcnabbIntersliceLeakageIntraslice2020,   riskImpactsSimultaneousMultislice2018, toddEvaluation2DMultiband2016`, along with metadata sharing standards and even conversion methods.
3. **Data conversion and standardization.** As established, raw {{DICOM}} data aggregated in *.dcm* files needs to be converted to {{NIfTI}} and packaged to comply with the {{BIDS}} standard. *dcm2niix* {cite}`liFirstStepNeuroimaging2016` (https://github.com/rordenlab/dcm2niix) provides exceptionally reliable format-conversion functionality, including {{JSON}}-sidecar generation (as specified in the {{BIDS}} standard). Once converted, the generated *.nii* and *.json* files must remain indefinitely associated with their original represenation as a {{DICOM}} series. Organization of the files as a {{BIDS}}-compliant dataset, however, is still only partially automated. While several tools offering semi-automated configurable workflows (e.g. *HeuDiConv*, *Dcm2Bids*) or interactive {{GUI}}s (see *ezbids*, available at https://brainlife.io/ezbids/ {cite}`avesaniOpenDiffusionData2019`) are in continuous development, a completely automated solution has yet to emerge. In addition, the {{RDM}} would need to be able to reorganize and validate the standardization of data "pulled" from external repositories. For {{BIDS}}-compliant datasets, this can be handled relatively easily by serialization of the encoded metadata to the database alongside minor reorganization or renaming of the source directories. Other cases, however, such as the {{HCP}}, would require more customized translation methods.
4. **Efficient querying and distribution functionality.** Once archived and packaged, the data must become accessible to the appropriate researchers. The application needs to provide comprehensive querying capabilities, covering both research entity relations and raw acquisition metadata. In addition, once a queryset has been curated, some method of distribution is required in order to dependably export the data to remote servers or workstations.
    ```{figure} ./assets/data_flow.png
    ---
    name: data-flow-diagram
    alt: A schematic representation of the fundamental requirements from a neuroimaging RDM system.
    width: 750px
    ---
    Schematic representation of the fundamental requirements from a       neuroimaging {{RDM}} system. Numbers circled in green correspond to the numbers of the requirements as listed above. Blue user represents an admin or laboratory manager providing general research information.
    ```

5. **Analysis workflow registration and orchestration.** While not strictly in the scope of an {{RDM}}, collaboration on a large neuroimaging dataset mandates a shared analytical workflow management tool. The scale of the data and resources required to preprocess it render the raw dataset practically unusable to most researchers {cite}`plisCOINSTACPrivacyEnabled2016`. Instead, administrators should be able to register analytical pipelines, execute them, and enable access to the results. In addition to enabling researchers to study a much larger dataset than otherwise possible and the more economical allocation of resources, as well as the significant enhancement in reproducibility, having all workflows and their parameters documented and organized provides an opportunity to better understand the effects of various preprocessing parameters on derived results.
