(measurements:methods)=
# Materials and Methods

<hr>

## Participants

This study uses a dataset collected from **N** participants (**N** female and **N** male), **N-N** years old (mean: **N**, SD: **N**; see **figure** for participant age and sex distribution). Participants were neurologically and radiologically healthy, with no history of neurological disease, and normal appearance in a clinical {{MRI}} protocol. The imaging protocol was approved by the Institutional Review Boards of [Sheba Tel HaShomer Medical Center](https://eng.sheba.co.il/) and [Tel Aviv University](https://english.tau.ac.il/), where the {{MRI}} investigations were performed. All participants provided signed informed consent before enrollment in the study.

## MRI Acquisition

Participants were scanned in compliance with the {{TAU}} Brain Brank Initiative's standardized scanning protocol at the [Alfredo Federico Strauss Center for Computational Neuroimaging](https://mri.tau.ac.il/) at Tel Aviv University. Scans were acquired with a 3T Siemens MAGNETOM Prisma {{MRI}} scanner ([Siemens Medical Solutions](https://www.siemens.com/global/en.html), Erlangen, Germany) using a 64-channel {{RF}} head coil. For the purposes of this study, only the {{sMRI}} subset of the protocol which is used for anatomical preprocessing with *FreeSurfer* will be included (see {numref}`smri-sequences` for an overview of acquisition parameters).

```{table} Summary of the {{TAU}} Brain Bank Initiative's {{sMRI}} acquisition parameters.
:name: smri-sequences

| **Sequence**    | TR (ms) | TE (ms) | TI (ms) | Spatial Resolution ($mm^3$) | Number of Slices |
|:---------------:|:-------:|:-------:|:-------:|:---------------------------:|:----------------:|
| **MPRAGE**      | 2400    | 2.78    | 1000    | 0.9 🞩 0.9 🞩 0.9           | 176              |
| **T2-weighted** | 3200    | 554     | -       | 0.9 🞩 0.9 🞩 0.9           | 176              |
| **FLAIR**       | 8000    | 81      | 2370    | 0.72 🞩 0.72 🞩 4           | 52               |

```

## MRI Data Analysis

To study the effects of various execution configurations, *FreeSurfer* v7.2.0 was used to preprocess the anatomical data cross-sectionally (i.e. as individual datasets, as opposed to longitudinally) using a number of predefined configurations. While *FreeSurfer* does also have a longitudinal processing stream which uses results from the cross-sectional analysis of all time points to create an unbiased within-subject template, the objective of this study is to evaluate inter-subject vs. intra-subject similarity independently of prior knowledge.

```{figure} ./assets/preprocessing_overview.png
---
name: preprocessing-overview
alt: An overview of the anatomical preprocessing workflow.
width: 750px
---
An overview of the anatomical MRI preprocessing workflow. The {{TAU}} Brain Bank Initiative's dataset was filtered for multi-session subjects and a subset of possible *FreeSurfer* execution configurations was processed for each scan independently.
```

According to the *FreeSurfer* documentation site (see https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferWiki), using {{T2w}} or {{FLAIR}} data (mutually exclusive) improves pial surface estimation (see https://surfer.nmr.mgh.harvard.edu/fswiki/recon-all), and specifying *3T* and *mprage* (non-mutually exclusive) alters various analysis assumptions and steps to optimize for the corresponding magnetic field magnitude and acquisition protocol (see https://surfer.nmr.mgh.harvard.edu/fswiki/OtherUsefulFlags). {numref}`freesurfer-parameters` provides a summary of the execution configurations included in this study.

```{table} *FreeSurfer*'s cross-sectional anatomical preprocessing workflow configurations included in this study.
:name: freesurfer-parameters
:class: cell-text-center

| Use T2 | Use FLAIR | MPRAGE | 3T |
|:------:|:---------:|:------:|:--:|
| {{ redCross }} | {{ redCross }} | {{ redCross }} | {{ redCross }}  |
| {{ greenCheckmark }} | {{ redCross }} | {{ redCross }} | {{ redCross }} |
| {{ redCross }} | {{ greenCheckmark }} | {{ redCross }} | {{ redCross }} |
| {{ greenCheckmark }} | {{ redCross }} | {{ greenCheckmark }} | {{ redCross }} |
| {{ redCross }} | {{ greenCheckmark }} | {{ greenCheckmark }} | {{ redCross }} |
| {{ greenCheckmark }} | {{ redCross }} | {{ greenCheckmark }} | {{ greenCheckmark }} |
| {{ redCross }} | {{ greenCheckmark }} | {{ greenCheckmark }} | {{ greenCheckmark }} |

```
