# Vinted View Boost Bot

A simple, multi-threaded Python script to increase the view count of a Vinted item using rotating proxies and randomized user agents.

## Features

- Multi-threading to speed up the process
- Rotating proxies to bypass request limitations
- Randomized user agents to mimic real users

## Requirements

- Python 3.6+
- `requests` module
- `fake-useragent` module

## Installation

1. Clone the repository or download the source code:

```bash
git clone https://github.com/kWAYTV/vinted-view-bot.git
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Add your proxies to the `proxies.txt` file, one proxy per line. Use `user:pass@ip:port` format.

## Usage

1. Run the script:

```bash
python main.py
```

2. Enter the Vinted link and the number of threads when prompted.

3. The script will start sending requests to the provided Vinted link, and the view count will increase.

## Note

This script is for educational purposes only. Misusing the script may violate Vinted's terms of service. Use it responsibly and at your own risk.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
