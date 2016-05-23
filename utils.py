import database

def tree_data():
    print 'hi'
    r={}
    deps=database.get_all_dependencies()
    childs=[y for x in deps.values() for y in x]
    print childs
    roots=[x for x in deps.keys() if x not in childs]
    #return roots
     
def generate_tree():
    """
    Generates tree based on top-level courses that have no prereqs
    """
    
    l = []
    top = database.get_top_level()
    for course in top:
        find_children(course, l)
    d = [{"parent": "null", "name": "Stuff", "children": l}]
    return d

def find_children(code, l):
    """
    Recursively finds children and appends to given list
    """
    course = database.get_course(code)
    deps = database.get_dependencies(code)
    d = {"name": course['name'],
         "parent": code,
         "code": course['code'],
         "year": course['year'],
         "children": []}
    if deps:
        for dep in deps:
            find_children(dep, d["children"])
    l.append(d)

#print tree_data()

print generate_tree()
