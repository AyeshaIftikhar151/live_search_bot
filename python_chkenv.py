from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

print("🔍 Checking environment variables...")

# Read values
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_KEY = os.getenv("GOOGLE_CSE_KEY")
GOOGLE_CX = os.getenv("GOOGLE_CX")

# Print (masking sensitive parts)
def mask(value):
    if value and len(value) > 6:
        return value[:4] + "..." + value[-4:]
    return value

print("GOOGLE_API_KEY:", mask(GOOGLE_API_KEY))
print("GOOGLE_CSE_KEY:", mask(GOOGLE_CSE_KEY))
print("GOOGLE_CX:", GOOGLE_CX)
