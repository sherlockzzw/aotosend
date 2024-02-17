import time
import pyautogui
import pytesseract
from PIL import Image
import pygetwindow as gw
from PIL import Image
import cv2
import pytesseract


#初步完成自动发送广告脚本

text_to_type = 'weixin'
# 打开微信
pyautogui.hotkey('command', 'space',interval = 1)
time.sleep(1)

pyautogui.typewrite(text_to_type)
time.sleep(1)

pyautogui.press('enter',interval = 1)

print('open success!')

time.sleep(1)

# 读取两张图片
# image1 = cv2.imread('WechatIMG42.jpg')
# image2 = cv2.imread('WechatIMG43.jpg')

# image1 = cv2.imread('WechatIMG42.jpg', cv2.IMREAD_GRAYSCALE)
# image2 = cv2.imread('WechatIMG43.jpg', cv2.IMREAD_GRAYSCALE)

# # Perform template matching
# result = cv2.matchTemplate(image2, image1, cv2.TM_CCOEFF_NORMED)

# # Get the location of the best match
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# # Extract the coordinates of the top-left corner of the matched region
# x, y = max_loc

# # Print the coordinates
# print(f"The coordinates of image1 within image2 are: ({x}, {y})")

sercheTitle = 'zhediedequnliao'
x = 360
y = 265

# 将鼠标移动到指定位置
pyautogui.moveTo(x, y, duration=1)

time.sleep(1)
# 点击鼠标
pyautogui.click()

# 输入文本
pyautogui.typewrite(sercheTitle)
time.sleep(1)
# 回车进入折叠群聊
pyautogui.press('enter',interval = 1)

# 群聊窗口坐标
qlx = 365

qly = 370
pyautogui.moveTo(qlx, qly, duration=1) 
time.sleep(0.5)
# yy = 433
# pyautogui.moveTo(qlx, yy, duration=1) 
for _ in range(3): 
    pyautogui.moveTo(qlx, qly, duration=1) 
    pyautogui.click()
    
    # 等待一段时间确保聚焦
    time.sleep(1)
    
   
    pyautogui.hotkey('command', 'v')
    time.sleep(1)
    
    pyautogui.hotkey('command', 'a')
    time.sleep(1)

    pyautogui.press('backspace')
    
    time.sleep(1)
    
    pyautogui.press('down')