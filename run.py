"""This module is responsible for running the fastapi server on the given host and port."""
import uvicorn
from main import app
from dotenv import load_dotenv
from utils import env_config

load_dotenv()

if __name__ == '__main__':
    uvicorn.run("main:app",
                port=int(env_config.SERVER_PORT),
                host=env_config.SERVER_HOST,
                reload=True)

