import random
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}
spread = {}
def my_tarot():
    card_key = random.randint(1, 22)
    while tarot.get(card_key):
        spread["past"] = tarot.pop(card_key)
    card_key = random.randint(1, 22)
    while tarot.get(card_key):
        spread["present"] = tarot.pop(card_key)
    card_key = random.randint(1, 22)
    while tarot.get(card_key):
        spread["future"] = tarot.pop(card_key)

def question(answer):
    if answer.title() == "Yes":
        my_tarot()
    elif answer.title() == "No":
        print("Then what are you doing here??")
    else:
        print("WTF is that? don't you know how to spell \"Yes\" or \"No\"?!")

answer = input("Are ready to play the game? Yes/No\n")
question(answer)

for card, value in spread.items():
  print("Your " + card + " is the " + value + " card.")

answer = input("\nWanna try again?")
question(answer)
