import argparse
import sys
import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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
        time.sleep(1)
        
    def search(self, search_term):
        # Find the search bar and enter the search term
        search_bar = self.driver.find_element(By.ID, self.search_bar_id)
        search_bar.clear()
        search_bar.send_keys(search_term)

        # Find the search button and click it
        search_button = self.driver.find_element(By.ID, self.search_button_id)
        search_button.click()
        time.sleep(1)

        # Wait for the search results to load
        EC.presence_of_element_located((By.ID, "course-search-results"))
    
    def __del__(self):
        # Close the browser window
        self.driver.quit()

class Course:
    """
    A class representing a course.

    Attributes:
    - course_id(int): identifier for the course.
    - title(str): title of the course.
    - credits(int): credits of each course.
    - description(str): brief description of the course.
    - prerequisites(list): string list of prerequisites required for course.
    - department(str): department course is a part of.
    - sections(list): string list of the section a course is a part of.
    """
    def __init__(self, course_id, title, credits, description, prerequisites, department, sections):
        self.course_id = course_id
        self.title = title
        self.credits = credits
        self.description = description
        self.prerequisites = prerequisites
        self.department = department
        self.sections = sections


class Section:
    """
    A class representing a section of a course.

    Attributes:
    - section_number(int): unique section number.
    - instructor(str): instructor teaching course section.
    - seats(int): number of seats in the section.
    - section_time(str): time the section is.
    - location(str): location of the section.
    """
    def __init__(self, section_number, instructor, seats, section_time, location):
        self.section_number = section_number
        self.instructor = instructor
        self.seats = seats
        self.section_time = section_time
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
    #Represents a SQLite database for storing course and section information

    def __init__(self, db_path):
        #Initializes the Database class with the path to the SQLite database file

        
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        #Creates the necessary tables in the database
        self.cursor.execute('''DROP TABLE IF EXISTS courses''')
        self.cursor.execute('''CREATE TABLE courses
            (course_id TEXT PRIMARY KEY,
            title TEXT,
            credits INTEGER,
            description TEXT,
            prerequisites TEXT,
            department TEXT)''')
        self.conn.commit()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS sections (
            section_number INTEGER PRIMARY KEY,
            course_id TEXT,
            instructor TEXT,
            seats TEXT,
            section_time TEXT,
            location TEXT,
            FOREIGN KEY(course_id) REFERENCES courses(course_id)
        )''')

        self.conn.commit()

    def add_course(self, course):
        #Adds a course to the courses table in the database
        try:
            self.cursor.execute('''INSERT INTO courses (course_id, title, credits, description, prerequisites, department) VALUES (?, ?, ?, ?, ?, ?)''', (course.course_id, course.title, course.credits, course.description, course.prerequisites, course.department))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print(f"Course {course.course_id} already exists in database")

    def add_section(self, section_number, course_id, instructor, seats, section_time, location):
        #Adds a section to the sections table in the database
        try:
            self.cursor.execute('''INSERT INTO sections VALUES (?, ?, ?, ?, ?, ?)''', (section_number, course_id, instructor, seats, section_time, location))
            self.conn.commit()
            print(f"Added section {section_number} of course {course_id}")
        except sqlite3.IntegrityError:
            print(f"Section{section_number} of course already exists in database")
          

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
