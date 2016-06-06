# Super-Broccoli
Software Development 2 Final Project (2016)

##Deployment Guide
This guide is for installing and running Course Broccoli on a DigitalOcean droplet with Ubuntu 14.04.4+<br>

In a terminal session, ssh into the droplet IP provided by DigitalOcean. You may need to ssh into root@DROPLET_IP in order for installation to work. The root password should be included in the e-mail sent by DigitalOcean upon droplet creation.
```
$ ssh root@<YOUR DROPLET IP>
$ root@<YOUR DROPLET IP>'s password: <ROOT PASSWORD>
```
Once you have successfully connected to the droplet, clone this repository to a directory of your choice. If git is not installed, you can do so by running:
```
sudo apt-get install git
```
To clone the repo, run:
```
git clone https://github.com/FelicityPictures/Super-Broccoli.git
```
Course Broccoli imports various python libraries (these can be found in requirements.txt). To make sure all of the requirements are installed, run each of the following commands and follow installation instructions.
```
pip install flask
pip install pymongo
sudo apt-get install python-pandas
```
Course Broccoli also uses a MongoDB server. If a local server is not already running, you can do so by running: (Note: This requires a ~/data/db directory to exist)
```
mongod
```
Once all the required libraries are installed, the Flask app is ready to be run. To keep the app running in the background, use the console application Screen. If screen is not installed, you can do so by running:
```
sudo apt-get update
sudo apt-get install screen
```
Start a new session by running 
```
screen
```
A licensing page should appear. Press "return" or "enter" to continue. To run the Flask app, cd into the repository and run the python app. 
```
cd Super-Broccoli
python app.py
```
To detatch from the screen, use the keyboard shortcut Ctrl-a d<br>
If all of this is done successfully, then Course Broccoli will have been deployed. Horray!

##devlog
<b>5/13:</b> Client meeting #1 <br>
<b>5/16:</b> Went over client meeting, made vague timeline, added base files <br>
<b>5/17:</b> Planned basic appearance, database structure, and divided labor <br>
<b>5/18-20:</b> Created mongo database with query functions<br>
<b>5/21-22:</b> Implemented basic tree diagram, populated with sample data<br>
<b>5/23-24:</b> Implemented pan and zoom for tree diagram, added more sample data <br>
<b>5-24:</b> Client meeting #2<br>
<b>6-6:</b> Deployment Guide tested and added, preliminary superuser functions added<br>

##deadlines
<b>5/27:</b> Send client deadlines, engage in more frequent e-mail communication<br>
<b>5/28:</b> Have a display for course metadata, solidify design, oAuth should be done at this point<br>
<b>5/29:</b> Implement selection of parent node, Schedule planning thing prototype<br>
<b>5/30:</b> Implement visual cues for dependency (colors, etc) Should be nearing final model of the tree<br>
<b>6/1:</b> Implement graduation requirement checking, coordinate with Team Tetrabyte (as per Mr. Brown's instructions)<br>
<b>6/3:</b> Final Prototype, website complete and not ugly, schedule final client meeting<br>
<b>6/6-10:</b> Polish Polish Polish, Bug testing, setup on DO and everything will be henshin a-gogo<br>

Deploy!<br>
![Whoo!](https://scontent-lga3-1.xx.fbcdn.net/t39.1997-6/p128x128/851574_457535061023413_1593043981_n.png)
