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
    d = [{"parent": None, "name": "Department", "children": l}]
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
         "description": course['description'],
         "children": []}
    if deps:
        for dep in deps:
            find_children(dep, d["children"])
    l.append(d)

def user_add_course(form):
    code=form['code']
    name=form['name']
    year=form['year']
    desc=form['desc']
    #database.add_course(code, name, year, desc)
    print 'success'

def user_rem_course(form):
    code=form['code']
    #database.remove_course(code)

def user_add_dependency(form):
    master=form['master']
    slave=form['slave']
    #database.add_dependency(master, slave)

def user_rem_dependency(form):
    for key in form.keys():
        entry=form[key].split(':')
        master=entry[0]
        slave=entry[1]
        print 'master: '+master
        print 'slave: '+slave
        #database.remove_dependency(master, slave)
        
#print tree_data()


#generate_tree()
