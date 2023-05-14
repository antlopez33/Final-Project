from recommender import *

def test_catalog():
    catalog = Catalog("https://app.testudo.umd.edu/soc/", "./chromedriver.exe", "course-id-input", "search-button")
    assert catalog.url == "https://app.testudo.umd.edu/soc/"
    assert catalog.driver_path == "./chromedriver.exe"
    assert catalog.search_bar_id == "course-id-input"
    assert catalog.search_button_id == "search-button"
    catalog.__del__()

def test_course():
    course = Course("CMSC131", "Object-Oriented Programming I", 4, 
                    "Introduction to programming and computer science. Emphasizes understanding and implementation of applications using object-oriented techniques. Develops skills such as program design and testing as well as implementation of programs using a graphical IDE. Programming done in Java.", 
                    "Corequisite: MATH140. Credit only granted for: CMSC131, CMSC133, or IMDM127.", "CMSC", [])
    assert course.course_id == "CMSC131"
    assert course.title == "Object-Oriented Programming I"
    assert course.credits == 4
    assert course.description == "Introduction to programming and computer science. Emphasizes understanding and implementation of applications using object-oriented techniques. Develops skills such as program design and testing as well as implementation of programs using a graphical IDE. Programming done in Java."
    assert course.prerequisites == "Corequisite: MATH140. Credit only granted for: CMSC131, CMSC133, or IMDM127."
    assert course.department == "CMSC"
    assert course.sections == []
    
def test_section():
    section = Section("0101", "Nelson Padua-Perez", "Seats (Total: 34, Open: 25, Waitlist: 0 )", "MWF 2:00pm - 2:50pm", "IRB 0324")
    assert section.section_number == "0101"
    assert section.instructor == "Nelson Padua-Perez"
    assert section.seats == "Seats (Total: 34, Open: 25, Waitlist: 0 )"
    assert section.section_time == "MWF 2:00pm - 2:50pm"
    assert section.location == "IRB 0324"

def test_database():
    db = Database("courses.db")
    assert isinstance(db.conn, sqlite3.Connection)
    assert isinstance(db.cursor, sqlite3.Cursor)
    db.conn.close()

def test_search():
    catalog = Catalog("https://app.testudo.umd.edu/soc/", "./chromedriver.exe", "course-id-input", "search-button")
    catalog.search("CMSC")
    assert catalog.driver.find_elements(By.CLASS_NAME, "course") is not None
    catalog.__del__()

if __name__ == "__main__":
    test_catalog()
    test_course()
    test_section()
    test_database()
    test_search()
