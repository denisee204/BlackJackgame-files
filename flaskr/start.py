from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
bp= Blueprint('start', __name__)

from . import BJGame

@bp.route('/start')
def blackJackStart():
    g.game=BJGame.BlackJack()
    images=g.game.deal2()
    pics= g.game.deal2dealer()
    if g.game.winWith2()== True:
        win2=g.game.winWith2()
        for i in images:
            print (i)
        return render_template('game/win2.html', images=images)
    elif g.game.winWith2Dealer()== True:
        win2dealer=g.game.winWith2Dealer()
        for i in images:
            print (i)
        return render_template('game/dealerwin.html', images=images)
    elif g.game.winWith2Dealer()==True:
        win2dealer=g.game.winWith2Dealer()
        for i in images:
            print(i)
        return render_template('game/dealerwin.html')
    else:
        for i in images:
            print (i)
        return render_template('game/start.html', images=images)

@bp.route('/choice', methods=(['GET']))
def choice():
    if g.game.winWith2()== False and g.game.winWith2Dealer()==False:
        g.game.playerChoice()
        if request.method == 'GET':
            hit = g.game.choice()==h
            for i in images:
                print(i)
                return render_template('game/choice.html', images=images)
    else:
        g.game.dealerStrategy()
    for i in images:
        print(i)
    return render_template('game/choice.html', images=images)
@bp.route('/stay', methods=(['GET']))
def stay():
    if g.game.winWith2()== False and g.game.winWith2Dealer()==False:
        if request.method == 'GET':
            for i in images:
                print(i)
            return render_template('game/choice.html', images=images)
