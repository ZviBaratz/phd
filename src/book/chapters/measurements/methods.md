(measurements:methods)=
# Materials and Methods

<hr>

## Participants

This study uses a dataset collected from **N** participants (**N** female and **N** male), **N-N** years old (mean: **N**, SD: **N**; see **figure** for participant age and sex distribution). Participants were neurologically and radiologically healthy, with no history of neurological disease, and normal appearance in a clinical {{MRI}} protocol. The imaging protocol was approved by the Institutional Review Boards of [Sheba Tel HaShomer Medical Center](https://eng.sheba.co.il/) and [Tel Aviv University](https://english.tau.ac.il/), where the {{MRI}} investigations were performed. All participants provided signed informed consent before enrollment in the study.

## MRI Acquisition

All participants were scanned in compliance with the {{TAU}} Brain Brank Initiative's standardized scanning protocol at the [Alfredo Federico Strauss Center for Computational Neuroimaging](https://mri.tau.ac.il/) at [Tel Aviv University](https://english.tau.ac.il/). Scans were acquired with a 3T Siemens MAGNETOM Prisma {{MRI}} scanner ([Siemens Medical Solutions](https://www.siemens.com/global/en.html), Erlangen, Germany) using a 64-channel {{RF}} head coil. For the purposes of this study, only the {{sMRI}} subset of the protocol which is used for anatomical preprocessing will be included (see {numref}`smri-sequences` for an overview of acquisition parameters).

```{table} Summary of the {{TAU}} Brain Bank Initiative's {{sMRI}} acquisition parameters
:name: smri-sequences

| **Sequence**    | TR (ms) | TE (ms) | TI (ms) | Spatial Resolution ($mm^3$) | Number of Slices |
|:---------------:|:-------:|:-------:|:-------:|:---------------------------:|:----------------:|
| **MPRAGE**      | 2400    | 2.78    | 1000    | 0.9 🞩 0.9 🞩 0.9           | 176              |
| **T2-weighted** | 3200    | 554     | -       | 0.9 🞩 0.9 🞩 0.9           | 176              |
| **FLAIR**       | 8000    | 81      | 2370    | 0.72 🞩 0.72 🞩 4           | 52               |

```