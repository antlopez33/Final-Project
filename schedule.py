import argparse
import sys
import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Catalog:
    """ CLass to represent a university catalog website """
    def __init__(self, url, driver_path, search_bar_id, search_button_id):
        self.url = url
        self.driver_path = driver_path
        self.search_bar_id = search_bar_id
        self.search_button_id = search_button_id

        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome(executable_path=self.driver_path)

        # Navigate to the catalog page
        self.driver.get(self.url)
        time.sleep(3)
        
    def search(self, search_term):
        # Find the search bar and enter the search term
        search_bar = self.driver.find_element(By.ID, self.search_bar_id)
        search_bar.clear()
        search_bar.send_keys(search_term)

        # Find the search button and click it
        search_button = self.driver.find_element(By.ID, self.search_button_id)
        search_button.click()
        time.sleep(3)

        # Wait for the search results to load
        """WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "course-search-results"))
            )"""
        EC.presence_of_element_located((By.ID, "course-search-results"))
    
    def __del__(self):
        # Close the browser window
        self.driver.quit()

class Course:
    """ Represents a course """
    def __init__(self, section, title, credits, description, prerequisites, department, seats, time, location):
        """ Initializes the class with the course information """
        self.section = section
        self.title = title
        self.credits = credits
        self.description = description
        self.prerequisites = prerequisites
        self.department = department
        self.seats = seats
        self.time = time
        self.location = location

    def to_dict(self):
        """ Returns the course information as a dictionary """ 
        return {
            "section": self.section,
            "title": self.title,
            "credits": self.credits,
            "description": self.description,
            "prerequisites": self.prerequisites,
            "department": self.department,
            "seats": self.seats,
            "time": self.time,
            "location": self.location,
        }
    
class Database:
    """ code for storing course information in a SQLite database """
    def __init__(self, database_name):
        self.database_name = databaseName
        self.connection=None
        
    def connect(self):
        """ Connects to the database using database credentials defined in main.py """
        self.connection = sqlite3.connect(self.database_name)
    
    def create_tables(self):
        """ Creates the necessary tables in the database """ 
        pass
    
    def insert_course(self, course):
        """ Inserts a single Course object into the database """
        if not self.connection:
            self.connect()

def main(words):
    catalog = Catalog(
        url="https://app.testudo.umd.edu/soc/",
        driver_path="./chromedriver.exe",
        search_bar_id="course-id-input",
        search_button_id="search-button"
    )
    department_list = []
    time.sleep(3)
    departments = catalog.driver.find_elements(By.XPATH, ".//div[@id='course-prefixes-page']//div[@class='course-prefix row']")
    for department in departments:
        department_list.append(department.find_element(By.XPATH, ".//span[@class='prefix-abbrev push_one two columns']").text)

    # Search for each department and parse the course info based on keywords
    for department_name in department_list:
        # Search for the department
        catalog.search(department_name)
        time.sleep(3)

        # Get all the courses
        courses = catalog.driver.find_elements(By.XPATH, ".//div[@class='course']")

        # Parse each course for keywords
        for course in courses:
            # Get the course title and description
            title = course.find_element(By.XPATH, ".//span[@class='course-title']").text
            description = course.find_element(By.XPATH, "//div[@class='row']//div[@class='approved-course-text']").text

            # Check if any of the keywords are in the title or description
            for keyword in words.keywords:
                if keyword.lower() in title.lower() or keyword.lower() in description.lower():
                    print(f"{department_name}: {title}")
                    break

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('keywords', metavar='keyword', type=str, nargs='+', help='keywords to search for')
    
    args = parser.parse_args(args_list)
    
    return args

if __name__ == "__main__":
    arguments = parse_args(sys.argv[1:])
    main(arguments.keywords)
