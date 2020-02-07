# Flask App Template

## Quick Setup:

Code to clone and break reference:
```bash
git clone https://github.com/upperlinecode/flaskproject
cd flaskproject
rm -rf .git
```

Code to install Flask (only necessary once):
```bash
pip3 install flask
```

Code to configure your flask app (you may need to set these once each time you open a new terminal):
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

**If you're developing in the cs50 IDE, ignore this next part.**
If you're developing locally, you can probably save time on the environment variables, by installing the [python-dotenv](https://pypi.org/project/python-dotenv/) package, which automatically loads the settings we're currently setting with `export`:
```bash
pip3 install python-dotenv
```

If that installation works, you should be able to create a file called `.env` and add the `export` statements above to it, that way these configurations won't need to be made every time. 

[troubleshooting](#troubleshooting-package-installation)

## Virtual Environments (optional)

If you're running this locally, you will likely want to run this program inside a virtual environment - that way changes to your Python configuration don't persist and impact other Python programs on your machine. If you're running this program in a remote environment like Cloud Shell, Cloud9, or cs50, adding a virtual environment within those containers may complicate things more than helping them. 

To create a virtual environment (you only need to do this once), run this code in terminal:
```bash
python3 -m venv venv
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

To start, the only package you need to run is `flask` for (hopefully) obvious reasons.

To install flask, run this code in terminal.
```bash
pip3 install flask
```
Remember, if you're using a virtual environment, these packages will only be installed IN the virtual environment (which is part of why we don't recommend it in cs50 where we won't need it - students will accidentally forget where they've configured different settings).

### Troubleshooting package installation

If your IDE throws errors on either of these commands saying that you aren't authorized, your account may not be authorized to install packages on the IDE you're using. There are two ways to work around this. The first is by adding the user flag:
```bash
pip3 install --user flask
```
The other way around this is to try adding the 'switch user and do' command ('sudo' for short):
```bash
sudo pip3 install flask
```


The settings will not be stored between sessions, so every time you open a new terminal, you'll need to run these commands, which are stored in the `run-variables.md` file for your convenience:
```bash
export FLASK_APP=main.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=8080
export FLASK_DEBUG=1
```

After that you should be able to execute the `flask run` command normally.
