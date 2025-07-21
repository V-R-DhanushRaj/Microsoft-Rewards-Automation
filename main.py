from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, random
import words

USER_DATA_DIR = r""
PROFILE_LIST = ['Profile 1', 'Profile 2']
DRIVER_PATH = ""
NO_OF_SEARCHES = 15

Service = webdriver.EdgeService(executable_path=DRIVER_PATH)


class WebProfile(webdriver.Edge):
    def __init__(self, option):
        super().__init__(service=Service, options=option)
        self.get('https://www.bing.com')
        time.sleep(10)  # Time required to login

    def do_search(self, no):
        word_list = words.WORDS_LIST
        for _ in range(no):
            word = random.choice(word_list)
            try:
                search_box = self.find_element(By.NAME, 'q')
                search_box.clear()

                search_box.send_keys(word)
                search_box.send_keys(Keys.RETURN)
                time.sleep(20)  # For Gap between Search

            except:
                print('Error')
            word_list.remove(word)




for profile in PROFILE_LIST:
    profile_option = Options()
    profile_option.add_argument(f"user-data-dir={USER_DATA_DIR}")
    profile_option.add_argument(f'profile-directory={profile}')

    web = WebProfile(profile_option)
    web.do_search(NO_OF_SEARCHES)
    time.sleep(10)

    web.quit()

