from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def new_item():
    return render_template('new_item.html')


if __name__ == '__main__':
    app.run(debug=True)