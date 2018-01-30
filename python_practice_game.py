#Work with functions
print("Hello, this story about one guy, who decide to travel around the world. First, he wants to start from Asia..... Yeah ")
print("But he doesnt know where he can go first")

start_choice=input("""Please, help him, choose any options:\n1. start from: China\n2. start from: Japan\n3. start from: India
""")


def china_go():
    choice=input("you start from China, did you like it?:")
    if choice=="yes":
        print("Was incredible woooow")
    else:
        print("Was not good idea start from china, I spent a lot of money from my first trip OMG")
    money_china=input("Did you spent a lot of $$$ there?")
    if money_china=="yes":
        print("I spent more than 2000$ 😞")
    else:
        print("Everything was soooo cheap, I didn't spent a lot")
    people_china=input("Chinese people are friendly?:")
    if people_china=="yes":
        print("They are so awesome and they are so funny when they smiling")
    else:
        print("One Chinese guy told me --my dog ate my homework so I ate my dog--!!!!")
if start_choice=="1":
    china_go()
def japan_go():
    choice_jap=input("you started from Japan, did you like it?: ")
    if choice_jap=="yes":
        print("Was AMAZING!!!!!")
    else:
        print("Was okay, but not like I was expected!!")
    money_japan=input("Did you spent a lot of $$$ there?")
    if money_japan=="yes":
        print("I spent more than 1000$ 😞")
    else:
        print("Everything was cheap, I didn't spent a lot")
    people_japan=input("Do u have some funny stories about japan or people from japan?:")
    if people_japan=="yes":
        print("They have Toilet museums😞")
    else:
        print("One Japanese guy told me --my Cat ate my homework so I ate my cat--!!!!")
if start_choice=="2":
    japan_go()
def india_go():
    choice_ind=input("you started from Japan, did you like it?: ")
    if choice_ind=="yes":
        print("Was AMAZING KRUUUTOOOO!!!!!")
    else:
        print("No I didn't. It not good place to visit.I had to start from China !")

if start_choice=="3":
    india_go()
