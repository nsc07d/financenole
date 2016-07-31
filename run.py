from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('index.html', my_string="Wheeeee!", my_list=[0, 1, 2, 3, 4, 5])


@app.route("/login")
def user_info():
    return render_template('user_info.html')

@app.route("/tips")
def tips():
    return render_template('tips.html')


@app.route('/template', methods=['POST'])
def template():
    progress_bar = 0
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    ef = request.form['ef']
    gmi = request.form['gmi']
    c401K = request.form['c401K']
    rent = request.form['rent']
    util = request.form['util']
    if ef == u'Yes':
        progress_bar += 30
    if c401K == u'Yes':
        progress_bar += 30

    return render_template('template.html', firstname=firstname, lastname=lastname, email=email,ef=ef, gmi=gmi, c401K=c401K, rent=rent, util=util, status=progress_bar)


if __name__ == '__main__':
    app.run(debug=True)
