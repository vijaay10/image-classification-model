import modal
import tensorflow as tf
from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image as PILImage
import numpy as np
from io import BytesIO

app = modal.App("car-bike-app")
volume = modal.Volume.from_name("car-bike-model-vol", create_if_missing=True)

custom_image = modal.Image.debian_slim().pip_install(
    "fastapi[standard]", "tensorflow", "numpy", "Pillow"
)

@app.local_entrypoint()
def main():
    try:
        with volume.batch_upload() as batch:
            batch.put_file("car_vs_bike_model.h5", "/model/car_vs_bike_model.h5")
            print("✅ Model uploaded to volume.")
    except FileExistsError:
        print("⚠️ Model already exists in volume. Skipping upload.")

@app.function(image=custom_image, volumes={"/model": volume})
def web_app():
    fastapi_app = FastAPI()
    model = tf.keras.models.load_model("/model/car_vs_bike_model.h5")

    def preprocess(file: UploadFile):
        image = PILImage.open(BytesIO(file.file.read())).convert("RGB").resize((224, 224))
        image_array = np.array(image).astype("float32") / 255.0
        return np.expand_dims(image_array, axis=0)

    @fastapi_app.post("/predict")
    async def predict(file: UploadFile):
        input_array = preprocess(file)
        prediction = model.predict(input_array)[0]
        label = "Car" if np.argmax(prediction) == 0 else "Bike"

        return JSONResponse({
            "label": label,
            "car": float(prediction[0]),
            "bike": float(prediction[1])
        })

    return fastapi_app

@app.function(
    name="classify_image",
    serialized=True,
    volumes={"/model": volume},
    image=modal.Image.debian_slim().pip_install("tensorflow", "Pillow", "numpy")
)
def classify_image(image_bytes: bytes) -> str:
    model = tf.keras.models.load_model("/model/car_vs_bike_model.h5")

    img = PILImage.open(BytesIO(image_bytes)).convert("RGB").resize((224, 224))
    img_array = np.array(img).astype("float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0]
    label = "Car" if np.argmax(prediction) == 1 else "Bike"
    return label