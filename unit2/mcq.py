import time

def game():
    print("Thorndike's 'Law of Effect' states that:\n"
          "a) Any behaviour that is followed by pleasant consequences is likely to be repeated, and any behaviour followed by unpleasant consequences is likely to be stopped\n"
          "b) Any behaviour that is followed by unpleasant consequences is likely to be repeated, and any behaviour followed by pleasant consequences is likely to be stopped\n"
          "c) A highly preferred activity can be used effectively as a reinforcer for a less preferred activity\n"
          "d) Reinforcement can be used to build up desired complex behaviours\n")

    answer = input("What is your answer? ")
    return answer

# first round!
answer = game()

# feeedback
if answer == "a":
    print("Ding ding ding, that's correct!")
else:
    print("Not quite, try again!\n")
    time.sleep(1)
    # retry
    answer = game()
