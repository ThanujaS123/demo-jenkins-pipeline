# print("Hello Jenkins")
# print("Version 2.0")
# print("New line added for development branch")
# print("This line is added to test Jenkins pipeline3")


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Jenkins Pipeline"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)