class Package:
    def __init__(self, date, owner, code, origin=None,
                 destination=None, description=None):
        self.date = date
        self.client = owner
        self.code = code
        self.description = description
        self.origin = origin
        self.destination = destination
