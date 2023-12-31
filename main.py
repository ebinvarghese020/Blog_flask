from flask import *
import requests

app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()

data = response.json()
titles = [item["title"] for item in data]
subtitle = [item["subtitle"] for item in data]
body = [item["body"] for item in data]
id = [item["id"] for item in data]
print(id)

print(titles)


@app.route("/")
def home():
    return render_template('index.html', data=data)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact",  methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        pass

    return render_template("contact.html")


@app.route("/mail", methods=['POST'])
def mail():
    if request.method == "POST":
        return "ok"
    else:
        return "ERROR"


@app.route("/post/<int:id1>")
def post(id1):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == id1:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/test")
def test():
    return render_template("post.html")