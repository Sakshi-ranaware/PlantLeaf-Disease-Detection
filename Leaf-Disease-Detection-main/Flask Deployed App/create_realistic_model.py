import torch
import CNN
import numpy as np

# Create a more realistic dummy model for testing
def create_realistic_dummy_model():
    """Create a dummy model with better weight initialization"""
    model = CNN.CNN(39)
    
    # Initialize with more realistic weights
    for param in model.parameters():
        if param.dim() > 1:
            torch.nn.init.xavier_uniform_(param)
        else:
            torch.nn.init.normal_(param, 0, 0.01)
    
    # Save the model
    torch.save(model.state_dict(), "plant_disease_model_1_latest.pt")
    print("✅ Realistic dummy model created successfully!")
    print("📁 Saved as: plant_disease_model_1_latest.pt")
    print("🎯 This will provide more varied predictions for testing")
    
    return model

if __name__ == "__main__":
    create_realistic_dummy_model()
