from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Hello world"


@app.route("/", methods=['GET', 'POST'])#renders the login page
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invailid credentials. Please try again.'
        else:
            return redirect(url_('index'))
    return render_template('login.html', error=error)

    if __name__ == '__main__':
        app.run(debug=True)

@app.route("/register")#renders the the register page
def register():
    error = None
    return render_template('Register.html', error=error)

@app.route("/mainpage")#renders the the home page
def mainpage():
    error = None
    return render_template('mainpage.html', error=error)

@app.route("/aboutgame")#renders the the about game page
def aboutgame():
    error = None
    return render_template('aboutgame.html', error=error)

@app.route("/aboutus")#renders the the about us page
def aboutus():
    error = None
    return render_template('aboutus.html', error=error)

@app.route("/score")#renders the the about us page
def score():
    error = None
    return render_template('score.html', error=error)
