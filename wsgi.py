"""App entry point."""
import os
from app import create_app
from dotenv import load_dotenv
load_dotenv()


app = create_app()
port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
