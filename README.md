# Biometric-Access-Controlled-Automotive-Security-System

This project enhances vehicle security by replacing traditional keys with a biometric fingerprint recognition system. It provides a secure, user-friendly solution for automotive access and control.

## Features
- Fingerprint authentication for secure vehicle access.
- Easy enrollment and verification of fingerprints.
- Compact and efficient circuit design.

## Directory Structure
```
Fingerprint-Security-System/ │ ├── README.md # Project overview and setup instructions ├── images/ # Contains visual resources, including: │ ├── component_setup.jpg # Image of the hardware setup │ ├── fingerprint_module.jpg # Close-up of the fingerprint sensor │ └── screenshots.jpg # Screenshots of code output ├── videos/ # Contains project demonstration videos, such as: │ ├── demo_enrollment.mp4 # Enrollment process video │ └── demo_verification.mp4 # Fingerprint verification demo ├── models/ # Stores fingerprint template files, if applicable │ └── example_template.bin # Example fingerprint data ├── src/ # Source code directory, includes: │ ├── enrollment_code.ino # Arduino code for enrolling fingerprints │ ├── verification_code.ino # Arduino code for verifying fingerprints │ └── utils.h # Optional utility functions for modularity ├── docs/ # Additional documentation, including: │ ├── user_manual.pdf # Detailed user guide │ └── technical_specifications.pdf # Sensor and system specifications ├── circuit-diagrams/ # Contains electronic schematics: │ └── system_schematic.png # Full circuit diagram ├── requirements.txt # Lists required dependencies and libraries └── LICENSE # Licensing information for the project
```


## Getting Started

### Prerequisites
- Arduino IDE installed on your system.
- Required library: Adafruit Fingerprint Sensor Library (v2.0.4).
- Basic understanding of Arduino and circuits.

### Setup Instructions

#### Hardware Setup
- Connect the AS608 fingerprint sensor to the Arduino UNO.
- Follow the circuit schematic for proper connections.

#### Software Setup
- Open the `src/enrollment_code.ino` in the Arduino IDE and upload it for enrollment.

## How It Works

### Enrollment
- Assign unique IDs to fingerprints and store them securely.

### Verification
- Match fingerprints against stored templates to allow or deny access.

## Contribution
Contributions are welcome! Feel free to submit issues or pull requests to improve this project.
