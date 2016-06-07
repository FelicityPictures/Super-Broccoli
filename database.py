from pymongo import MongoClient
import pandas

#connection = MongoClient()
connection = MongoClient('159.203.113.27', 27010) #droplet ip
db = connection["broccoli"]

"""
COLLECTIONS
courses: code, name, misc, description
dependencies: master (req), slave
"""

def add_course(code, name, misc, descript):
    """
    Adds a new course to the database, but will fail if a course with the same code already exists

    Params: code - string (course code)
            name - string (course name)
            misc - string?   (miscellaneous information)
            descript - string (stunning description of course)
    Returns: True if insertion successful
             False otherwise
    """
    c = list(db.courses.find({"code": code}))
    if not c:
        course = {"code": code,
                  "name": name,
                  "misc": misc,
                  "description": descript}
        db.courses.insert(course)
        return True
    print 'db add course'
    return False

def update_course(code, newCode=None, name=None, misc=None, description=None):
    '''
    Modifies course information for a course already in the database. Can not modify course code (must delete and readd course with new code)

    Params: code - string (course code)
            newCode - string
            name - string
            misc - string
            description - string
    Returns: True if edit successful
             False otherwise
    '''
    args = locals()
    arg_keys = args.keys()
    update_dict = {key:args[key] for key in arg_keys if args[key] != None}
    ures = db.courses.update_one({"code":code},{"$set": update_dict })
    if newCode:
        update_dependency(code,newCode)
    print 'db update course'
    return ures.modified_count == 1

def remove_course(code):
    dres = db.courses.delete_one({"code":code})
    print 'db remove course'
    return dres.deleted_count == 1

def get_course(code):
    """
    Retrieve a course based on the course code

    Params: code - string
    Returns: course - dictionary
    """
    course = db.courses.find_one({"code": code})
    if not course:
        return None
    return course

def add_dependency(master, slave):
    """
    Adds a new dependency to the database, but fails if one or both courses does not exist, or it the dependency already exists, or if both courses are the same

    Params: master - string (course code)
            slave - string (course code)
    Returns: True if insertion successful
             False otherwise
    """
    if master != slave:
        m = db.courses.find_one({"code": master})
        s = db.courses.find_one({"code": slave})
        d = {"master": master,
            "slave": slave}
        q = db.dependencies.find_one(d)

        if m and s and not q:
            db.dependencies.insert(d)
            print 'db add dependency'
            return True
    return False

def get_dependencies(master):
    """
    Retrieves course codes of all courses dependent on master. Returns empty list if course doesn't exist or if course has no dependents
    """
    dep = list(db.dependencies.find({"master": master}))
    if dep:
        return [x["slave"] for x in dep]
    return []

def get_all_dependencies():
    """
    Get a master dictionary of all the dependencies

    Returns: dictionary
    key -> master course code
    value -> list of slave course codes
    """
    ret = {}
    courses = db.courses.find();
    for course in courses:
        code = course['code']
        deps = get_dependencies(code)
        ret[code] = deps
    return ret

def update_dependency(code,newCode):
    umres = db.dependencies.update_many({"master":code},{"$set":{"master":newCode}})
    usres = db.dependencies.update_many({"slave":code},{"$set":{"slave":newCode}})
    return umres.matched_count + usres.matched_count #strange type issue prevents modified_count from being reported so this will do

def remove_dependency(master,slave):
    dres = db.dependencies.delete_one({'master':master,'slave':slave})
    print 'db remove dependency'
    return dres.deleted_count == 1

def remove_all_dependents(code):
    dres = db.dependencies.delete_many({ "$or": [{'master':code},{'slave':code}]})
    return dres.deleted_count

def get_top_level():
    courses = db.courses.find()

    l = [course['code'] for course in courses
        if not db.dependencies.find_one({"slave": course['code']})]

    return l

def get_courses():
    c=db.courses.find()
    return [x['code'] for x in c]

def update_info():
    db.drop_collection("courses")
    db.drop_collection("dependencies")
    catalog = pandas.read_csv('courses.txt',dtype=str,sep='|').values
    for row in catalog:
        code = row[0]
        name = row[1]
        misc = row[2]
        desc = row[3]
        add_course(code,name,misc,desc)
    dps = pandas.read_csv('dependency.txt',dtype=str,sep='|').values
    for row in dps:
        master = row[0]
        slave = row[1]
        add_dependency(master,slave)

if __name__ == "__main__":


    # db.drop_collection("courses")
    # db.drop_collection("dependencies")
    #
    # print add_course("MKS66C", "Modern Biology", "All", "a description")
    # print add_course("SBS11QAS", "Anthropology & Sociobiology", "Juniors and Seniors", "another description")
    # print add_course("DWAI", "Don Worr' 'bout it", "yes", "a good class")
    # print add_dependency("SLS43", "SBS11QAS")
    # print add_dependency("SLS43", "DWAI")
    # print add_dependency("DWAI", "DWAI")
    """
    courses = db.courses.find()
    for course in courses:
        print course

    deps = db.dependencies.find()
    for dep in deps:
        print dep

    edit_course('DWAI', {'name':"Don't worry about it"})

    print get_course('DWAI')

    """
    """
    print get_dependencies("SLS43")

    print get_all_dependencies()

    print get_top_level()
    """

    update_info()

    #print get_top_level()

    '''
    update_course('MKS21X',newCode='APCS')
    courses = db.courses.find()
    for course in courses:
        print course


    deps = db.dependencies.find()
    for dep in deps:
        print dep

    # print update_course('DWAI',{'description':'spaghetti','name':'graphics'})

    # print get_all_dependencies()
    # print remove_course('MKS21X')
    # print remove_all_dependents('MKS21X')
    # print get_all_dependencies()


    # courses = db.courses.find()
    # for course in courses:
    #     print course
    '''
