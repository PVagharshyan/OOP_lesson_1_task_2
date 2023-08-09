class Car:
    model:str
    year:int
    _total_cars = 0
    def __init__(self, model, year):
        self.m_model = model
        if not self._check_year(year):
            raise ValueError()
        self.m_year = year
        Car._total_cars += 1
    def __str__(self):
        return f"model: {self.m_model}, year: {self.m_year}"
    @classmethod
    def get_total_cars(cls):
        return cls._total_cars
    @staticmethod
    def _check_year(year):
        if year < 2023 and year > 0:
            return True
        return False

