from flask import Flask, render_template, request, url_for
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from string import Template

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

    header = '<html><head><style>table,th, td, tr{border: 1px solid black;}th {te\
    xt-align: center;background-color:#862633;color: white;padding: 15px;}td {pad\
    ding: 15px;}tr:nth-child(even){background-color:#E7C779}</style></head><body>'
    
    body = '<p>Hi, Thank you for using FinanceNole! Here are your results from you\
    r query!</p><table style ="width:100%"><tr><th><p>Category:</p></th><th><p>Amount\
    :</p></th><th><p>Average:</p></th></tr><tr><td>Gross Monthly Income:</td><td>\
    $ $gmi</td><td>$1,200 (<a target="_blank" href="http://ehow.com/info_7934153_a\
    verage-college-students-income.html">College Student</a>)</td></tr><tr><td>Re\
    nt:</td> <td>$ $rent</td> <td>$650 1 Br/Bath (<a target="_blank" href="http://\
    housing.fsu.edu">FSU Housing</a>)</td></tr> <tr> <td>Utilities:</td> <td>$ $ut\
    il</td> <td>$167.45 (<a target="_blank" href="https://numbeo.com/cost-of-livi\
    ng/city_result.jsp?country=United+States&city=Tallahassee%2C+FL">Water/Electr\
    icity/Garbage</a>)</td> </tr> <tr> <td>Transport:</td> <td>$ $transport</td> <\
    td>$15 (<a target="_blank" href="https://washingtonpost.com/news/wonk/wp/2013\
    /12/13/cars-in-the-u-s-are-more-fuel-efficient-than-ever-heres-how-it-happene\
    d/">Living within 3 mile radius</a>)</td> </tr> <tr> <td>Insurance:</td> <td>\
    $ $insurance</td> <td>$204 (<a target="_blank" href="https://coverhound.com">C\
    ollege Student Insurance</a>)</td> </tr> <tr> <td>Loans:</td> <td>$ $loans</td\
    > <td>$458.33 (<a target="_blank" href="https://petersons.com/college-search/\
    college-loan-borrowing-questions.aspx">Petersons</a>)</td> </tr> <tr> <td>Mis\
    c:</td> <td>$ $misc</td> <td>$300 (<a target="_blank" href="http://loweryoursp\
    ending.com/average-cost-for-food-per-month-for-one-person.html">Groceries</a>\
    )</td> </tr> <tr> <td>Tuition:</td> <td>$ $tuition</td> <td>$313.5 (<a target=\
    "_blank" href="http://registrar.fsu.edu/bulletin/undergrad/info/financial_inf\
    o.htm">FSU Year: $2508.00</a>)</td> </tr> <tr> <td><strong>Total Monthly Expe\
    nses:</strong></td><td>$ $total *</td> <td>$1924.5</td> </tr> <tr> <td><str\
    ong>Personal Remaining:</strong></td> <td>$ $totleft</td> <td></td> </tr> </table>'
    
    footer = '</body></html>'
    html1 = Template(header+body+footer)
    
    result = html1.safe_substitute(gmi=gmi, rent=rent, util=util, transport=transport\
    , insurance=insurance, loans=loans, misc=misc, tuition=tuition)
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Link"
    msg['From'] = 'financenole@gmail.com'
    msg['To'] = str(email)
    html = str(result)
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('financenole@gmail.com', 'GoNoles!')
    mail.sendmail('financenole@gmail.com', str(email), msg.as_string())
    mail.quit()


    return render_template('template.html', firstname=firstname, lastname=lastname, email=email,ef=ef, gmi=gmi, c401K=c401K, rent=rent, util=util, transport=transport, insurance=insurance, loans=loans, misc=misc, tuition=tuition, total=total, totleft=totleft, progress_bar=progress_bar, apr=apr)


if __name__ == '__main__':
    app.run(debug=True)
