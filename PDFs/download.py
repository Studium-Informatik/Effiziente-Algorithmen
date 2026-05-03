import time
import os
import shutil
import re
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# --- CONFIGURATION ---
TEMP_DOWNLOAD_DIR = os.path.abspath("./temp_download")
MOODLE_LOGIN_URL = "https://moodle2.uni-potsdam.de" 
MOODLE_COURSE_URL = "https://moodle2.uni-potsdam.de/course/view.php?id=49346"

# Map categories to their target directories relative to the script
TARGET_DIRS = {
    "Vorlesung": os.path.abspath("./VL"),
    "Übung": os.path.abspath("./Ue"),
    "Hausaufgabe": os.path.abspath("./hausaufgaben"),
    "Other": os.path.abspath("./Other") # Fallback for anything else
}

def extract_course_data(html):
    """Parses the Moodle HTML and returns structured course data."""
    soup = BeautifulSoup(html, 'html.parser')
    course_data = []

    sections = soup.find_all('li', class_=lambda c: c and 'course-section' in c.split())
    
    for section in sections:
        section_name_tag = section.find('h3', class_='sectionname')
        section_name = section_name_tag.text.strip() if section_name_tag else "Unknown Section"
        
        section_dict = {"section_name": section_name, "content": []}
        activities = section.find_all('li', class_=lambda c: c and 'activity' in c.split())
        
        for activity in activities:
            link_tag = activity.find('a', class_='aalink')
            if not link_tag:
                continue
            
            # 1. Extract URL (Prioritize standard href, fallback to onclick popup target)
            url = link_tag.get('href', '')
            if not url:
                window_target = link_tag.get('onclick', '')
                window_url_match = re.search(r"window\.open\(['\"](.*?)['\"]", window_target)
                if window_url_match:
                    url = window_url_match.group(1)
            
            if not url:
                continue
            
            # 2. Extract and clean the title
            name_tag = link_tag.find('span', class_='instancename')
            raw_title = name_tag.text if name_tag else link_tag.text
            title = re.sub(r'\s*(Datei|Forum|Freie Gruppeneinteilung|Aufgabe)$', '', raw_title.strip())
            
            # 3. Determine the Type
            activity_classes = activity.get('class', [])
            if 'modtype_resource' in activity_classes:
                content_type = "PDF" 
            elif 'modtype_assign' in activity_classes:
                content_type = "Assignment"
            elif 'modtype_forum' in activity_classes:
                content_type = "Forum"
            else:
                content_type = "Unknown"
                
            # 4. Determine Category
            category = "Other"
            lower_title = title.lower()
            if "vorlesung" in lower_title or "vorbesprechung" in lower_title:
                category = "Vorlesung"
            elif "übung" in lower_title:
                category = "Übung"
            elif "hausaufgabe" in lower_title:
                category = "Hausaufgabe"
                
            section_dict["content"].append({
                "title": title,
                "url": url,
                "type": content_type,
                "category": category
            })
            
        course_data.append(section_dict)
        
    return course_data


def setup_browser():
    """Configures and returns the Selenium Chrome driver."""
    # Ensure all directories exist
    os.makedirs(TEMP_DOWNLOAD_DIR, exist_ok=True)
    for target_dir in TARGET_DIRS.values():
        os.makedirs(target_dir, exist_ok=True)

    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": TEMP_DOWNLOAD_DIR,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "plugins.always_open_pdf_externally": True
    })

    chromedriver_path = shutil.which("chromedriver")
    if not chromedriver_path:
        raise FileNotFoundError("chromedriver not found in PATH. Make sure it is installed via Nix.")

    service = Service(executable_path=chromedriver_path)
    return webdriver.Chrome(service=service, options=chrome_options)


