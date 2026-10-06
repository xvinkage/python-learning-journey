from selenium import webdriver
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



load_dotenv()
ACCOUNT_EMAIL = os.getenv("ACCOUNT_EMAIL") # The email you registered with
ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")      # The password you used during registration
URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

#clicks login
login_form = driver.find_element(By.CSS_SELECTOR, "button")
login_form.click()

#enter email
WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.ID, "email-input")))
email = driver.find_element(By.CSS_SELECTOR, "#email-input")
email.send_keys(ACCOUNT_EMAIL)

#enter password
password = driver.find_element(By.CSS_SELECTOR, "#password-input")
password.send_keys(ACCOUNT_PASSWORD)

#submit login info
login = driver.find_element(By.CSS_SELECTOR, "#submit-button")
login.click()

#day of week
WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".Schedule_dayTitle__YBybs")))

# Find all class cards
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
booked = 0
waitlisted = 0
already_booked_count = 0
class_detail = []

for card in class_cards:
    # Get the day title from the parent day group
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Check if this is a Tuesday    
    if "Tue" in day_title or "Thu" in day_title:
        # Check if this is a 6pm class
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            # Get the class name
            
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            class_info = f"{class_name} on {day_title}"


            # Find and click the book button
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            if button.text == "Booked":
                print(f"✓ Already Booked: {class_info}")
                already_booked_count += 1
                class_detail.append(f"[Booked] {class_info}")

            elif button.text == "Waitlisted":
                print(f"✓ Already on waitlist: {class_info}")
                already_booked_count += 1
                class_detail.append(f"[Waitlisted] {class_info}")

            elif button.text == "Join Waitlist":
                button.click()
                waitlisted += 1
                print(f"✓ Joined waitlist: {class_info}")
                class_detail.append(f"[New Waitlist] {class_info}")

            else:
                button.click()
                booked += 1
                class_detail.append(f"[New Booking] {class_info}")
                print(f"✓ Booked: {class_info}")
print(f'''
--- BOOKING SUMMARY ---
Classes booked: {booked}
Waitlists joined: {waitlisted}
Already booked/waitlisted: {already_booked_count}
Total Tuesday 6pm classes processed: {booked + waitlisted + already_booked_count}

--- DETAILED CLASS LIST ---''')
for detail in class_detail:
    print(f"• {detail}")

my_bookings = driver.find_element(By.CSS_SELECTOR, "#my-bookings-link")    
WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#my-bookings-link")))

my_bookings.click()

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='booking-card-booking_']")
# verified_classes = []
verified_count = 0 
total_booked = booked + waitlisted + already_booked_count

for card in class_cards:
    when = card.find_element(By.CSS_SELECTOR, "p").text
    if "Tue" in when or "Thu" in when:
        if "6:00 PM" in when:
            button_name = card.find_element(By.TAG_NAME, "button")
            if button_name.text == "Cancel Booking":
                verified_count += 1
            # class_name = card.find_element(By.TAG_NAME, "h3").text
            # verified_classes.append
print(f"""
--- VERIFICATION RESULT ---


Expected: {verified_count} verified bookings
Found: {total_booked} bookings""")

if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")

driver.quit()