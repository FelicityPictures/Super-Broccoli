from flask import Flask, render_template, redirect, request, session, url_for
import database
import utils
import json
import auth

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
    
@app.route('/courses', methods=['GET'])
def send_info():
    course_info = utils.generate_tree()
    return json.dumps(course_info)
    #with open('courses.json', 'w') as outfile:
       # json.dump(course_info, outfile)
    #return json.dumps("success")

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method=="GET":
        #if 'username' in session:
        #    return session['username'] +' is already logged in.'
        #else:
        return render_template('login.html')
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
            #print error
            return render_template('login.html', fml='fuckmylife'), 401 

@app.route('/logout', methods=['GET'])
def logout():
    if request.method=='GET':
        session.pop('username',None)
        return render_template('login.html'), 200
    else:
        return redirect(url_for('home'))

@app.route('/add')
def test():
    return 'test page'

if __name__=='__main__':
    app.debug=True
    app.secret_key='here come dat boi'
    app.run(host='0.0.0.0', port=5000)

