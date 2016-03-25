import random


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    success = 0.0

    for _ in range(numTrials):
        bucket = ['red', 'red', 'red', 'green', 'green', 'green']
        failed = False

        init_color = random.choice(bucket)
        bucket.remove(init_color)

        for i in range(2):
            next_pick = random.choice(bucket)
            bucket.remove(next_pick)

            if next_pick != init_color:
                failed = True
                break

        if not failed:
            success += 1

    return success / numTrials


for i in range(5):
    print noReplacementSimulation(100000)
