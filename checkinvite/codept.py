import requests
import random

def check_invite(code):
    """Verifica se o código dado é um convite válido do Discord."""
    url = f"https://discord.com/api/v9/invites/{code}?with_counts=true&with_expiration=true"
    headers = {
        'User-Agent': random.choice([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'
        ])
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return True
    elif response.status_code == 404 and response.json().get('code') == 10006:
        return False
    else:
        print(f"Erro na requisição: {response.status_code} - {response.text}")
        return False

def main():
    user_input = input("Digite os links de convite do Discord separados por vírgulas: ").strip()
    links = user_input.split(',')

    for link in links:
        code = link.split('/')[-1].strip()
        is_valid = check_invite(code)
        status = "válido" if is_valid else "inválido"
        print(f"{link.strip()} - {status}")

if __name__ == "__main__":
    main()
