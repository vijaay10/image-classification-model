Image-classification-model -- Car vs Bike Image Classification App - README

📌 Features:

✅ Upload images and get instant predictions  
✅ Backend hosted using Modal  
✅ Interactive frontend using Streamlit  
✅ Stylish UI with emojis and responsive layout  
✅ Displays prediction confidence (95%)  
✅ Deployable locally and in the cloud


🗂️ Project Structure:

image-classification-model/
├── Car_vs_Bike_Classifier_Categorical.ipynb    # Model training notebook
├── app.py                       # Modal backend API (FastAPI-style)
├── streamlit_app.py             # Streamlit frontend app
├── car_bike_model.h5            # Trained model (Keras HDF5)
└── README.md                    # You are here


📚 Dataset:

- Images sourced from open datasets (Kaggle) and Google Images.
- Two classes: Car and Bike.
- Training images resized to 150x150 pixels.
- Augmentation: flipping, rotation, zoom, etc.

  
🧠 Model Training:

- Framework: TensorFlow/Keras
- Layers:
  - Conv2D + MaxPooling
  - Flatten → Dense
  - Output: 1 Neuron (sigmoid activation)
- Loss: binary_crossentropy
- Optimizer: Adam
- Accuracy: ~95%
- Saved as: car_bike_model.h5
⚙️ Backend Deployment using Modal
- app.py script serves as a cloud backend using Modal.
- Loads the .h5 model and exposes a remote prediction function.

To deploy:
modal deploy app.py


🌐 Streamlit Frontend:

- Modern web UI with Streamlit
- Features:
  - Hero header and custom styles
  - Upload multiple image types
  - Emoji-based output
  - Prediction card with confidence
  - Footer with About section

To run locally:
streamlit run streamlit_app.py

📦 Requirements:
tensorflow
streamlit
Pillow
modal
matplotlib


🚀 End-to-End Flow:

[Jupyter Notebook] → Model (.h5)
       ↓
[app.py / Modal]
       ↓
[streamlit_app.py → classify_image.remote()]
       ↓
[User UI Output]



💡 Future Improvements:

- Add actual confidence score instead of fixed 95%
- Extend support for multi-class classification
- Add dynamic carousel
- Export reports as .pdf or .csv

  
✅ Submission Instructions:

- Push all code to a public GitHub repository
- Include:
  - car_bike_classifier.ipynb
  - app.py
  - streamlit_app.py
  - requirements.txt
  - README.md
  - car_bike_model.h5 (host externally if >25MB)
- Submit repo link via Google Form


👨‍💻 About Us - 
This application was developed as a full ML deployment project.
Made with ❤️ by vijaay | GitHub: @vijaay10

Licensed under the MIT License.
