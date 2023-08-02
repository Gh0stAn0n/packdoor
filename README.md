# About 'packdoor'

<p align="center">
   </a>
      <a href="https://github.com/Gh0stAn0n/packdoor">
      <img src="https://img.shields.io/badge/Version-1.0.0-darkgreen">
        <img src="https://img.shields.io/badge/Release%20Date-august%202023-purple">
  <img src="https://shields.io/badge/Python-100%25-066da5">
  <img src="https://shields.io/badge/Platform-Linux-darkred">
    </a>
  </p>
</p>

packdoor is a simple Backdoor written in Python that implements a simple bind shell, allowing remote access to the target system. It establishes a TCP server on the specified IP and port, listening for incoming connections. Once a connection is established, the script allows the user to execute shell commands on the target system.

### Features

Reliable Communication: The script uses JSON encoding to ensure reliable communication between the attacker and the target.
File Upload and Download: It supports uploading and downloading files to/from the target system.
Basic Command Execution: Allows executing shell commands on the target system.

### Prerequisites

To run this script, you need:

Python 3.x installed on your machine.

### Usage

Clone this repository to your local machine.
Customize the IP address and port in the script to yours.
Launch the script on your attacker machine using the command: python packdoor.py.
Packdoor will start listening for incoming connections.
For windows distribution, type: pyinstaller .\backdoor.py --onefile --noconsole .into the CMD to make the python file executable, the executable file will be at dist.
Run the backdoor file on the target machine.
Execute a reverse shell.

### Disclaimer

This script is intended for educational and testing purposes only. Unauthorized access to computer systems is illegal and unethical. Use this script responsibly and only on systems you own or have explicit permission to test.
