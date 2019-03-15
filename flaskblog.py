from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Keith Chasen',
        'title': 'Blog Post 1',
        'content': 'This is a brand new post',
        'date_posted': 'March 15, 2019'
    },
    {
        'author': 'Jack Doe',
        'title': 'Blog Post 2',
        'content': 'This is another post',
        'date_posted': 'March 15, 2019'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)