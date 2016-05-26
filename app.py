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
    print 'loading home'
    if 'username' in session:
        print 'user in sesh'
        return render_template('index2.html')
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

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template('login2.html')
    else:
        id_token=request.form['id']
        if auth.authenticate(id_token):
            user=auth.getName(id_token)
            session['username']=user
            print session['username']
            print 'authenticated'
            return render_template('index.html'), 200
        #msg=request.form['msg']
        #print msg
        #return redirect('/test')
        else:
            print 'not logged in'
            return render_template('login2.html', error=auth.getError()), 401 

@app.route('/logout', methods=['GET'])
def logout():
    if request.method=='GET':
        session.pop('username',None)
        return render_template('login2.html'), 200
    else:
        return redirect(url_for('home'))

if __name__=='__main__':
    app.debug=True
    app.secret_key='here come dat boi'
    app.run(host='0.0.0.0', port=5000)

