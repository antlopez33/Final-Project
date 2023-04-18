import argparse
import sys
import sqlite3

class Catalog:
    def __init__(self, url, driver_path, search_bar_id, search_button_id):
        pass

    def search(self, keyword):
        pass

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