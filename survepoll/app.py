from flask import Flask, render_template, request,redirect
from markupsafe import escape
import re
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html",methods=["POST"]

url_pattern = re.compile(r'^[A-Za-z0-9-_./ ]*$')

def is_valid_url(url):
    return bool(url_pattern.match(url))

# Example usage:
url = "https://github.com/Lenson200/ourpollsurvey/tree/main/survepoll"
if is_valid_url(url):
    print("URL is valid!")
else:
    print("URL is not valid.")
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='127.0.0.1', port=80)
