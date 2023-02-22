# version 1.0 한국은행경제통계 사이트에서 주택가격전망CSI 최근 월의 값을 가져오기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# # script 실행 완료 후에도 WebDriver 동작 유지 목적
options = Options()
options.add_experimental_option("detach", True)
# 최신 Chrome driver 이용 Service object 생성
service = Service(ChromeDriverManager().install())
# create a WebDriver instance using the Service object
driver = webdriver.Chrome(service=service, options=options) #, options=options
driver.maximize_window()

# url = 'https://ecos.bok.or.kr/#/Short/c531ec'
url = "https:/ecos.bok.or.kr"

# navigate to a webpage
driver.get(url)
driver.implicitly_wait(2)

# 검색어 "소비자동향조사(전국, 월, 2008.9~)" 입력하고 enter
element_search = driver.find_element(By.CSS_SELECTOR, ".main_searchInput")
element_search.send_keys("소비자동향조사(전국, 월, 2008.9~)")
element_search.send_keys("\n")
driver.implicitly_wait(30)

# "소비자동향조사(전국, 월, 2008.9~)" 항목이 첫번째에 있어서 첫번째 board_items 선택하여 click
element_item = driver.find_elements(By.CSS_SELECTOR, ".board_items")[0]
element_item.click()
# driver.implicitly_wait(10)
time.sleep(10)

# ### 여기서부터 나누면 되고, 합하면 안되네 ㅠㅠ
# ### time.sleep 시간을 충분히 주니 잘 동작

# 통계항목에 "주택가격전망CSI"를 입력하고 enter
element_statistic_item = driver.find_elements(By.CSS_SELECTOR, ".form-control")[2]
element_statistic_item.send_keys("주택가격전망CSI")
element_statistic_item.send_keys("\n")
driver.implicitly_wait(2)

# "주택가격전망CSI" click 하여 checkbox check
element_house_CSI_click = driver.find_element(By.XPATH, "//*[text()='주택가격전망CSI']")
element_house_CSI_click.click()
driver.implicitly_wait(2)

# "전체" click 하여 checkbox check
element_house_CSI_click = driver.find_element(By.XPATH, "//*[text()='전체']")
element_house_CSI_click.click()
driver.implicitly_wait(2)

# "빠른 조회" 버튼 click
element_quick_query = driver.find_element(By.XPATH, "//*[text()='빠른 조회']")
element_quick_query.click()
time.sleep(5)

# "오름차순" 버튼 click
element_descending_button = driver.find_element(By.XPATH, "//*[text()='오름차순']")
element_descending_button.click()
time.sleep(5)

# 조회하는 달 element
element_month = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[8]/div/div[2]/div/div/div/div/div/div[2]/div/div[4]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/table/tbody/tr/td[1]/div/span")

# CSI 지수 element
element_no_of_csi = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[8]/div/div[2]/div/div/div/div/div/div[2]/div/div[4]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/table/tbody/tr/td[1]/div")

# 출력
print(f"{element_month.text}월의 주택가격전망CSI는 {element_no_of_csi.text}입니다.")

driver.close()