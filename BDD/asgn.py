from flask import Flask, request, render_template

app = Flask(__name__)
host="localhost"
port="5000"
address="http://{0}:{1}".format(host,port)

users = {"test":"test123", "admin":"admin"}
emails = {}

def serve_forever():
    app.run(host, port)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError("Not running with Werkzeug server")
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        emailexists = emails.get(email)

        if emailexists == "yes":
            return "Fail"
        else:
           emails[email]="yes"
           return "Success"
    else:
        return render_template("signup.html")


if __name__ == '__main__':
    serve_forever()