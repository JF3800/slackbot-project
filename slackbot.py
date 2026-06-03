import os
import time
from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Force Python to find the .env file in the exact same directory as this script
env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

# Initialize your app with your bot token
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# This handles the ping command and calculates latency
@app.command("/slck-ping")
def handle_ping(ack, respond):
    start = time.time()  # Start the clock
    ack()                # Acknowledge the command
    
    # Calculate latency in milliseconds
    latency = int((time.time() - start) * 1000) 
    
    respond(f"Pong!\nLatency: {latency}ms")

# Start your app in Socket Mode
if __name__ == "__main__":
    print("bot is running!")
    handler = SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN"))
    handler.start()