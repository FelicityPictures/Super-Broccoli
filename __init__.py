from flask import Flask, render_template, redirect, request, session, url_for
import database
import utils
import json
import auth
import os

app=Flask(__name__)

#@app.route('/home', methods=['GET'])
@app.route('/')
@app.route('/home')
def home():
    if 'username' in session:
        print 'Going to home'
        return render_template('index.html', user=session['username'])
    else:
        print 'Not logged in, going to login'
        return redirect(url_for('login'))
    
@app.route('/courses', methods=['GET', 'POST'])
def send_info():
    root = request.form['r']
    print root
    course_info = utils.generate_tree(root=root)
    return json.dumps(course_info)
    

@app.route('/login', methods=["GET","POST"])
@app.route('/login/<error>', methods=['GET','POST'])
def login(error=None):
    if request.method=="GET":
        print error
        err=''
        if error:
            err=auth.getError()
            if 'username' in session:
                session.pop('username',None)
        #if 'username' in session:
        #    return session['username'] +' is already logged in.'
        #else:
        
        return render_template('login.html', err=err)
    else:
        id_token=request.form['id']
        if auth.authenticate(id_token):
            user=auth.getName(id_token)
            session['username']=user
            #print session['username']
            #print 'authenticated'
            return render_template('index.html', user=session['username']), 200
        #msg=request.form['msg']
        #print msg
        #return redirect('/test')
        else:
            #print 'not logged in'
            error=auth.getError()
            print error
            return render_template('login.html'), 401 

@app.route('/logout', methods=['GET'])
def logout():
    if request.method=='GET':
        session.pop('username',None)
        return render_template('login.html'), 200
    else:
        return redirect(url_for('home'))

@app.route('/add')
def adder():
    if 'username' in session:
        if auth.authSuper(session['username']):
            deps=database.get_all_dependencies()
            courses=database.get_courses()
            print 'TESTCODE' in courses
            return render_template('adder.html', deps=deps, courses=courses, user=session['username'])
        else:
            return render_template('master.html', error='You do not have the permission for this.')
    else:
        return redirect(url_for('login'))

@app.route('/add_course', methods=["POST"])
def add_course():
    print 'add course'
    print request.form
    utils.user_add_course(request.form)
    return redirect(url_for('adder'))

@app.route('/remove_course', methods=['POST'])
def rem_course():
    print 'rem course'
    print request.form
    utils.user_rem_course(request.form)
    return redirect(url_for('adder'))

@app.route('/update_course', methods=['POST'])
def upd_course():
    print 'upd course'
    print request.form
    return redirect(url_for('adder'))

@app.route('/add_dependency', methods=['POST'])
def add_dep():
    print 'add dep'
    print request.form
    utils.user_add_dependency(request.form)
    return redirect(url_for('adder'))

@app.route('/remove_dependency', methods=['POST'])
def rem_dep():
    print 'rem dep'
    print request.form
    utils.user_rem_dependency(request.form)
    return redirect(url_for('adder'))

if __name__=='__main__':
    #app.debug=True
    app.secret_key=os.urandom(32)
    #print app.secret_key
    #app.run(host='0.0.0.0', port=5000)
    app.run()
