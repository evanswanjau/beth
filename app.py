# simple AI CML that says hello
# request name
def requestName():
    # beth says hello
    name = input("\nHi I'm Beth, what's your name? ")

    nameInteraction(name)



# user name interaction
def nameInteraction(name):
    # assing user first name
    name = name.split(' ')
    name = name[0]

    # request what they want to do
    feel = input("\nHi " + name + ", what do you feel like doing today? ")

    feelLike(feel)



# ask user feeling
def feelLike(feel):

    feel = feel.lower()

    if feel == 'nothing':
        print("\n :( You're boring I want nothing to do with you")
    else:
        feel = feel.replace("ing", "")

        print("\nThat sounds like fun. ")
        answer = input("\nDo you think we could " + feel + " together? ")
        answerFeel(answer)




'''
--------------------------------------------------
Answer functionality that will return yes, no or
maybe according to the answer given
-------------------------------------------------
'''
# answer function
def returnAnser(answer):

    returnValue = ''

    answer = answer.lower()

    yes = ['yes', 'yea', 'yeah', 'sure', 'ofcourse', 'heck yea', 'heck yeah', 'absolutely']
    no = ['no', 'nop', 'nope', 'heck no', 'i dont think so']
    maybe = ['maybe', 'not sure', 'i\'m not sure']

    for i in yes:
        if i == answer:
            returnValue = 'yes'
            break
        else:
            for i in no:
                if i == answer:
                    returnValue = 'no'
                    break
                else:
                    for i in maybe:
                        if i == answer:
                            returnValue = 'maybe'
                        else:
                            returnValue = 'Oh my could you please much more simpler word I\'m not that advanced in English'

    return returnValue



# after answering whether we should hang
def answerFeel(answer):

    answer = returnAnser(answer)

    if answer == 'yes':
        next = input("\nAwesome! How should we get started")
    elif answer == 'no':
        next = input("\nHow come? I thought we were getting along quite well")
    else:
        next = input("\nSo that maybe could be a future yes?")


    print(next)




requestName()
