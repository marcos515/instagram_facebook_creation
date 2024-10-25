from requests import get
from json import loads
from time import sleep
from random import sample, choice
from string import ascii_lowercase, digits
import re

def gerar_email_secmail():
    try:
        usuario_email = ''.join(sample(ascii_lowercase + digits, 25))
        
        api_dominios = get(
            url='https://www.1secmail.com/api/v1/',
            params={
                'action': 'getDomainList'
            }
        )

        dominios = loads(api_dominios.text)

        try:
            dominios.remove('dpptd.com')
            dominios.remove('rteet.com')
        except:
            pass
        email = f'{usuario_email}@{choice(dominios)}'
        return email
    
    except:
        return False

def pegar_codigo_secmail(email, tempo):
    resultado = False

    for x in range(int(tempo)):
        try:
            login = email.split('@')[0]
            dominio = email.split('@')[1]
            
            api = get(
                url='https://www.1secmail.com/api/v1/',
                params={
                    'action': 'getMessages',
                    'login': login,
                    'domain': dominio
                }
            )
            message_id = loads(api.text)[0]['id']
            
            html_body = get(
                url='https://www.1secmail.com/api/v1/',
                params={
                    'action': 'readMessage',
                    'login': login,
                    'domain': dominio,
                    'id': message_id
                }
            ).json()['body']
            
            match = re.search(r'confirmation code:.*?(\d{6})', html_body)
            if match:
                return match.group(1)
        
        except:
            continue
        finally:
            sleep(5)
    return resultado


if __name__ == "__main__":
    email = gerar_email_secmail()
    print(email)
    print(pegar_codigo_secmail(email, 10))