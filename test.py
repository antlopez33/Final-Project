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

if __name__ == "__main__":
    test_catalog()
    test_course()