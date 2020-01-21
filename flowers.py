
class Flower:
    def __init__(self, length, container):
        self.stem_length = length
        self.container = container
class IFlower:

class Rose(Flower):
    def __init__(self, color, length, container):
        Flower.__init__(self, length, container)
        self.color = color
        # self.stem_length = "7 Inches"
        # self.container = "refrigerated"

class Daisies(Flower):
    def __init__(self, length, container):
        Flower.__init__(self, length, container)
        # self.stem_length = "4 Inches"
        # self.container = "non-refrigerated"

class Baby_breath(Flower):
    def __init__(self, length, container):
        Flower.__init__(self, length, container)
        # self.stem_length = "4 Inches"
        # self.container = "non-refrigerated"

class Poppies(Flower):
    def __init__(self, length, container):
        Flower.__init__(self, length, container)
        # self.stem_length = "4 Inches"
        # self.container = "non-refrigerated"

class Lillies(Flower):
    def __init__(self, length, container):
        Flower.__init__(self, length, container)
        # self.stem_length = "7 Inches"
        # self.container = "refrigerated"
class Alstroemeria(Flower):
    def __init__(self, length, container):
        Flower.__init__(self, length, container)
        # self.stem_length = "7 Inches"
        # self.container = "refrigerated"