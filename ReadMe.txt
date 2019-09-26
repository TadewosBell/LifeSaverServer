This tutorial shows you how download and install a simple flask app from git, and how to properly run it(Virtual Machines!!!)

it shows you a simple string being returned and also a complex JSON object while using a seperate custom python module with
a custom function


Make Project Directory

Make Virtual ENV in project directory [If you dont have pip install pip(it's a package manager)]
	documentation: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
	command: py -m venv env
		or python -m venv env
		or python3 -m venv env

	comment: env is the environment name

activate virtual env:
	command: 
		windows:  env\Scripts\activate
		mac or linux:  source env/bin/activate

git clone repository:
	run git clone https://github.com/TadewosBell/LifeSaverServer

pip install requirements:
	pip install -r requirements.txt

run 
	python app.py

got to:
	http://localhost:5000/
	http://localhost:5000/JsonObject

if you have done everything right, and solved all the errors you got on the way, you should see:
	Hello World: for the home directory

{"functionReturn":{"JsonObject":{"Variable":"nestedVariable"}},"testBool":false,"testNumber":1,"testString":"1"}: for the JsonObject directory


now just think, you can build any type of response you want and activate 
any function based on a url string that was entered after this let your imagination run free




