REST Service

This is a simple RESTful service built with Python and Flask. It provides a single endpoint to greet users.

Features
	•	Endpoint: /api/v1/greet
	•	HTTP Method: GET
	•	Behavior:
	•	Responds with Hello <name>! if the name query parameter is provided.
	•	Responds with Hello World! if no name is provided.

Requirements
	•	Python: 3.9 or higher
	•	Dependencies:
	•	Flask (listed in requirements.txt)

How to Run

1. Run Locally
	1.	Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


	2.	Install dependencies:

pip install -r requirements.txt


	3.	Start the application:

python app.py


	4.	Access the service at http://127.0.0.1:5000.

2. Run with Docker
	1.	Build the Docker image:

docker build -t rest-service .


	2.	Run the container:

docker run -p 5000:5000 rest-service


	3.	Access the service at http://localhost:5000.

Testing the Endpoint
	•	With name query parameter:

curl "http://localhost:5000/api/v1/greet?name=John"

Response:

{
  "message": "Hello John!"
}


	•	Without name query parameter:

curl "http://localhost:5000/api/v1/greet"

Response:

{
  "message": "Hello World!"
}

Project Structure

rest-service/
├── api/
│   ├── v1/
│   │   ├── routes.py         # API endpoint definitions
│   ├── __init__.py           # API initialization
├── app.py                    # Main application
├── config.py                 # Configuration file
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker configuration

