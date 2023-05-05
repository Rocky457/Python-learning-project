print("...Welcome to our Quiz game...")

playing = input("DO YOU WANT TO PLAY yes or no? ")
if playing.lower() != 'yes':
    quit()
print('ok lets play...')
score = 0
anwser = input(' 5 + 6  =')
if anwser == '11':
    print('correct')
    score += 1
else:
    print('INCORRECT!')
anwser = input(' 11 + 10 =')
if anwser == '22':
    print('correct')
    score += 1
else:
    print('INCORRECT!')
anwser = input(' 10 * 12 =')
if anwser == '120':
    print('correct')
    score += 1
else:
    print('INCORRECT!')
anwser = input(' 5 * 5  =')
if anwser == '25':
    print('correct')
    score += 1
else:
    print('INCORRECT!')

print(f' You got {score} of 4 questions right for {str((score/4)*100)} %')
