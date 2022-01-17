#!/usr/bin/env python
# coding: utf-8

# (methods:imaging)=
# # Imaging

# ## Structural MRI

# ### T1-weighted

# #### MPRAGE

# The three-dimensional magnetization-prepared rapid gradient-echo (3D {{MPRAGE}}) {cite}`muglerThreedimensionalMagnetizationpreparedRapid1990` is a commonly used {{T1w}} {{sMRI}} scanning sequence which optimizes the contrast between different types of tissue and provides anatomical information with outstanding detail. It is a standard sequence, also included in other contemporary large-scale neuroimaging datasets, such as the {{HCP}} {cite}`harmsExtendingHumanConnectome2018`, {{ABIDE}} II {cite}`dimartinoEnhancingStudiesConnectome2017`, and {{ADNI}} {cite}`hua3DCharacterizationBrain2008`. Unfortunately, some variation does still exist in the scanning parameters. The following table summarizes the prevalence of each distinct protocol specification in the included dataset:

# In[1]:


from phd.methods.tables import display_mprage_counts

display_mprage_counts()


# ### Diffusion-weighted MRI

# ## Functional MRI

# ### rs-fMRI
