# Bitcoin Price Menu Bar App

A simple macOS menu bar application that displays the current Bitcoin price.

![Bitcoin Price Menu Bar App](screenshots/preview.png)

## Features
- Displays real-time Bitcoin price in USD in your menu bar
- Updates automatically every minute
- Manual refresh option
- Uses Coinbase API for reliable price data
- Native macOS menu bar integration

## Installation

### Download
Download the latest release from the [Releases](https://github.com/yourusername/bitcoin-price-menubar/releases) page.

### Build from Source
1. Clone this repository:
```bash
git clone https://github.com/yourusername/bitcoin-price-menubar.git
cd bitcoin-price-menubar
```

2. Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Build the app:
```bash
python setup.py py2app
```

The built application will be in the `dist` directory.

## Development

### Requirements
- Python 3.11 or higher
- macOS 10.15 or higher

### Setup Development Environment
1. Clone the repository
2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app in development mode:
```bash
python bitcoin_price.py
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
