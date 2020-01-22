'''
Valentine's Day Arrangement

The Valentine's Day arrangement includes the traditional rose. Jake has red, pink, and blue ones to send the right message. It also has lillies and alstroemeria to add more depth to the color of the arrangement.

This arrangment is flamboyant and extravagent. Each flower stem is cut to 7 inches. Flowers in this arrangement are not organically grown, so they can be transported in a refrigerated container.
'''
from arrangement import Arrangement
from flowers import Rose, Lillies, Alstroemeria, IValentineFlower
class ValentinesDay(Arrangement):
    def __init__(self):
        super().__init__()
    
    @property # The flowers getter
    def flowers(self):
        try:
            return self.__flowers # Note there are 2 underscores here
        except AttributeError:
            return ""
    
    @flowers.setter # The flower setter
    def flowers(self, new_flowers):
        # if new_flowers.container == "refrigerated":
        if self.theme == Love:
            self.enhance(new_flowers)
        else:
            raise TypeError('That type of flower cannot be put into this arrangement')

    
        

    
