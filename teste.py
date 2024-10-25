import sys
import importlib
from generators import gerar_dados_perfil, gerar_senha_perfil, secmail, image_worker
from selenium.webdriver.common.by import By

def import_without_cache(module_name):
    # Remove the module from cache if it exists
    if module_name in sys.modules:
        del sys.modules[module_name]
    # Import the module freshly
    return importlib.import_module(module_name)

def main():
    global driver, InstagramScrapper, importlib, import_without_cache, sys
    global gerar_dados_perfil, gerar_senha_perfil, secmail, By, image_worker, teste, user_agent
    
    InstagramScrapper = import_without_cache("instagramScrapper").InstagramScrapper
    secmail = import_without_cache("generators.secmail")
    
    cookies = """[{'domain': '.instagram.com', 'httpOnly': True, 'name': 'rur', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '"VLL\\05469756023872\\0541761318292:01f7cf81b5a811a3fbda7cb6c8d5c1f222e0389012fb7eccc762264de01789d0cfc7cd67"'}, {'domain': '.instagram.com', 'expiry': 1737558292, 'httpOnly': False, 'name': 'ds_user_id', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '69756023872'}, {'domain': '.instagram.com', 'expiry': 1761231892, 'httpOnly': False, 'name': 'csrftoken', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'RCDpusvOc1KR6tDFQWZM7ACzWD881b6I'}, {'domain': '.instagram.com', 'expiry': 1761318111, 'httpOnly': True, 'name': 'sessionid', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '69756023872%3Ai1XPPEGG97zOmh%3A14%3AAYeTqtMRJEPNg3EjPfvfCd9o67qJ2lSUhZ-pAjn3Uw'}, {'domain': '.instagram.com', 'expiry': 1761318068, 'httpOnly': False, 'name': 'fbm_124024574287414', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'base_domain=.instagram.com'}, {'domain': '.instagram.com', 'expiry': 1730387073, 'httpOnly': False, 'name': 'wd', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '1920x909'}, {'domain': '.instagram.com', 'expiry': 1764342067, 'httpOnly': True, 'name': 'datr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'I2EaZ-sZy9ePrIaqEsPrn6WN'}, {'domain': '.instagram.com', 'expiry': 1761318069, 'httpOnly': True, 'name': 'ig_did', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '29FE7D84-B80D-46BE-85CE-F907699B9B8C'}, {'domain': 'www.instagram.com', 'httpOnly': False, 'name': 'fbsr_124024574287414', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'vbsYJCBvks2QrD3HWtnDaiM0-sm_QPCiJ1dcApG5wpI.eyJ1c2VyX2lkIjoiNjE1Njc2Nzk5NjY5NTgiLCJjb2RlIjoiQVFBR2dOekFNc2pfWHJ4bklVZHVfMVZUelFDSWdnQUk0c1BkTkxsSElhUXhScDNDd2pKYWVOejIxUWVWQXZnU2otOWh6dDJJV0hydnp1aGNoSjR0UlJGSjhrR19HdVJIcy04U0hQZzdoRTloclF0cUZ0cnF0U29ldTA4NXhqLXlCSEpCd1JyWkY5LURqNHpnZWZsdm5xZTNEUmV3NnRDemJCNDQzalNJdktmejVJdktqQ1Jsd0NuR2ZGLUlkWkoyRlU2SkZTaVFGaHBleUk4QmNyU0VtOGtRMC1qX2d2WE1CNU5KOTJQVmxDeDNIa05fWmoxcDBYSThOVlJ2Q0JyTDhwWWN4M1E4QmplQmY0RGNmcmlwVmJtU1VUWjlJYkNWVkx6QTVjclQ1MTZsdXc1T0NDNlZTU2hiLTJqbWU4MmJJSUFqc2ROcnNOc0dkejI4c0w2TDEtZXQiLCJvYXV0aF90b2tlbiI6IkVBQUJ3ekxpeG5qWUJPMGQ1d1dVeDlzRmFKOTlFVE1WaDMxTlVHV3k2WkJaQ1lGVE1hNmFZNFFtd29iUlV6MmRFQ1R2U29aQjlaQzhiaFFXdVZrMlI2Y3duelU4RlV6dmlVM1pDZUh0eDdCV0dmczljQUhkRjcwRFZUeHU1aFZhZjFkZnZJTjJWcEdFRjAzRmpUZUJhbWlFN29BWkJrdXpaQVltNjJPVzZRdmpHZ1pDRXA0ZWhyNzhLazJ2REs2blJicUlaQXV6eGNXSEQ5enBRWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTcyOTc4MjA2OH0'}, {'domain': '.instagram.com', 'expiry': 1761318066, 'httpOnly': False, 'name': 'ig_nrcb', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '1'}, {'domain': '.instagram.com', 'httpOnly': False, 'name': 'fbsr_124024574287414', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'vbsYJCBvks2QrD3HWtnDaiM0-sm_QPCiJ1dcApG5wpI.eyJ1c2VyX2lkIjoiNjE1Njc2Nzk5NjY5NTgiLCJjb2RlIjoiQVFBR2dOekFNc2pfWHJ4bklVZHVfMVZUelFDSWdnQUk0c1BkTkxsSElhUXhScDNDd2pKYWVOejIxUWVWQXZnU2otOWh6dDJJV0hydnp1aGNoSjR0UlJGSjhrR19HdVJIcy04U0hQZzdoRTloclF0cUZ0cnF0U29ldTA4NXhqLXlCSEpCd1JyWkY5LURqNHpnZWZsdm5xZTNEUmV3NnRDemJCNDQzalNJdktmejVJdktqQ1Jsd0NuR2ZGLUlkWkoyRlU2SkZTaVFGaHBleUk4QmNyU0VtOGtRMC1qX2d2WE1CNU5KOTJQVmxDeDNIa05fWmoxcDBYSThOVlJ2Q0JyTDhwWWN4M1E4QmplQmY0RGNmcmlwVmJtU1VUWjlJYkNWVkx6QTVjclQ1MTZsdXc1T0NDNlZTU2hiLTJqbWU4MmJJSUFqc2ROcnNOc0dkejI4c0w2TDEtZXQiLCJvYXV0aF90b2tlbiI6IkVBQUJ3ekxpeG5qWUJPMGQ1d1dVeDlzRmFKOTlFVE1WaDMxTlVHV3k2WkJaQ1lGVE1hNmFZNFFtd29iUlV6MmRFQ1R2U29aQjlaQzhiaFFXdVZrMlI2Y3duelU4RlV6dmlVM1pDZUh0eDdCV0dmczljQUhkRjcwRFZUeHU1aFZhZjFkZnZJTjJWcEdFRjAzRmpUZUJhbWlFN29BWkJrdXpaQVltNjJPVzZRdmpHZ1pDRXA0ZWhyNzhLazJ2REs2blJicUlaQXV6eGNXSEQ5enBRWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTcyOTc4MjA2OH0'}, {'domain': '.instagram.com', 'expiry': 1764342066, 'httpOnly': False, 'name': 'mid', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'ZxphMgALAAHxnNyotz8vLj0rs-Ah'}]"""
    instagram_scrapper = InstagramScrapper(driver, cookies)
    
    # driver.get("https://www.instagram.com/")
    # instagram_scrapper.set_cookies()
    # input("Pressione Enter para continuar...")        
    # driver.refresh()
    
    username = "alineribeiro5745"
    email = "zuq5nx7wsrlg9ec34jm8fobkh@1secmail.com"
    # driver.get(f"https://www.instagram.com/{username}")
    # image_original_path = "./imagem/img.jpg"
    # imgage_output_path = "./imagem/img_sem_metadados.jpg"
    
    # image_worker.remove_metadata(image_original_path, imgage_output_path)
    # image_worker.modify_image_to_change_hash(imgage_output_path, imgage_output_path)
    
    # from instagram_api import InstagramAPI
    
    # instagram_api = InstagramAPI(user_agent, cookies, email, username)
    input("FIM... pressione enter para continuar")

def parse_header_cookies_to_dict(header):
    cookies = {}
    for cookie in header.split(";"):
        try:
            key, value = cookie.split("=", 1)
            cookies[key] = value
        except:
            print(cookie)
    return cookies

main()
