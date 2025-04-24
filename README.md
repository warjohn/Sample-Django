# Media API Project

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

This is a Django REST API for uploading and processing videos and images.

## Getting Started <a name = "getting_started"></a>

### Requirements

- Python 3.8+
- PostgreSQL
- Dependencies from `requirements.txt`


### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/warjohn/Sample-Django.git
   cd media-api
   ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```python 
    pip install -r requirements.txt
    ```

4. #### Change the settings in the database block in your database

5. Apply migrations:
    ```python
    python manage.py migrate
    ```

6. Run the server:
    ```python
    python manage.py runserver
    ```

## Usage <a name = "usage"></a>

1. Upload video: POST /api/upload-video/
2. Upload image: POST /api/upload-image/
     

