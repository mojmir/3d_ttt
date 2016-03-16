class Point:
    """
    Represents one playing stone
    """
    def __init__(self, value=0):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)
