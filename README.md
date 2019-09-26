# Life Saver Server

## Installation

This tutorial shows you how download and install a simple flask app from git, and how to properly run it (Virtual Machines!!!)

It shows you a simple string being returned and also a complex JSON object while using a seperate custom python module with
a custom function

### Clone the repository

```bash
git clone https://github.com/TadewosBell/LifeSaverServer
```
### Set up the virtual environment

Make Virtual ENV in project directory [If you dont have pip install pip(it's a package manager)]

Documentation: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

Create the enviroment with one of these commands:

```bash
python -m venv env
```
```bash
python3 -m venv env
```
```bash
py -m venv env
```
Activate the virtual enviroment:

```bash
env\Scripts\activate
```
Install the requirements:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python app.py
```

Go to:
	http://localhost:5000/
	http://localhost:5000/JsonObject

if you have done everything right, and solved all the errors you got on the way, you should see:
	Hello World: for the home directory

```javascript
{"functionReturn":{"JsonObject":{"Variable":"nestedVariable"}},"testBool":false,"testNumber":1,"testString":"1"}: for the JsonObject directory
```


now just think, you can build any type of response you want and activate 
any function based on a url string that was entered after this let your imagination run free




