# Neverland

## Setup

The first time, create an environment:

```
virtualenv -p /usr/bin/python3 env

```

To work on the project, activate the environment:
```
source env/bin/activate
```

The first time, install the dependencies:

```
pip install requirements.txt
```

Run the project:

```
FLASK_APP=main.py flask run
```
