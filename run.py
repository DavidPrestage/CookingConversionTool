# Entry point for app.
from app import app    # Allows app to be discovered by 'flask' command.
from app import views  # Connects view.py to website

if __name__ == "__main__":
    app.run()