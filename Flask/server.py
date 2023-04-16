from flask import Flask, render_template, request, redirect, url_for
import re
from main import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form1', methods=['GET', 'POST'])
def form1():
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        if not re.match(r'^\+[1-9]\d{1,14}$', phone_number) or len(phone_number) != 12:
            return render_template('form1.html', error='Invalid phone number format. Please enter a number in the format +13161234567.')
        print(phone_number)
        print(str(phone_number))
        
        with open('numbers.txt', 'w') as numbers:
            numbers.write(phone_number)
            
        return redirect(url_for('form2', phone_number=phone_number))
    return render_template('form1.html')



@app.route('/form2', methods=['GET', 'POST'])
def form2():
    oil_change = False
    coolant_change = False
    tire_alignment = False
    oil_change_date = ''
    coolant_change_date = ''
    tire_alignment_date = ''

    if request.method == 'POST':
        if 'oil_change' in request.form:
            oil_change = True
        if 'coolant_change' in request.form:
            coolant_change = True
        if 'tire_alignment' in request.form:
            tire_alignment = True
        oil_change_date = request.form.get('oil_change_date')
        coolant_change_date = request.form.get('coolant_change_date')
        tire_alignment_date = request.form.get('tire_alignment_date')
        if oil_change and not oil_change_date:
            return render_template('form2.html', error='Please enter the date of your last oil change')
        if coolant_change and not coolant_change_date:
            return render_template('form2.html', error='Please enter the date of your last coolant change')
        if tire_alignment and not tire_alignment_date:
            return render_template('form2.html', error='Please enter the date of your last tire alignment')
        
        with open('dates.txt', 'w') as dates:

                dates.write(oil_change_date + '\n')
                dates.write(coolant_change_date + '\n')
                dates.write(tire_alignment_date + '\n')
                
        main()
        return redirect('/thanks')

    return render_template('form2.html', oil_change=oil_change, coolant_change=coolant_change, tire_alignment=tire_alignment, oil_change_date=oil_change_date, coolant_change_date=coolant_change_date, tire_alignment_date=tire_alignment_date)

@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    return render_template('thanks.html')


if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    