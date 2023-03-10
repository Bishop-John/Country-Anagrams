import random
score = 0
allCountries = []
with open('Countries.txt', 'r') as file:
    lines = file.readlines()

for i in range(len(lines)):
    allCountries.append(lines[i][:-1])

playing = True
while playing == True:
    currentWord = random.choice(allCountries)
    wordToShuffle = list(currentWord)
    random.shuffle(wordToShuffle)
    shuffledWord = ''.join(wordToShuffle)

    print ("Guess this country -", shuffledWord)

    guess = input("Your answer - ").upper()
    if guess != currentWord:
        print ("That was incorrect, the answer was -", currentWord)
        playing = False
    if guess == currentWord:
        print ("Well done!!!", len(currentWord), "points!")
        score += len(currentWord)

print ("---GAME OVER---")
print ("Your final score was", score)
