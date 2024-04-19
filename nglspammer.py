import requests
import time

def send_post_spam(username, message):
    url = 'https://ngl.link/api/submit'
    payload = {'username': username, 'question': message, 'deviceId': ""}
    headers = {'Content-Type': 'application/json'} 
    response = requests.post(url, json=payload, headers=headers) 
    return response.status_code

def main():
    banner_text = """
    █▄░█ █▀▀ █░░ █▀ █▀█ ▄▀█ █▀▄▀█
    █░▀█ █▄█ █▄▄ ▄█ █▀▀ █▀█ █░▀░█
    by libyzxy0
    """
    banner = f"\033[94m{banner_text}\033[0m"
    print(banner)
    username = input("\033[92mEnter username: \033[0m")
    message = input("\033[92mEnter message: \033[0m")
    amount = int(input("\033[92mEnter amount: \033[0m"))

    for i in range(amount):
        status_code = send_post_spam(username, message)
        colored_message = f"\033[94m[{i}][{'success' if status_code == 200 else 'error'}]: Message sent to target: {username}\033[0m"
        print(colored_message)
        time.sleep(1) # delay for 1 econds

if __name__ == "__main__":
    main()
