import os
import zipfile
from selenium import webdriver
from fake_useragent import UserAgent

ua = UserAgent(platforms='pc')

def get_chromedriver(proxy, headless=False):
    try:
        PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS = proxy.split(":")
        print(f"Using proxy: {PROXY_HOST}:{PROXY_PORT} with user: {PROXY_USER}")
    except ValueError:
        raise ValueError("PROXY environment variable is not set correctly. Use format 'host:port:user:pass'.")

    # Chrome extension manifest for proxy
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    # JavaScript for background script to handle proxy authentication
    background_js = f"""
    var config = {{
            mode: "fixed_servers",
            rules: {{
            singleProxy: {{
                scheme: "http",
                host: "{PROXY_HOST}",
                port: parseInt({PROXY_PORT})
            }},
            bypassList: ["localhost"]
            }}
        }};

    chrome.proxy.settings.set({{value: config, scope: "regular"}}, function() {{}});

    function callbackFn(details) {{
        return {{
            authCredentials: {{
                username: "{PROXY_USER}",
                password: "{PROXY_PASS}"
            }}
        }};
    }}

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {{urls: ["<all_urls>"]}},
                ['blocking']
    );
    """

    # Path setup for storing the proxy plugin
    path = os.path.dirname(os.path.abspath(__file__))
    chrome_options = webdriver.ChromeOptions()
    user_agent = ua.random
    chrome_options.add_argument(f'--user-agent={user_agent}')
    chrome_options.add_argument("--start-maximized")  # Adiciona a janela cheia
    
    pluginfile = os.path.join(path, 'proxy_auth_plugin.zip')

    # Create the proxy plugin zip file
    with zipfile.ZipFile(pluginfile, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    chrome_options.add_extension(pluginfile)

    # Set the path to the Chrome binary and driver
    chrome_options.binary_location = '/usr/bin/google-chrome'  # Adjust if necessary
    
    if headless:
        chrome_options.add_argument("--headless")
        
    driver = webdriver.Chrome(options=chrome_options)
    return driver, user_agent

def main():
    # Load environment variables from .env file
    from dotenv import load_dotenv
    load_dotenv()

    # Initialize Chrome WebDriver with proxy
    driver = get_chromedriver(use_proxy=True)

    try:
        driver.get('https://httpbin.org/ip')
    except Exception as e:
        print(f"Error while browsing: {e}")
    finally:
        input("Press Enter to close the browser...")
        driver.quit()

if __name__ == '__main__':
    main()
