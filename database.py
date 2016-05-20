from pymongo import MongoClient

#connection = MongoClient()
connection = MongoClient('159.203.113.27', 27010) #droplet ip
db = connection["broccoli"]

"""
COLLECTIONS
courses: code, name, year, description 
dependencies: master (req), slave
"""

def add_course(code, name, year, descript):
    """
    Adds a new course to the database, but will fail if a course with the same code already exists 
    """
    c = list(db.courses.find({"code": code}))
    if not c:
        course = {"code": code,
                  "name": name,
                  "year": year,
                  "description": descript}
        db.courses.insert(course)
        return True
    return False


def get_course(code):
    """
    Retrieve a course based on the course code
    """
    course = db.courses.find_one({"code": code})
    if not course:
        return None
    return course


def add_dependency(master, slave):
    """
    Adds a new dependency to the database, but fails if one or both courses does not exist, or it the dependency already exists
    """
    m = db.courses.find_one({"code": master})
    s = db.courses.find_one({"code": slave})
    d = {"master": master,
         "slave": slave}
    q = db.dependencies.find_one(d)

    if m and s and not q:
        db.dependencies.insert(d)
        return True
    return False

def get_dependencies(master):
    """
    Retrieves course codes of all courses dependent on master. Returns None if course doesn't exist or if course has no dependents
    """
    dep = list(db.dependencies.find({"master": master}))
    if dep:
        return dep
    return None


if __name__ == "__main__":
    db.drop_collection("courses")
    db.drop_collection("dependencies")

    print add_course("SLS43", "Modern Biology", "All", "a description")
    print add_course("SBS11QAS", "Anthropology & Sociobiology", "Juniors and Seniors", "another description")
    print add_dependency("SLS43", "SBS11QAS")
    print add_dependency("SLS43", "DWAI")

    courses = db.courses.find()
    for course in courses:
        print course

    deps = db.dependencies.find()
    for dep in deps:
        print dep
