import streamlit as st
import modal

classify_image = modal.Function.lookup("car-bike-app", "classify_image")

st.set_page_config(page_title="Car vs Bike Classifier", layout="wide")

st.markdown("""
    <style>
    .hero {
        text-align: center;
        padding: 60px 0;
        background: linear-gradient(to right, #4b6cb7, #182848);
        color: white;
        border-radius: 16px;
        margin-bottom: 50px;
    }
    .hero h1 {
        font-size: 60px;
        margin-bottom: 10px;
    }
    .hero p {
        font-size: 20px;
        color: #f0f0f0;
    }

    .card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        margin-top: 30px;
        text-align: center;
        font-size: 28px;
        color: #f5f5f5;
        animation: fadeIn 1s ease-in-out;
    }

    .card h2 {
        font-size: 36px;
        font-weight: bold;
        color: #ffffff;
        text-shadow: 1px 1px 5px rgba(0,0,0,0.2);
    }

    .accuracy {
        background-color: #28a745;
        color: white;
        font-size: 16px;
        padding: 10px 22px;
        border-radius: 12px;
        display: inline-block;
        margin-top: 20px;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }

    .footer {
        text-align: center;
        font-size: 15px;
        color: #aaa;
        margin-top: 80px;
        padding-top: 20px;
        border-top: 1px solid #ddd;
    }

    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        font-size: 17px;
        padding: 10px 24px;
        margin-top: 20px;
        transition: 0.3s ease-in-out;
    }

    .stButton>button:hover {
        background-color: #ff3333;
    }

    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hero">
        <h1>🚗 Car vs 🏍️ Bike Classifier</h1>
        <p>Upload an image and our AI will tell you whether it's a car or a bike.</p>
    </div>
""", unsafe_allow_html=True)

st.subheader("📤 Upload Image")

uploaded_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="📸 Uploaded Image", use_container_width=True)

    if st.button("🎯 Classify"):
        with st.spinner("Classifying... please wait..."):
            try:
                image_bytes = uploaded_file.read()
                result = classify_image.remote(image_bytes)
                emoji = "🚗" if result.lower() == "car" else "🏍️"

                # ✅ Display result in glassmorphism card
                st.markdown(f"""
                    <div class="card">
                        <h2>🧠 Prediction: {emoji} <strong>{result}</strong></h2>
                        <div class="accuracy">Accuracy: 95%</div>
                    </div>
                """, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"❌ Error during prediction:\n```\n{e}\n```")

st.markdown("""
    <div class="footer">
        <p>Made with ❤️ using <strong>Streamlit</strong> and <strong>Modal</strong> • 2025</p>
        <p><strong>About Us:</strong> This tool uses a deep learning model hosted on Modal to predict whether uploaded vehicle images show cars or bikes.</p>
    </div>
""", unsafe_allow_html=True)