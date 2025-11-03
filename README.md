# AI Background Removal Telegram Bot

A production-ready Telegram bot that uses state-of-the-art AI to remove backgrounds from images instantly. Built with Python 3.13, deployed on a self-managed AlmaLinux VPS, and designed for 24/7 operation.

## 🎯 Features

### Core Functionality
- **AI-Powered Background Removal**: Utilizes U²-Net deep learning model via rembg library
- **High-Quality Output**: Preserves image quality while removing backgrounds with precision
- **PNG Export**: Returns images with transparent backgrounds in PNG format
- **Real-time Processing**: Instant feedback and processing status updates
- **Memory-Efficient**: Processes images entirely in-memory without disk I/O

### Production Features
- **Comprehensive Logging**: Time-based log rotation (daily at midnight, 7-day retention)
- **Error Handling**: Graceful error recovery with user-friendly error messages
- **Async Architecture**: Built on python-telegram-bot's async framework for optimal performance
- **Environment Configuration**: Secure token management via environment variables

## 🏗️ Architecture

### Project Structure
background-remover-bot/
├── main.py # Application entry point, bot initialization
├── bot.py # Command handlers and business logic
├── bg_rem.py # Background removal processing module
├── config.py # Environment configuration
├── pyproject.toml # Project dependencies and metadata
├── .env # Environment variables (not in repo)
└── bot.log # Application logs (auto-rotated)

### Technology Stack
- **Runtime**: Python 3.13+
- **Bot Framework**: python-telegram-bot 22.5
- **AI Model**: rembg 2.0.67 (U²-Net architecture)
- **Image Processing**: Pillow 12.0.0
- **ML Inference**: ONNX Runtime 1.23.2
- **Package Manager**: uv (Astral's fast Python package installer)

## 📋 Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome message and bot introduction |
| `/help` | List all available commands |
| `/test` | Health check endpoint |
| `/echo <text>` | Echo back user input (utility function) |
| **Send Photo** | Automatically triggers background removal |

## 🚀 Deployment

### VPS Setup (AlmaLinux)
This bot is deployed on a bare-metal AlmaLinux server configured from scratch:

1. **Server Provisioning**

Fresh AlmaLinux installation

sudo dnf update -y
sudo dnf install git curl -y

text

2. **uv Installation**

curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env

text

3. **Repository Deployment**

git clone https://github.com/YOUR_USERNAME/bg-remover-bot.git
cd bg-remover-bot

text

4. **Environment Setup**

Create .env file

echo "BOT_TOKEN=your_bot_token_from_botfather" > .env
Install dependencies and create virtual environment

uv sync

text

5. **Launch Bot**

Production run (uses logging, no console output)

uv run main.py
Development run (with console logging)
Uncomment StreamHandler in main.py

text

### Continuous Operation
The bot runs 24/7 on the VPS using systemd service management:

Create systemd service file

sudo nano /etc/systemd/system/bg-remover-bot.service

text
undefined

[Unit]
Description=Telegram Background Remover Bot
After=network.target

[Service]
Type=simple
User=your_user
WorkingDirectory=/path/to/bg-remover-bot
ExecStart=/home/your_user/.cargo/bin/uv run main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target

text
undefined

Enable and start service

sudo systemctl enable bg-remover-bot
sudo systemctl start bg-remover-bot
sudo systemctl status bg-remover-bot

text

## 📊 Logging System

### Log Rotation Strategy
- **Type**: Time-based rotation
- **Frequency**: Daily at midnight
- **Retention**: 7 days (7 backup files)
- **Format**: ISO 8601 timestamp + log level + message
- **Location**: `./bot.log` (current), `./bot.log.YYYY-MM-DD` (archives)

### Log Levels
- `INFO`: Command execution, user interactions
- `ERROR`: Processing failures, API errors
- `WARNING`: Unusual events requiring attention

### Monitoring Logs

Real-time log monitoring

tail -f bot.log
Search for errors

grep ERROR bot.log*
View specific date

cat bot.log.2025-11-02

text

## 🔐 Security & Privacy

### Current Implementation
- Environment-based secret management (`.env` file)
- No data persistence - images processed in-memory only
- No user tracking or analytics

### Planned Enhancements
- **Rate Limiting**: Prevent API abuse (coming soon)
- **User Authentication**: Whitelist/blacklist functionality (in development)
- **Usage Quotas**: Per-user daily limits (roadmap item)

## 🎥 Live Demo

**Bot Link**: Available upon request in my resume for recruiter testing.

> **Note**: The bot link is not publicly shared to prevent abuse. If you're a recruiter or potential employer interested in testing the bot, please find the link in my resume or contact me directly.

## 🛠️ Local Development

### Prerequisites
- Python 3.13+
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- uv package manager

### Quick Start

Clone repository

git clone https://github.com/YOUR_USERNAME/bg-remover-bot.git
cd bg-remover-bot
Install uv (if not already installed)

curl -LsSf https://astral.sh/uv/install.sh | sh
Create .env file

echo "BOT_TOKEN=your_token_here" > .env
Install dependencies

uv sync
Run bot

uv run main.py

text

### First Run Notes
- Initial startup takes 2-5 minutes while rembg downloads AI models (~100MB)
- Models are cached locally after first run
- Subsequent starts are instant

## 📝 Code Quality

### Module Breakdown

#### `main.py` (Entry Point)
- Bot initialization and configuration
- Logging setup with TimedRotatingFileHandler
- Handler registration for commands and messages
- Application lifecycle management

#### `bot.py` (Command Handlers)
- Async command handlers using python-telegram-bot patterns
- User interaction logic
- Error handling and user feedback
- Integration with processing modules

#### `bg_rem.py` (Processing Engine)
- Image background removal using rembg
- BytesIO stream handling for memory efficiency
- PNG format conversion and optimization

#### `config.py` (Configuration)
- Environment variable loading via python-dotenv
- Centralized configuration management
- Secrets handling

## 🐛 Known Limitations

### Current Constraints
- No rate limiting implemented (planned)
- No user authentication system (in development)
- Single-threaded processing (optimized for VPS resources)
- No image size validation (accepts Telegram's limits)

### Future Roadmap
1. **Phase 1**: Rate limiting per user
2. **Phase 2**: User authentication system
3. **Phase 3**: Batch processing support
4. **Phase 4**: Multiple AI model support (quality presets)

## 📜 License

This project is for portfolio demonstration purposes.

## 🙏 Acknowledgments

- **python-telegram-bot**: Excellent async bot framework
- **rembg**: Powerful background removal library
- **U²-Net**: State-of-the-art salient object detection model
- **AlmaLinux**: Stable and reliable server OS

---

**Last Updated**: November 2025  
**Status**: ✅ Production (Running on AlmaLinux VPS)  
**Uptime**: 24/7 operation with systemd supervision