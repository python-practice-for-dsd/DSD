from flask import Flask, render_template, request

app = Flask(__name__, static_folder=".", static_url_path="")


@app.route("/")
def home():
    kwargs = {}
    kwargs["thing"] = request.args.get("thing")
    kwargs["height"] = request.args.get("height")
    kwargs["color"] = request.args.get("color")
    return render_template("home.html", **kwargs)


app.run(port=5000, debug=True)

# http://127.0.0.1:5000?thing=aaa&height=bbb&color=ccc
