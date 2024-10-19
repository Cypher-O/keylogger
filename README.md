# Keylogger APP

## Description

This project implements a keylogger using Python. It captures keystrokes and can save them to a file or send them via email. The primary goal of this project is for educational purposes only, to understand how keylogging works and the importance of cybersecurity.

## Features

- Keylogging functionality
- Option to save logs to a file
- Option to send logs via email
- Configurable logging interval

## Requirements

- Python 3.x
- Required libraries:
  - `keyboard`
  - `smtplib`
  - `email`

## Installation

### 1. Clone the Repository

 ```sh
    git clone https://github.com/YourUsername/keylogger.git
 ```

### 2. Navigate to the project directory

 ```sh
    cd keylogger
 ```

### 3. Install the required dependencies

 ```sh
    pip install -r requirements.txt
 ```

### 4. Update the configuration file located at config/config.ini with your email details.

## Usage

### Run the keylogger:

 ```sh
    sudo python main.py
 ```

The keylogger will start logging keystrokes according to the specified interval in the configuration file.

## Important Note

This project is intended for educational purposes only. Please ensure you have permission before using this software on any machine.

## License

This project is licensed under the MIT License. However, it is intended for educational purposes only. Please do not use it for any malicious activities or without consent. Please ensure you have permission before using this software on any machine. - see the [LICENSE](LICENSE) file for details.

