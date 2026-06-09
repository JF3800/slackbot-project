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
@app.command    ("/slck-ping")
def handle_ping(ack, respond):
    start = time.time()  # Start the clock
    ack()                # Acknowledge the command
    
    # Calculate latency in milliseconds
    latency = int((time.time() - start) * 1000) 
    
    respond(f"Pong!\nLatency: {latency}ms")

#This handls the Greet command and responds with a greeting message
@app.command("/slck-hello")
def handle_hello(ack, respond, command):
    ack()  # Acknowledge the command

    user = command.get("user_name", "User") 

    respond(f"Hello, {user}! :wave:. Welcome to my Stardust challange project! :tada:")

#this handels the coin flip command which responds with heads or tails randomly.
@app.command("/slck-coin")
def handle_coin(ack, respond):
    ack()  # Acknowledge the command

    import random
    result = random.choice(["Heads", "Tails"])
    respond(f"The coin landed on: {result}")

#This handles the dice roll command which responds with a random number between 1 and 20.
@app.command("/slck-dice")
def handle_dice(ack, respond):
    ack()

    import random
    result = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    respond(f"The dice landed on: {result}!")
    
@app.command("/slck-time")
def handle_time(ack, respond):
    ack()

    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    respond(f"The current time is: {current_time}")

#Command that responds with shrug emoji
@app.command("/slck-shrug")
def handle_shrug(ack, respond):
    ack()

    respond("¯\\\(ツ)\/¯")

#Command that responds with an motivational quote
@app.command("/slck-motivate")
def handle_motivate(ack,respond):
    ack()

    import random
    quote = random.choice(["Action is the Foundational Key To All Sucess - Pablo Picasso", "Keep going, You got this!", "Do the thing you think you cannot do! <3", "Keep Going!", "The Future Belongs to those who belive in their beauty of their dreams.", "Keep Going, You've done so much already!", "Belive in your work no matter what you doing", "Always give 100% of your effort!"])
    respond(quote)

#This handles the list command which lists all the commands available in the bot so far.
@app.command("/slck-list")
def handle_list(ack, respond):
    ack()

    respond("Here are the available commands:\n"
            "1. `/slck-ping` - Check the latency of the bot.\n"
            "2. `/slck-hello` - Get a personalized greeting message.\n"
            "3. `/slck-list` - List all available commands.\n"
            "4. `/slck-coin` - Flips a random coin and returns heads or tails.\n"
            "5. `/slck-dice` - Rolls a 20 sided dice.")

# Start your app in Socket Mode
if __name__ == "__main__":
    print("bot is running!")
    handler = SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN"))
    handler.start()