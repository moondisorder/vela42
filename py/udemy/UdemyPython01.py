
##### TRUE OR FALSE TEST #####################
##boobquestion = input("Do you have boobs?")
#if boobquestion=="yes":
#    print("I have boobs. Oppai!")
#else: 
#    print("I dont have boobs. Flat justice.❤️‍🔥")

### True or False ID showing question.###################
#age = int(input('''
#How old are you? 
#Show me your ID!'''))
#age = int(age)

#age>=21

#if age>=21:
#    print('''Come on in and drink!
#    🍷🍸🍹🍺🍻🍾''')
#else: 
#    print("Go home kid!😠")

######################################################
### ELSE for every other option.

#color = "orange"

#if color == "green":
#    print("Beginner!")
#elif color == "blue":
#    print("Intermediate")
#elif color == "black":
#    print("ADVANCED!")
#else:
#    print("I have no idea what you are talking about!")

#first_name = input('What is your first name?')
#last_name = input('What is your last name?')
#print("***********************************")
#length = len(first_name)+len(last_name)

#if length>=12:
#    print(f"{first_name} {last_name} is longer than your average Australian name.")
#elif length>=5:
#    print(f"{first_name} {last_name}, that's a very short name!")
#print("*"*50)

#######################################
#import random  ##have to import things!
#print(random.randint(1,6))
######################### TWEET COUNTER #####
#tweet = input("enter your tweet")
#char_count = len(tweet)
#max_chars=130
#if char_count<max_chars:
#    print("It's not too long.")
#else: 
#    print(f"Your tweet is {char_count} is {char_count - max_chars } char tweet is too long ")

################ BMI CALCULATOR #################
#height = float(input("Enter your height"))
#weight = float(input("Enter your weight"))
#category = "none"
#bmi = ((weight*703) / (height ** 2))
#bmi = round(bmi,1)
#if bmi < 16:
#    category = "severely underweight"
#    print("You're underweight!")
#elif bmi <18.4:
#    category = "underweight"
#    print("Under weight.")
#elif bmi<24.9:
#    category = "normal"
#    print("Normal!")
#elif bmi <29.9:
#    category = "overweight"
#    print("Overweight")
#elif bmi < 34:
#    category = "obese"
#    print ("Obese")
#elif bmi < 39:
#    category = "morbidly obese"
#    print("Morbidly obese")

#print(f"Your BMI of {bmi} makes you {category}!")
###################################################
#num = 3<4 and 3>8
#if num == True and True:
#    print(num)
#else:
#    print("Thats wrong!")
################################################
#word = input("Type a word!:")

#if word[0]=="g" and len(word)>=3:
#    print("Word starts with G and is greater or less than three!")
#else:
#    print("Word invalid!")
################################################
#color = input("Enter a color!")
#if color:
#    print(f"{color} is my fave color too!")
#else:
#    print("NO.")

## 
#answer = input("Please say hi. :)")
#while answer !="hi":
#    answer=input("RUDE SAY HI.")
#print("Hi to you too!")

#count = 1;
#while count <=10:
    #print(f"Count is {count}.")
#    print("*"*count )
#    count+=1
#print("Count is greater than 10.")
#word = "asshole"
#for char in word:
#    print(char)

#for num in range(-5,10):
#    print(num)

#for num_bottles in range(99,0,-1): 
#    #stepping down means -1
#    print(f"{num_bottles} bottles of beer on the wall.")
#    print(f"{num_bottles} bottles of beer.")
#    if num_bottles==1:
#        print(f"Take one down, pass it around, no more bottles of beer on the wall.")
#    else:
#        print(f"Take one down, pass it around, {num_bottles-1} bottles of beer on the wall.")
#    print("*"*50)

#message = input("Say ass")
#while True:
#    if message =="ass":
#        break
#    message = input("please say ass")
#print("Finally! :)")
#from random import randint
#num_dice = int(input("How many dice are we rolling?"))
#num_sides = int(input("How many sides are on each die?"))

#while True:
#    result="|"
#    for die in range(num_dice):
#        rand = randint(1,num_sides)
#        result +=f"{rand}|"
#    print(result)
#    reply = input("Roll again? or type Q to quit:")
#    if reply == "q":
#        break
############# FUNCTIONS #############################
#def laugh(intensity):
#    print(f"ha!*{intensity}") 

#laugh(2)

#def divide(num1,num2):
#    print(num1/num2)
#divide(13,3)

#def is_even(num):
#    if num % 2 ==0:
#        return True
#    else:
#        return False 

#def is_even(num):
#   return num % 2 ==0

#print(is_even(7))
#############################
#slugify

#def slugify(phrase):
#    return phrase.lower().strip().replace(" ","-")

#print(slugify("No I will not eat GREEEN eggs and ham"))

###VOWEL COUNTER 
#def count_vowels(word):
#    count  = 0
#    for char in word:
#        if char  in "aeiou":
#            count += 1
#    return count 

#print(count_vowels("hello"))

##enclosing 
#def outer():
#    global animal ##scoped globally
#    animal = "spider crab"
#outer()

#print(animal)

#high_scores =["trash","me"]
#print(high_scores)

#ass = list("asshole")
#print(ass)

#waitlist=[5,34,73]
#waitlist.append('Andrew')
#print(waitlist)
#sp="Superdooper"[3:7]
#print(sp)

#emails = ['griffith@falconia.com','GUTS@berserker.net']
#for email in emails: 
#    print("****Sending email to****")
#    print(email)

###########LISTS 
#list = [
#    ['banana','apple','orange'],
#    ['cat','dog','giraffe'],
#    ['griffith','guts','caska']
#    ]
#print(list[2][2])
#list = [2,4,6,8]

### SPLIT & JOING #############################
#full_name = ["Vela", "Marissa", "Noble"]
#print("*~#n_n*".join(full_name)) ## JOINS TOGETHER
#print(full_name.split(" "))

#from struct import unpack

#things = ["grey","teal","salmon"]
#monochrome, greyblue, pinkish = things 
#print(monochrome,greyblue,pinkish)

####DICTIONARIES #############################
#movie  = {
#    "title" : "The BEErserk movie",
#    "year" : 2013,
#    "imdb" : 60.3,
#    "runtime": "Too long",
#    "rating": "R",
#    "reviews": "Bad"
#}


##give KEY and VALUE separated by :
#print(type(movie))

#vela = {'awesomelevel':9000, 'self esteem': 0 }
#me = {'vela': '28 years old', 'mood' :'alright',
#'hobby': 'dancing in the dark'}
#print(me['mood'])

#me['hobby'] = 'dancing in the dark to anime music'
#print(me)
#even = {10,14,40}
#even.add(12) # this is important lol 
#print(even)

######### ARGS! ########################
#def count_stuff(*args):
#    print(f"You passed me {len(args)} arguments.")
#print(count_stuff(1,2,3,4))

#### KEYWORD ARGS KWARGS ###################** ###############
## order kinda matters
#def display_info(person,*args,status='single'):
#    print(f"Person is {person}")
#    print(f"Status is {status}")
#    print(f"Miscellaneous is {args}")


#print(display_info('Vela',3,4,5,status='a unicorn'))



