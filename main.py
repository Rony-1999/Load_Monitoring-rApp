from flask import Flask
from flask_cors import CORS
from routes.policy_routes import bp
from config import HOST_IP, HOST_PORT

app = Flask(__name__)
CORS(app)

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host=HOST_IP, port=HOST_PORT, debug=True)

