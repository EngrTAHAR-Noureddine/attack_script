import json

from faker import Faker
import requests
import sys
import time


def send_data(base_url, data):
    # Define the API endpoint URL
    api_url = "http://" + base_url + "/register"
    # Convert the data to JSON format
    json_data = json.dumps(data)
    # Set the headers (if needed)
    headers = {
        "Content-Type": "application/json"
    }
    # Make the POST request
    response = requests.post(api_url, data=json_data, headers=headers)


def send_register(base_url):
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    password = fake.password()

    resource_info = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password
    }
    send_data(base_url, resource_info)


if __name__ == '__main__':
    # print(sys.argv)
    if len(sys.argv) > 0:
        base_url = sys.argv[1]
        while True:
            try:
                print("Send user...")
                send_register(base_url)
            except Exception as error:
                print("error : ", error)
                pass
            time.sleep(1)
