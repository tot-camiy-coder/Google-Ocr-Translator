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


# -- PREFERENSES --
DOWNLOAD_FILE = 'C:/Users/none/Downloads/translated_image_ru.png'

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
    # Функция для клика через JS
    def click_js(selector, index=0):
        script = f"""
        var elems = document.querySelectorAll('{selector}');
        if(elems.length > {index}) {{
            elems[{index}].click();
            return true;
        }} else {{
            return false;
        }}
        """
        return driver.execute_script(script)

    # если есть кнопка закрытия, закрываем
    try:
        if not click_js('.VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.mN1ivc.B0czFe'):
            print("no found close button 1/4")
    except:
        print("no found close button 1/4")

    time.sleep(0.1)

    # вставляем скопированное изображение в Google
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    time.sleep(0.1)
    
    # ждём и кликаем по кнопке загрузки
    try:
        for i in range(6):
            #print(driver.execute_script("return document.querySelectorAll('.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.LjDxcd.XhPA0b.LQeN7.qaqQfe').length"))
            if not click_js(".VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.LjDxcd.XhPA0b.LQeN7.qaqQfe", 1):
                time.sleep(.1)
                set_focus()
                continue
            else:
                break
        else:
            raise None
    except:
        print("no found download button 2/4")
        try:
            for i in range(6):
                if not click_js(".VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.mN1ivc.VThJZd", 1):
                    time.sleep(.1)
                    set_focus()
                    continue
                else:
                    break
            else:
                raise None
        except:
            print("no found small download button 3/4")
    
    
    # если есть кнопка закрытия, закрываем
    try:
        if not click_js('.VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.mN1ivc.B0czFe'):
            print("no found close button 1/4")
    except:
        print("no found close button 1/4")

    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    time.sleep(0.05)
    pyautogui.keyUp('alt')
    # ждём загрузки .png файла
    time.sleep(.4)


def download():
    def click_js(selector, index=0):
        script = f"""
        var elems = document.querySelectorAll('{selector}');
        if(elems.length > {index}) {{
            elems[{index}].click();
            return true;
        }} else {{
            return false;
        }}
        """
        return driver.execute_script(script)
    try:
        for i in range(6):
            #print(driver.execute_script("return document.querySelectorAll('.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.LjDxcd.XhPA0b.LQeN7.qaqQfe').length"))
            if not click_js(".VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.LjDxcd.XhPA0b.LQeN7.qaqQfe", 1):
                time.sleep(.1)
                set_focus()
                continue
            else:
                break
        else:
            raise None
    except:
        print("no found download button 2/4")
        try:
            for i in range(6):
                if not click_js(".VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.mN1ivc.VThJZd", 1):
                    time.sleep(.1)
                    set_focus()
                    continue
                else:
                    break
            else:
                raise None
        except:
            print("no found small download button 3/4")

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


if __name__ == '__main__':
    keyboard.add_hotkey("ctrl+alt+x", work4screatch)
    keyboard.add_hotkey("ctrl+alt+c", work4already)

    print("* Ctrl+Alt+X - перевести скриншот. \n* Ctrl+Alt+C - перевести изображение которое в буфере обмена. \n* ESC - для выхода.")

    keyboard.wait('esc')