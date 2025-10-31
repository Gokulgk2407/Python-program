# ePropelled Dashboard - Welcome Wizard

A modern GUI application for the ePropelled manufacturer dashboard, featuring device scanning and connection management.

## Features

- **Modern UI Design**: Clean, professional interface matching the ePropelled brand
- **Navigation Sidebar**: Full menu with all dashboard sections
- **Device Scanning**: Automatically detect connected serial devices
- **Baud Rate Selection**: Choose from common baud rates (9600, 19200, 38400, 57600, 115200)
- **Device Connection**: Connect to selected devices with chosen baud rate

## Installation

1. Install Python 3.8 or higher
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python gui.py
```

## Components

### Left Sidebar
- Search functionality
- Navigation menu items:
  - Welcome Wizard (current page)
  - Products
  - Firmware
  - Operation Settings
  - Motor Settings
  - System Control Parameters
  - Drive Control Panel
  - System Status
  - Diagnostics
  - Data Analysis
  - Live Dashboard
  - System Logs
- Help, Log out, and Settings options

### Main Content Area
- **Info Bar**: Information about the app-wide status messaging system
- **Device Status**: 
  - Scan for connected serial devices
  - Select baud rate
  - Connect to devices

## Dependencies

- **customtkinter**: Modern UI framework for Python
- **pyserial**: Serial communication library for device detection

## Screenshots

The interface is based on the ePropelled Manufacturer Dashboard design with:
- Clean white sidebar with green accent for active items
- Light gray main content area
- Blue action buttons
- Professional typography and spacing

## Future Enhancements

- Implement actual serial communication
- Add other dashboard pages (Products, Firmware, etc.)
- Real-time device monitoring
- Data logging and analysis
- Settings configuration panel
