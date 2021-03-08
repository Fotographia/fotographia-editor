# Install Fotogràphia Editor

## Run

### Manually
You should have [Python 3.9](https://www.python.org/downloads/release/python-390/) and [Pip](https://pip.pypa.io/en/stable/installing/) installed.
```
# Clone the repository 
$ git clone https://github.com/Fotographia/fotographia-editor.git

# Navigate to the project's folder
$ cd fotographia-editor

# Install virtualenv
$ pip install virtualenv

# Create a python virtual envinonment
$ python -m virtualenv venv

# Enter the environment
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Export envinonment variables
$ export PORT=5000
$ export FLASK_ENV=development

# Run application
$ python run.py
```

Open your browser and go to localhost:5000

### Docker
You should have [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed.
```
# Clone the repository 
$ git clone https://github.com/Fotographia/fotographia-editor.git

# Navigate to the project's folder
$ cd fotographia-editor

# Run docker
$ docker-compose up -d --build 
```

Open your browser and go to localhost:5000

Note: If you use docker, please install [flake8](https://pypi.org/project/flake8/) and [black](https://pypi.org/project/black/) 
at your PC. Also, change the path at the vscode settings.json file.

```json
{
    "python.linting.flake8Enabled": true,
    // delete this
-   "python.linting.flake8Path": "./venv/bin/flake8",
    // add this
+   "python.linting.flake8Path": "./local/bin/flake8",
    "python.formatting.provider": "black",
    //delete this
-   "python.formatting.blackPath": "./venv/bin/black",
    // add this
+   "python.formatting.blackPath": "./local/bin/black",
    "[python]": {
        "editor.formatOnSave": true,
    },
}
```