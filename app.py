import gradio as gr
import os
from Core.predict import ImageClassifier
from PIL import Image

cwd = os.getcwd()
model_path = os.path.join(cwd, "model", "cnn_model.pth")
assert os.path.exists(model_path), "Model file not found!"

classifier = ImageClassifier(model_path, class_name=None)


def classify_image(image):
    image_path = os.path.join(cwd, "uploaded_image.jpg")
    image.save(image_path)

    label, output_path = classifier.predict(image_path)
    return label, Image.open(output_path).convert("RGB")


demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil", image_mode="RGB"),
    outputs=[
        gr.Textbox(label="Prediction"),
        gr.Image(label="Labeled Image")
    ],
    title="Image Classification Gradio App",
    description="Upload an image to classify it as Dog, Cat, or Person"
)

if __name__ == "__main__":
    demo.launch()
