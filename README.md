# ITRI616_ML_PROJECT

## Deep Convolutional Neural Network (DCNN)
## Random Forest (RF)

### Overview of Notebooks

- `notebook_identity.ipynb`:  
  For training a DCNN on **binary grayscale portrait images** with **different identities** to evaluate the effect of identity variation and apply basic augmentations to improve generalization.

- `notebook_dcnn_rf.ipynb`:  
  Extraction of deep image features from the trained **DCNN**, followed by training a **Random Forest (RF)** classifier on those features for comparative evaluation and hybrid modeling.

### Dictionary for Spell Checker

- `.cspell.json`:  
  JSON file containing common words used to avoid unnecessary spell checking warnings in the editor (e.g., model names, acronyms).

### File to Ignore Commits

- `.gitignore`:  
  Specifies which folders/files to exclude from version control (e.g., `venv/`, dataset folders, checkpoints).

### Run Initial Python Scripts for Dataset Preparation

To segment your binary dataset for identity-based training, run:

```bash
!python python_scripts/identity_split_dataset.py