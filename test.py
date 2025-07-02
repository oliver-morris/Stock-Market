from dotenv import load_dotenv
import os

load_dotenv()  # Automatically loads .env from the same dir (or parent)

print(os.getenv("STOCK_KEY"))
