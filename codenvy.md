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
