'''
Created on Sep 11, 2015

@author: Jonathan Yu
'''

import random

def chin_cleft():
    #returns a cleft chin
    a1 = r"\_             _/"
    a2 = r"  \_         _/  "
    a3 = r"    \__/ \__/    "
    return a1 + "\n" + a2 + "\n" + a3

def chin_goatee():
    #returns a chin with a goatee
    a1 = r"\_             _/"
    a2 = r"  \_         _/  "
    a3 = r"    \__   __/    "
    a4 = r"       |||       "
    a5 = r"       |||       "
    a6 = r"       |||       "
    return a1 + "\n" + a2 + "\n" + a3 + "\n" + a4 + "\n" + a5 + "\n" + a6

def chin_tusks():
    #returns a chin with tusks
    a1 = r"\_||         ||_/"
    a2 = r"  ||         ||  "
    a3 = r"  ||\_     _/||  "
    a4 = r"  ||  \___/  ||  "
    a5 = r"  ||         ||  "
    a6 = r"  ||         ||  "
    a7 = r"  \/         \/  "
    return a1 + "\n" + a2 + "\n" + a3 + "\n" + a4 + "\n" + a5 + "\n" + a6 + "\n" + a7

def eye_dead():
    #returns dead eyes (x-ed out)
    a1 = r"    \ /   \ /    "
    a2 = r"     x     x     "
    a3 = r"    / \   / \    "
    return a1 + "\n" + a2 + "\n" + a3

def eye_lazy():
    #returns a set of eyes with one lazy eye
    a1 = r"   ___     ___   "
    a2 = r"  /   \   /   \  "
    a3 = r" |o    | |  o  | "
    a4 = r"  \___/   \___/  "
    return a1 + "\n" + a2 + "\n" + a3 + "\n" + a4

def eye_squinted():
    #returns squinted eyes
    a1 = r"   ___     ___   "
    a2 = r"  /___\   /___\  "
    a3 = r" | _o_ | | _o_ | "
    a4 = r"  \___/   \___/  "
    return a1 + "\n" + a2 + "\n" + a3 + "\n" + a4

def eye_straight():
    #returns eyes that are looking straight
    a1 = r"   ___     ___   "
    a2 = r"  /   \   /   \  "
    a3 = r" |  o  | |  o  | "
    a4 = r"  \___/   \___/  "
    return a1 + "\n" + a2 + "\n" + a3 + "\n" + a4

def hair_bald():
    #returns a bald head
    a1 = r"      _____      "
    a2 = r"   __/     \__   "
    a3 = r" _/           \_ "
    a4 = r"/               \ "
    return a1 + "\n" + a2 + "\n" + a3 + "\n" + a4

def hair_johnnybravo():
    #returns hair like Johnny Bravo's (as close as I could get it)
    a1 = r" ____            "
    a2 = r"|\\\\|           "
    a3 = r"|\\\\\|          "
    a4 = r"|\\\\\\|         "
    a5 = r"|\\\\\\\|        "
    a6 = r" |\\\\\\\|       "
    a7 = r" |\\\\\\\\|      "
    a8 = r" |\\\\\\\\\|     "
    a9 = r" |\\\\\\\\\\|    "
    a10 = r" |\\\\\\\\\\\|   "
    a11 = r" |\\\\\\\\\\\\|  "
    a12 = r" |\\\\\\\\\\\\\| "
    a13 = r"/               \ "
    return a1 + "\n" + a2 + "\n" + a3 + "\n" + a4 + "\n" + a5 + "\n" + a6 + "\n" + a7 + "\n" + a8 + "\n" + a9 + "\n" + a10 + "\n" + a11 + "\n" + a12  + "\n" +  a13

def hair_mohawk():
    #returns a mohawk
    a1 = r"      |||||      "
    a2 = r"      |||||      "
    a3 = r"    __|||||__    "
    a4 = r"  _/         \_  "
    a5 = r" /             \ "
    a6 = r"/               \ "
    return a1 + "\n" + a2 + "\n" + a3 + "\n" + a4 + "\n" + a5 + "\n" + a6

