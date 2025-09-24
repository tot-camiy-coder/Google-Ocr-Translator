# Google-Ocr-Translator

Скрипт для быстрого перевода изображений через [GoogleTranslate](https://translate.google.com/)
> [!NOTE]
> Мне нужно было быстро получать перевод части экрана через Google Translate, но вариант \ **Shift+Win+S** + **Alt+Tab** + **Ctrl+V** мне не понравился, 
> и я решил написать данный скрипт.

## Функции

-   Перевод части экрана (**Ctrl+Alt+X**, **Click** - закрыть).
-   Перевод скопированного изображения (**Ctrl+Alt+C**, **DoubleClick** - закрыть, **Scroll** - увеличить/уменьшить, **ЛКМ** - переместить).
-   Не требует **Google Cloud API**, всё работает через эмуляцию браузера.

## Установка

``` bash
git clone https://github.com/tot-camiy-coder/Google-Ocr-Translator.git
cd Google-Ocr-Translator
pip install selenium undetected-chromedriver pyautogui pygetwindow pillow keyboard pywin32
```

> [!WARNING] 
> В `main.py` нужно изменить строку `DOWNLOAD_PATH` на
> путь, куда у вас сохраняются файлы в **Chrome**.

После этого запустите:

``` bash
python main.py
```

## TODO:
-   [x] 50/50 Исправить переход в браузер
-   [x] Добавить обработчик ошибок
-   [x] Исправить вставку изображения
-   [x] Перейти с JS на .click()
-   [ ] Поддержка лёгкой смены языка
-   [ ] Улучшить взаимодействие с браузером
-   [x] Отключить **Ctrl+Alt+C** без скриншота в буфере
-   [ ] Исправить говнокод

## Скриншоты:

![](https://github.com/user-attachments/assets/4ca0456b-b858-4847-91b9-f7cc5864d549)\
![](https://images2.imgbox.com/c5/7d/ihFcOpJK_o.png)\
![](https://images2.imgbox.com/e0/9c/hcI2Jgis_o.png)

> [!CAUTION] 
> Я просто предоставляю исходный код скрипта. Я не несу ответственности за ваш компьютер!
> Google может заблокировать ваш IP адрес за множество запросов!
