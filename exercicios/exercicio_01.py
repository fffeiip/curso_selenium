from selenium.webdriver import Firefox
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition
from selenium.webdriver.common.by import By



browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser.get(url)
timeout = 5


try:
    header_loaded = condition.presence_of_element_located((By.TAG_NAME, 'h1'))
    WebDriverWait(browser, timeout).until(header_loaded)
    header = browser.find_element(By.TAG_NAME,'h1')
    paragrafs = browser.find_elements(By.TAG_NAME,'p')

except TimeoutException:
    print('Page timeout')


def get_paragrafs():
    dic = {}
    for paragraf in paragrafs:
        dic.update({paragraf.get_attribute('atributo'):paragraf.text})    
    return dic

dicionario = {
    header.tag_name: get_paragrafs()        
}

print(dicionario)