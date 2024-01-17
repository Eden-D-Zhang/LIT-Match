import json

def load_gbooks_key(file_path = "api_keys.json"):
    try:
        with open(file_path, "r") as file:
            api_keys = json.load(file)
            gbooks_key = api_keys.get("google_books", {}).get("api_key")
        return gbooks_key
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to decode {file_path}.")
        return None
    
def load_openai_key(file_path = "api_keys.json"):
    try:
        with open(file_path, "r") as file:
            api_keys = json.load(file)
            openAI_key = api_keys.get("openAI", {}).get("api_key")
        return openAI_key
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to decode {file_path}.")
        return None