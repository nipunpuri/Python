#Should You Pay $250 To Play This Casino Game?
#http://fivethirtyeight.com/features/should-you-pay-250-to-play-this-casino-game/


x = numpy.random.uniform(low=0.0, high=1.0, size=None)

def game(): ##Return the number of trials untill it all adds up to 1
    n = range(100)
    y = 0
    for i in n:
        if y < 1:
            y = y + numpy.random.uniform(low=0.0, high=1.0, size=None)
        else:
            return i
            break
            
def play(k):
    n = range(k) #Playing this game 10,000 times
    x = 0
    for i in n:
        wins = 100*game()
        x = x + wins
    x = x/k
    return(x)
    
money = play(10000) - 250
    
print "Expected Payoff is $ %d" %money

        
        

    
    