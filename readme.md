# Flask App Template

## Setup:

Install flask:
```bash
sudo pip install flask
```

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
