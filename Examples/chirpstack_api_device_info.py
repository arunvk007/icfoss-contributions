import requests
import datetime 

# Chirpstack - credentials & urls
chirpstack_email = "email"  # Replace with your Chirpstack email
chirpstack_password = "password"  # Replace with your Chirpstack password
chirpstack_url = "url"  # Replace with your Chirpstack server URL

# Function to get device information
# API - /api/devices
def get_device_info(url, token): 
    # Set headers with authentication token
    headers = {
        "Accept": "application/json",
        "Grpc-Metadata-Authorization": "Bearer " + token
    }
    # Make a GET request to fetch device information
    response = requests.get(url + "/api/devices?limit=1", headers=headers, stream=False)
    # Parse the JSON response and extract device details
    response = response.json()['result']
    return response

# Function to get JWT token for authentication
# API - /api/internal/login
def apilogin(email, password, url):
    url = url + '/api/internal/login'
    credentials = '{"password": "' + password + '","email": "' + email + '"}'
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    # Make a POST request to obtain the JWT token
    response = requests.post(url, data=credentials, headers=headers)
    data = response.json()
    return data['jwt']

# Main function
def main():
    # Get the JWT token for authentication
    token = apilogin(chirpstack_email, chirpstack_password, chirpstack_url)
    
    # Fetch and print device information
    devices_info = get_device_info(chirpstack_url, token)
    print(devices_info)
           
     
if __name__ == "__main__":
    main()