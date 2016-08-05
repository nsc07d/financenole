from flask import Flask, render_template, request, url_for
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

app = Flask(__name__)

"""Home page where the website welcomes the user
along with an area below to provide contact information """
@app.route("/")
def template_test():
    return render_template('index.html')

"""login page where user inputs all the necessary information 
needed to return back the results. 'user_info.html' has the
resources needed to store all user inputs for the results 
page"""
@app.route("/login")
def user_info():
    return render_template('user_info.html')
    
"""General tips page where the user can inform themself
of money-saving tips. 'tips.html' has stored inside all 
this information regarding tips""" 
@app.route("/tips")
def tips():
    return render_template('tips.html')

"""All these variables are storing the info
inside the request forms to calculate total
expenses along with the amount left available.
apr,emf, and c401k will all affect the progress 
bar and it's completion. Concerning the e-mail 
delivery, the sections 'From'/'To'/'Subject' 
are all filled in respectively from the website
email along with the results to the e-mail the
user has provided. It logs onto gmail server and sends
email to the user with the table generated with
their respective information. Lastly, it renders 
the template with all the information needed to 
generate the table to display on the website and 
e-mail provided."""
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
    apr = request.form['apr']
    
    util = request.form['util']
    transport = request.form["transport"]
    insurance = request.form["insurance"]
    loans = request.form["loans"]
    misc = request.form["misc"]
    tuition = request.form["tuition"]
    try:
        total = int(rent)+int(util)+int(transport)+int(insurance)+int(loans)+int(misc)+int(tuition)
        totleft = float(gmi) - int(total)
    except:
        total = 0
        totleft = 0
        
    
    if apr > 7:
        progress_bar +=5
    elif apr > 5:
        progress_bar += 7
    elif apr >= 2:
        progress_bar += 10
    util = request.form['util']
    if ef == u'Yes':
        progress_bar += 40
    if c401K == u'Yes':
        progress_bar += 40
    if c401K == u'Yes' and ef == u'Yes' and apr < '4':
        progress_bar = (progress_bar - 10) + 20

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


    return render_template('template.html', firstname=firstname, lastname=lastname, email=email,ef=ef, gmi=gmi, c401K=c401K, rent=rent, util=util, transport=transport, insurance=insurance, loans=loans, misc=misc, tuition=tuition, total=total, totleft=totleft, progress_bar=progress_bar, apr=apr)


if __name__ == '__main__':
    app.run(debug=True)
