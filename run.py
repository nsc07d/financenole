from flask import Flask, render_template, request, url_for
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('index.html')


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
        progress_bar += 37
    if c401K == u'Yes':
        progress_bar += 37
        
    msg = MIMEMultipart()
    msg['From'] = 'financenole@gmail.com'
    msg['To'] = str(email)
    msg['Subject'] = 'FSU FinanceNole'
    message = 'here is the email'
    msg.attach(MIMEText(message))
    
    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login('financenole@gmail.com', 'GoNoles!')
    
    mailserver.sendmail('financenole@gmail.com', str(email), msg.as_string())
    
    mailserver.quit()

    return render_template('template.html', firstname=firstname, lastname=lastname, email=email,ef=ef, gmi=gmi, c401K=c401K, rent=rent, util=util, progress_bar=progress_bar)


if __name__ == '__main__':
    app.run(debug=True)
