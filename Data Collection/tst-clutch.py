import time
import re
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument(f"user-agent={user_agent}")
driver = webdriver.Chrome(options=options)  # You can replace this with the path to your WebDriver executable

# Open the website
driver.get("https://clutch.co/sitemap")

# Find all <div> elements with the class "sitemap-wrap"
div_elements = driver.find_elements(By.CLASS_NAME, "sitemap-wrap")

dev_links = []
design_links = []
mark_links = []
it_links = []
bs_links=[]
ress = []
pacs = []
pris = []
all_links = [mark_links, dev_links, design_links, it_links, bs_links, ress, pacs, pris]
# Iterate through each <div> element and extract the text
for i in range(8):
	div_element = div_elements[i]

	link_elements = div_element.find_elements(By.CLASS_NAME, "sitemap-data__wrap-link")
	print(f"***********{div_element.text}****************")
	for link_element in link_elements:
		link = link_element.get_attribute('href')
		all_links[i].append(link)

dev_links = list(set(dev_links))
design_links = list(set(design_links))
mark_links = list(set(mark_links))
it_links = list(set(it_links))
bs_links = list(set(bs_links))
ress = list(set(ress))
pacs = list(set(pacs))
pris = list(set(pris))

# with open("Development.csv", "w", newline="") as file:
# 	csv_writer = csv.writer(file)
# 	csv_writer.writerow(["Links", "FirmNumber"])

# 	for dev_link in dev_links:
# 		# dev_link_text = dev_link.split("/")[-1]
# 		# print(dev_link_text)
# 		user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
# 		options = webdriver.ChromeOptions()
# 		options.add_argument("--headless")
# 		options.add_argument(f"user-agent={user_agent}")
# 		driver1 = webdriver.Chrome(options=options)
# 		driver1.get(dev_link)
# 		time.sleep(5)
# 		firm_num = driver1.find_element(By.CLASS_NAME, 'infobar__counter').text
# 		firm_number = int(re.sub(r"[^\d]", "", firm_num))
# 		# print(f"{dev_link} ===> {firm_number}")
# 		csv_writer.writerow([dev_link, firm_number])
# 		driver1.quit()
# Find the <button> element by its text content
# button_element = driver.find_element(By.XPATH, "//button[contains(text(), 'Advertising & Marketing')]")

# Click the button
# button_element.click()
# links=[]
# link_elements = driver.find_elements(By.CLASS_NAME, "sitemap-data__wrap-link")
# for link_element in link_elements:
# 	link = link_element.get_attribute('href')
# 	links.append(link)
# 	print(link)
# print(len(links))
# with open("Designing.csv", "w", newline="") as file:
# 	csv_writer = csv.writer(file)
# 	csv_writer.writerow(["Links", "FirmNumber"])

# 	for design_link in design_links:
# 		# dev_link_text = dev_link.split("/")[-1]
# 		# print(dev_link_text)
# 		user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
# 		options = webdriver.ChromeOptions()
# 		options.add_argument("--headless")
# 		options.add_argument(f"user-agent={user_agent}")
# 		driver1 = webdriver.Chrome(options=options)
# 		driver1.get(design_link)
# 		time.sleep(5)
# 		firm_num = driver1.find_element(By.CLASS_NAME, 'infobar__counter').text
# 		firm_number = int(re.sub(r"[^\d]", "", firm_num))
# 		# print(f"{dev_link} ===> {firm_number}")
# 		csv_writer.writerow([design_link, firm_number])
# 		driver1.quit()

# with open("Marketing.csv", "w", newline="") as file:
# 	csv_writer = csv.writer(file)
# 	csv_writer.writerow(["Links", "FirmNumber"])

# 	for mark_link in mark_links:
# 		# dev_link_text = dev_link.split("/")[-1]
# 		# print(dev_link_text)
# 		user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
# 		options = webdriver.ChromeOptions()
# 		options.add_argument("--headless")
# 		options.add_argument(f"user-agent={user_agent}")
# 		driver1 = webdriver.Chrome(options=options)
# 		driver1.get(mark_link)
# 		time.sleep(5)
# 		firm_num = driver1.find_element(By.CLASS_NAME, 'infobar__counter').text
# 		firm_number = int(re.sub(r"[^\d]", "", firm_num))
# 		# print(f"{dev_link} ===> {firm_number}")
# 		csv_writer.writerow([mark_link, firm_number])
# 		driver1.quit()

# with open("ITService.csv", "w", newline="") as file:
# 	csv_writer = csv.writer(file)
# 	csv_writer.writerow(["Links", "FirmNumber"])

# 	for it_link in it_links:
# 		# dev_link_text = dev_link.split("/")[-1]
# 		# print(dev_link_text)
# 		user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
# 		options = webdriver.ChromeOptions()
# 		options.add_argument("--headless")
# 		options.add_argument(f"user-agent={user_agent}")
# 		driver1 = webdriver.Chrome(options=options)
# 		driver1.get(it_link)
# 		time.sleep(5)
# 		firm_num = driver1.find_element(By.CLASS_NAME, 'infobar__counter').text
# 		firm_number = int(re.sub(r"[^\d]", "", firm_num))
# 		# print(f"{dev_link} ===> {firm_number}")
# 		csv_writer.writerow([it_link, firm_number])
# 		driver1.quit()

with open("Business.csv", "w", newline="") as file:
	csv_writer = csv.writer(file)
	csv_writer.writerow(["Links", "FirmNumber"])

	for bs_link in bs_links:
		# dev_link_text = dev_link.split("/")[-1]
		# print(dev_link_text)
		user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
		options = webdriver.ChromeOptions()
		options.add_argument("--headless")
		options.add_argument(f"user-agent={user_agent}")
		driver1 = webdriver.Chrome(options=options)
		driver1.get(bs_link)
		time.sleep(5)
		firm_num = driver1.find_element(By.CLASS_NAME, 'infobar__counter').text
		firm_number = int(re.sub(r"[^\d]", "", firm_num))
		# print(f"{dev_link} ===> {firm_number}")
		csv_writer.writerow([bs_link, firm_number])
		driver1.quit()

# Close the browser
driver.quit()
