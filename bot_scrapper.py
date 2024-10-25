import dotenv
dotenv.load_dotenv()
from generators import gerar_dados_perfil, gerar_senha_perfil, secmail
from selenium.webdriver.common.by import By
from instagramScrapper import InstagramScrapper
from chrome_driver import get_chromedriver

def bot_scrapper(facebook_cookies, proxy, bot_index, headless):
    driver, user_agent = get_chromedriver(proxy, headless)
    
    email = secmail.gerar_email_secmail()
    senha = gerar_senha_perfil.gerar_senha_perfil()
    print(f"Senha: {senha}")
    print(f"Email: {email}")
    
    instagram_scrapper = InstagramScrapper(driver, facebook_cookies)
        
    res = instagram_scrapper.entrar_facebook()
    
    if not res:
        print("Erro ao entrar no facebook")
        exit(1)
    
    username = instagram_scrapper.signup_instagram(senha)
    print(f"Username: {username}")
    
    if not username:
        print("Erro ao criar conta no instagram")
        exit(1)
    
    instagram_scrapper.desvincular_facebook()
    
    instagram_scrapper.adicionar_email(email)
    
    instagram_scrapper.seguir_contas()
    
    insta_cookies = driver.get_cookies()
    
    
    print(f"Cookie: {insta_cookies}")
    
    # append to file
    with open(f"contas_criadas_bot_{bot_index}.txt", "a") as f:
        f.write("\n\n\n")
        f.write(f"Username: {username}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Senha: {senha}\n")
        f.write(f"Cookie: {insta_cookies}\n\n")