from flask import Flask

from api.reports import reports_api

app = Flask(__name__)

app.register_blueprint(reports_api)

app.run(debug=True, host='0.0.0.0')