import Questions #import the dictionary of questions
import Hackathon #import the sets of music recomendations
import random
from matplotlib import pyplot as plt
import numpy as np

dict = Questions.Q

mood = 0 #temporary variable to represent user input
calm = dark = energ = joy = sorrow = 0 #variables corresponding to each mood type within the moods[] list
moods = [calm,dark,energ,joy,sorrow] #each index of the list corresponds to the specific mood

def questions():
    print("\n****~~~~~~~~~For the following questions, please answer with the corresponding number!~~~~~~~~***\n")
    for ques in dict: #iterate thru the questions aka keys in the question dictionary
        print(ques) #print out the question for the user to read
        print("\nYour Answer [1 thru 5]: ")
        mood = (input()) #take the user input
        dict[ques] = mood #set value within dictionary
        if mood == "1": #update count of each mood variable depending on user input
            moods[0] += 1
        elif(mood == "2"):
            moods[1] += 1
        elif(mood == "3"):
            moods[2] += 1
        elif(mood == "4"):
            moods[3] += 1
        elif(mood == "5"):
            moods[4] += 1
        else:
            print("\nThis is not a valid mood\n")

def maxIndex(moods): #return the index of the max mood variable
    index = (moods.index(max(moods)))
    return index

def getSongList(One,Two,cat): #Get the list of songs based on the two highest mood scores and the genre of music selected
    inter = []
    if cat == 1:
        masterList = Hackathon.classical
    elif cat == 2:
        masterList = Hackathon.popRetro
    else:
        masterList = Hackathon.popToday

    if(Two != 0): #First look for intersections between the two highest mood scores
        for x in range(len(masterList[One])):
            for y in range(len(masterList[Two])):
                if masterList[One][x].upper() == masterList[Two][y].upper():
                    inter.append(masterList[Two][y])

    if len(inter) == 0 or Two == 0: #If no intersection, then return the list of songs within the highest mood category
        for z in range(len(masterList[One])):
            inter.append(masterList[One][z])

    return inter


def main():
    print("\nPlease enter the type of music you'd like chosen for yourself!\n\n1 = Classical \n2 = Retro Pop \n3 = Recent Pop\n\nYour Answer [1 thru 3]: ")
    category = int(input())

    questions()

    GoldMood = maxIndex(moods) #Get the index of the largest mood variable
    popped = moods[GoldMood]
    moods.pop(GoldMood) #Set the largest back to zero
    SilverMood = maxIndex(moods) #Get the index of the second largest mood variable
    if SilverMood > 0:
        SilverMood +=1
    moods.insert(GoldMood,popped) #Insert back the highest mood score
    songList = getSongList(GoldMood, SilverMood,category) #Get the list of song matches based on your mood scores and category
    print("Our recomendation!:\n")
    ran = random.randint(0,len(songList)-1)
    print(songList[ran]) #Print out a random song from songList

    print("\nWould you like more suggestions? (Y/N)\n")

    yesoryes = str(input()).upper()
    if yesoryes == 'Y': #Print out the entire list of song matches if they desire so
        if len(songList) == 1:
            print("There aren't anymore songs like that one!\n")
        else:
            print("\nHere are the all of your matches!\n")
            for z in range(len(songList)):
                print("[" + str(z+1) + "]: " + str(songList[z]) + "\n")

    #Print out graphical representation of the mood scores
    a = np.array(moods)
    x = np.arange(5)
    fig, ax = plt.subplots()
    plt.bar(x,moods)
    plt.xticks(x, ("Calm", "Dark", "Energetic", "Joyful", "Sorrowful"))
    plt.show()

main()
