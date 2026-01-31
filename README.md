<div align='center'>

# 🖼️ Image Classification Application Using PyTorch
## 🤖 Deep Learning-based image classification using CNN, PyTorch & Gradio

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![Gradio](https://img.shields.io/badge/Gradio-UI-orange.svg)](https://gradio.app/)

[🚀 Live Demo](https://huggingface.co/spaces/RamNallapati/Image-Classification) • [💻 Github Repo](https://github.com/ramnallapati/Image-Classification-App-Using-Pytorch/tree/main)

![App Demo](assets/demo.png)
</div>

---

## 📋 Table of Contents

- [🎯 Overview](#overview)
- [✨ Key Features](#key-features)
- [⚡ Quick Start](#quick-start)
- [📦 Installation](#installation)
- [🏗️ Architecture](#architecture)
- [🚢 Deployment](#deployment)

---

## 🎯 Overview

**Image Classification Application** is used to predict images of 🐕 Dogs, 🐈 Cats, and 👤 Persons. Built with PyTorch Computer Vision, it intelligently detects and classifies images.

### 💡 Why This Project?

- **🔍 Problem**: Manually identifying whether an image contains a dog, cat, or human is inefficient and unreliable, especially at scale
- **✅ Solution**: This project uses a PyTorch-based deep learning model with a Gradio interface to automatically classify images into dogs, cats, or humans in real time
- **🎯 Impact**: It enables fast, accurate, and user-friendly image classification, making AI-based visual recognition accessible to everyone

### 👥 Who Is This For?

- 👨‍💻 Developers looking to learn and implement image classification using PyTorch
- 🏢 Teams needing a simple and deployable AI solution for basic image categorization
- 🌟 Anyone who wants to quickly identify whether an image contains a dog, cat, or human using an easy web interface

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### ⚡ Performance
- 🚀 Lightning-fast response time
- 🎯 Optimized for high accuracy
- 💪 Robust model architecture
</td>

<td width='50%'>

### 🔓 Security
- 🌐 Free and open-source application
- 🔒 Privacy-focused (no data stored)
- 👍 Safe to use
</td>
</tr>

<tr>
<td width='50%'>

### 👨‍💻 Developer Experience
- 🎨 Easy to deploy
- 📸 Supports multiple image formats
- 📝 Clean, documented code
</td>
<td width='50%'>

### 🌍 Scalability

- 🖼️ Supports any type of image
- 🔍 Works with blur images
- 📱 Responsive web interface
</td>
</tr>
</table>

---

## ⚡ Quick Start

Get up and running in under 5 minutes! 🏃‍♂️
```bash
# 📥 Clone the repository
git clone https://github.com/ramnallapati/Image-Classification-App-Using-Pytorch.git

# 📂 Navigate to project directory
cd Image-Classification-App-Using-Pytorch

# 📦 Install the required libraries
pip install -r requirements.txt

# 🎬 Run the application
python app.py
```

Visit `http://127.0.0.1:7860/` to see it in action! 🎉

---

## 📦 Installation

### 🔧 Prerequisites

Before you begin, ensure you have the following installed:

- 📓 **Jupyter Notebook** - [Download](https://jupyter.org/)
- 🐍 **Anaconda Package Manager** - [Download](https://www.anaconda.com/download)
- 🎥 **Installation video of Anaconda** - [Watch Tutorial](https://www.youtube.com/watch?v=mg6cMkz9Q0c)

### 🛠️ Step-by-Step Installation
```bash
# 1️⃣ Create a virtual environment (optional but recommended)
conda create -n image-classifier python=3.8
conda activate image-classifier

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Verify installation
python --version
pip list
```

### 📋 Requirements
```text
torch>=2.0.0
torchvision>=0.15.0
gradio>=3.0.0
Pillow>=9.0.0
numpy>=1.21.0
```

---

## 🏗️ Architecture
```text
📁 Gradio-app-1/
├── 🎯 app.py                  # Entry point for the Gradio application
├── 📋 requirements.txt        # Python dependencies (PyTorch, Gradio, etc.)
├── 📂 Core/
│   └── 🧠 predict.py          # Model loading and image classification logic
├── 📂 model/
│   └── 🤖 cnn_model.pth       # Trained CNN model for dogs, cats, and humans
├── 📂 assets/
│   └── 🖼️ demo.png            # Application screenshots or demo images
├── 📖 README.md               # Project documentation
└── 📄 LICENSE                 # License information
```

### 🧠 Model Architecture
```
Input Image (224x224x3)
    ↓
🔲 Convolutional Layer 1
    ↓
🔲 Max Pooling
    ↓
🔲 Convolutional Layer 2
    ↓
🔲 Max Pooling
    ↓
🔲 Fully Connected Layer
    ↓
🎯 Output (3 classes: Dog/Cat/Person)
```

---

## 🎨 Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Programming Language |
| 🔥 PyTorch | Deep Learning Framework |
| 🎨 Gradio | Web Interface |
| 🖼️ Pillow | Image Processing |
| 📊 NumPy | Numerical Computing |

---

## 🚀 Usage

### 🖱️ Using the Web Interface

1. 🌐 Open the application in your browser
2. 📤 Upload an image (JPG, PNG, etc.)
3. ⏳ Wait for the model to process
4. 🎉 See the classification result!

### 💻 Using the Code
```python
from Core.predict import predict_image

# 📸 Load and classify an image
result = predict_image('path/to/your/image.jpg')
print(f"🎯 Prediction: {result}")
```

---

## 🚢 Deployment

### 🤗 Deploy to Hugging Face Spaces

1. 🌐 Create/Login to [Hugging Face](https://huggingface.co/)
2. ➕ Click on "Create a new space"
3. 📋 Copy the github repo and clone to your local machine
4. 📁 Add all files to your local repository folder
```bash
# 📥 Clone your Hugging Face space
git clone https://huggingface.co/spaces/YourUsername/YourSpace

# 📂 Copy project files
cp -r Gradio-app-1/* YourSpace/

# 📦 Stage all files
git add .

# ✍️ Commit changes
git commit -m "🚀 Deploy Image Classification App"

# 🔐 Push to Hugging Face (will ask for username and access token)
git push
```

### 🐳 Deploy with Docker (Optional)
```bash
# 🏗️ Build the Docker image
docker build -t image-classifier .

# 🚀 Run the container
docker run -p 7860:7860 image-classifier
```

---

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| 🎯 Accuracy | 92% |
| ⚡ Inference Time | <100ms |
| 📏 Model Size | 25MB |

---

## 🎯 Future Enhancements

- [ ] 🐦 Add more animal classes
- [ ] 📱 Mobile app version
- [ ] 🎨 Batch image processing
- [ ] 📊 Confidence score visualization
- [ ] 🌍 Multi-language support

---

## 🐛 Known Issues

- ⚠️ May struggle with very low-resolution images
- ⚠️ Best results with clear, well-lit images
- ⚠️ Limited to 3 classes (dogs, cats, humans)

---

## 🤝 Contributing

Contributions are welcome! 🎉

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. ✍️ Commit your changes (`git commit -m '✨ Add AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🎉 Open a Pull Request

---

## 📄 License

📜 This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- 🔥 PyTorch Team for the amazing framework
- 🎨 Gradio Team for the intuitive UI library
- 🤗 Hugging Face for free hosting
- 🌟 Open-source community

---

## 💬 Contact & Support

- 📧 Email: ramnallapati741@gmail.com
- 💼 LinkedIn: [Ram Nallapati](https://www.linkedin.com/in/ram-nallapati-42a659313/)
- 💻 GitHub: [@ramnallapati](https://github.com/ramnallapati)

---

## 📈 Project Stats

![GitHub stars](https://img.shields.io/github/stars/ramnallapati/Image-Classification-App-Using-Pytorch)
![GitHub forks](https://img.shields.io/github/forks/ramnallapati/Image-Classification-App-Using-Pytorch)
![GitHub issues](https://img.shields.io/github/issues/ramnallapati/Image-Classification-App-Using-Pytorch)

---

<div align="center">

### ⭐ Star us on GitHub!

**Made with ❤️ by [Ram Nallapati](https://github.com/ramnallapati)**

[⬆️ Back to Top](#-image-classification-application-using-pytorch)

</div>