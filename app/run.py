"""app/run.py"""
from flask import Flask
app = Flask(__name__)

nav = """
<nav>
    <a href="/">Home</a> |
    <a href="/about">About</a> |
    <a href="/contact">Contact</a>
</nav>
"""


@app.route('/')
@app.route('/home/')
def home():
    title = "Home"
    return f"""
        <!Docstring html>
        <html>
            <header>
               <title>{title}</title>
            </header>
            <body>
                {nav}
                <h1>{title}</h1>
                <p>Home page</p>
            </body>
        </html>
    """


@app.route('/about/')
def about():
    title = "About"
    return f"""
        <!Docstring html>
        <html>
            <header>
                <title>{title}</title>
            </header>
            <body>
                {nav}
                <h1>{title}</h1>
                <p>About page</p>
            </body>
        </html>
    """


@app.route('/contact/')
def contact():
    title = "Contact"
    return f"""
        <!Docstring html>
        <html>
            <header>
                <title>{title}</title>
            </header>
            <body>
                {nav}
                <h1>{title}</h1>
                <p>Contact details here</p>
            </body>
        </html>
    """


@app.errorhandler(404)
def page_not_found(e):
    title = "Flask drive page not found"
    return f"""
       <!Docstring html>
        <html>
            <header>
                <title>{title}</title>
            </header>
            <body>
                {nav}
                <h1>{title}</h1>
                <p>You seem to be lost!
                   Please use navigation to go to right page</p>
            </body>
        </html>
    """


if __name__ == '__main__':
    app.run()

