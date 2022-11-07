from flask import Flask

app = Flask(__name__)

def calculate (a, b):
    c = a+b
    return c
def divide(a, b):
    return round(a/b, 2)

def pull_request():
    print('Test Pull request')
@app.route("/")
def index():

    return "This is a payment page! Please pay %s USD"%(calculate(10, 20))

if __name__== "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)