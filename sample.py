import requests

# Replace these with your actual API credentials from FYERS developer portal
CLIENT_ID = 'your_client_id'
SECRET_KEY = 'your_secret_key'

# FYERS API base URL
API_BASE_URL = 'https://api.fyers.in/api/v1/'

# API endpoints
LOGIN_ENDPOINT = 'auth'
ACCOUNT_INFO_ENDPOINT = 'profile'

def get_access_token():
    auth_params = {
        'appId': CLIENT_ID,
        'secretKey': SECRET_KEY
    }

    response = requests.post(API_BASE_URL + LOGIN_ENDPOINT, data=auth_params)
    if response.status_code == 200:
        return response.json().get('data', {}).get('accessToken')
    else:
        raise Exception("Failed to get access token.")

def get_account_info(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(API_BASE_URL + ACCOUNT_INFO_ENDPOINT, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to get account information.")

if __name__ == "__main__":
    try:
        access_token = get_access_token()
        print("Access Token:", access_token)

        account_info = get_account_info(access_token)
        print("Account Information:")
        print(account_info)

    except Exception as e:
        print("Error:", e)
