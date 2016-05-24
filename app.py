from flask import Flask, render_template, redirect, request, session, url_for
import database
import utils
import json
import auth

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    print 'loading home'
    if 'username' in session:
        print 'user in sesh'
        return render_template('index.html',user=session['username'])
    else:
        print 'not logged in'
        return redirect(url_for('login'))
    
@app.route('/courses', methods=['GET'])
def send_info():
    course_info = utils.generate_tree()
    return json.dumps(course_info)
    #with open('courses.json', 'w') as outfile:
       # json.dump(course_info, outfile)
    #return json.dumps("success")

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        id_token=request.form['id']
        if auth.authenticate(id_token):
            session['username']=auth.getName(id_token)
            print 'authenticated'
            return redirect('/home')
    print 'not logged in'
    return render_template('login.html', error=auth.getError()) 

@app.route('/logout', methods=['GET'])
def logout():
    if request.method=='GET':
        session.pop('username',None)
        return render_template('login.html')
    else:
        return redirect(url_for('home'))

if __name__=='__main__':
    app.debug=True
    app.secret_key='here come dat boi'
    app.run(host='0.0.0.0', port=5000)

