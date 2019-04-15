# Flask App Template

## Quick Setup:

Code to clone and break reference:
```bash
git clone https://github.com/upperlinecode/flaskproject
cd flaskproject
rm -rf .git
```

Code to configure your flask app (run once each time you open a new terminal):
```bash
export FLASK_APP=main.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=8080
export FLASK_DEBUG=1
```

Code to run flask:
```bash
flask run
```

To save time on the environment variables, some IDEs will let you install the python-dotenv package, which loads these up every time:
```bash
pip install python-dotenv
```
[troubleshooting](#troubleshooting-package-installation)



## Virtual Environments (optional)

If you're running this locally, you may want to run this program inside a virtual environment - that way changes to your Python configuration don't persist and impact other python programs on your machine.

To create a virtual environment (you only need to do this once), run this code in terminal:
```bash
python -m venv venv
```

To ENTER your virtual environment (you'll need to do this every time you open up a new terminal), run this code:
```bash
. venv/bin/activate
```

To EXIT your virtual environment (you'll want to do this if you decide to change projects - think of it like shutting this one down), you just need one word:
```bash
deactivate
```

If you're using a virtual environment like Codenvy, the virtual environment produces more problems than it solves, so consider skipping this step.

## Python packages

The only packages you need to run are `flask` (for obvious reasons), and `python-dotenv` which allows us to store configuration information in the files `.env` and `.flaskenv`.

To install these packages, run this code.
```bash
pip install flask
pip install python-dotenv
```
Remember, if you're using a virtual environment, these packages will only be installed IN the virtual environment (which is part of why we don't recommend it if you don't need it - students will accidentally forget where they've configured different settings).

If this has worked, and python-dotenv is working, then running a flask application is pretty simple:
```bash
flask run
```

### Troubleshooting package installation

If your IDE throws errors on either of these commands saying that you aren't authorized, your account may not be authorized to install packages on the IDE you're using, so try adding the 'switch user and do' command ('sudo' for short):
```bash
sudo pip install flask
sudo pip install python-dotenv
```

If you encountered errors with the python-dotenv package, we can still configure those settings manually. You'll need to run these commands once each time you open a terminal:
```bash
export FLASK_APP=main.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=8080
export FLASK_DEBUG=1
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
```

After that you should be able to execute the `flask run` command normally.

## Codenvy Run Command:

Here's the you'll want to run in your custom command:
```bash
cd <your-directory-name-here>
export FLASK_APP=main.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=8080
export FLASK_DEBUG=1
flask run
```
If you clone this directly, your `<your-directory-name-here>` will be `flaskproject`.

Here's the code for to generate your preview URL:
```bash
http://${server.port.8080}
```

## Local Run Command

Running locally is simpler. Just navigate to the your flask project in the command line, and then run the following commands:
```bash
export FLASK_APP=main.py
export FLASK_DEBUG=1
flask run
```

You can also simplify this to just `flask run` if you `pip install python-dotenv` and then use the `.flaskenv` file to hold the flask app and the debug settings.  
