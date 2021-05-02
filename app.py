from flask import Flask
app = Flask(__name__)


@app.route('/')
def main():
    return "Welcome to TechCraft Assignment"

@app.route('/<name>')
def main(name):
    return "Hello" + " " + name


if __name__ == '__main__':
    app.run()
