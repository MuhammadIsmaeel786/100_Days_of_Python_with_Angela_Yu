print(''' 
                                        .-"""""-. 
                                      .'_________'. 
                                     /_/_|__|__|_\_\
                                    ;'-._       _.-';
               ,--------------------|    `-. .-'    |--------------------,
                ``""--..__    ___   ;       '       ;   ___    __..--""``
                          `"-// \\.._\             /_..// \\-"`
                             \\_//    '._       _.'    \\_//
                              `"`        ``---``        `"`
      
        ''')


print("Welcome to the game of Treasure!")
print("Your Mission is to find the Treasure")
step1 =  input("Left or Right : ")
if step1 == "left":
    step2 = input("Swim or Wait : ")
    if step2 == "wait":
        step3 = input("Which Door : ")
        if step3 == "Blue":
            print("You found the Treasure! ")
        elif step3 == "red":
            print("Burned by fire Game Over.")
        elif step3 == "Yellow":
            print("You Won the Game !!!!")
        else:
            print("Game Over!")
    else: 
        print("Attacked by trout Game Over.")
else:
   print("Fall into a hole Game Over.")
    
