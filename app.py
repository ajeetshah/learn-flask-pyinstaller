from flask import Flask
import numpy as np
from gunicorn.app.base import BaseApplication
import importlib.util

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
        <p>Hello, World!</p>
        <ul>
            <li><a href="http://localhost:8000">Index</a></li>
            <li><a href="http://localhost:8000/np-version">NP Version</a></li>
            <li><a href="http://localhost:8000/np-array-sum">NP Array Sum</a></li>
        </ul>
    """

@app.route("/np-version")
def np_version():
    return np.__version__

@app.route("/np-array-sum")
def np_array():
    arr = np.array([2, 3, 4])
    return "Sum of {0}: {1}".format(arr, sum(arr))

class GunicornServer(BaseApplication):
    def __init__(self, app, config_path=None):
        self.application = app
        self.options = self.load_config_from_file(config_path) if config_path else {}
        super().__init__()
    
    def load_config_from_file(self, config_path):
        config = {}
        spec = importlib.util.spec_from_file_location("gunicorn_config", config_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for key in dir(module):
            if not key.startswith("__"):
                config[key] = getattr(module, key)
        return config
    
    def load_config(self):
        for key, value in self.options.items():
            if key in self.cfg.settings and value is not None:
                self.cfg.set(key, value)

    def load(self):
        return self.application

if __name__ == "__main__":
    config_file = "config/gunicorn_config.py"
    GunicornServer(app, config_file).run()