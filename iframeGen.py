from flask import Flask
from pesapal_py.payments import PesaPal
import jwt
import requests

app = Flask(__name__)


@app.route('/pesapal/iframeGen', methods=['POST'])
def get_iframe_url():
    # utilizing the demo-keys provided by pesapal sandbox
    merchant_key = 'qkio1BGGYAXTu2JOfm7XSXNruoZsrqEW'
    merchant_secret = 'osGQ364R49cXKeOYSpaOnT++rHs='

    pesapal = PesaPal(merchant_key, merchant_secret)
    auth = pesapal.authenticate()
    api_key = auth['token']

    merchant_info = {
        'consumer_key': merchant_key,
        'api_key': api_key,
    }
    # encode the merchant info into a jwt token
    jwt_token = jwt.encode(merchant_info, merchant_secret, algorithm='HS256')


if __name__ == '__main__':
    app.run(debug=True)
