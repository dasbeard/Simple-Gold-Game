from flask import Flask, redirect, render_template, request, session
from random import randrange
from datetime import datetime
app=Flask(__name__)
app.secret_key="itsAsecret"


def addGoldActivity(num, action, place):
    time = datetime.now()
    if place == 'farm':
        session['activity'].append(['add', 'Earned {} gold from the {}! ({})'.format(num, place, time)])
        # print session['activity']
    elif place == 'caves':
        session['activity'].append(['add', 'Earned {} gold from the {}! ({})'.format(num, place, time)])
    elif place == 'house':
        session['activity'].append(['add', 'Earned {} gold from the {}! ({})'.format(num, place, time)])
    elif place == 'casino':
        if action == 'earned':
            earned = 'Earned {} gold from the {}! ({})'.format(num, place, time)
            session['activity'].append(['add', earned])
        elif action == 'lost':
            loss = 'Lost {} gold in the {}... ouch ({})'.format(num, place, time)
            session['activity'].append(['loss', loss])
        else:
            print 'error'
    else:
        print 'error'

        print session
@app.route('/')
def index():
    if 'myGold' not in session:
        session['myGold']=0
    if 'activity' not in session:
        session['activity']=[]


    return render_template('index.html', activities=session['activity'], gold=session['myGold'])
                                                    # , log=log

@app.route('/process_money', methods=['POST'])
def process_money():

    if request.form['action'] == 'farm':
        gold = randrange(10,21)
        session['myGold'] += gold
        addGoldActivity(gold, 'earned', 'farm')

    elif request.form['action'] == 'caves':
        gold = randrange(5,11)
        session['myGold'] += gold
        addGoldActivity(gold, 'earned', 'caves')


    elif request.form['action'] == 'house':
        gold = randrange(2,6)
        session['myGold'] += gold
        addGoldActivity(gold, 'earned', 'house')


    elif request.form['action'] == 'casino':
        gold = randrange(-50,51)
        session['myGold'] += gold
        if int(gold)>0:
            addGoldActivity(gold, 'earned', 'casino')
        else:
            addGoldActivity(gold, 'lost', 'casino')

    # print time, gold
    return redirect ('/')


@app.route('/reset', methods=['POST'])
def reset():
    session['myGold']=0
    session['activity'] = []

    return redirect('/')




app.run(debug=True)
