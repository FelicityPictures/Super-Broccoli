import database

def tree_data():
    print 'hi'
    r={}
    deps=database.get_all_dependencies()
    childs=[y for x in deps.values() for y in x]
    print childs
    roots=[x for x in deps.keys() if x not in childs]
    #return roots

def generate_tree(root=None):
    """
    Generates tree based on top-level courses that have no prereqs
    """
    l = []
    if root:
        top = root
        course = database.get_course(root)
        find_children(course['code'], l)
        d = [{"parent": None, "name": course['name'], "code": course['code'], "misc": course['misc'], "description": course['description'], "children": l}]
    else:
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
         "misc": course['misc'],
         "description": course['description'],
         "children": []}
    if deps:
        for dep in deps:
            find_children(dep, d["children"])
    l.append(d)

def user_add_course(form):
    code=form['code']
    name=form['name']
    desc=form['desc']
    database.add_course(code, name, None, desc)
    print 'success'

def user_rem_course(form):
    code=form['code']
    database.remove_course(code)

def user_upd_course(form):
    code_ident=form['course_toup']
    code_new=form['code']
    name_new=form['name']
    desc_new=form['desc']
    database.update_course(code_ident, code_new, name_new, desc_new)

def user_add_dependency(form):
    master=form['master']
    slave=form['slave']
    database.add_dependency(master, slave)

def user_rem_dependency(form):
    for key in form.keys():
        entry=form[key].split(':')
        master=entry[0]
        slave=entry[1]
        print 'master: '+master
        print 'slave: '+slave
        database.remove_dependency(master, slave)

#print tree_data()


#generate_tree()
