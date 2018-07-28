from flask import Flask, render_template, jsonify


app = Flask(__name__)


@app.route('/')
def main():
    return "Hi"


if __name__ == '__main__':
    app.run()
