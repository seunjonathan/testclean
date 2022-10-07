from flask import Flask, render_template, request, flash, redirect, url_for, session, logging

app = Flask(__name__)


#Home
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')





if __name__ == '__main__':    #saying if this flie was selected to run, execute whats below, but if it was ref as a library, dont run
    app.secret_key='secret123'
    app.run(debug=True)