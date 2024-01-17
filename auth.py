import jwt
import requests
from pesapal_py.payments import PesaPal


def authentication():
    # Utilizing the demo-keys provided by Pesapal Sandbox in their documentation
    global auth_response
    merchant_key = 'qkio1BGGYAXTu2JOfm7XSXNruoZsrqEW'
    merchant_secret = 'osGQ364R49cXKeOYSpaOnT++rHs='

    pesapal = PesaPal(merchant_key, merchant_secret)
    auth = pesapal.authenticate()
    api_key = auth['token']

    merchant_info = {
        'consumer_key': merchant_key,
        'api_key': api_key,
    }
    # Encode the merchant info into a JWT token
    jwt_token = jwt.encode(merchant_info, merchant_secret, algorithm='HS256')
    api_url = 'https://cybqa.pesapal.com/pesapalv3/api/Auth/RequestToken'
    headers = {
        'Authorization': f'Bearer {jwt_token}',
        'Content-Type': 'application/json'
    }

    try:
        auth_response = requests.post(api_url, headers=headers)
        auth_response.raise_for_status()  # Raise an exception if the response status code is not 200
        print(auth_response.text)  # Print the response content for debugging
    except requests.RequestException as e:
        print(f"Error during API request: {e}")

    return auth_response.json()['token']
