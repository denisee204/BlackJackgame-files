g=BlackJack()

def testBlackJack(times):
    'Plays a Black Jack deck the number of times indicated using test mode.'
    scores = []
    playerscore=0
    dealerscore=0
    time = 1
    for i in range(times):
        g = BlackJack()
        g.test = True
        g.play()
        scores.append(g.scores)
        playerscore=playerscore+g.scores.player
        dealerscore=dealerscore+g.scores.dealer
        time = time+1
    return (g, scores, playerscore, dealerscore)

g.play()
