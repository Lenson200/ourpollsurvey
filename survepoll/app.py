from flask import Flask, render_template, request,redirect
from markupsafe import escape

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html",methods=["POST"])

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='127.0.0.1', port=80)
# REGISTRANTS = {}

# SPORTS = [
#     "Basketball",
#     "Soccer",
#     "Ultimate Frisbee"
# ]
# @app.route("/")
# def index():
#     return render_template("index.html",sports=SPORTS)
# @app.route("/register", methods=["POST"])
# def register():

#     # Validate name
#     name = request.form.get("name")
#     if not name:
#         return render_template("registrant.html", message="Missing name")

#     # Validate sport
#     sport = request.form.get("sport")
#     if not sport:
#         return render_template("failure.html", message="Missing sport")
#     else:
#          return render_template("success.html", message="{sport}")
#     if sport not in SPORTS:
#         return render_template("failure.html", message="Invalid sport")

#     # Remember registrant
#     REGISTRANTS[name] = sport

#     # Confirm registration
#     return redirect("/index.html")


# @app.route("/registrants")
# def registrants():
#     return render_template("registrants.html", registrants=REGISTRANTS)

# if __name__ == '__main__':
#     app.run(debug=True)
