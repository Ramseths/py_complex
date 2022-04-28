class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, another_coordinate):
        x_diff = (self.x -another_coordinate.x) ** 2
        y_diff = (self.y - another_coordinate.y) ** 2
        return (x_diff + y_diff) ** 0.5

if __name__ == '__main__':
    coordinate_one = Coordinate(4, 40)
    coordinate_two = Coordinate(5, 9)
    print(coordinate_one.distance(coordinate_two)) 
