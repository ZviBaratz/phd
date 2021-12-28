# Hypothesis and Goals

<hr>

## Hypothesis

The hypothesis driving this study is that individual differences in brain features, as estimated using MRI, are representative of individual differences in identity.

Our brains are not just unique to us at birth, they are unique to our environment and experiences (REFERENCES). The opposite is true as well, shared traits and experiences mutate the composition and dynamics of our brains in similar ways (REFERENCES). The ability to characterize the expression of these variations and similarities is, first and foremost, limited by the ability to acquire adequately detailed and precise representations over a large enough population.

This study will assess the ability to demonstrate a statistically significant relationship between commonly used MRI-derived brain features and subject-specific cognitive and demographic information.

## Goals

### Creating the foundations for customized large-scale MRI data aggregation and analytics

The management and distribution of highly variable MRI and demographic data from a large population, collected over many years and across imaging centers, requires a framework that will enable the production of robust and reproducible findings.

In order to maximize available resources, a dedicated database application will be created to centralize and orchestrate all data archiving and preprocessing requirements. This preliminary step will also provide the foundation for further investigation of the aggregated dataset in the future, outside the scope of this thesis. The focus of the application will be:

1. **Managing general research information and subject identities.** Being able to reliably identify subjects and associate collected data is a fundamental prerequisite of any scientific study. The complexity of this procedure is drastically inflated by the scale and variability in the collected sample.
2. **Automatic raw MRI data conversion, metadata extraction, and cataloging.** The application will use existing tools and prior knowledge to automatically transform raw DICOM format files to a BIDS-compatible dataset. In addition, all relevant metadata will be serialized to an SQL-based database for safe and efficient querying.
3. **Preprocessing pipelines orchestration.** Batch execution of preconfigured preprocessing pipelines will be managed by the application and all execution parameters, inputs, and outputs will be serialized to the database.
4. **Access and data distribution management.** Collaborators and administrators should be able to easily access the platform, query information, and retrieve data or preprocessing results.

### *Establishing the reliability and specificity of the collected measurements*

Assuming the hypothesis is correct, differences in subject representations represent differences in identity. This distance may be quantified and used as a metric to demonstrate that:

  1. **Differences in estimated brain features vary significantly more across subjects than within.** A single subject's representation in the MR space should be distinguishably closer to the same subject's representation in a different time point than to another subject's. This idea is comparable to a "brainprint", and will serve to support the underlying assumption that our instruments are accurate and detailed enough to generate an identity-informative representation at all. In the words of Heraclitus: "No man ever steps in the same river twice. For it’s not the same river, and he’s not the same man."
  2. **Same-subject differences in estimated brain features grow over time.** Assuming the variation in the estimated brain features originates more from changes in their true values than it does from noise, it should be possible to demonstrate a correlation between the single-subject representation differences and the difference in time.

### *Characterizing the expression of subject traits and demographic information*

Having established the relationship between the estimated brain features and subject identity, the final goal will be to lay a robust foundation for the characterization of various subject traits and demographic information from MRI-derived data. The main obstacle in increasing the specificity of the target subject variable is that the size of the sample dramatically shrinks (more specific information is available for fewer subjects). For the purposes of this study, the following attributes will be used: *sex, dominant hand, age, height, weight, BFI scores*.

Extensive EDA will be applied to evaluate the variance of the chosen attributes in the sample and inform any subsequent statistical or modeling decisions.
