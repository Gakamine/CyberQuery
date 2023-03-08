from flask import Flask, render_template, request
from src import core

app = Flask(__name__)


@app.route('/')
def main():
    query = request.args.get('q')
    if query:
        result = core.search(query)
        return render_template('index.html', result=result)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)