# Biometric-Access-Controlled-Automotive-Security-System

This project enhances vehicle security by replacing traditional keys with a biometric fingerprint recognition system. It provides a secure, user-friendly solution for automotive access and control.

## Features
- Fingerprint authentication for secure vehicle access.
- Easy enrollment and verification of fingerprints.
- Compact and efficient circuit design.

## Directory Structure
```
Fingerprint-Security-System/
├── README.md               
├── images/                  
│   ├── component_setup.jpg     
│   ├── fingerprint_module.jpg        
├── videos/                     
│   └── demo_verification.mp4   
├── models/                  
│   └── example_template.bin    
├── src/                    
│   ├── enrollment_code.ino     
│   ├── verification_code.ino                    
├── docs/                   
│   ├── user_manual.pdf         
│   └── technical_specifications.pdf 
├── circuit-diagrams/       
│   └── system_schematic.png    
├── requirements.txt         
└── LICENSE                  

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
