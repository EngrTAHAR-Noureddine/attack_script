import random
import string
import json
import requests
import sys
import time


def generate_random_word(length):
    characters = string.printable  # All printable ASCII characters
    word = ''.join(random.choice(characters) for _ in range(length))
    return word


def get_data(base_url, data):
    # Define the API endpoint URL
    api_url = "http://" + base_url + "/api/md5/decrypt?password="+data
    # Make the POST request
    response = requests.get(api_url)

    return response.json()


def send_request(base_url):
    try:
        word_length = random.randint(1, 50)
        word = generate_random_word(word_length)
        get_data(base_url, word)
    except Exception as error:
        pass


if __name__ == '__main__':
    # print(sys.argv)
    if len(sys.argv) > 0:
        base_url = sys.argv[1]
        while True:
            try:
                print("get password...")
                send_request(base_url)
            except Exception as error:
                print("error : ", error)
                pass
            time.sleep(1)
