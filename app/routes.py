import requests
from app import app
from app.forms import LoginForm, CurrencyForm
from flask import render_template, flash, redirect

@app.route('/')
@app.route('/index')
def index():
    url = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0"
    r = requests.get(url)
    rez = r.json()
    posts = {}
    for i in rez:
        posts[i['Cur_Abbreviation']] = i['Cur_OfficialRate']
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/convert', methods=['GET', 'POST'])
def convert():

    def convert_currency(_from, _to, user_value):
        url = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0"
        r = requests.get(url)
        rez = r.json()
        currencies = {}
        for i in rez:
            currencies[i['Cur_Abbreviation']] = i['Cur_OfficialRate']
        ammount = float(user_value)
        if _from == 'BYN':
            currencies[_from] = 1
        if _to == 'BYN':
            conversion = ammount * currencies[_from]
        else:
            rate = currencies[_from] / currencies[_to]
            conversion = ammount * rate
        return " {0} {1} is equal to {2} {3}.".format(user_value, _from, "{0:.4f}".format(conversion), _to)

    def logic():
        form = CurrencyForm()
        if form.validate_on_submit():
            flash('VALUE: {}'.format(form.currency_count.data))
            flash(convert_currency(form.currency_from.data, form.currency_to.data, form.currency_count.data))
            return redirect('/index')
        return render_template('converter.html', title='Converter', form=form)

    return logic()