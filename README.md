# PesaPal Payment Integration

This project demonstrates how to integrate PesaPal payment gateway into a Flask application. It consists of two main
parts: authentication and iframe generation.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

### Prerequisites

- Python 3.6+
- Flask
- Requests
- PyJWT

You can install the Python packages with pip:

```bash
pip install -r requirements.txt
```

## Usage

The project consists of two Python files: `authentication.py` and `iframe_fetching.py`.

## Authentication

The authentication.py file contains the authentication function which is responsible for authenticating the application
with PesaPal using the merchant’s key and secret. It sends a POST request to the PesaPal API and returns the token from
the response.

## Iframe Generation

The `iframeGen.py` file contains a Flask application with a single route (`/pesapal/iframeGen`) that handles POST
requests. When a request is made to this route, it calls the authentication function to get a token, and then it sends a
POST request to the PesaPal API to generate an iframe URL for the payment page.

## Running the Application

To run the application, navigate to the directory containing iframeGen.py and use the following command:

```bash
python iframeGen.py
```

The application will start a server at http://localhost:5000. thus navigate to the
url  http://127.0.0.1:5000/pesapal/iframeGen to view the iframe URL.