def is_temp_file(filename):
    """Checks if a file is a known browser temporary/downloading file."""
    return (
        filename.endswith('.crdownload') or 
        filename.endswith('.tmp') or 
        filename.startswith('.org.chromium') or
        filename.startswith('.com.google.Chrome') or
        filename.startswith('.goutputstream') or
        'Unconfirmed' in filename
    )

def wait_and_move_download(existing_files, target_dir, timeout=15):
    """Waits for a new file to download and moves it to the appropriate category directory."""
    end_time = time.time() + timeout
    while time.time() < end_time:
        current_files = set(os.listdir(TEMP_DOWNLOAD_DIR))
        new_files = current_files - existing_files
        
        # Filter out any files that match known temporary downloading patterns
        finished_files = [f for f in new_files if not is_temp_file(f)]
        
        # If we have a file that isn't a temp file, Chrome has finished renaming it
        if finished_files:
            for f in finished_files:
                src = os.path.join(TEMP_DOWNLOAD_DIR, f)
                dst = os.path.join(target_dir, f)
                
                # Handle duplicate names by replacing
                if os.path.exists(dst):
                    os.remove(dst)
                    
                shutil.move(src, dst)
                print(f" -> Downloaded and moved: {f} -> {os.path.basename(target_dir)}/")
            return True
            
        time.sleep(0.5)
        
    print(" -> Timeout: Could not detect downloaded file.")
    return False


def main():
    print("Launching browser...")
    driver = setup_browser()

    try:
        # --- LOGIN PHASE ---
        driver.get(MOODLE_LOGIN_URL)
        print("\n" + "="*50)
        print("ACTION REQUIRED: Please log in to Moodle in the browser window.")
        print("Navigate to the dashboard if not already there.")
        input("Press [ENTER] in this terminal once you are logged in...")
        print("="*50 + "\n")
        
        # --- SCRAPING PHASE ---
        print(f"Loading course page: {MOODLE_COURSE_URL}")
        driver.get(MOODLE_COURSE_URL)
        
        # Give Moodle a moment to fully render dynamic elements
        time.sleep(3) 
        
        print("Parsing course structure...")
        data = extract_course_data(driver.page_source)
        print(f" -> Found {len(data)} sections.\n")

        # --- DOWNLOAD PHASE ---
        print("Starting downloads...")
        for section in data:
            for item in section.get("content", []):
                name = item.get("title", "Unknown Document")
                url = item.get("url")
                item_type = item.get("type")
                category = item.get("category", "Other")
                
                if not url or item_type not in ["PDF", "Assignment"]:
                    continue
                    
                print(f"Processing [{item_type}]: {name}")
                
                target_directory = TARGET_DIRS.get(category)
                existing_files = set(os.listdir(TEMP_DOWNLOAD_DIR))
                
                # Open a new tab for the download to protect the main session state
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[-1])
                
                try:
                    if item_type == "PDF":
                        download_url = f"{url}&redirect=1" if "redirect=1" not in url else url
                        driver.get(download_url)
                        wait_and_move_download(existing_files, target_directory)
                        
                    elif item_type == "Assignment":
                        driver.get(url)
                        try:
                            wait = WebDriverWait(driver, 5)
                            download_link = wait.until(EC.element_to_be_clickable(
                                (By.XPATH, "//a[contains(@href, 'forcedownload=1')]")
                            ))
                            download_link.click()
                            wait_and_move_download(existing_files, target_directory)
                            
                        except TimeoutException:
                            print(" -> No downloadable attachment found on this assignment page.")
                            
                finally:
                    # Always close the temporary tab and return to the main page
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    
    except Exception as e:
        print(f"An error occurred during execution: {e}")

    finally:
        print("Closing browser and cleaning up...")
        driver.quit()
        # Clean up the temporary download directory
        if os.path.exists(TEMP_DOWNLOAD_DIR):
            shutil.rmtree(TEMP_DOWNLOAD_DIR)
        print("Cleanup complete. Files sorted successfully.")


if __name__ == "__main__":
    main()