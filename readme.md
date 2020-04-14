# Flask App Template

1. [Quick Setup for Cloud Shell](#setup)
2. [Running the App](#run)
3. [Anatomy of the App](#anatomy)

## Quick Setup for Cloud Shell<a id="setup"></a>

Before we can even really get started with a Flask application, we need to get a few things configured in our Cloud Shell environments. Follow these steps to install Flask and make sure that installation sticks.

#### Setup Step 1

In Cloud Shell, there are a few settings that we need to set manually. In particular, we want to install the Flask microframework specifically using Python3, and change a few of the default settings.

If you type `python --version`, it will show an older version of Python (2.7) that is popular, but that officially went out of date as of January 1, 2020, and therefore will not be used in this class.

Slack out this code, and have them copy paste it into their Cloud Shell terminals.

```bash
sudo pip3 install flask
```

You will likely get a prompt to upgrade Pip - we recommend avoiding that step as we have tested the default version that comes packaged with Cloud Shell, but may not have tested the most recent version at the time of your reading this guide.   

You can confirm that the installation has worked by typing `flask --version`. If Flask is found to be running with Python 3.7 or higher, step 1 is complete.

#### Setup Step 2

We also want to set up debug mode for our Flask applications. This is a setting that makes sure the server we run in terminal is listening for any changes to our file - that way if we make a change, the server can automatically restart, meaning we always work from the latest version.

This level of convenience does *not* play nicely with Cloud Shell's autosave feature, so **be sure to disable autosave in the "File" menu**.

Once that's done, you can setup debug mode for Flask applications with this line of code:

```bash
export FLASK_DEBUG=1
```

#### Setup Step 3

This is great, but Cloud Shell does not persist package installations or global settings like these. Every time you leave it idle for more then a few hours, Cloud Shell will stop running. For the most part, that is a good thing! it saves energy and helps keep Cloud Shell free. But the bad news is that that means you'll have to reinstall Flask each time you start up the environment.

The following three lines of code will set up a script to do this for us in the future, once each time Cloud Shell resets.

```bash
touch ~/.customize_environment
echo 'sudo pip3 install flask' >> ~/.customize_environment
echo 'export FLASK_DEBUG=1' >> ~/.customize_environment
```

This creates a hidden file called `.customize_environment` that Cloud Shell always looks for when starting an environment. If you have the file, which you now do, then it runs whatever lines of code are written there for you behind the scenes as part of its startup process.

#### Setup Conclusions

Any time you find yourself installing a new Python package as time goes on, be sure to consider the following recommendations:
* Instead of running `pip install _______`, you'll need to run `sudo pip3 install _______` because in this virtual environment, you'll want to install as part of Cloud Shell's Python 3 (instead of the default Python 2).
* If you want that package to persist (to remain installed after you log out each evening), be sure to add that to the `.customize_environment` file. You can do this either by using the command `echo 'sudo pip3 install ______' >> ~/.customize_environment`, or by opening the customization script using `cloudshell open ~/.customize_environment` to modify your startup script manually.

## Running the App<a id="run"></a>

Run this app by navigating to the directory where it is housed and running `flask run`. Then click the IP address in terminal to be redirected to the location where the app is running.

## Anatomy of the app<a id="anatomy"></a>

Here's everything inside our Flask template. Files a first-time learner should pay attention to are listed in bold.

<pre>
flaskproject
├── .gitignore - shows which files (like .pyc) for git to ignore.
├── Procfile - Ignore. Used for deployment.
├── app.py - This is the main file for our app.
├── model.py - This is where we will write the logic of our app.
├── readme.md - That's this file!
├── requirements.txt - Used for deployment to say what packages are needed.
├── runtime.txt - Ignore. Used for deployment.
├── static - This is where we house assets like images and stylesheets.
│   ├── css - Put stylesheets here.
│   │   └── style.css
│   └── images - Put images here.
│       └── micropig.jpg
└── templates - Put templates (views) in this folder.
    └── index.html - This will be the first template we render.
</pre>
