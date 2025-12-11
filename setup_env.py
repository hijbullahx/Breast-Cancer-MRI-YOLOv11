import os
import torch
import sys

# 1. Deterministic Seed (Critical for Reproducibility)
torch.manual_seed(42)

def setup_project_structure():
    """
    Creates the standard directory structure for the thesis.
    """
    folders = [
        "src",              # Python scripts
        "data/raw",         # Original DICOM images
        "data/processed",   # Converted PNG images
        "docs",             # Thesis text and figures
        "models/yolo",      # Saved YOLO weights
        "notebooks"         # Experimental notebooks
    ]
    
    print(f"Creating project structure...")
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        # Create a .gitkeep file so Git tracks empty folders
        with open(os.path.join(folder, ".gitkeep"), 'w') as f:
            pass
        print(f"✔ Created: {folder}")

def check_environment():
    """
    Checks if PyTorch and GPU are ready.
    """
    print(f"\n--- Environment Check ---")
    print(f"Python: {sys.version.split()[0]}")
    print(f"PyTorch: {torch.__version__}")
    
    if torch.cuda.is_available():
        print(f"✔ GPU Available: {torch.cuda.get_device_name(0)}")
    else:
        print(f"⚠ GPU NOT Available (Fine for coding, but need GPU for training)")

if __name__ == "__main__":
    setup_project_structure()
    check_environment()