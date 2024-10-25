from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generators import secmail
from time import sleep
import logging

# Configurando o logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - Step %(step)s - %(message)s')
logger = logging.getLogger(__name__)

class InstagramScrapper:
    def __init__(self, driver, facebook_cookies):
        self.driver = driver
        self._facebook_cookies = facebook_cookies
    
    def set_cookies(self):
        is_headers_cookies = not self._facebook_cookies.startswith("[{")
        if is_headers_cookies:
            for cookie in self._facebook_cookies.split(";"):
                try:
                    self.driver.add_cookie({"name": cookie.split("=")[0], "value": cookie.split("=")[1]})
                except Exception as e:
                    print(cookie)
                    self.log_step(2, f"Erro ao adicionar cookie: {e}")
        else:
            json_cookies = eval(self._facebook_cookies)
            for cookie in json_cookies:
                try:
                    self.driver.add_cookie(cookie)
                except Exception as e:
                    self.log_step(2, f"Erro ao adicionar cookie: {e}")
                
    def log_step(self, step_number, message):
        """Logs each step with a specific number for detailed tracking."""
        logger.info(message, extra={'step': step_number})

    def entrar_facebook(self, timeout=30):
        self.log_step(1, "Acessando Facebook.")
        self.driver.get("https://web.facebook.com/")
        sleep(5)  # Pequeno atraso para simular atraso humano
        self.log_step(2, "Adicionando cookies para login automático.")
        self.set_cookies()
        self.log_step(3, "Atualizando a página para validar login.")
        self.driver.refresh()
        sleep(10)  # Pequeno atraso para simular atraso humano
        
        self.log_step(4, "Verificando se o login foi bem-sucedido.")
        if "login" not in self.driver.current_url and "checkpoint" not in self.driver.current_url:
            if "log in" in self.driver.title or "sign" in self.driver.title:
                self.log_step(5, "Falha no login do Facebook.")
                # input("Pressione Enter para continuar (salvar cookie)...")
                # print(self.driver.get_cookies())
                return False
            self.log_step(5, "Login no Facebook bem-sucedido.")
            return True
        
        self.log_step(5, "Falha no login do Facebook.")
        return False

    def signup_instagram(self, password):
        self.log_step(6, "Acessando a página de registro do Instagram.")
        self.driver.get("https://www.instagram.com/accounts/emailsignup/")
        WebDriverWait(self.driver, 60).until(EC.url_contains("emailsignup"))

        self.log_step(7, "Clicando em 'Entrar com Facebook'.")
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CLASS_NAME, '_acan._acap._acas._aj1-._ap30'))
        ).click()
        sleep(2)  # Simulando atraso humano

        self.log_step(8, "Confirmando login como usuário do Facebook.")
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, '__CONFIRM__'))
        ).click()
        sleep(2)  # Simulando atraso humano

        self.log_step(9, "Finalizando o cadastro.")
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Yes, finish adding"]'))
        ).click()
        sleep(2)  # Simulando atraso humano

        self.log_step(10, "Inserindo senha.")
        input_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        input_password.send_keys(password)
        sleep(1)  # Pequeno atraso humano

        self.log_step(11, "Gerando nome de usuário sugerido.")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[span[text()="Refresh suggestion"]]'))
        ).click()

        sleep(2)  # Simulando atraso humano

        username = self.driver.find_element(By.NAME, "username").get_attribute("value")
        self.log_step(12, f"Nome de usuário gerado: {username}")

        self.log_step(13, "Confirmando o cadastro.")
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Sign up"]'))
        ).click()
        sleep(20)  # Simulando espera para o processo de cadastro
        
        if "sign up" in self.driver.title.lower():
            self.log_step(13, "Erro ao criar conta no Instagram.")
            sleep(20)
            if "sign up" in self.driver.title:
                self.log_step(13, "Erro ao criar conta no Instagram.")
                return None
        return username

    def desvincular_facebook(self):
        self.log_step(14, "Desvinculando Facebook da conta do Instagram.")
        self.driver.get("https://accountscenter.instagram.com/accounts/")
        WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@role="listitem"]')))
        sleep(2)  # Simulando atraso humano

        self.log_step(15, "Procurando cards relacionados ao Facebook.")
        cards = self.driver.find_elements(By.XPATH, '//div[@role="listitem"]')
        
        for idx, card in enumerate(cards, start=1):
            card_html = card.get_attribute('outerHTML')
            if "Facebook" in card_html:
                try:
                    self.log_step(16, f"Tentando remover a conexão do Facebook no Card {idx}.")
                    botao_remove = card.find_element(By.XPATH, './/a[contains(@aria-label, "Remove") or .//span[contains(text(), "Remove")]]')
                    botao_remove.click()
                    sleep(2)  # Simulando atraso humano
                except Exception as e:
                    self.log_step(16, f"Erro ao tentar remover no Card {idx}: {e}")
                    
        sleep(2)
        # Continuação dos passos para clicar nos botões de confirmação
        self._click_buttons("Remove account")
        sleep(2)  # Simulando atraso humano
        self._click_buttons("Continue")
        sleep(2)  # Simulando atraso humano
        self._click_buttons("Yes, remove")

        sleep(30)  # Espera final após remoção

    def _click_buttons(self, *button_texts):
        """Helper method to click buttons by their text, used in desvincular_facebook."""
        for text in button_texts:
            buttons = self.driver.find_elements(By.XPATH, '//*[@role="button"]')
            for button in buttons:
                button_html = button.get_attribute('outerHTML')
                if text in button_html and not "disabled" in button_html:
                    try:
                        button.click()
                        self.log_step(17, f"Botão '{text}' clicado com sucesso.")
                        sleep(2)  # Simulando atraso humano
                        break
                    except Exception as e:
                        # self.log_step(17, f"Erro ao clicar no botão '{text}'")
                        pass

    def adicionar_email(self, email):
        self.log_step(18, "Adicionando email ao perfil.")
        self.driver.get("https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point")
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//label[contains(text(), "Enter email address")]'))
        )
        sleep(1)  # Simulando atraso humano

        # Inserindo o endereço de e-mail
        label = self.driver.find_element(By.XPATH, '//label[contains(text(), "Enter email address")]')
        parent_div = label.find_element(By.XPATH, '..')
        input_field = parent_div.find_element(By.XPATH, './/input[@type="text"]')
        input_field.send_keys(email)

        self.log_step(19, "Selecionando checkbox de confirmação.")
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox' and @name='noform']"))
        )
        if not checkbox.is_selected():
            checkbox.click()
            sleep(1)  # Simulando atraso humano
            
        sleep(2)

        # Clique no botão "Next" ou "Continue"
        if not self._click_buttons("Next"):
            self._click_buttons("Continue")

        confirmation_code = secmail.pegar_codigo_secmail(email, 10)
        sleep(2)  # Simulando atraso humano

        self.log_step(20, "Inserindo código de confirmação.")

        # Checando entre dois possíveis labels para o código de confirmação
        try:
            label = self.driver.find_element(By.XPATH, '//label[contains(text(), "Enter confirmation code")]')
        except Exception:
            label = self.driver.find_element(By.XPATH, '//label[contains(text(), "Code")]')

        parent_div = label.find_element(By.XPATH, '..')
        input_field = parent_div.find_element(By.XPATH, './/input[@type="text"]')
        input_field.send_keys(confirmation_code)
        sleep(5)  # Pequeno atraso humano

        # Clique no botão "Next" ou "Continue" após inserir o código
        if not self._click_buttons("Next"):
            self._click_buttons("Continue")

        sleep(15)  # Simulando espera final para confirmação

    def _click_buttons(self, *button_texts):
        """Helper method to click buttons by their text, used in adicionar_email and desvincular_facebook."""
        for text in button_texts:
            buttons = self.driver.find_elements(By.XPATH, '//*[@role="button"]')
            for button in buttons:
                button_html = button.get_attribute('outerHTML')
                if text in button_html and not "disabled" in button_html:
                    try:
                        button.click()
                        self.log_step(21, f"Botão '{text}' clicado com sucesso.")
                        sleep(2)  # Simulando atraso humano
                        return True
                    except Exception as e:
                        #self.log_step(21, f"Erro ao clicar no botão '{text}'")
                        pass
        return False

    def seguir_contas(self):
        self.log_step(21, "Seguindo contas sugeridas no Instagram.")
        self.driver.get('https://www.instagram.com/explore/people/')
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//button[div/div[text()="Follow"]]')))
        sleep(2)  # Simulando atraso humano
        
        botoes_seguir = self.driver.find_elements(By.XPATH, '//button[div/div[text()="Follow"]]')
        seguir = 6
        for botao_seguir in botoes_seguir:
            if seguir == 0:
                break
            botao_seguir.click()
            seguir -= 1
            sleep(2)  # Atraso humano entre cliques
        sleep(5)  # Espera final após seguir as contas
