import streamlit as st

def app():
    st.title("📖 How to Run the Plant Disease Predictor App")

    container_style = """
        border: 2px solid white; 
        padding: 20px; 
        border-radius: 10px; 
        color: white; 
        background-color: #222;
        font-family: monospace;
    """

    with st.container():
      

        st.markdown("### Step 1: Clone the Repository")
        st.code("""
git clone https://github.com/muraxxxsrin/PAVAMAN.git
cd PAVAMAN
        """, language="bash")

        st.markdown("---")

        st.markdown("### Step 2: Install Dependencies")
        st.code("pip install -r requirements.txt", language="bash")

        st.markdown("---")

        st.markdown("### Step 3: Run the Streamlit App")
        st.code("streamlit run app.py", language="bash")

        st.markdown("---")

        st.markdown("### Step 4: Open the App in Browser")
        st.markdown(
            "After running the command, open the URL shown in your terminal "
            "(usually http://localhost:8501)."
        )

        st.markdown("---")

        st.markdown("### Notes:")
        st.markdown(
            "- Make sure your model files (.keras) are placed correctly.\n"
            "- Stop the app anytime by pressing Ctrl+C in your terminal."
        )

        st.markdown("</div>", unsafe_allow_html=True)
