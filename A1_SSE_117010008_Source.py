import random    #import random to choose numbers from list randomly

number_list_four = []      #new list to store all numbers (4 digits)
number_list_three = []     #new list to store all numbers (3 digits)
correct_list = []
exact_list = []
numb_list = []       #list to store history numbers
numlist = []         # store the tested numbers
usernumber = 0
correct = 0      # numbers of correct values
exact = 0        # numbers in exact positions
counter = 0      #count how many rounds the game runs


#create the list for four digits
def list_four():
    for i in range(1,10):
        for o in range(10):
            for p in range(10):
                for q in range(10):
                    if i!= o and i!= p and i!= q and o!= p and o!= q and p != q:
                        number_list_four.append((i,o,p,q))
    return number_list_four

    
#create the list for three digits  
def list_three():
    for i in range(10):
        for o in range(10):
            for p in range(10):
                if i != o and i != p and o != p:
                    number_list_three.append((i,o,p))
    return number_list_three 

# input digit
def list_create():
    global number_list
    while True:
        digit_remember = input('choose numbers of how many digits 3 or 4 >>>')
        if digit_remember.isdigit():
            digit_remember = int(digit_remember)
            if digit_remember == 3:
                number_list = list_three()
                break
            elif digit_remember ==4:
                number_list = list_four()
                break
            else: 
                print('plz input only 3 or 4 ')
                continue
        else:
            print('wrong input. digit only')
            continue
    return digit_remember

#get the number user is thinking
def inputnumber(digit_value):
    repeat_number = 0
    user_number_list = []
    while True:
        try:
            usernumber = int(input('input the number you what the computer to guess >>>'))
            usernumber = str(usernumber)
            if usernumber.isdigit() == True:
                for i in usernumber:
                    user_number_list.append(i)
                for i in user_number_list:
                    if user_number_list.count(i) > 1:
                        repeat_number = 1
                if repeat_number == 1 :
                    print('the number you input must be numbers without repeated digits.')
                    user_number_list = []
                    repeat_number = 0
                    continue
                elif len(usernumber) == digit_value:
                    break
                elif len(usernumber) != digit_value:
                    print('check the digit of your input again.')
                    user_number_list = []
                    continue
                else: 
                    break
            else:
                print('plz enter a number #')
        except ValueError:
            print('plz enter a number #.')
            continue	

    #the number of correct value and exact position
def user_inter(digit_value):
    while True:
        correct = input('how many correct nunbers (x to quit) ? >>>')
        try:
            if correct == 'x' :
                print('thanks for playing, quitting the program')
                input('press any button to quit now')
                quit()
            else:
                correct = int(correct)
                correct_list.append(correct)
                if correct > digit_value :
                    print('wrong input, plz check again #')
                    continue
                else: break
        except ValueError:
            print('plz input a number #')
            continue
    while True:
        exact = input('how many in exact positions (x to quit) ? >>>')
        try:    
            if correct == 0:
                print('the exact number then must be zero')
                exact =0
                break
            elif exact == 'x':
                print('thanks for playing, quitting the program')
                input('press any button to quit now')
                quit()
            else:
                exact = int(exact)
                exact_list.append(exact)
                if exact > correct:
                    print('wrong input, plz check again #')
                    continue
                else: break
        except ValueError:
            print('plz input a number #')
            continue 
    return correct , exact


#find numbers from the original list
def pick_numbers_find(find,finder,correct_num,exact_num):
    correct_n = 0           #correct digit counter
    exact_n = 0           #exact digit counter
    for x in find:
        if x in finder:
            correct_n += 1
    for i in range(len(finder)):
        if finder[i] == find[i]:
            exact_n += 1
    if correct_num == correct_n and exact_num == exact_n:
        return True
    else:
        return False



# main program
def start_game():
    global number_list
    starter = input('''Input Y to start game(only capital Y), N to quit game(capital N conly) ,help for more information >>>''')
    if starter == 'help':
        print('''Choose a 3 or 4 digits number and input the number you would like
        to let the computer to guess. You shall tell the computer how many correct
        values of numbers and how many digits at exact places. ****the number you 
        choose cannot have repeated digits****''')
        starter = input('Play the game? Y/N >>>')
    if starter == 'N':
        print('thanks for using the program, byebye')
        quit()
    if starter == 'Y':
        counter = 0
        digit_value = list_create()
        inputnumber(digit_value)
        while True:
            numlist = []
            try:
                radnum = random.choice(number_list)
                if digit_value == 4:
                    for i in radnum:
                        aaa = radnum[0]*1000
                        bbb = radnum[1]*100
                        ccc = radnum[2]*10
                        ddd = radnum[3]
                        numb_b = aaa+bbb+ccc+ddd
                    numb_list.append(numb_b)
                else:
                    for i in radnum:
                        aaa = radnum[0]*100
                        bbb = radnum[1]*10
                        ccc = radnum[2]
                        numb_b = aaa+bbb+ccc
                    numb_list.append(numb_b)
            except:
                print('cannot guess the number. the correct and exact input must be wrong')
                while True:
                    again = input('want to play again ? input anything to play again or input quit to QUIT')
                    while again != 'quit':
                        start_game()
                    else:
                        print('thanks for playing !')
                        quit()
            counter += 1
            for i in range(counter):
                if i== 0:
                    numb_list.append(numb_b)
                else:
                    print()
                    print('the ', i ,'/ 10 time of guessing')
                    print(numb_list[i] , 'correct >', correct_list[i-1] ,'exact >', exact_list[i-1])
            print('the ',counter,'/ 10 time of guessing')
            for i in radnum:
                print(str(i),end = '')
            print()
            userinput = user_inter(digit_value)
            if userinput[1] == digit_value:
                while True:
                    print('The number has been guessed !!! ([^v^]) !!')
                    again = input('want to play again ? input anything to play again or input quit to QUIT')
                    while again != 'quit':
                        start_game()
                    else:
                        print('thanks for playing !')
                        quit()
                break
            for o in number_list:
                if pick_numbers_find(radnum,o,userinput[0],userinput[1]):
                    numlist.append(o)
            number_list = numlist
        return again

#call the main program function
start_game()
again = input('want to play again ? input anything to play again or input quit to QUIT')
while again != 'quit':
    start_game()
else:
    print('thanks for playing !')
    quit()