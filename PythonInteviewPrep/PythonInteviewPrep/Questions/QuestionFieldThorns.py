'''
Question - Field of Thorns
input:
1) initial velocity
2) start point
3) 1D boolean array representing a field of thorns - 0 is clear, 1 - is a thorn

output:
can u throw a ball from the start point so it'll land:
1) inside the field
2) not on a thorn
3) when the ball velocity reaches 0

how does the ball move?
after the ball hits the ground it can:
1) continue with the same speed
2) raise speed by 1
3) lower speed by 1
'''

#---------------- solutions beyond this point --------------------
# question type - iteration with multiple choise


# assumptions that were not part of the question
# assumption group A
# velocity is not real velocity, it indicates how many cells in the array will the ball traverse
# all possible ball movements are legal, only a solution with any legal movements is required
# if ball reaches velocity 0 it cannot change anymore
# ball landing on thorn while velocity is not 0 - game over

# solution 1 - recursive - A
def CanBallLandSafely1ARecursive(Velocity, StartIndex, FieldOfThorns):
    # we passed end of field with last throw - fail
    if StartIndex + Velocity > len(FieldOfThorns):
        return False
    # we landed on a thorn with last throw - fail
    elif FieldOfThorns[StartIndex + Velocity]:
        return False
    # not failed yet
    else:
        # we landed on a clear space with speed 0 - pass
        if Velocity == 0:
            return True
        # we landed on a clear space but we still have velocity - continue
        else:
            OptionSame = CanBallLandSafely1ARecursive(Velocity, StartIndex + Velocity, FieldOfThorns)
            OptionIncrease = CanBallLandSafely1ARecursive(Velocity + 1, StartIndex + Velocity, FieldOfThorns)
            OptionDecrease = CanBallLandSafely1ARecursive(Velocity - 1, StartIndex + Velocity, FieldOfThorns)
            return OptionIncrease or OptionSame or OptionDecrease




# solution 2 - stack and while - A - UNSOLVED
def CanBallLandSafely2AStackWhile(Velocity, StartIndex, FieldOfThorns):
    ChoiseStack = [-1]
    PassedField = StartIndex + Velocity > len(FieldOfThorns)
    HitThorn = FieldOfThorns[StartIndex + Velocity]
    BallStopped = Velocity == 0
    GameOver = PassedField or HitThorn or BallStopped
    NewStart = StartIndex + Velocity
    NewVelocity = Velocity - 1
    while not GameOver:
        StartIndex = StartIndex + Velocity
        # take tha last choise made
        CurrentChoise = ChoiseStack[len(ChoiseStack) - 1]
        # find new start point with 
        PassedField = StartIndex + Velocity > len(FieldOfThorns)
        HitThorn = FieldOfThorns[StartIndex + Velocity]
        BallStopped = Velocity == 0
        GameOver = PassedField or HitThorn or BallStopped
    return BallStopped and not HitThorn and not PassedField

