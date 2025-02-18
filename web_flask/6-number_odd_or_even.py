#!/usr/bin/python3
"""
Write a script that starts
a Flask web application:

Your web application must be
listening on 0.0.0.0, port 5000

Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”,
followed by the value of the text variable
(replace underscore _ symbols with a space )

/python/(<text>): display “Python ”,
followed by the value of the text variable
(replace underscore _ symbols with a space )

The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
H1 tag: “Number: n” inside the tag BODY

/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY

You must use the option
strict_slashes=False in your route definition
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def womp():
    """HTML indicates an exchange of information is forthcoming"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def wompo():
    """Return the HBNB web?"""
    return "HBNB"


@app.route('/c/<stuff>', strict_slashes=False)
def wompa(stuff):
    """Return the url of the page?"""
    return "C {}".format(stuff.replace("_", " "))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def wompu(text="is cool"):
    """Just saying, cool people don't say they're cool"""
    return "Python %s" % text.replace('_', ' ')


@app.route('/number/<int:char>', strict_slashes=False)
def checkInt(char):
    """A number passed is a number used"""
    return "%d is a number" % char


@app.route('/number_template/<int:char>', strict_slashes=False)
def checkIntTemplate(char):
    """Show char if char is a number"""
    return render_template('5-number.html', value=char)


@app.route('/number_odd_or_even/<int:womp>', strict_slashes=False)
def modulo2(womp):
    """Define whether is odd or squad"""
    if womp % 2 == 0:
        womp = str(womp) + " is even"
    else:
        womp = str(womp) + " is odd"
    return render_template('6-number_odd_or_even.html', value=womp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
