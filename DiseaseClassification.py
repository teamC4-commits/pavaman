
from advisory import get_advisory
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
from io import BytesIO
import base64
from tensorflow.keras.applications.efficientnet import preprocess_input

# Load model once and cache
@st.cache_resource
def load_my_model():
    return load_model("model.keras")

class_labels=['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Background_without_leaves',
 'Blueberry___healthy',
 'Cherry___Powdery_mildew',
 'Cherry___healthy',
 'Corn___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn___Common_rust',
 'Corn___Northern_Leaf_Blight',
 'Corn___healthy',
 'Grape___Black_rot',
 'Grape__Esca(Black_Measles)',
 'Grape__Leaf_blight(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange__Haunglongbing(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,bell__Bacterial_spot',
 'Pepper,bell__healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']

# Convert image to base64 for HTML rendering
def image_to_base64(img):
    buffer = BytesIO()
    img.save(buffer, format="JPEG")
    return base64.b64encode(buffer.getvalue()).decode()

def predict_disease(img: Image.Image, model, class_labels):
    img = img.resize((160, 160))  
    img_array = preprocess_input(image.img_to_array(img))
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    predicted_class = class_labels[np.argmax(prediction)]
    confidence = np.max(prediction) * 100
    return predicted_class, confidence


def app():
    st.title("Plant Disease Predictor")

    uploaded_file = st.file_uploader("Upload leaf image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        model = load_my_model()
        predicted_class, confidence = predict_disease(img, model, class_labels)
        advisory = get_advisory(predicted_class)

       
        left_col, right_col = st.columns(2)

        with left_col:
            st.markdown(
                f"""
                <img src="data:image/jpeg;base64,{image_to_base64(img)}"
                     width="350" height="250"
                     style="object-fit: cover; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.2);">
                """,
                unsafe_allow_html=True
            )

        with right_col:
            youtube_link = advisory["youtube_link"]

            if youtube_link:
                youtube_embed = youtube_link.replace("watch?v=", "embed/")
                st.markdown(
                    f"""
                    <iframe width="350" height="250"
                    src="{youtube_embed}"
                    frameborder="0"
                    allowfullscreen
                    style="border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.2);">
                </iframe>
                """,
                unsafe_allow_html=True
                )
            else:
                st.warning("YouTube video not available for this disease.")
        st.markdown("---")

        info_box = f"""
        <div style="
            border: 2px solid white;
            padding: 20px;
            border-radius: 10px;
            color: white;
            background-color: transparent;
            margin-top: 20px;
            font-size: 16px;
        ">
            <p><b>Prediction:</b> {predicted_class}</p>
            <p><b>Disease Name:</b> {advisory['disease_name']}</p>
            <p><b>Description:</b> {advisory['description']}</p>
            <p><b>Treatment:</b> {advisory['treatment']}</p>
            <p><b>Prevention:</b> {advisory['prevention']}</p>
        </div>
        """

        st.markdown(info_box, unsafe_allow_html=True)


