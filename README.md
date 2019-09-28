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

Documentation: <https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>

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

* <http://localhost:5000/>
* <http://localhost:5000/JsonObject>

If you have done everything right you should see:

### <http://localhost:5000/>

```sh
Hello World
```

### <http://localhost:5000/JsonObject>

```js
{"functionReturn":{"JsonObject":{"Variable":"nestedVariable"}},"testBool":false,"testNumber":1,"testString":"1"}: for the JsonObject directory
```

Now just think, you can build any type of response you want and activate any function based on a url string that was entered after this, let your imagination run free.

## Contributing

### Creating a new feature branch

**Never** commit directly to the `master` branch. Always create a new feature branch for adding new code.

First, checkout the `master` branch if you haven't already.

```sh
git checkout master
```

Then, pull the most recent version of `master` from GitHub

```sh
git pull
```

Finally, create a new branch. This one will be for a new Button component.

```sh
git checkout -b button-component
```

### Committing your changes

Whenver your code gets to a "saveable" state, stage any changes you'd like to keep and commit them.

#### Stage changes

View changes:

```sh
git status
```

Add all changes:

```sh
git add *
```

Add specific change:

```sh
git add Button.jsx
```

#### Commit changes

```sh
git commit -m "Add initial Button code"
```

#### Create a draft pull request

Replace button-component with the name of your branch

```sh
git push origin button-component
```

Then, go to GitHub, click the compare and pull request button, click the dropdown on "Create Pull Request", and create a draft pull request.

#### Keep Working

Then, keep committing and pushing your branch to the origin. New commits in the branch will automatically be added to the pull request.

#### Merge the feature branch

When the branch is done, go to GitHub, and click "Ready for review".

Confirm that all of the changes are ok with the other team members.

Select "Squash and Merge" from the "Merge pull request" dropdown and click it.

And you're done a feature!

#### Review

* **Never** commit directly to master
* **Never** merge your branch to master locally, always create a pull request instead
* **Do** periodically merge from master into your branch so that you can incorporate important changes from other team members.

## Suggested Visual Studio Code Extensions

* Python (Microsoft)
* GitHub Pull Requests (GitHub) <- Use this for Pull Requests
* GitLens (Eric Amodio)
* markdownlint (David Anson)

Note: Make sure to sign in to the GitHub extension, and make sure the Python at the bottom left is set to your virtual environment.
