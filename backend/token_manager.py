import json
import os

TOKENS_FILE = "tokens.json"

def ensure_token_file():
    """Ensures that the tokens file exists."""
    if not os.path.exists(TOKENS_FILE):
        with open(TOKENS_FILE, "w") as file:
            json.dump({}, file, indent=4)

def save_tokens(data):
    """Saves tokens to a file."""
    ensure_token_file()
    with open(TOKENS_FILE, "w") as file:
        json.dump(data, file, indent=4)
    print("Tokens saved successfully.")

def load_tokens():
    """Loads tokens from a file."""
    ensure_token_file()
    try:
        with open(TOKENS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}