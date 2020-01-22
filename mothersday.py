'''
Mother's Day Arrangement

The Mother's Day arrangement contains daisies, baby's breath, and poppies. This arrangement is a bit more reserved, and Jake makes sure that each flower stem is cut to 4 inches.

Also, each flower in this arrangement is organically grown with no pesticides used. Because of this, these arrangements have to be transported in a non-refrigerated container.
'''
from arrangement import Arrangement
class MothersDay(Arrangement):

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
        if new_flowers.theme == False:
            self.enhance(new_flowers)
        else:
            raise TypeError('That type of flower cannot be put into this arrangement')

    # Override the `enhance` method to ensure only
    # roses, lillies, and alstroemeria can be added


