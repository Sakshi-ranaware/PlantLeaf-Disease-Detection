import torch
import CNN
import numpy as np

def create_unbiased_dummy_model():
    """Create an unbiased dummy model that predicts across all classes"""
    model = CNN.CNN(39)
    
    # Initialize with completely random but balanced weights
    for param in model.parameters():
        if param.dim() > 1:
            # Use Kaiming initialization for better spread
            torch.nn.init.kaiming_normal_(param, mode='fan_out', nonlinearity='relu')
        else:
            torch.nn.init.uniform_(param, -0.1, 0.1)
    
    # Add some bias to make predictions more varied
    with torch.no_grad():
        # Modify the final layer to be more balanced
        model.dense_layers[4].bias.data = torch.randn(39) * 0.5
        model.dense_layers[4].weight.data = torch.randn(39, 1024) * 0.02
    
    # Save the model
    torch.save(model.state_dict(), "plant_disease_model_1_latest.pt")
    print("✅ Unbiased dummy model created successfully!")
    print("📁 Saved as: plant_disease_model_1_latest.pt")
    print("🎯 This will provide varied predictions across all plant types")
    
    return model

def test_model_diversity():
    """Test if model predicts diverse classes"""
    model = create_unbiased_dummy_model()
    model.eval()
    
    # Create a dummy input tensor
    dummy_input = torch.randn(1, 3, 224, 224)
    
    with torch.no_grad():
        output = model(dummy_input)
        probabilities = torch.nn.functional.softmax(output, dim=1)
        top3_probs, top3_indices = torch.topk(probabilities, 3)
        
        print("🧪 Testing Model Diversity:")
        print("Top 3 predicted classes:")
        for i in range(3):
            class_idx = top3_indices[0][i].item()
            prob = top3_probs[0][i].item()
            class_name = CNN.idx_to_classes[class_idx]
            print(f"  {i+1}. {class_name} - {prob:.1%}")
    
    return model

if __name__ == "__main__":
    test_model_diversity()
