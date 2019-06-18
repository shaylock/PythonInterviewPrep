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
# question type - iteration with multiple choise - maze question with no loops


# assumptions that were not part of the question
# assumption group A
# velocity is not real velocity, it indicates how many cells in the array will the ball traverse
# all possible ball movements are legal, only a solution with any legal movements is required
# if ball reaches velocity 0 it cannot change anymore
# ball landing on thorn while velocity is not 0 - game over

# solution 1 - recursive - A
def CanBallLandSafely1ARecursive(Velocity, StartIndex, FieldOfThorns):
    # we passed end of field with last throw - fail
    if StartIndex + Velocity >= len(FieldOfThorns):
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
    ChoiseStack = [-2]
    PassedField = StartIndex + Velocity >= len(FieldOfThorns)
    HitThorn = FieldOfThorns[StartIndex + Velocity]
    GameFail = PassedField or HitThorn
    if (Velocity == 0) and not GameFail:
        return True
    StartIndex += Velocity
    while ChoiseStack: # and not GameFail:
        # progress last choise to next choise
        ChoiseStack[-1] += 1
        # check the top of the stack
        CurrentChoise = ChoiseStack[-1]
        # check how this choise affects the status
        PassedField = StartIndex + Velocity + CurrentChoise >= len(FieldOfThorns)
        HitThorn = FieldOfThorns[StartIndex + Velocity + CurrentChoise] if not PassedField else HitThorn
        GameFail = PassedField or HitThorn
        # last choise was bad and needs to be replaced
        if GameFail:
            # last choise cannot be promoted
            if ChoiseStack[-1] == 1:
                # entire branch must be deleted
                del ChoiseStack[-1]
                # revert changes made in this branch
                if ChoiseStack:
                    StartIndex -= Velocity
                    Velocity -= ChoiseStack[-1]
            # last choise can still be promoted - will be handled in the next iteration
            else:
                pass
        # last choise was good so far
        else:
            # check if reached 0 velocity
            if Velocity == 0:
                return True
            # choise is legal and we need to apply a new choise
            else:
                # append a new element to the stack
                ChoiseStack.append(-2)
                # set start and velocity to portray the last good choise
                Velocity += CurrentChoise
                StartIndex += Velocity
    return False
#BallStopped and not HitThorn and not PassedField

# test cases
test1 = [0, 1, 1, 0, 1, 0, 1, 1, 1] # start 0 velocity 4 pass
test2 = [0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0] # start 0 velocity 4 pass
print(CanBallLandSafely1ARecursive(4, 0, test1))
print(CanBallLandSafely2AStackWhile(4, 0, test1))
print(CanBallLandSafely1ARecursive(4, 0, test2))
print(CanBallLandSafely2AStackWhile(4, 0, test2))