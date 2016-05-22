from flask import Flask, render_template, redirect
import database
import json

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/courses', methods=['GET'])
def send_info():
    course_info=database.get_all_dependencies()
    #return json.dumps(course_info)
    with open('courses.json', 'w') as outfile:
        json.dump(course_info, outfile)
    return json.dumps("success")

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=5000)
