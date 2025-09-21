import pyautogui
from PIL import Image
import io
import win32clipboard

def screenshot_region(region: tuple[int, int, int, int]):
    x1, y1, x2, y2 = region
    width = x2 - x1
    height = y2 - y1
    return pyautogui.screenshot(region=(x1, y1, width, height))

def img2clipboard(img: Image.Image):
    output = io.BytesIO()
    img.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()