# Google-Ocr-Translator

Скрипт для быстрого перевода изображений через [Google Translate](https://translate.google.com/) 
> [!NOTE]
> Мне нужно было быстро получать перевод части экрана через Google Translate, но вариант **Shift+Win+S** + **Alt+Tab** + **Ctrl+V** мне не понравился
> и я решил написать данный скрипт.

## Функции
- Перевод части экрана (**Ctrl+Alt+X**, **Click** — закрыть).
- Перевод скопированного изображения (**Ctrl+Alt+C**, **DoubleClick** — закрыть, **Scroll** — увеличить/уменьшить, **ЛКМ** — переместить).
- Не требует **Google Cloud API**, всё работает через эмуляцию браузера.

## Установка
```bash
git clone https://github.com/tot-camiy-coder/Google-Ocr-Translator.git
cd Google-Ocr-Translator
pip install selenium undetected-chromedriver pyautogui pygetwindow pillow keyboard
```
> [!WARNING]
> В `main.py` нужно изменить строку `DOWNLOAD_PATH` на путь, куда у вас сохраняются файлы в **Chrome**.

После этого запустить:
```bash
python main.py
```

## Скриншоты:
![](https://github.com/user-attachments/assets/4ca0456b-b858-4847-91b9-f7cc5864d549)  
![](https://images2.imgbox.com/c5/7d/ihFcOpJK_o.png)  
![](https://images2.imgbox.com/e0/9c/hcI2Jgis_o.png)  

> [!CAUTION]
> Я просто предоставляю исходный код скрипта. Я не несу ответственности за ваш компьютер!
