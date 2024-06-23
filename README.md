# ContractGuard

ContractGuard is a comprehensive smart contract auditing tool designed with a user-friendly graphical interface. It allows users to paste URLs of smart contracts, download them, and perform extensive vulnerability scans. The tool aims to help developers and security researchers identify potential issues in Ethereum smart contracts.

## Features

- **Graphical User Interface (GUI)**: User-friendly interface built with `tkinter` for easy interaction.
- **URL Input**: Paste smart contract URLs to download and audit the code.
- **Vulnerability Scanning**: Detect common vulnerabilities such as reentrancy, integer overflow, unchecked call returns, and more.
- **Detailed Reports**: Generate and display comprehensive audit reports, with options to export to PDF.
- **Static Analysis Integration**: Utilizes tools like `mythril` and `slither` for in-depth security analysis.

## Installation

### Prerequisites

- Python 3.7 or higher
- `tkinter` (usually included with Python installations)
- Virtual environment setup (optional but recommended)

### Steps

1. **Clone the Repository**
```
git clone https://github.com/your-username/ContractGuard.git
cd ContractGuard
```

2. Set Up a Virtual Environment
```
python3 -m venv env
source env/bin/activate # On Windows, use 'env\Scripts\activate`
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Install `tkinter`
* On Debian-based Linux (including Ubuntu):
```
sudo apt-get update && sudo apt-get install -y python3-tk
```
* On Fedora:
```
sudo dnf install python3-tkinter
```

### Usage
1. Run the Application
```
python3 ChainInspect.py
```
2. Using the GUI
* Paste the URL of the smart contract in the input field.
* Click the "Download" button to fetch the smart contract code.
* Click the "Scan" button to perform a vulnerability audit.
* View the detailed report in the GUI or export it to a PDF file.

### Contributin
_We welcome contribution to enhance ChainInspect! Here's how you can contribute:_
1. Fork the Repository
   * Click the "Fork" button at the top right of the repository page.
2. Clone Your Fork
```
git clone https://github.com/RoguePayload/ChainInspect.git
cd ChainInspect
```
3. Create a Branch for Your Feature
```
git checkout -b feature-name
```
4. Make Your Changes
    * Implement your feature or bug fix.
5. Commit Your Changes
```
git add .
git commit -m "Description of your feature or fix"
```
6. Push to Your Fork
```
git push origin feature-name
```
7. Create a Pull Request
    * Navigate to the original repository and create a pull request from your fork.

### License
_This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for details._

### Contact
_For any inquiries or support, please contact:_  
* Author: Dr. Aubrey W. Love II (AKA Rogue Payload)  
* Email: [roguepaylaod@darkmcs.com](mailto:roguepayload@darkmcs.com)  
* GitHub: [Rogue Payload](https://github.com/RoguePayload)  

We appreciate your interest in ChainInspect! Together, we can improve the security & reliability of smart contracts.
