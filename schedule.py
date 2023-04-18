import argparse
import sys
import sqlite3

class Catalog:
    def __init__(self, url, driver_path, search_bar_id, search_button_id):
        self.url = url
        self.driver_path = driverPath
        self.search_bar_id = searchBarID
        self.search_button_id = searchButtonID

    def search(self, keyword):
        self.keyword = keyword

    def extract_courses(self):
        pass

class Course:
    def __init__(self, section, title, credits, description, prerequisites, department, seats, time, location):
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
        return
    
class Database:
    def __init__(self, database_name):
        self.database_name = databaseName
        
    def connect(self):
        pass
    
    def create_tables(self):
        pass
    
    def insert_course(self, course):
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
