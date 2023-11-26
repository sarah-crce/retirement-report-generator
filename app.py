from flask import Flask, redirect, request, render_template, send_file, send_from_directory, url_for
import report

app = Flask(__name__)

@app.route('/')
def take_input():
    return render_template('index.html')


@app.route('/gen_report',methods=['POST','GET'])
def gen_report():
    if request.method=='POST':
        name=str((request.form['name']))
        age=int((request.form['age']))
        retirementAge = int((request.form['retirementAge']))
        savings = int((request.form['savings']))
        income = int((request.form['income']))
        livingExpenses = int((request.form['livingExpenses']))
        healthcareExpenses = int((request.form['healthcareExpenses']))
        miscellaneousExpenses = int((request.form['miscellaneousExpenses']))
        lifeSpan = 80
        report.exp.expense_projector(name, age, retirementAge, lifeSpan, savings, income, livingExpenses, healthcareExpenses, miscellaneousExpenses)
        report.create_pdf(name, age, retirementAge, lifeSpan, savings, income, livingExpenses, healthcareExpenses, miscellaneousExpenses)
        return redirect(url_for('result_page'))
    
@app.route('/result_page')
def result_page():
    return render_template('report.html')
    
@app.route('/output_report.pdf')
def download_report():
    return send_file('static/output_report.pdf', as_attachment=True)