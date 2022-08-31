
class Region(object):
    def __init__(self, description):
        self.description = description

    def describe(self):
        print(self.description)

class Grasslands(Region):
    def __init__(self, description):
        # I should be able to use inheritance to avoid having to define var below?
        self.description = description