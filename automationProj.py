from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the driver and open the web page
url = 'https://www.indeed.com'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)


# Find the search box and enter our query
search_box = driver.find_element_by_name('q')
search_box.send_keys('cybersecurity')
search_box.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(2)

# Click the "Entry Level" filter
entry_level_filter = driver.find_element_by_xpath("//span[text()='Entry Level']")
entry_level_filter.click()

# Wait for the page to load
time.sleep(2)

# Find all job listings and loop through them
job_listings = driver.find_elements_by_xpath("//a[contains(@href,'/rc/clk?')]")
for job_listing in job_listings:
    # Click the job listing to view the details
    job_listing.click()
    
    # Wait for the page to load
    time.sleep(2)
    
    # Check if the "Easily Apply" button exists
    try:
        easily_apply_button = driver.find_element_by_xpath("//span[text()='Easily apply']")
        easily_apply_button.click()
        
        # Wait for the page to load
        time.sleep(2)
        
        # Fill out the application form with preloaded information
        name_field = driver.find_element_by_name('name')
        name_field.send_keys('Nathaniel Gomez')
        
        email_field = driver.find_element_by_name('email')
        email_field.send_keys('nathanielGomez@gmail.com')
        
        phone_field = driver.find_element_by_name('phone')
        phone_field.send_keys('123-456-7890')
        
        resume_field = driver.find_element_by_name('resume')
        resume_field.send_keys('C:/Users/Nate/Desktop/gomezResume.docx')
        
        submit_button = driver.find_element_by_xpath("//button[@type='submit']")
        submit_button.click()
        
        # Wait for the page to load
        time.sleep(2)
        
    except:
        pass
        
# Close the browser
driver.quit()