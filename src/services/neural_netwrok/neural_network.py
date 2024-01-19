import torchvision.transforms as transforms
import torch
from src.services.neural_netwrok.resnet_netwrok import  ResNet


class NeuralNetwork:
    def __init__(self):
        self.device = None
        self.get_default_device()
        self.model = ResNet()
        self.to_device(self.model, self.device)
        self.model.load_state_dict(torch.load("model_file.pt", map_location=torch.device(self.device)))
        self.model.eval()
        self.transformations = transforms.Compose([transforms.Resize((256, 256)), transforms.ToTensor()])
        self.classes = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

    def predict_image(self, img):
        # Convert to a batch of 1
        xb = self.to_device(img.unsqueeze(0), self.device)
        # Get predictions from model
        yb = self.model(xb)
        # Pick index with the highest probability
        prob, preds = torch.max(yb, dim=1)
        # Retrieve the class label
        return self.classes[preds[0].item()]

    def get_default_device(self):
        """Pick GPU if available, else CPU"""
        if torch.cuda.is_available():
            self.device = torch.device('cuda')
        else:
            self.device = torch.device('cpu')

    def predict_external_image(self, image):
        return self.predict_image(self.transformations(image))

    def to_device(self, data, device):
        """Move tensor(s) to chosen device"""
        if isinstance(data, (list, tuple)):
            return [self.to_device(x, device) for x in data]
        return data.to(device, non_blocking=True)

    def predict_image(self, img, model):
        # Convert to a batch of 1
        xb = self.to_device(img.unsqueeze(0), self.device)
        # Get predictions from model
        yb = model(xb)
        # Pick index with the highest probability
        prob, preds = torch.max(yb, dim=1)
        # Retrieve the class label
        return self.classes[preds[0].item()]

    def predict_external_image(self, model, image):
        return self.predict_image(self.transformations(image), model)

