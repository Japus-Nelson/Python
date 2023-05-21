def minion_game(string):
    # your code goes here
    vowels = "aeiou".upper()
    # print(len(string))
    # # kevin = sum([len(string) - i for i in range(len(string)) if string[i] in vowels  ])
    # stuart = len(string) * (len(string) + 1/ 2) - Kevin
    # li = []
    # for i in range(len(string)):
    #     if string[i] in vowels:
    #         li.append(li)   # or li.append(len(string - i))
    # if Kevin == Stuart:
    #     print("Draw")
    # elif Stuart > Kevin:
    #     print("%s %s" % ("Stuart", Stuart))
    # else:
    #     print("%s %s" % ("Kevin", Kevin))

    scores = {'Kevin' : 0 , 'Stuart' : 0 }
    for i in range(len(string)):
        if string[i] in vowels:
            scores['Kevin'] += sum([len(string) - i])
        else:
            scores['Stuart'] += sum([len(string) - i])


    if scores['Kevin'] == scores['Stuart']:
        print("Draw")
    elif scores["Stuart"] > scores["Kevin"]:
        print("%s %s" % ("Stuart", scores["Stuart"]))
    else:
        print("%s %s" % ("Kevin", scores["Kevin"]))


if __name__ == '__main__':
    s = input()
    minion_game(s)


'''
Question

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

banana.png

Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Constraints



Sample Input

BANANA
Sample Output

Stuart 12'''