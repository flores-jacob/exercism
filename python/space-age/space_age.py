class SpaceAge(object):
    def __init__(self, seconds):
        self.age_in_seconds = seconds
        self.earth_age = seconds/31557600

    def on_mercury(self):
        return round(self.earth_age/0.2408467, 2)
