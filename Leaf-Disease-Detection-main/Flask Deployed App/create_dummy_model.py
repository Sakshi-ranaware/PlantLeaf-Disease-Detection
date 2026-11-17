import torch
import CNN

# Create a dummy model for testing the interface
model = CNN.CNN(39)
torch.save(model.state_dict(), "plant_disease_model_1_latest.pt")
print("Dummy model created successfully!")
