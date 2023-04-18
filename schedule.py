import argparse
import sys
import sqlite3

class Catalog:
    """ CLass to represent a university catalog website """
    
    def __init__(self, url, driver_path, search_bar_id, search_button_id):
        """ Initializes the class with the URL of the university catalog website and any necesssary web driver settings """
        self.url = url
        self.driver_path = driverPath
        self.search_bar_id = searchBarID
        self.search_button_id = searchButtonID

    def search(self, keyword):
        """ Navigates to the search page of the university catalog website and searches for courses related to the given keyword """
        self.keyword = keyword

    def extract_courses(self):
        """  Extracts course information from the search results page and returns it as a list of Course objects """
        pass

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
        return
    
class Database:
    """ code for storing course information in a SQLite database """
    def __init__(self, database_name):
        self.database_name = databaseName
        
    def connect(self):
        """ Connects to the database using database credentials defined in main.py """
        pass
    
    def create_tables(self):
        """ Creates the necessary tables in the database """ 
        pass
    
    def insert_course(self, course):
        """ Inserts a single Course object into the database """
        self.course = course

def main(keywords):
    pass

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
