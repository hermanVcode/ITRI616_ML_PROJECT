# Deep Convolutional Neural Network (DCNN) for Feature Extraction and Classification of Images

## ITRI616 MACHINE LEARNING CLASSIFICATION PROJECT

### Project Description

A Deep Convolutional Neural Network (DCNN) is used to extract deep features from face images and perform binary classification (**smiling** vs. **not smiling**).

#### Dataset
- The classification was done using the [CelebA dataset](https://www.kaggle.com/datasets/jessicali9530/celeba-dataset).

#### License
- The dataset is available for non-commercial research purposes only, as per its license. All images are the property of their respective authors.

---

### Project Structure

- **Notebook:**  
  `notebooks/notebook_smile.ipynb`  
  Loads preprocessed images, trains DCNN, evaluates performance, and saves the trained model.

- **Script:**  
  `python_scripts/preprocessing_image_size.py`  
  Resizes CelebA images from original size to 128x128 and saves them in the `data/img_align_preprocessed/` folder.

- **Models:**  
  `models/`  
  Directory where trained models (with timestamps) are saved.

- **Dictionary for Spell Checker:**  
  `.cspell.json`  
  Contains common words used in the project to avoid unnecessary spell-check warnings (e.g., model names, acronyms).

- **Git Ignore File:**  
  `.gitignore`  
  Specifies which folders/files to exclude from version control (e.g., `venv/`, dataset folders, checkpoints).

---

### Setup 

1. **Create and activate a virtual environment** (recommended):

   **On Windows:**
   - bash
   - python -m venv venv
   - venv\Scripts\activate
  
   **On Mac/Linux:**
   - bash
   - python3 -m venv venv
   - source venv/bin/activate
2. **Install dependencies:**
   - bash
   - pip install -r requirements.txt
3. Preprocess the dataset:
   - Open the `preprocessing_image_size.py` script, and adjust the amount of samples in `images_to_process = int(`<amount_here>`)`.
   - Enter the following in the terminal **(Ensure that it is entered in the root of the directory with venv activated)**`python python_scripts/preprocessing_image_size.py`.
   - This will (resize the amount of images selected to 128x128).
4. Run the notebook:
   - Open the `notebooks/notebook_smile.ipynb` in **Jupyter/VS Code**.
   - In the VS Code command palette (Ctrl+Shift+p), type `Jupyter: Restart Kernel and Run All Cells`.
   - This will run all cells to train, evaluate, and save the model. 
