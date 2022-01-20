(labbing:intro)=
# Introduction

<hr>

## Public Large-scale Neuroimaging Datasets

Centralized data collection and distribution efforts are key to the advancement of neuroscientific research {cite}`milhamAssessmentImpactShared2018`. Larger publicly available samples enable the detection and study of phenomena with smaller effect sizes more rapidly, by more people, and with more confidence {cite}`smithStatisticalChallengesBig2018, lairdLargeOpenDatasets2021, madanScanOnceAnalyse2021`. Data sharing enhances the reporoducibility of findings, reduces time and costs for new research, promotes transparency, and encourages collaboration across fields {cite}`marHowProducePersonality2013a, poldrackMakingBigData2014, madanAdvancesStudyingBrain2017, milhamAssessmentImpactShared2018`. In recent years, such public datsets have become more numerous and increasingly accessible. The following table, taken from a practical guide to end-users (researchers interested in using public neuroimaging datasets) published in *Nature Human Behaviour* (https://www.nature.com/nathumbehav/) {cite}`horienHitchhikerGuideWorking2021`, offers a summary of currently available datasets, including sample size, modalities, processing stages, and access policy:

```{figure-md} markdown-fig
<img src="https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41562-020-01005-4/MediaObjects/41562_2020_1005_Fig1_HTML.png?as=webp" alt="Neuroimaging Datasets Summary" class="bg-primary mb-1" width="750px">

**Taken from "A hitchhiker’s guide to working with large, open-source neuroimaging datasets" {cite}`horienHitchhikerGuideWorking2021`.**<br />**a**, For each dataset listed in the leftmost column, sample size is indicated, along with the type of data included (‘Data modalities’). ‘Data level’ refers to the level of preprocessing: white circle, raw data; grey circle, some level of preprocessed data; black, processed data (for example, statistical maps, connectivity matrices, etc.). **b**, For each open repository (i.e., a collection of open datasets) listed in the leftmost column, an estimate of the number of open datasets is listed. Datasets of particular interest are highlighted (‘Featured large datasets’). Sample sizes and the number of open datasets are current as of October 2020. Users are encouraged to visit the website associated with each dataset before use, as sample sizes, access conditions, etc. may change.
```

This unprecedented scale and availability of data has proven impact on the field of neuroimaging {cite}`milhamAssessmentImpactShared2018`. However, there are still practical issues that hinder the ability of researchers to fully leverage these assets to optimize the quantity and quality of their scientific findings, both individually and in collaboration. The management of subject information and both raw and packaged {{MRI}} data (i.e. converted to {{NIfTI}} and organized to conform with the {{BIDS}} standard) along with preprocessing results, in scale, raises challenges. In one report, it is estimated that it generally takes two or three researchers working on a project based on data from public datasets roughly 6 to 9 months to download, process, and prepare the data for analysis {cite}`horienHitchhikerGuideWorking2021`. This period of time is also fertile ground for the introduction of more degrees of freedom to the analytical workflow (as well as human error), severly undermining the reproducibility of the results {cite}`botvinik-nezerVariabilityAnalysisSingle2020`. To better facilitate large-scale neuroimaging research, dedicated data and analysis management solutions are required.

## Neuroimaging Data Management

### Existing Solutions

#### LORIS

#### XNAT

#### Brainlife.io

## Collaborative Open-source Software Development