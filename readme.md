# Flask App Template

1. [Quick Setup for Replit](#setup)
2. [Local Setup](#local-setup)
2. [Running the App](#run)
3. [Anatomy of the App](#anatomy)

## Quick Setup for Replit<a id="setup"></a>

Click "use this template" and create your own copy. Then clone this project down to Replit using the "import from GitHub" feature - feel free to ask a peer or instructor if you have trouble with this, as it's a feature that changes somewhat frequently. 

## Local Setup<a id="local-setup"></a>

Click "use this template" and create your own copy. Then clone it down to your local environment in the directory of your choice, and `cd` into this project. 

Install Flask by running `pip3 install flask` - type `flask --version` to see if the installation was successful. Try `sudo pip3 install flask` instead if you have any trouble getting that to work.


## Running the App<a id="run"></a>

If you're using Replit, just press the "RUN" button. Use the "open in new tab" button to get a full-sized preview. 

If you're running this application locally, navigate to the directory where it is housed and run `flask run`. Then click the IP address in terminal to be redirected to the location where the app is running. 

## Anatomy of the app<a id="anatomy"></a>

Here's everything inside our Flask template. A first-time learner should really only start by looking at the **app.py**, the **model.py**, the **templates** folder, and the **static** folder. Almost everything else operates more behind the scenes, and can be a later focus. 

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

If you want a more detailed explanation, keep reading.

### Files you WILL need to know about / focus on:

#### The `app.py`

This is the most important part of your Flask application - it's the code that tells your application how to respond to the requests your users make when they visit your page, and it's really the main thing separating our web application from a standard website. For example, with a webSITE, if we went to `petespizza.com/myaccount`, it would display the same information for every user. With a webAPP, we can make sure `petespizza.com/myaccount` is unique to each user by coding out some behavior in our `app.py`.

#### The `model.py`

The `app.py` is really just meant to be air-traffic control for our web application's visitors - the complex logic should live here in `model.py`. 

#### The `templates` folder

We're upgrading from HTML pages to HTML templates - the big difference here is that templates can be injected with Python to generate new content. Instead of needing to code out 100 `myaccount` for 100 users, you can code just 1 page, and use template logic to provide each user with a customized experience. 

#### The `static` folder

Images and CSS files are generally items we want our user to be able to access easily and directly - that doesn't need to come through the application. The `static` folder is also sometimes called the "public" folder for that exact reason. This template uses it for images and for CSS, which are two of the most common things you'll encounter in a web application's public folder no matter what language the app itself is written in. 

### Files you can ignore for now

We won't use these files - they're just here to make the application play nicely with Replit and/or Heroku. 

#### `.replit`

This file only has two lines of code in it, and may even be hidden once you open the code in Replit. This is just a set of instructions to set up the big green "> RUN" button at the top of a Repl.

```
language = "bash"
run = "python3 replitwrapper.py"
```

The first line tells Replit to create a bash repl, which allows us to use bash commands to control our application. This is the same environment and language you'd see if you just opened up the terminal on your Mac or Linux computer. The second line is the script that will be executed when "RUN" is pressed. We set up the run button to activate a file called "replitwrapper" which is where our Flask app starts (at least while it's in development). 

#### `.flaskenv`

This only includes one line of code: `FLASK_DEBUG=1`

This tells Flask to restart the application every time you save changes. Since Replit autosaves, this should mean that most changes you make should go live instantly. 

#### `.gitignore`

This tells Replit which files don't need to be included when you save your changes to GitHub. It's already set up pretty well, so we probably won't use it at all. 

#### `Procfile`

This also includes only one line of code: `web: gunicorn app:app`
You can't deploy a Flask application live without a wraparound tool like [Green Unicorn](https://gunicorn.org/) - how and why it works is beyond the scope of this course, but your deployment wouldn't work without it. 

#### `replitwrapper.py`

Replit needs a package called "web" to run our web apps. But Heroku doesn't know what "web" is, and can't use it. So ONE of our platforms MUST have this, but the other CAN'T have it. The solution we found was to create two different entry points into our application. The `replitwrapper.py` is where Replit enters our application, and uses the necessary package, and then loads in the app from `app.py`.

Heroku will enter our app directly from `app.py` - problem solved!

#### `runtime.txt`

This specifies the version of Python we'll use in deployment with Heroku. Most of the curriculum has been tested and runs correctly in the version listed in this file, but if you notice that your app is failing on Heroku but working on Replit, you may want to make sure these versions match by typing `python3 --version` in the Replit console, and then updating this file to the version that Replit is currently using. 