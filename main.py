from valentine import ValentinesDay
from flowers import Rose, Baby_breath

# if __name__ == "__main__":
for_beth = ValentinesDay()
red_rose = Rose("Red")
blue_rose = Rose("Blue")
pink_rose = Rose("Pink")
flo = Baby_breath()
for_beth.flowers = red_rose
for_beth.enhance(blue_rose)
for_beth.enhance(blue_rose)

# for_beth.flowers.append(pink_rose)

# for flower in for_beth.flowers:
#     print(flower.container)