from flask import Flask, render_template, request, abort
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/user/<name>')
@app.route('/user/')
def user(name=None):
    if name in None:
        name = request.args.get('name')
    if name:
        return render_template('hello.html', hame=name)
    else:
        abort(404)



if __name__ == '__main__':
    app.run(debug=True)