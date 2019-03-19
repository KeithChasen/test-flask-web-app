from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '27526d42886bf80c026c9e2838b62f7a'

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
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)