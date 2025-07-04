import subprocess
import time
import os

# Start FastAPI backend
backend = subprocess.Popen(["uvicorn", "app.api:app", "--reload"])

# Wait a bit to make sure the backend boots
time.sleep(3)

# Start Streamlit frontend
frontend = subprocess.Popen(["streamlit", "run", "ui/streamlit_app.py"])

# Keep the script running while both are active
try:
    backend.wait()
    frontend.wait()
except KeyboardInterrupt:
    print("Shutting down...")
    backend.terminate()
    frontend.terminate()
