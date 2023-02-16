from flask import Flask, render_template
import os

# -------------------- Flask variables --------------------
app = Flask('__app__')
app.config['SECRET_KEY'] = os.environ.get('PORTFOLIO_FLASK_KEY')


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


