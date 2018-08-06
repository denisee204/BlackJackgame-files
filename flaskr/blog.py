from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,session
)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
from BJGame import BlackJack
bp= Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html')

@bp.route('/game')
def game():
    g.game= BlackJack()
    playerhand = g.game.deal2()
    dealerhand = g.game.deal2dealer()
    playerhand = g.game.player
    dealerhand = g.game.dealer
    images = playerhand + dealerhand
    # print('player hand is:'+str(playerhand))
    session["playerhand"]= playerhand
    session["dealerhand"]= dealerhand
    session["deck"]=g.game.deck
    session["player"]=g.game.scores.player
    session["dealer"]=g.game.scores.dealer
    if g.game.winWith2()== True:
        stringimages=handToString(images)
        print('stringimages from winWith2'+ str(stringimages))
        return render_template('blog/win2.html', images=stringimages)
    elif g.game.winWith2Dealer()== True:
        win2dealer=g.game.winWith2Dealer()
        stringimages= handToString(images)
        print('stringimages from winWith2dealer'+ str(stringimages))
        return render_template('blog/dealerwin.html', images=stringimages)
    else:
        g.game.playerhand= session["playerhand"]
        images= g.game.playerhand
        if request.method == 'GET':
            stringimages= handToString(images)
            print('stringimages from index'+ str(stringimages))
        return render_template('blog/game.html', images=stringimages)

def handToString(images):
    ranks= {1:'Ace',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Jack',12:'Queen',13:'King'}
    g.game.playerhand= session["playerhand"]
    stringimages=[]
    for i in range(len(images)):
        if (images[i][1]==0):
            suit='Heart_'
        elif (images[i][1]==1):
            suit='Diamond_'
        elif (images[i][1]==2):
            suit='Spade_'
        elif (images[i][1]==3):
            suit='Club_'
        rank=ranks[images[i][0]]
        stringimages.append(suit + rank +'_RA.gif')
        #stringimages.append('Heart_'+'Seven'+'_RA.gif')
    return stringimages

@bp.route('/blog/dealer')
def dealer():
    g.game= BlackJack()
    g.game.player= session["playerhand"]
    g.game.dealer= session["dealerhand"]
    g.game.deck= session ["deck"]
    g.game.scores.player= session["player"]
    g.game.scores.dealer= session["dealer"]
    g.game.dealerStrategy()
    g.game.whoWon()
    status= g.game.status
    pimages= g.game.player
    dimages=g.game.dealer
    print("printing pimages, dimages", pimages, dimages)
    if request.method == 'GET':
        pstringimages= handToString(pimages)
        print(pstringimages)
        dstringimages= handToString(dimages)
        print(dstringimages)
        stringimages= [pstringimages , dstringimages]
        print ('printing stringimages', stringimages)
        if status == BlackJack.playerWon:
            session["player"] = session["player"]+1
            return render_template('/blog/playerWon.html', images=stringimages)
        if status == BlackJack.dealerWon:
            session["dealer"] = session["dealer"]+1
            return render_template('/blog/dealerWon.html', images=stringimages)
        if status == BlackJack.tie:
            return render_template('/blog/tie.html', images=stringimages)
        if status == BlackJack.endGame:
            return render_template('/blog/Quit.html')


@bp.route('/blog/choice')
def choice():
    g.game=BlackJack()
    g.game.deck=session["deck"]
    g.game.dealer=session["dealerhand"]
    g.game.player=session["playerhand"]
    if g.game.winWith2()== False and g.game.winWith2Dealer()==False:
        g.game.playerhand= session["playerhand"]
        images=g.game.playerChoice()
        images= g.game.playerhand
        g.game.playerhand= images
        session["playerhand"]= g.game.playerhand
        print(images)
        stringimages=[]
        if request.method == 'GET':
            stringimages= handToString(images)

            print('stringimages from playerChoice'+ str(stringimages))

            return render_template('blog/choice.html', images=stringimages)

@bp.route('/blog/New', methods=('GET', 'POST'))
def newHand():
    g.game= BlackJack()
    g.game.deck=session["deck"]
    g.game.scores.player=session["player"]
    g.game.scores.dealer=session["dealer"]
    playerhand = g.game.deal2()
    dealerhand = g.game.deal2dealer()
    playerhand = g.game.player
    dealerhand = g.game.dealer
    images = playerhand + dealerhand
    # print('player hand is:'+str(playerhand))
    session["playerhand"]= playerhand
    session["dealerhand"]= dealerhand

    if g.game.winWith2()== True:
        stringimages=handToString(images)
        print('stringimages from winWith2'+ str(stringimages))
        return render_template('blog/win2.html', images=stringimages)
    elif g.game.winWith2Dealer()== True:
        win2dealer=g.game.winWith2Dealer()
        stringimages= handToString(images)
        print('stringimages from winWith2dealer'+ str(stringimages))
        return render_template('blog/dealerwin.html', images=stringimages)
    else:
        g.game.playerhand= session["playerhand"]
        images= g.game.playerhand
        if request.method == 'GET':
            stringimages= handToString(images)
            print('stringimages from index'+ str(stringimages))
        return render_template('blog/newHand.html', images=stringimages)



@bp.route('/blog/stand', methods=('GET', 'POST'))
def stand():
    ranks= {1:'Ace',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Jack',12:'Queen',13:'King'}
    g.game= BlackJack()
    g.game.playerhand= session["playerhand"]
    images= g.game.playerhand
    print(images)
    if g.game.winWith2()== False and g.game.winWith2Dealer()==False:
        if request.method == 'GET':
            stringimages= handToString(images)
            print(stringimages)
        return render_template('/blog/stand.html', images=stringimages)

@bp.route('/blog/Quit.html')
def Quit():
    #put tom's db code Here
    return render_template('/auth/')
