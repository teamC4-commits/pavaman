

`markdown
# 🌾 CropScope - Multispectral Crop Analysis & Disease Detection Platform

**Empowering Precision Farming with Multispectral Imaging + Deep Learning**

CropScope is an AI-powered platform for precision agriculture that combines multispectral vegetation analysis with deep learning–based disease detection. Designed with a simple Streamlit interface, the platform helps farmers and researchers assess plant health, monitor crop growth, and receive real-time disease advisories.

---

## 🚀 Demo

📺 https://hackathonpavaman2.streamlit.app/

---

## 📌 Features

### 🛰 Multispectral Health Analysis
- NDVI and NDRE index calculations from TIFF images (DJI drones)
- Time-series NDRE comparison to estimate crop growth or stress
- Heatmaps, overlays, and trend visualizations

### 🌿 Disease Detection (39 Plant classes)
- Classify leaf images using EfficientNet CNN
- Trained on PlantVillage dataset
- Displays disease name, treatment steps, prevention advice, and embedded YouTube tutorials

### 🖥 Streamlit Web Interface
- Upload multispectral `.tiff` bands or RGB leaf images
- Dual mode: Vegetation Health & Disease Prediction
- Real-time classification + user-friendly visual output

---

## 💻 Streamlit Application Overview

CropScope’s Streamlit app provides an intuitive interface for agricultural image analysis with focus on NDVI and NDRE-based assessments.

### 🔑 Key Streamlit Features

#### 🧾 User Interface:
- Option to choose analysis type (NDVI / NDRE / Disease Detection)
- Upload .tiff files with drag-and-drop support
- Classification results + visualization shown side by side

#### 🌈 Image Processing:
- Uses `tifffile` to read multispectral Red, NIR, and Red Edge bands
- Computes NDVI and NDRE indices and displays them as color-mapped images

#### 📊 NDVI/NDRE Analysis:
- **NDVI**: Assesses vegetation health
- **NDRE**: Assesses nutrient stress and growth stage
- Time-series comparison for growth estimation via NDRE difference maps

#### 🧠 Model Integration:
- Random Forest classifier for NDVI health categories
- CNN (EfficientNetB4) model for disease detection from RGB leaf images

#### 📉 Visualization:
- Uses `matplotlib` for rendering maps with consistent layout, colorbars, and titles
- NDRE difference maps display growth:  
  - 🔼 Positive  → Growth  
  - 🔽 Negative  → Regression  
  - ⚪ Zero  → Stagnation

---

## 🧠 Tech Stack

| Layer       | Tools / Frameworks             |
|------------|---------------------------------|
| Frontend   | Streamlit (Python)              |
| Backend    | Python, TensorFlow/Keras, scikit-learn |
| ML Models  | Random Forest (NDVI), EfficientNetB4 (Disease CNN) |
| Visualization | Matplotlib, OpenCV, Seaborn    |
| Data       | TIFF bands (DJI drone), PlantVillage dataset |

---

## 🗂 Dataset Summary

- **Multispectral TIFFs** from DJI drone (Red, Green, NIR, Red Edge)
- **RGB Leaf Images** from PlantVillage – 38 disease classes
- Indexes calculated:
  - `NDVI = (NIR - Red) / (NIR + Red + 1e-6)`
  - `NDRE = (NIR - Red Edge) / (NIR + Red Edge + 1e-6)`

---

## 📊 Model Performance

### NDVI Classifier (Random Forest)
- Output Labels: `Healthy`, `Sparse`, `Barren`

### Disease Detector (EfficientNetB4)
- **Accuracy:** 98.7%
- **Precision/Recall:** ~95%+
- Example IoU:
  - Tomato Yellow Leaf Curl Virus: 98.71%
  - Potato Late Blight: 87.38%
  - Grape Leaf Blight: 99.08%

---

## 📈 Visual Outputs

- NDVI/NDRE heatmaps (RdYlGn colormap)
- NDRE overlays on RGB images
- NDRE difference maps for growth tracking
- Clustering (KMeans) and regression analysis for NDVI/NDRE evaluation

---

## 🔮 Future Scope

- Mobile app with field capture + instant advisory
- Real-time satellite image integration
- Pest detection using object detection (YOLOv8 or DETR)
- Voice-based chatbot for farmer queries

---

## ❌ Limitations

- No GPS/geotagging
- No hyperspectral or LiDAR support

---

## 🛠 How to Run Locally

bash
git clone [https://github.com/teamC4-commits/pavaman]
cd CropScope
pip install -r requirements.txt
streamlit run main.py
`

> 💡 Sample TIFF images and trained models should be placed in the `/data` and `/models` folders respectively.

---

## 📚 Research Contribution

CropScope contributes toward democratizing precision agriculture using low-cost drones, computer vision, and deep learning. The platform architecture can be adapted for future research in smart farming, disease surveillance, and AI in agriculture.

---

## 👨‍💻 Team C4 - Hackathon Edition

* 🔬 Backend & Modeling: NDVI/NDRE indexers, CNN model
* 🎨 UI & Integration: Streamlit web interface, data visualizations
* 📖 Research & Advisory Mapping: Disease info, treatments, YouTube embeds

---

## 📎 License

This project is for academic and hackathon use only.
