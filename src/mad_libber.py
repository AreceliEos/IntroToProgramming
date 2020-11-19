print("Madlib Maker")
print("Verb: dancing")
print("Place: Barcelona")
print("Name: La Rambla")
print("Noun: Hurt")

verb = ("dancing")
place = ("Barcelona")
name = ("La Rambla")
noun = ("hurt")

firstline = "Then I'm verbholder in placeholder"
secondline = "verbholder with my feet ten feet off of nameholder"
thirdline = "verbholder in placeholder"
fourthline = "But do I really nounholder the way I nounholder"

firstline = firstline.replace("verbholder", verb)
firstline = firstline.replace("placeholder", place)

secondline = secondline.replace('verbholder', verb)
secondline = secondline.replace('nameholder', name)

thirdline = thirdline.replace("verbholder", verb)
thirdline = thirdline.replace("placeholder", place)

fourthline = fourthline.replace("nounholder", noun)
fourthline = fourthline.replace("nounholder", noun)

print('\n',firstline,'\n',secondline,'\n',thirdline,'\n',fourthline)
