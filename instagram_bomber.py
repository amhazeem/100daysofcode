from pprint import pprint
from time import sleep
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException, TimeoutException
from selenium.webdriver import Chrome
import random
import pyperclip

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait

name=['ade','yosola','align','Willia','Abisade','aliyu','risikat','rahmanfire']
CHAR = "qwertyuipoiuytrwertkjhgfdzxcvbnm"
data={}
driver = Chrome('chromedriver.exe')
wait=WebDriverWait(driver,10)
def generate_details():
    print("Starting program")
    data['username']="__".join( ["".join(random.sample(name,3)) ,"".join(random.sample(CHAR,3)) ])
    data['email'] =data['username'] + "@yahoo.com"
    data['password']="P@ssword123*"
    data['fullname']=" ".join(data['username'].split('_'))

def main():
    generate_details()
    POST_URL=pyperclip.paste()
    driver.get('https://instagram.com')
    driver.find_element_by_name('emailOrPhone').send_keys(data['email'].lower())
    sleep(1)
    driver.find_element_by_name('fullName').send_keys(data['fullname'])
    sleep(1)
    driver.find_element_by_name('username').send_keys(data['username'].lower())
    sleep(1)
    driver.find_element_by_name('password').send_keys(data['password'])
    sleep(1)
    print("Details updated \n Using: ")
    pprint(data)
    # submit registration
    btn = driver.find_elements_by_tag_name('button')
    sign_up = next((x for x in btn if x.text == "Sign up"), None)
    print("Signing Up")
    sign_up.click()
    sleep(4)
    try:
        sign_up.click()
    except WebDriverException:
        sleep(3)
        sign_up.click()
    sleep(5)
    suggested_follow = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.TAG_NAME,'button'),'Follow')) #driver.find_elements_by_tag_name('button')
    if suggested_follow is not None:
        suggested_follow=driver.find_elements_by_tag_name('button')
        print([a.text for a in suggested_follow])
        print("Cancelling desktop notifications")
        suggested_follow[-1].click()
        print("Following a couple of users")
        for a in suggested_follow[:3]:
            a.click()
            sleep(1)
        # Navigate to the instagram post
        sleep(2)
        print("Navigatign to the post")
        driver.get(POST_URL)
        # Play video
        print("Trying to play video")
        sleep(5)
        element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.TAG_NAME,'video')))
        if element:
            # driver.execute_script('document.getElementsByTagName("video")[0].play()')
            pass
        # Like Video

        print('Liking video')
        btn = driver.find_element_by_xpath("//span[@class='fr66n']/button").click()
        # Comment
        print("Commenting Yes!!")
        # element = WebDriverWait(driver, 5).until(
        #     EC.presence_of_element_located((By.XPATH, "//textarea[@class='Ypffh'")))
        # element.send_keys("Yes")
        # # Type Enter
        # element.send_keys(Keys.ENTER)
        print('Success')
        print("Closing this account")
        driver.quit()

if __name__ == '__main__':
    while True:

        try:
            main()
        except Exception:
            driver.quit()
            driver.close()
        except StaleElementReferenceException:
            driver.quit()
            driver.close()
        except TimeoutException:
            driver.quit()
            driver.close()
        finally:
            driver=Chrome()
            main()