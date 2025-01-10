from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import re
import time
import csv

type_of_agency = "Packaging Design"
pages = 5

# Define the CSV file name
csv_filename = f"{type_of_agency}.csv"

# Open the CSV file in write mode
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row to the CSV file
    headers = ["Name", "Type of Agency", "Tagline", "Ratings", "Reviews", "Sponsor", "MinProjectSize", "HourlyRate", "TeamSize", "Location", "ServiceNames", "ServicePercentages", "Feedback", "WebsiteLink", "ClutchDirectoryLink"]
    csvwriter.writerow(headers)

    for page in range(0,pages):
        url = f"https://clutch.co/agencies/packaging-design?page={page}"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--log-level=3")
        options.add_argument(f"user-agent={user_agent}")

        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(3)
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.END)

        # Extract details
        # row_elements = driver.find_elements(By.CLASS_NAME, "row")
        row_elements = driver.find_elements(By.CSS_SELECTOR, "li.provider.provider-row")
        num = 0
        for row in row_elements:
            try:
                name = row.find_element(By.CSS_SELECTOR, ".company_info a.company_title").text
                # name = row.find_element(By.CLASS_NAME, "company_info").text

                # Tagline
                try:
                    # tag_line = row.find_element(By.CLASS_NAME, "tagline").text
                    tag_line = row.find_element(By.CLASS_NAME, "tagline").text
                except NoSuchElementException:
                    tag_line = None

                # Ratings
                try:
                    ratings = row.find_element(By.CLASS_NAME, "rating").text
                except NoSuchElementException:
                    ratings = None

                # Reviews
                try:
                    reviews = row.find_element(By.CLASS_NAME, "reviews-link").text
                except NoSuchElementException:
                    reviews = None

                # isSponsor
                try:
                    sponsor = row.find_element(By.CLASS_NAME, "company_sponsor__text").text
                    is_sponsor = "Yes" if sponsor else "No"
                except NoSuchElementException:
                    is_sponsor = "No"

                # Minimum Budget
                try:
                    min_project_size = row.find_element(By.XPATH, ".//div[@class='list-item block_tag custom_popover']").text
                except NoSuchElementException:
                    min_project_size = None

                # Hourly Rate
                try:
                    hourly_rate = row.find_element(By.XPATH, ".//div[@class='list-item custom_popover'][1]").text
                except NoSuchElementException:
                    hourly_rate = None

                # Team Size
                try:
                    team_size = row.find_element(By.XPATH, ".//div[@class='list-item custom_popover'][2]").text
                except NoSuchElementException:
                    team_size = None

                # Location
                try:
                    location = row.find_element(By.XPATH, ".//div[@class='list-item custom_popover'][3]").text
                except NoSuchElementException:
                    location = None

                # Services
                services = row.find_elements(By.XPATH, ".//div[@class='chartAreaContainer spm-bar-chart']/div")
                service_names = []
                service_percentages = []
                for service in services:
                    service_info = service.get_attribute('data-content')
                    # Extract service name and percentage from 'service_info' and append to their respective lists
                    # Extracting percentage using regex
                    percentage_match = re.search(r"<i>(\d+)%</i>", service_info)
                    if percentage_match:
                        service_percent = percentage_match.group(1)
                        service_percentages.append(service_percent)
                    
                    # Extracting service name using regex
                    service_name_match = re.search(r"<b>(.*?)</b>", service_info)
                    if service_name_match:
                        service_name = service_name_match.group(1)
                        service_names.append(service_name)

                # Feedback
                try:
                    feedback = row.find_element(By.TAG_NAME, "blockquote").text
                except NoSuchElementException:
                    feedback = None

                # Website Link
                try:
                    website_link = row.find_element(By.CLASS_NAME, "website-link__item").get_attribute('href')
                except NoSuchElementException:
                    website_link = None

                # Clutch Directory Link
                try:
                    clutch_directory_link = row.find_element(By.CLASS_NAME, "directory_profile").get_attribute('href')
                except NoSuchElementException:
                    clutch_directory_link = None

                # Print the extracted details
                # print(f"<================Agency No. {num}=============>'\n'")
                # print(f"{name} \n {type_of_agency}\n {tag_line}\n {ratings}\n {reviews}\n {is_sponsor}\n {min_project_size}\n {hourly_rate}\n {team_size}\n {location}\n {service_names}\n {service_percentages}\n {feedback}\n {website_link}\n {clutch_directory_link}")

                # Write the extracted data to the CSV file
                csvwriter.writerow([name, type_of_agency, tag_line, ratings, reviews, is_sponsor, min_project_size, hourly_rate, team_size, location, ','.join(service_names), ','.join(service_percentages), feedback, website_link, clutch_directory_link])
            except Exception as e:
                pass
        driver.quit()
        print(f"Data Extraction is completed for page {page} URL====> {url}")

print(f"Data written to {csv_filename}")
