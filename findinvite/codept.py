import requests
import itertools
import time
import random

def generate_combinations(code):
    """Generate all possible combinations of upper and lower case for a given code."""
    return set([''.join(combination) for combination in itertools.product(*((char.lower(), char.upper()) for char in code))])

def check_invite(code):
    """Check if the given code is a valid Discord invite."""
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
        return response.json()
    elif response.status_code == 404 and response.json().get('code') == 10006:
        return None
    else:
        print(f"Erro na requisição: {response.status_code} - {response.text}")
        return None

def main():
    user_input = input("Digite o link do convite do Discord: ").strip()
    code = user_input.split('/')[-1]

    # Test the original code first
    print(f"Testando o código original: {code}")
    result = check_invite(code)
    if result:
        print(f"Convite encontrado: {code}")
        print(f"https://discord.gg/{code}")
        return

    # If the original code is not valid, generate and test combinations
    combinations = generate_combinations(code)
    total_combinations = len(combinations)

    print(f"Número estimado de tentativas: {total_combinations}")

    for index, combination in enumerate(combinations):
        result = check_invite(combination)
        
        if result:
            print(f"Convite encontrado: {combination}")
            print(f"https://discord.gg/{combination}")
            break

        time.sleep(1)  # Delay to avoid hitting rate limits
        print(f"Tentativa {index + 1}/{total_combinations} - {combination} não é válido")

    print("Nenhuma combinação válida encontrada.")

if __name__ == "__main__":
    main()
