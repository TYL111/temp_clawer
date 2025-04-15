from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import matplotlib.pyplot as plt

#中文
plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.rcParams['axes.unicode_minus'] = False


driver = webdriver.Chrome()
driver.get("https://weather.com/zh-TW/weather/tenday/l/e0153cbf7b2c41b79835d16eb78622d142ae11887d1b61f1bb6167fa1ef9e557")
time.sleep(3)


days = []
temps = []

for index in range(1, 10):
    day_element = driver.find_element(By.CSS_SELECTOR, f"#detailIndex{index} > summary > div > div > h2")
    temp_element = driver.find_element(By.CSS_SELECTOR, f"#detailIndex{index} > summary > div > div > div.DetailsSummary--temperature--YGmQ5 > span.DetailsSummary--highTempValue--VHKaO")        
    day = day_element.text.strip()
    temp = temp_element.text.strip().replace("°", "")
    days.append(day)
    temps.append(int(temp))

driver.quit()

df = pd.DataFrame({
    "日期": days,
    "高溫(°C)": temps
})


plt.figure(figsize=(10, 5))
plt.plot(df["日期"], df["高溫(°C)"], marker='o', color='tomato')
plt.title("淡水未來氣溫")
plt.xlabel("日期")
plt.ylabel("高溫 (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()
