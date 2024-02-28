
# Ph and NPK Tester Mobile Application

This mobile application is designed for users who want to monitor the pH level of water and the NPK (Nitrogen, Phosphorus, Potassium) values in a convenient and mobile-friendly way. The application interfaces with Arduino, which is connected to NPK and Water pH sensors, providing real-time data through Bluetooth.

## Purpose

The primary purpose of this application is to streamline the process of monitoring and analyzing water quality for agricultural, research, or hobbyist purposes. By leveraging the simplicity of a mobile interface, users can easily keep track of crucial parameters without the need for complex setups.

## How It Works

The mobile application communicates with Arduino, which collects data from NPK and Water pH sensors. The Arduino then sends this data over Bluetooth to the mobile device, where it is displayed in an easy-to-understand format. This enables users to make informed decisions based on the current water quality metrics.

## Code Overview

The application is built using the Kivy framework in Python. The main components include:

- **Main Application (`ph_npk_tester_app.py`):** The core application logic and user interface.
- **Arduino Code (`arduino_sensor_reader.ino`):** Arduino code to read data from NPK and Water pH sensors and transmit it over Bluetooth.

## Getting Started

1. Connect your NPK and Water pH sensors to Arduino.
2. Install the required Python packages using the following command:
   ```bash
   pip install kivy pyobjc
   ```
3. Ensure Bluetooth is enabled on your mobile device.
4. Run the mobile application (`ph_npk_tester_app.py`) and discover paired Bluetooth devices.

## Usage

1. Launch the application on your mobile device.
2. Press the "Start Test" button.
3. If the sensors are connected, it will display real-time values; otherwise, a popup will notify you to connect the sensors.

## Dependencies

- Kivy: A Python framework for developing multi-touch applications.
- PyObjC: A Python library for interacting with Objective-C code (required for Bluetooth functionality on macOS).

## Author

Ahmed Alzeidi

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This extended readme provides more context about the project's purpose, how it works, the code structure, dependencies, and steps for getting started. Adjust it further based on your project's specifics.# PH_NPK_Tester_MobileApplication
