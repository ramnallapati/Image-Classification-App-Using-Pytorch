import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import cv2
import os


# -----------------------------
# Custom Convolutional Model
# -----------------------------
class CustomCNNModel(nn.Module):
    def __init__(self, input_dim, num_classes):
        super().__init__()
        self.input_dim = input_dim
        self.num_classes = num_classes

        # Convolutional layers
        self.conv_layers = nn.Sequential(
            # Convolution block 1
            nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),

            # Convolution block 2
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),

            # Convolution block 3
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),

            # Convolution block 4
            nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )

        # Automatically calculate FC input size
        self._to_linear = None
        self._get_conv_output(self.input_dim)

        # Fully connected layers
        self.fc_layer = nn.Sequential(
            nn.Linear(self._to_linear, 512),
            nn.ReLU(),
            nn.Linear(512, 128),
            nn.ReLU(),
            nn.Linear(128, self.num_classes)
        )

    def _get_conv_output(self, input_dim):
        with torch.no_grad():
            dummy_input = torch.zeros(1, 3, input_dim, input_dim)
            output = self.conv_layers(dummy_input)
            self._to_linear = output.view(1, -1).size(1)

    def forward(self, x):
        x = self.conv_layers(x)
        x = x.view(x.size(0), -1)
        x = self.fc_layer(x)
        return x


# -----------------------------
# Image Classifier (Inference)
# -----------------------------
class ImageClassifier:
    def __init__(self, model_path, class_name=None):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.model = CustomCNNModel(input_dim=128, num_classes=3).to(self.device)

        self.model.load_state_dict(
            torch.load(model_path, map_location=self.device)
        )
        self.model.eval()

        if class_name is None:
            self.class_name = {0: 'Cat', 1: 'Dog', 1: 'Person'}
        else:
            self.class_name = class_name

        self.transform = transforms.Compose([
            transforms.Resize((128, 128)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5],
                                 std=[0.5, 0.5, 0.5])
        ])

    def predict(self, image_path):
        image = Image.open(image_path).convert("RGB")
        image_tensor = self.transform(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            output = self.model(image_tensor)
            _, predicted = torch.max(output, 1)

        label = self.class_name[predicted.item()]

        # Draw prediction on image
        image_cv = cv2.imread(image_path)
        cv2.putText(
            image_cv,
            label,
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        output_path = "labeled_image.jpg"
        cv2.imwrite(output_path, image_cv)

        output_path = os.path.join(os.getcwd(), output_path)
        return label, output_path