def hair_slanted():
    #returns hair that is slanted
    a1 = r"  ///////////////"
    a2 = r" /////////////// "
    a3 = r"/               \ "
    return a1 + "\n" + a2 + "\n" + a3

def hair_spiky():
    #returns spiky hair
    a1 = r" ||||||||||||||| "
    a2 = r" ||||||||||||||| "
    a3 = r"/               \ "
    return a1 + "\n" + a2 + "\n" + a3

def mouth_buckteeth():
    #returns buckteeth
    a1 = r"     _______     "
    a2 = r"      |_|_|      "
    return a1 + "\n" + a2

def mouth_horrified():
    #returns a horrified frown
    a1 = r"      _____      "
    a2 = r"     /     \     "
    a3 = r"    / _____ \    "
    a4 = r"   /_/     \_\   "
    return a1 + "\n" + a2 + "\n" + a3 + "\n" + a4

def mouth_smirk():
    #returns a smirk
    a1 = r"      ___/|      "
    a2 = r"     |____/      "
    return "\n" + a1 + "\n" + a2

def mouth_tongue():
    #returns a mouth with a tongue sticking out
    a1 = r"    _________    "
    a2 = r"   |___   ___|   "
    a3 = r"       |_|       "
    return a1 + "\n" + a2 + "\n" + a3
    
def nose_line():
    #returns a nose in the shape of a vertical line
    a1 = r"        |        "
    return a1 + "\n" + a1

def nose_small_trapezoid():
    #returns a nose in the general shape of a trapezoid
    a1 = r"        _        "
    a2 = r"       / \       "
    return a1 + "\n" + a2

def nose_snout():
    #returns a snout (just the nostrils)
    a1 = r"       o o       "
    return " \n" + a1

def nose_squidward():
    #returns a nose like Squidward's
    a1 = r"       / \       "
    a2 = r"       | |       "
    a3 = r"       | |       "
    a4 = r"       ._.       "
    return a1 + "\n" + a2 + "\n" + a3 +"\n" + a4

def totem():
    #prints a totem pole with three heads (pre-determined)
    # the first head of the totem pole
    print hair_johnnybravo()
    print eye_lazy()
    print nose_small_trapezoid()
    print mouth_smirk()
    print chin_cleft()
    print
    # the second head of the totem pole
    print hair_mohawk()
    print eye_dead()
    print nose_snout()
    print mouth_buckteeth()
    print chin_tusks()
    print
    # the third head of the totem pole
    print hair_slanted()
    print eye_squinted()
    print nose_squidward()
    print mouth_horrified()
    print chin_goatee()

def randompole():
    #prints a randomly-generated totem pole with three heads
    a = [1,2,3]
    for index in a:
        #each of the three iterations of this for loop creates one head
        #each of the three conditional statements prints the returned string of a randomly selected part function for a certain type of part (hair, eye, nose, mouth, chin)
        choice = random.randint(1,5)
        if choice == 1:
            print hair_bald()
        elif choice == 2:
            print hair_johnnybravo()
        elif choice == 3:
            print hair_mohawk()
        elif choice == 4:
            print hair_slanted()
        else:
            print hair_spiky()
        
        choice = random.randint(1,4)
        if choice == 1:
            print eye_dead()
        elif choice == 2:
            print eye_lazy()
        elif choice == 3:
            print eye_squinted()
        else:
            print eye_straight()
        
        choice = random.randint(1,5)
        if choice == 1:
            print nose_line()
        elif choice == 2:
            print nose_small_trapezoid()
        elif choice == 3:
            print nose_snout()
        elif choice == 4:
            print nose_squidward()
        #there is a chance that this conditional does not print any nose
        
        choice = random.randint(1,4)
        if choice == 1:
            print mouth_buckteeth()
        elif choice == 2:
            print mouth_horrified()
        elif choice == 3:
            print mouth_smirk()
        else:
            print mouth_tongue()
        
        choice = random.randint(1,3)
        if choice == 1:
            print chin_cleft()
        elif choice == 2:
            print chin_goatee()
        else:
            print chin_tusks()
            
        print
    
if __name__ == '__main__':
    # main function to print a totem pole with three heads followed by a random totem pole
    print "My totem pole"
    print
    totem()
    print
    print
    print "My random totem pole"
    print
    randompole()
