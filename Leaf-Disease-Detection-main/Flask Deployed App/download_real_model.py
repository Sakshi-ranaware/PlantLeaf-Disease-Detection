import requests
import os

def download_model():
    """Download the real trained model for plant disease detection"""
    
    # Google Drive direct download link
    url = "https://drive.google.com/uc?export=download&id=1JsUW38lrsyAYG0ORjqwQxQiRZpPIoc0c"
    
    print("🌿 Downloading Real Plant Disease Model...")
    print("This may take a few minutes depending on your internet connection...")
    
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open('plant_disease_model_1_latest.pt', 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    progress = (downloaded / total_size) * 100 if total_size > 0 else 0
                    print(f"\rProgress: {progress:.1f}%", end='', flush=True)
        
        print(f"\n✅ Model downloaded successfully!")
        print(f"📁 Saved as: plant_disease_model_1_latest.pt")
        print(f"📊 Size: {downloaded / (1024*1024):.1f} MB")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error downloading model: {e}")
        print("\n📋 Alternative options:")
        print("1. Download manually from: https://drive.google.com/file/d/1JsUW38lrsyAYG0ORjqwQxQiRZpPIoc0c/view?usp=sharing")
        print("2. Place the file in this directory as 'plant_disease_model_1_latest.pt'")
        return False

if __name__ == "__main__":
    if download_model():
        print("\n🎉 Ready to test with real model!")
        print("Run 'python test_model.py' to verify predictions.")
    else:
        print("\n⚠️ Please download the model manually to continue.")
