import dotenv
dotenv.load_dotenv()
from generators import gerar_dados_perfil, gerar_senha_perfil, secmail
from selenium.webdriver.common.by import By
from instagramScrapper import InstagramScrapper
from chrome_driver import get_chromedriver


cookies = 'csrftoken=zOQpybprGdhe98JteHWV22XsKxACmWem;ig_did=84B9A427-E7CD-4711-B747-8D13A081DAEE;ig_nrcb=1;mid=ZxlecQALAAGHnBid5JIvdYdfmYZc;csrftoken=A1RCnLYfRpLGDzNHMxPFkF6N4kiaF5Fb;ds_user_id=70360256204;ig_did=84B9A427-E7CD-4711-B747-8D13A081DAEE;ig_nrcb=1;mid=ZxlecQALAAGHnBid5JIvdYdfmYZc;rur="EAG\05470360256204\0541761251857:01f7358bfb91d6b7f761712330bdd1f4397b47ec248e6c2d78200865c1e18e441964beca";sessionid=70360256204%3APT1ezWoCQY7MOF%3A27%3AAYdBrAJctF32kWzk6t3IDQd1IQfv89oqdx6Q7XEciQ'

driver, user_agent = get_chromedriver(use_proxy=True)

def exec_file(file_path):
    with open(file_path, "r") as f:
        exec(f.read(), globals(), locals())
        
if __name__ == "__main__":
    while True:
        try:
            exec_file("teste.py")
        except Exception as e:
            print(f"Erro: {e}")
            input("ERRO... Pressione enter para continuar")
            
            
    # email = secmail.gerar_email_secmail()
    # senha = gerar_senha_perfil.gerar_senha_perfil()
    # print(f"Senha: {senha}")
    # print(f"Email: {email}")
    
    # instagram_scrapper = InstagramScrapper(driver, cookies)
        
    # res = instagram_scrapper.entrar_facebook()
    
    # if not res:
    #     print("Erro ao entrar no facebook")
    #     exit(1)
    
    # username = instagram_scrapper.signup_instagram(senha)
    # print(f"Username: {username}")
    
    # if not username:
    #     print("Erro ao criar conta no instagram")
    #     exit(1)
    
    # instagram_scrapper.desvincular_facebook()
    
    # instagram_scrapper.adicionar_email(email)
    
    # instagram_scrapper.seguir_contas()
    
    # insta_cookies = driver.get_cookies()
    
    
    # print(f"Cookie: {insta_cookies}")
    
    # # append to file
    # with open("contas.txt", "a") as f:
    #     f.write("\n\n\n")
    #     f.write(f"Username: {username}\n")
    #     f.write(f"Email: {email}\n")
    #     f.write(f"Senha: {senha}\n")
    #     f.write(f"Cookie: {insta_cookies}\n\n")