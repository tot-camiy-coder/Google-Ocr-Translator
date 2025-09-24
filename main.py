from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time
import keyboard
import grab, utils, os
from PIL import Image
import pygetwindow as gw
import pyautogui
import getpass
#

# -- PREFERENSES --
DOWNLOAD_FILE = 'C:/Users/'+getpass.getuser()+'/Downloads/translated_image_ru.png'
print(DOWNLOAD_FILE)

# -- START BROWSER --
options = uc.ChromeOptions()
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.clipboard": 1
})

driver = uc.Chrome(options=options)
driver.set_window_position(50,50)
driver.set_window_size(200,200)

driver.get("https://translate.google.co.in/?sl=auto&tl=ru&op=images")

time.sleep(6) # loading site


def paste_and_result():
    # если есть кнопка закрытия, закрываем
    try:
        elem = driver.find_element(By.CSS_SELECTOR, '.VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.mN1ivc.B0czFe')
        elem.click()
    except:
        print("no found close button ")

    time.sleep(0.1)

    download()
    
    # если есть кнопка закрытия, закрываем
    try:
        elem = driver.find_element(By.CSS_SELECTOR, '.VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.mN1ivc.B0czFe')
        elem.click()
    except:
        print("no found close button ")

    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    time.sleep(0.05)
    pyautogui.keyUp('alt')
    # ждём загрузки .png файла
    time.sleep(.4)


def download():
    # вставляем скопированное изображение в Google
    #ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    try:
        elem = driver.find_element(By.CSS_SELECTOR, '.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-INsAgc.VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.Rj2Mlf.OLiIxf.PDpWxe.LQeN7.yUbRwc.xupp0')
        elem.click()
    except:
        print("no found paste button")
    time.sleep(0.1)

    # Прокрутка в начало страницы
    driver.execute_script("window.scrollTo(0, 0);")

    # ждём и кликаем по кнопке загрузки
    try:
        for i in range(2):
            #print(driver.execute_script("return document.querySelectorAll('.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.LjDxcd.XhPA0b.LQeN7.qaqQfe').length"))
            elem = driver.find_elements(By.CSS_SELECTOR, ".VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.LjDxcd.XhPA0b.LQeN7.qaqQfe")
            elem[1].click()
            break
        else:
            raise None
    except:
        print("no found download button ")
        try:
            for i in range(2):
                elem = driver.find_elements(By.CSS_SELECTOR, ".VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.mN1ivc.VThJZd")
                elem[1].click()
                break
            else:
                raise None
        except:
            print("no found small download button ")

def work4screatch():
    region = grab.ScreenSelection().get_region()
    if region is None or all(v == 0 for v in region):
        return
    
    screenshot = utils.screenshot_region(region)
    if os.path.isfile(DOWNLOAD_FILE):
        os.remove(DOWNLOAD_FILE)
    utils.img2clipboard(screenshot)
    
    paste_and_result()

    while not os.path.isfile(DOWNLOAD_FILE):
        download()
        time.sleep(.4)
    
    grab.ImageRegion(region, Image.open(DOWNLOAD_FILE))

def work4already():
    if os.path.isfile(DOWNLOAD_FILE):
        os.remove(DOWNLOAD_FILE)
    
    paste_and_result()

    while not os.path.isfile(DOWNLOAD_FILE):
        download()
        time.sleep(.4)
    
    grab.ImageTopRight(Image.open(DOWNLOAD_FILE))

def set_focus():
    for i in range(5):
        try:
            win = gw.getWindowsWithTitle(driver.title)[0]
            win.activate()
            break
        except gw.PyGetWindowException:
            size = driver.get_window_size()
            x = size['width']
            y = size['height']
            driver.set_window_size(int(x)+10, int(y)+10)
            print("Size Up")


if __name__ == '__main__':
    keyboard.add_hotkey("ctrl+alt+x", work4screatch)
    keyboard.add_hotkey("ctrl+alt+c", work4already)

    print("* Ctrl+Alt+X - перевести скриншот. \n* Ctrl+Alt+C - перевести изображение которое в буфере обмена. \n* ESC - для выхода.")

    keyboard.wait('esc')