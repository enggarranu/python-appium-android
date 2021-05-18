from appium import webdriver
# Android environment
import unittest, time
from appium import webdriver
import random
import configparser

desired_caps = dict(
    platformName='Android',
    platformVersion='9',
    # automationName='uiautomator2',
    deviceName='xxxxxxxxxxxxxxxxxxxxxxx',
    # app='apk/TikTok-Lite-0.apk'
    appPackage='com.zhiliaoapp.musically.go',
    appActivity='com.ss.android.ugc.aweme.splash.SplashActivity',
    clearSystemFiles=False,
)
configuration_name = 'config.ini'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print("Buka Aplikasi Tiktok")
driver.launch_app()

print("Silahkan login di device..............")
x = range(15, 0, -1)
for n in x:
  print(n)
  time.sleep(1)

print("Scroll begin")
while True :
    config = configparser.ConfigParser()
    config.read(configuration_name)
    config.sections()
    sleep_random_min = config['scroll']['sleep_random_min']
    sleep_random_max = config['scroll']['sleep_random_max']
    timeSleep=random.randrange(int(sleep_random_min), int(sleep_random_max)) + random.randrange(1,10)
    print("Scroll "+str(timeSleep))
    print(sleep_random_min, sleep_random_max)
    print()
    
    startx_min = config['scroll_position']['startx_min']
    startx_max = config['scroll_position']['startx_max']
    starty_min = config['scroll_position']['starty_min']
    starty_max = config['scroll_position']['starty_max']
    endx_min = config['scroll_position']['endx_min']
    endx_max = config['scroll_position']['endx_max']
    endy_min = config['scroll_position']['endy_min']
    endy_max = config['scroll_position']['endy_max']
    duration_min = config['scroll_position']['duration_min']
    duration_max = config['scroll_position']['duration_max']
    
    # sweep
    driver.swipe(random.randrange(int(startx_min), int(startx_max)), random.randrange(int(starty_min), int(starty_max)), random.randrange(int(endx_min), int(endx_max)), random.randrange(int(endy_min), int(endy_max)), random.randrange(int(duration_min), int(duration_max)))
    
    # sleep
    x = range(timeSleep, 0, -1)
    for n in x:
        print(n)
        time.sleep(1)
    
print("Scroll End")


# print("close app")
# driver.close_app()

