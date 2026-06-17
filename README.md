# Justins-Slack-Bot

A 24/7 Slack bot built with Python and Slack Bolt that runs on a personal device using Socket Mode. It supports a set of custom slash commands including a ping latency checker, coin flip, dice roller, time checker, and motivational quote generator.

## Commands

| Command | Description |
|---|---|
| `/slck-ping` | Returns pong and shows the bot's latency |
| `/slck-hello` | Greets you by your Slack username |
| `/slck-coin` | Flips a coin - heads or tails |
| `/slck-dice` | Rolls a 20-sided dice |
| `/slck-time` | Returns the current time |
| `/slck-shrug` | ¯\(ツ)/¯ |
| `/slck-motivate` | Sends a random motivational quote |
| `/slck-list` | Lists all available commands |

## Stack

- Python 3
- Slack Bolt for Python
- Socket Mode
- python-dotenv

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/Justins-Slack-Bot.git
cd Justins-Slack-Bot
```

**2. Install dependencies**
```bash
pip install slack-bolt python-dotenv
```

**3. Create a `.env` file**

**4. Run the bot**
```bash
python slackbot.py
```

## Slack App Requirements

- **Bot Token Scopes:** `app_mentions:read`, `channels:history`, `chat:write`, `commands`
- **Socket Mode:** enabled
- **Slash Commands:** registered for each `/slck-*` command above
