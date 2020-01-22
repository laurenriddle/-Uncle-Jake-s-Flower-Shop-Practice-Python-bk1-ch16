from valentine import ValentinesDay
from flowers import Rose, Baby_breath, Daisies

'''
Uncle Jake (a.k.a. Jake Mendenhyll) opened his flower shop in 1972, at the height of the Flower Power cultural phenomenon. Since then, his two daughters, and 1 grandson have joined him in running the shop.

Their two biggest seasons are Mother's Day and Valentine's Day. Throughout Denver, the tradition of sending an Uncle Jake arrangement has passed across generations, and people trust Jake and his family to send the best flowers. Since 1980, the contents of each arrangement has never changed.



Mother's Day Arrangement
The Mother's Day arrangement contains daisies, baby's breath, and poppies. This arrangement is a bit more reserved, and Jake makes sure that each flower stem is cut to 4 inches.

Also, each flower in this arrangement is organically grown with no pesticides used. Because of this, these arrangements have to be transported in a non-refrigerated container.



Valentine's Day Arrangement
The Valentine's Day arrangement includes the traditional rose. Jake has red, pink, and blue ones to send the right message. It also has lillies and alstroemeria to add more depth to the color of the arrangement.

This arrangment is flamboyant and extravagent. Each flower stem is cut to 7 inches. Flowers in this arrangement are not organically grown, so they can be transported in a refrigerated container.





Instructions
Your task is to define classes for each type of flower, and a class for each arrangement type. Each arrangement instance should have an attribute of flowers which will contain at least one of each type of the corresponding flowers listed above.

Your code must ensure that only the right flowers can be added to each arrangement. Here's some terse starter code.

Rose, lillies, and alstroemeria share some attribute that the others do not (perfect case for an interface class)

All flowers share some common attributes
'''


# if __name__ == "__main__":
for_beth = ValentinesDay()
red_rose = Rose("Red", "7 Inches", "refrigerated")
blue_rose = Rose("Blue", "7 Inches", "refrigerated")
pink_rose = Rose("Pink", "7 Inches", "refrigerated")
for_beth.enhance(red_rose)
for_beth.enhance(blue_rose)
for_beth.enhance(pink_rose)
for_beth.flowers = red_rose
for_beth.flowers = blue_rose
for_beth.flowers = pink_rose
daisy = Daisies("4 Inches", "Non-refrigerated")
for_beth.flowers = daisy




# for_beth.flowers.append(pink_rose)

# for flower in for_beth.flowers:
#     print(flower.container)