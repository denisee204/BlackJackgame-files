from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,
)
from werkzeug.exceptions import abort

bp= Blueprint('start', __name__)
@bp.route('/start')
def blackJackStart():
    playerhand = g.game.deal2()
    dealerhand = g.game.deal2dealer()
    images = playerhand + dealerhand
    if g.game.winWith2()== True:
        for i in images:
            print (i)
        return render_template('game/win2.html', images=images)
    elif g.game.winWith2Dealer()== True:
        win2dealer=g.game.winWith2Dealer()
        for i in images:
            print (i)
        return render_template('game/dealerwin.html', images=images)
    else:
        for i in images:
            print (i)
        return render_template('game/start.html', images=images)

@bp.route('/choice', methods=(['GET']))
def choice():
    if g.game.winWith2()== False and g.game.winWith2Dealer()==False:
        g.game.playerChoice()
        playerhit= g.game.playerChoice()
        images = playerhit
        if request.method == 'GET':
            for i in images:
                print(i)
            return render_template('game/choice.html', images=images)
    # else:
    #     g.game.dealerStrategy()
    # for i in images:
    #     print(i)
    # return render_template('game/choice.html', images=images)
@bp.route('/stand', methods=(['GET']))
def stand():
    if g.game.winWith2()== False and g.game.winWith2Dealer()==False:

        if request.method == 'GET':
            for i in images:
                print(i)
        else:
            g.game.dealerStrategy()
            return render_template('game/stand.html', images=images)
