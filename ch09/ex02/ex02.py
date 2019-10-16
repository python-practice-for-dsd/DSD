from flask import Flask

app = Flask(__name__, static_folder=".", static_url_path="")


app.run(port=5000, debug=True)
