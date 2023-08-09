import Car

if __name__ == "__main__":
    c = Car.Car("Toyota", 2022)
    print(c)
    print("total_cars:", Car.Car.get_total_cars())

