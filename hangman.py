import random
import time
words = ["Abjure", "Agonistic", "Airline", "Bandit", "Banquet", "Binoculars", "Biologist", "Blackboard", "Board", "Bookworm", "Butterscotch", "Camera", "Campus", "Catfish", "Carsick", "Celebrate", "Celery", "Citizen", "Coloring", "Compact", "Dark", "Damage", "Dangerous", "Decorum", "Endorse", "Engender", "Erratic", "Envelope", "Etymology", "Evewitness", "Eulogy", "Fish", "Food", "Foreclose", "Extremely", "Fact", "First", "Firstly", "Finally", "Following", "Foremost", "From", "Fundamentally", "Furthermore", "Future", "Garland", "Gigantic", "Goofy", "Government", "Grandnieces", "Handbook", "Himself", "Indulge", "Inflatable", "Inimical", "Interim", "Invest", "Jackpot", "Kitchenette", "Law", "Life", "Lifeline", "Love", "Magnificent", "Malevolence", "Man"]
choosen_word = random.choice(words)
print(choosen_word)

def main() :
    choose_word()
    guess_word()
    
def choose_word () :
    print("word is being chosen...")
    time.sleep(1)
    print("word chosen! your word has {} letters.".format(len(choosen_word)))

def guess_word() :
    remaining_chance = 10
    print("_ " * len(choosen_word))                                    
    for i in range(len(choosen_word)) :
        guessted_letter = input("please guess a letter : ")
        print("wait please...")
        time.sleep(1)
        if choosen_word[i] == guessted_letter:
            print("there is a '{}' in choosen word".format(guessted_letter))
            a = list("_" * len(choosen_word))
            a[i] = guessted_letter
            print(" ".join(a))
            print(a)
            print("your remaining chance is not decreased")
        else :
            print("there is not a {} in choosen word".format(guessted_letter))
            print("your remaining chance is decrased by one")
            remaining_chance -= 1
            if remaining_chance == 9 :
                print("________")                           
                print("_ " * len(choosen_word))  
            elif remaining_chance == 8 :
                print("|\n|\n|\n|\n|\n|\n|\n|\n|\n|")
                print("|________" )   
                print("_ " * len(choosen_word))                                      
            elif remaining_chance == 7 :
                print("______________")
                print("|\n|\n|\n|\n|\n|\n|\n|\n|\n|")        
                print("|________")
                print("_ " * len(choosen_word))                                         
            elif remaining_chance == 6 :
                print("______________")
                print("|            |\n|            |\n|\n|\n|\n|\n|\n|\n|\n|")        
                print("|________")
                print("_ " * len(choosen_word)) 
            elif remaining_chance == 5 :
                print("______________")
                print("|            |\n|            |\n|            ◯\n|\n|\n|\n|\n|\n|\n|")        
                print("|________")      
                print("_ " * len(choosen_word)) 
            elif remaining_chance == 4 :
                print("______________")
                print("|            |\n|            |\n|            ◯\n|            |\n|            |\n|\n|\n|\n|\n|")        
                print("|________")
                print("_ " * len(choosen_word))             
            elif remaining_chance == 3 :
                print("______________")
                print("|            |\n|            |\n|            ◯\n|            |\n|            |\n|           /\n|          /\n|\n|\n|\n|")        
                print("|________")
                print("_ " * len(choosen_word))                                                     
            elif remaining_chance == 2 :
                print("______________")
                print("|            |\n|            |\n|            ◯\n|            |\n|            |\n|           / |\n|          /  |\n|\n|\n|\n|")        
                print("|________")
                print("_ " * len(choosen_word))  
            elif remaining_chance == 1 :
                print("______________")
                print("|            |\n|            |\n|            ◯\n|           /|\n|            |\n|           / |\n|          /  |\n|\n|\n|\n|")        
                print("|________")
                print("_ " * len(choosen_word))                                            
            elif remaining_chance == 0 :
                print("______________")
                print("|            |\n|            |\n|            ◯\n|           /|¯\n|            |\n|           / |\n|          /  |\n|\n|\n|\n|")        
                print("|________")
                print("_ " * len(choosen_word))    
                print("you lost")   

main()
