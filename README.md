# Life Saver Server

## Installation

This tutorial shows you how download and install a simple flask app from git, and how to properly run it (Virtual Machines!!!)

It shows you a simple string being returned and also a complex JSON object while using a seperate custom python module with
a custom function

### Clone the repository

```sh
git clone https://github.com/TadewosBell/LifeSaverServer
```
### Set up the virtual environment

Make Virtual ENV in project directory [If you dont have pip install pip(it's a package manager)]

Documentation: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

Create the enviroment with one of these commands:

```sh
python -m venv env
```
```sh
python3 -m venv env
```
```sh
py -m venv env
```
Activate the virtual enviroment:

Windows:
```sh
env\Scripts\activate
```

Mac/Linux:
```sh
source env/bin/activate
```

Install the requirements:

```sh
pip install -r requirements.txt
```
## Run the App

```sh
python app.py
```
Then go to:
..* http://localhost:5000/
..* http://localhost:5000/JsonObject

If you have done everything right you should see:

### http://localhost:5000/
```	
Hello World:
```
### http://localhost:5000/JsonObject
```js
{"functionReturn":{"JsonObject":{"Variable":"nestedVariable"}},"testBool":false,"testNumber":1,"testString":"1"}: for the JsonObject directory
```

Now just think, you can build any type of response you want and activate any function based on a url string that was entered after this, let your imagination run free.




