import requests
import random
from itertools import cycle

def send_post_spam(username, message, proxy):
    url = 'https://ngl.link/api/submit'
    payload = {'username': username, 'question': message, 'deviceId': ""}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers, proxies=proxy)
    return response.status_code

def read_proxies_from_file(filename):
    with open(filename, 'r') as file:
        proxies = [{'http': line.strip()} for line in file.readlines()]
    return proxies

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
    
    proxy_file = "proxy.txt"
    proxies = read_proxies_from_file(proxy_file)

    proxy_pool = cycle(proxies)
    success_count = 0
    for i in range(amount):
        proxy = next(proxy_pool)
        status_code = send_post_spam(username, message, proxy)
        if status_code == 200:
            success_count += 1
            colored_message = f"\033[92m[{success_count}][Success]: Message sent to target: {username}\033[0m"
            print(colored_message)

if __name__ == "__main__":
    main()
