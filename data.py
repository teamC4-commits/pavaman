import streamlit as st

def app():
    st.title("Dataset Structure")

    st.markdown("### Root Directory: `data/`")
    st.code(
        '''
data/
├── plantvillage_dataset/                  ← Original dataset folder
│   ├── Apple___Apple_scab/
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   │   └── ...
│   ├── Apple___Black_rot/
│   │   ├── img1.jpg
│   │   └── ...
│   └── ... (more class folders)

├── split/                                 ← Preprocessed split dataset
│   ├── train/
│   │   ├── Apple___Apple_scab/
│   │   │   ├── img1.jpg
│   │   │   └── ...
│   │   ├── Apple___Black_rot/
│   │   │   └── ...
│   │   └── ...
│
│   ├── test/
│   │   ├── Apple___Apple_scab/
│   │   │   └── ...
│   │   └── ...
│
│   └── val/
│       ├── Apple___Apple_scab/
│       │   └── ...
│       └── ...
        ''',
        language='text'
    )
    explanation = """
<div style="
    border: 2px solid white;
    padding: 15px;
    border-radius: 10px;
    color: white;
    background-color: transparent;
    margin-top: 20px;
">
    <p><b>Understanding TheDataset Structure</b></p>
    <p>Welcome to our Plant Disease Detection system! Here's a quick look at ho the our data is organized so that our model can learn effectively:</p>
    <p>🌱 <b>1. plantvillage_dataset/</b><br>
    This is the dataset, collected for the prediction project.<br>
    It contains thousands of images of crop leaves, with and without diseases.<br>
    Each folder inside this directory represents a specific disease or a healthy condition.</p>
    <p><b>2. split/ Folder</b><br>
    To train our machine learning model properly, we’ve divided the data into 3 parts:</p>
    <ul>
      <li><b>train/</b>: Used by our model to learn patterns from the data.</li>
      <li><b>val/ (validation):</b> Helps fine-tune the model while training.</li>
      <li><b>test/</b>: Used to evaluate the final model performance on unseen data.</li>
    </ul>
</div>
"""

    st.markdown(explanation, unsafe_allow_html=True)

   
