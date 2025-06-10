from appium.options.android import UiAutomator2Options
from appium import webdriver

# 配置測試參數
options = UiAutomator2Options()
options.set_capability("platformName", "Android")                # 平台名稱
options.set_capability("deviceName", "emulator-5556")         # 設備名稱
options.set_capability("appPackage", "com.money.smoney_android")      # 應用的包名
options.set_capability("appActivity", "com.money.smoney_android.ui.splash.SplashActivity")# 主Activity名稱

# 創建 WebDriver 實例
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

print("App started successfully!")
driver.quit()
