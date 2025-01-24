import os

# Define the directory structure
project_structure = {
    "Fingerprint-Security-System": {
        "README.md": None,
        "images": {
            "component_setup.jpg": None,
            "fingerprint_module.jpg": None,
            "screenshots.jpg": None,
        },
        "videos": {
            "demo_enrollment.mp4": None,
            "demo_verification.mp4": None,
        },
        "models": {
            "example_template.bin": None,
        },
        "src": {
            "enrollment_code.ino": None,
            "verification_code.ino": None,
            "utils.h": None,
        },
        "docs": {
            "user_manual.pdf": None,
            "technical_specifications.pdf": None,
        },
        "circuit-diagrams": {
            "system_schematic.png": None,
        },
        "requirements.txt": None,
        "LICENSE": None,
    }
}

# Function to create the directories and files
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)  # Recursive call for nested directories
        else:
            with open(path, 'w') as file:
                pass  # Create an empty file

# Create the project structure in the current directory
base_path = os.getcwd()  # Change this to the desired parent directory path if needed
create_structure(base_path, project_structure)

print("Directory structure created successfully.")
