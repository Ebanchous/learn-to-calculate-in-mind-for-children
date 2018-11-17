# question function

def function (x1, x2, action, actions):
    import random
    import operator
    answer = actions.get(action)(x1,x2)
    print('\nWhat is the result \n\n {} \n{} \n {}\n'.format(x1, action, x2))
    return answer

# guess function

def askQuestion(x1, x2, action, actions):
    answer = function(x1, x2, action, actions)
    try:
        guess = float(input(" "))
    except ValueError:
        print("\nOnly numbers to be entered!\n")
    else:
        return guess == answer

# Main function

def quiz():
    print('Hello. Please answer 10 questions\n')
    import random
    import operator
    actions = {'+':operator.add,'-':operator.sub}
    score = 0
    for i in range(10):
        x2 = random.randint(0,1000)
        x1 = random.randint(x2,1000)
        action = random.choice(list(actions.keys()))
        repeat = True
        while repeat:
            correct = askQuestion(x1, x2, action, actions)
            if correct:
                score += 1
                print('\nWell done!\nCorrect answer!\n')
                repeat = False
            else:
                print('\nWrong answer, Try once more!\n')       
    return 'You have answered correctly {}/10'.format(score)

# Start
quiz()