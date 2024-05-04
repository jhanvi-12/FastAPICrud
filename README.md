# FastAPI Application with CRUD Operations for MongoDB

This is a FastAPI application with CRUD (Create, Read, Update, Delete) operations for MongoDB, along with support for advanced queries.

## Prerequisites
Before you begin, ensure you have the following installed:
 
* [![Python][Python]][Python-url]
* [![FastAPI][FastAPI]][FastAPI-url]
* [![MongoDB][MongoDB]][MongoDB-url]

## Install + configure the project

### 1. Linux
```
# Create python virtual environment
python3 -m venv venv

# Activate the python virtual environment
source venv/bin/activate

# Install the requirements for the project into the virtual environment
pip install -r requirements.txt

# Install the dependencies of Fast API
pip install "fastapi[all]"

# Upgrade pip version
python -m pip install --upgrade pip==22.1.2
```
### 2. Windows
```
# Create python virtual environment
conda create --name venv python=3.8

# Activate the python virtual environment
conda activate venv

# Install the requirements for the project into the virtual environment in the following sequence:
pip install -r requirements.txt

# Install the dependencies of Fast API
pip install "fastapi[all]"

# Upgrade pip version
python -m pip install --upgrade pip==22.1.2
```

## Clone this repository:
```bash
git clone <repository_url>
cd <repository_name>
```

## Install the required dependencies:
```bash
pip install -r requirements.txt
or
pip install fastapi uvicorn pymongo
```

## Make sure you have MongoDB installed and running locally on "localhost:27017".

## Configuration
Before running the application, make sure to configure the MongoDB connection details. Edit the env_config.py file:
```bash
# env_config.py
MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB_NAME = "your_database_name"
```
Replace "mongodb://localhost:27017/" with your MongoDB connection URI and "your_database_name" with the name of your MongoDB database.

## Usage
To start the FastAPI application, run the following command:
```bash
python run.py
```

This will start the FastAPI application, and you can access the API documentation at "http://localhost:8003/docs".

## API Endpoints
```bash
POST /create: Create a new item.
GET /items: Retrieve all items.
PUT /update/book/{item_id}: Update details of a specific item by ID.
DELETE /{item_id}: Delete a specific item by ID.
GET /items/search?keyword={search_query}: Search for items by a specific query.
```



<!-- MARKDOWN LINKS & IMAGES -->
[Python]: https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=Blue
[Python-url]: https://docs.python.org/3.10/
[FastAPI]: https://img.shields.io/badge/FastAPI-20232A?style=for-the-badge&logo=fastapi&logoColor=009485
[FastAPI-url]: https://fastapi.tiangolo.com/
[MongoDB]: https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white
[MongoDB-url]: https://www.mongodb.com/docs/languages/python/pymongo-driver/current/