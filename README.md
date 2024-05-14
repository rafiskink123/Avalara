# Avalara
Avalara_TakeHome_Assignment
Date Range Overlap API
This project is a JSON-based API built with Flask that checks if two date ranges overlap.

Prerequisites
Before running the application, ensure you have the following installed:

Python (version 3.9 or higher)
Docker (optional, for containerized deployment)
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/date-range-overlap-api.git
Navigate to the project directory:

bash
Copy code
cd date-range-overlap-api
Install the Python dependencies using pip:

bash
Copy code
pip install -r requirements.txt
Usage
To run the API locally:

Set the Flask app environment variable:

bash
Copy code
export FLASK_APP=date_overlap_api.py
Run the Flask development server:

bash
Copy code
flask run
The API will be accessible at http://localhost:5000/overlap.

To run the API using Docker:

Build the Docker image:

bash
Copy code
docker build -t my-python-app .
Run a container based on the image:

bash
Copy code
docker run -d -p 5000:5000 my-python-app
The API will be accessible at http://localhost:5000/overlap.

API Endpoint
/overlap (POST)
Checks if two date ranges overlap.

Request Body:

json
Copy code
{
  "start1": "YYYY-MM-DD",
  "end1": "YYYY-MM-DD",
  "start2": "YYYY-MM-DD",
  "end2": "YYYY-MM-DD"
}
Response:

json
Copy code
{
  "overlap": true|false
}
Testing
Unit tests for the API are located in the tests directory. To run the tests, use:

bash
Copy code
python -m unittest discover tests
Contributing
Contributions are welcome! If you have any suggestions, bug fixes, or improvements, feel free to open an issue or submit a pull request.
