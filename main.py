from bot_scrapper import bot_scrapper
import json, os

def load_config():
    if os.path.exists('config.json') == False:
        print("Sem configuração salva")
        save_config({})
        return {}
    
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

def save_config(config):
    with open('config.json', 'w') as f:
        f.write(json.dumps(config))
        
def main():
    config = load_config()
    
    facebook_cookies = input(f"Insira cookies do facebook ({config.get('facebook_cookies', '')[:5]}): ") or config.get('facebook_cookies')
    proxy = input(f"Insira proxy ({config.get('proxy')}): ") or config.get('proxy')
    headless = input(f"Mostrar navegador? s/n ({config.get('headless')}): ") or config.get('headless')
    bot_index = input(f"Insira indice do bot (0): ") or 0
    
    config = {
        'facebook_cookies': facebook_cookies,
        'proxy': proxy,
        'headless': headless,
        'bot_index': bot_index
    }
    save_config(config)
    bot_scrapper(facebook_cookies, proxy, bot_index, headless=='n')
    

if __name__ == '__main__':
    main()