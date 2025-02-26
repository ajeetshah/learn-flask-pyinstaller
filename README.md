# learn-flask-pyinstaller

## Install dependencies

```shell
python3 -m venv .v-env
source .v-env/bin/activate
pip install -r requirements.txt
```

## Start the dev server

```shell
flask --app app run
```

## Start the production server

```shell
gunicorn -c config/gunicorn_config.py 'app:app'
```

## How to create dist/ with pyinstaller?

```shell
pyinstaller app.py
```
