from flask import Flask, jsonify
import requests
import auth

app = Flask(__name__)


@app.route('/pesapal/iframeGen', methods=['POST'])
def get_iframe_url():
    token = auth.authentication()

    api_url = " https://cybqa.pesapal.com/pesapalv3/api/Transactions/SubmitOrderRequest"
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    payload = {
        "Amount": 1000,
        "Description": 'Sample payment description',
        "Type": "MERCHANT",
        "Reference": "sample_transaction_id",
        "PhoneNumber": "254722001122",
        "Email": "ariesmanga@outlook.com",
        "Currency": "KES",
        "CallbackUrl": 'https://google.com',
    }
    response = requests.post(api_url, headers=headers, json=payload)

    # print(f"Response Content: {response.text}")
    # return {'message': response.text}, response.status_code

    if response.status_code == 200:
        iframe_url = response.json()
        return {'iframe_url': iframe_url}
    else:
        return {'message': response.text}, response.status_code


if __name__ == '__main__':
    app.run(debug=True)
