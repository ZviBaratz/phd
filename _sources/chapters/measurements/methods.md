(measurements:methods)=
# Materials and Methods

<hr>

## Participants

This study uses a dataset collected from **N** participants (**N** female and **N** male), **N-N** years old (mean: **N**, SD: **N**; see **figure** for participant age and sex distribution). Participants were neurologically and radiologically healthy, with no history of neurological disease, and normal appearance in a clinical {{MRI}} protocol. The imaging protocol was approved by the Institutional Review Boards of [Sheba Tel HaShomer Medical Center](https://eng.sheba.co.il/) and [Tel Aviv University](https://english.tau.ac.il/), where the {{MRI}} investigations were performed. All participants provided signed informed consent before enrollment in the study.

## MRI Acquisition

Participants were scanned in compliance with the {{TAU}} Brain Brank Initiative's standardized scanning protocol at the [Alfredo Federico Strauss Center for Computational Neuroimaging](https://mri.tau.ac.il/) at Tel Aviv University. Scans were acquired with a 3T Siemens MAGNETOM Prisma {{MRI}} scanner ([Siemens Medical Solutions](https://www.siemens.com/global/en.html), Erlangen, Germany) using a 64-channel {{RF}} head coil. For the purposes of this study, only the {{sMRI}} subset of the protocol which is used for anatomical preprocessing with *FreeSurfer* will be included (see {numref}`smri-sequences` for an overview of acquisition parameters).

```{table} Summary of the {{TAU}} Brain Bank Initiative's {{sMRI}} acquisition parameters.
:name: smri-sequences
:class: small-table

| **Sequence**    | {{TR}} (ms) | {{TE}} (ms) | {{TI}} (ms) | Spatial Resolution ($mm^3$) | Number of Slices | Flip Angle | {{FOV}} (mm) | Acquisition Matrix | Orientation |
|:---------------:|:-----------:|:-----------:|:-----------:|:---------------------------:|:----------------:|:----------:|:------------:|:------------------:|:-----------:|
| **{{MPRAGE}}**  | 2400        | 2.78        | 1000        | 0.9 🞩 0.9 🞩 0.9             | 176              | 8°         | 172 🞩 230    | 192 🞩 256          | Axial       |
| **{{T2w}}**     | 3200        | 554         | -           | 0.9 🞩 0.9 🞩 0.9             | 176              | 120°       | 172 🞩 230    | 192 🞩 256          | Axial       |
| **{{FLAIR}}**   | 8000        | 81          | 2370        | 0.72 🞩 0.72 🞩 4             | 52               | 150°       | 173 🞩 231    | 168 🞩 320          | Axial       |

```

## MRI Data Analysis

To study the effects of various execution configurations, *FreeSurfer* v7.2.0 was used to preprocess the anatomical data cross-sectionally (i.e. as individual datasets, as opposed to longitudinally) using a number of predefined configurations. While *FreeSurfer* does also have a longitudinal processing stream which uses results from the cross-sectional analysis of all time points to create an unbiased within-subject template, the objective of this study is to evaluate inter-subject vs. intra-subject similarity independently of prior knowledge. All runs were executed on a single 64-bit Debian GNU/Linux workstation. Anatomical statistics were extracted for the Destrieux atlas {cite}`Fischl01012004`, which is the most detailed atlas included with *FreeSurfer*'s default reconstruction pipeline's results, and consists of 74 regions per hemisphere.

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
:class: cell-text-center small-table

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

While these options are listed in the documentation website, only a very limited description of their respective effects is provided. In addition, it is unclear to what extent these options are, in fact, utilized by *FreeSurfer* users, and no existing evaluation of either expected effects or usage metrics could be found at the time of writing.

## Statistical Analysis

### Comparison of Anatomical Statistics

Region-wise statistics were generated per scan for the detailed execution configurations (see {numref}`freesurfer-parameters`). Each Destrieux atlas region was represented by four estimated statistics: mean and standard deviation of the cortical thickness, surface area, and grey matter volume. Both whole-brain and region-wise distributions of values were compared.

#### Two-sample Kolmogorov–Smirnov test

The two-sample Kolmogorov–Smirnov ({{KS}}) test is a nonparametric test which qunatifies the distance between the two samples' empirical distribution functions and evaluates the probability of them having been sampled from the same probability distribution. The {{KS}} test was applied using SciPy {cite}`virtanenSciPyFundamentalAlgorithms2020` (see https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ks_2samp.html) to all combinations of *FreeSurfer* execution configurations and p-values were corrected to account for multiple comparisons with statsmodels {cite}`seabold2010statsmodels` (see https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html) using the Bonferroni method {cite}`bonferroni1935calcolo`.

### Model Selection and Optimization

Two types of modeling tasks are evaluated in this study for each execution configuration; (a) classification of the differences between *FreeSurfer*-derived anatomical statistics computed from two independent scans to estimate the probability of a pair of scans belonging to the same participant, and (b) prediction of representative participant attributes (sex, age, and BMI) from these anatomical statistics.

#### Automated Machine Learning

The term Automated Machine Learning (often abbreviated as {{AutoML}}) is used in a number of ways, but generally refers to frameworks built for the automation and optimization of various commonplace procedures often implemented in the process of preparing, training, and tuning machine learning models, particularly on a limited computational budget {cite}`he2021automl`. Using {{AutoML}} frameworks enables searching a very large range of models and optimizing hyperparameters in an effective and reproducible manner.

##### {{FLAML}}

{{FLAML}} is a fast and lightweight {{AutoML}} Python library that finds accurate machine learning models automatically, efficiently and economically {cite}`wang2021flaml` (see https://github.com/microsoft/FLAML). {{FLAML}} is powered by a new, cost-effective hyperparameter optimization and learner selection method invented by Microsoft Research {cite}`wu2021cfo`. It uses a simple, yet effective randomized search method termed FLOW<sup>2</sup> together with adaptive step sizes and random restarts. The estimators compared and optimized by {{FLAML}} include LightGBM {cite}`keLightGBMHighlyEfficient2017` (see https://lightgbm.readthedocs.io/) and XGBoost {cite}`chenXGBoostScalableTree2016` (see https://xgboost.readthedocs.io/), as well as the RandomForestClassifier, ExtraTreesClassifier, and L1 regularized LogisticRegression implementations from the scikit-learn {cite}`pedregosaScikitlearnMachineLearning` library (see https://scikit-learn.org/). All results were standardized within execution configuration as part of the fitting pipeline (see https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html and https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html).

##### {{TPOT}}

{{TPOT}} is a Python Automated Machine Learning tool that optimizes machine learning pipelines based on an evolutionary computation technique called genetic programming ({{GP}}) {cite}`OlsonGECCO2016, Olson2016EvoBio, le2020scaling` (see https://epistasislab.github.io/tpot/). Traditionally, {{GP}} builds trees of mathematical functions to optimize toward given criteria. In {{TPOT}}, GP is used to evolve the sequence of
pipeline operators as well as each operators' parameters (e.g., the number of trees in a random forest or the number of feature pairs to select during feature selection) to maximize the classification accuracy of the pipeline. In terms of the fitting pipeline, {{TPOT}} is based entirely on scikit-learn and includes feature preprocessing and selection.