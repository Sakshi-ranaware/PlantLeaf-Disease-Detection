import os
import pandas as pd

# Load the data
disease_info = pd.read_csv('disease_info.csv', encoding='cp1252')
supplement_info = pd.read_csv('supplement_info.csv', encoding='cp1252')

# Import the smart prediction function from app
import sys
sys.path.append('.')
from app import prediction
import CNN

def test_all_images():
    test_images_dir = '../test_images'
    results = []
    
    print("🌿 Testing Plant Disease Detection Model 🌿")
    print("=" * 60)
    
    for filename in os.listdir(test_images_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(test_images_dir, filename)
            
            try:
                result = prediction(image_path)
                predicted_disease = CNN.idx_to_classes[result['predicted_class']]
                confidence = result['confidence']
                
                # Extract actual disease from filename
                actual_disease = filename.replace('.jpg', '').replace('.JPG', '').replace('.jpeg', '').replace('.png', '')
                
                results.append({
                    'filename': filename,
                    'actual': actual_disease,
                    'predicted': predicted_disease,
                    'confidence': confidence,
                    'correct': actual_disease.lower() in predicted_disease.lower()
                })
                
                print(f"📸 {filename}")
                print(f"   Actual: {actual_disease}")
                print(f"   Predicted: {predicted_disease}")
                print(f"   Confidence: {confidence:.2%}")
                print(f"   ✅ Correct: {actual_disease.lower() in predicted_disease.lower()}")
                print("-" * 40)
                
            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")
    
    # Summary
    total = len(results)
    correct = sum(1 for r in results if r['correct'])
    accuracy = (correct / total) * 100 if total > 0 else 0
    
    print(f"\n📊 SUMMARY:")
    print(f"Total Images: {total}")
    print(f"Correct Predictions: {correct}")
    print(f"Accuracy: {accuracy:.1f}%")
    
    # Show incorrect predictions
    incorrect = [r for r in results if not r['correct']]
    if incorrect:
        print(f"\n❌ INCORRECT PREDICTIONS:")
        for r in incorrect:
            print(f"   {r['filename']}: {r['actual']} → {r['predicted']} ({r['confidence']:.1%})")
    
    return results

if __name__ == "__main__":
    test_all_images()
