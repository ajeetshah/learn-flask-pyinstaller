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
pyinstaller --clean --onefile --hidden-import=gunicorn \
--hidden-import=gunicorn.log \
--hidden-import=gunicorn.glogging \
--hidden-import=gunicorn.workers.gthread \
--add-data config:config app.py
```
