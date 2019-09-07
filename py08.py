# coding:utf-8
from selenium import webdriver
from time import sleep
import unittest
from PIL import Image
from PIL import ImageEnhance
import pytesseract
from aip import AipOcr # pip install baidu-aip

APP_ID = '16838310'  # 替换为实际申请值
API_KEY = '8GuIfzz8pSmg8x02GQNBWGyt'  # 替换为实际申请值
SECRET_KEY = 'MoEeNimMbs9IB8bBB6SXrgjoogmpIzKI'


driver=webdriver.Chrome()
driver.implicitly_wait(10)

url = "http://61-62-64.eg99.org:9080/login.html"   #一般在登录首页
driver.get(url)
driver.maximize_window()
sleep(2)
driver.save_screenshot(r"C:\\Users\\Administrator\\Desktop\\im\\aa.png")  #截取当前网页，
sleep(2)
imgelement = driver.find_element_by_id("verifyImg")  #定位验证码
location = imgelement.location  #获取验证码x,y轴坐标
print(location)
size=imgelement.size  #获取验证码的长宽
print(size)

# coderange=(int(location['x']),int(location['y']),int(location['x']+size['width']+2),
#     int(location['y']+size['height'])) #写成我们需要截取的位置坐标
coderange=(1055,660,1055+90,660+40)
print(coderange)
i = Image.open(r"C:\\Users\\Administrator\\Desktop\\im\\aa.png") #打开截图
frame4 = i.crop(coderange)  #使用Image的crop函数，从截图中再次截取我们需要的区域
frame4.save(r"C:\\Users\\Administrator\\Desktop\\im\\aa.png")    #保存截图
i2 = Image.open(r"C:\\Users\\Administrator\\Desktop\\im\\aa.png")  #打开截图
imgry = i2.convert('L')   #图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
sharpness = ImageEnhance.Contrast(imgry) #对比度增强
i3 = sharpness.enhance(3.0)  #3.0为图像的饱和度
i3.save("C:\\Users\\Administrator\\Desktop\\im\\image_code.png")
# i4 = Image.open("C:\\Users\\Administrator\\Desktop\\im\\image_code.png")
# text = pytesseract.image_to_string(i3).strip() #使用image_to_string识别验证码
# print(text.replace(' ',''))   #该方法的作用为 

img=open("C:\\Users\\Administrator\\Desktop\\im\\image_code.png","rb").read()
result = AipOcr(APP_ID, API_KEY, SECRET_KEY).webImage(img)
print(result)

yz=int(result)

driver.find_element_by_id("userName").send_keys("moli03")
driver.find_element_by_id("userpwd").send_keys("qwe123")
driver.find_element_by_id("yzm").send_keys(yz)

driver.find_element_by_id("login_bt").click()

