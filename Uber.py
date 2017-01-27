class UberManager:
    """A class responsible for keeping track of all cars in the system.
  
    === Private Attributes ===
    @type _cars: dict[str, Car]
        A map of unique string identifiers to the corresponding Car.
        For example, _cars['a01'] would be a Car object corresponding to
        the id 'a01'.
    """
    def __init__(self):
        """Initialize a new UberManager.
        There are no cars in the system when first created.
        @type self: UberManager
        @rtype: None
        """
        self._cars = {}

    def add_car(self, id_, fuel):
        """Add a new car to the system.
        The new car is identified by the string <id_>, and has initial amount
        of fuel <fuel>.
        Do nothing if there is already a car with the given id.
        @type self: UberManager
        @type id_: str
        @type fuel: int
        @rtype: None
        """
        if id_ not in self._cars:
            self._cars[id_] = Car(id_,fuel)


    def move_car(self, id_, new_x, new_y):
        """Move the car with the given id.
        The car called <id_> should be moved to position (<new_x>, <new_y>).
        Do nothing if there is no car with the given id,
        or if the corresponding car does not have enough fuel.
        @type self: UberManager
        @type id_: str
        @type new_x: int
        @type new_y: int
        @rtype: None
        """
        if id_ in self._cars:
            car = self._cars[id_]
            distance = abs(new_x - car.x) + abs(new_y - car.y)
            if car.fuel >= distance
                car.x = new_x
                car.y = new_y
                car.fuel -=distance


    def get_car_position(self, id_):
        """Return the position of the car with the given id.
        Return a tuple of the (x, y) position of the car with id <id_>.
        Return None if there is no car with the given id.
        @type self: UberManager
        @type id_: str
        @rtype: (int, int) | None
        """
        if id_ in self._cars:
            return(self._cars[id_].x, self._cars[id_].y)

    def get_car_fuel(self, id_):
        """Return the amount of fuel of the car with the given id.
        Return None if there is no car with the given id.
        @type self: UberManager
        @type id_: str
        @rtype: int | None
        """
         if id_ in self._cars:
            return self._cars[id_].fuel

    def dispatch(self, x, y):
        """Move a car to the given location.
        Choose a car to move based on the following criteria:
        (1) Only consider cars that *can* move to the location.
            (Ignore ones that don't have enough fuel.)
        (2) After (1), choose the car that would move the *least* distance to
            get to the location.
        (3) If there is a tie in (2), pick the car whose id comes first
            alphabetically. Use < to compare the strings.
        (4) If no cars can move to the given location, do nothing.
        @type self: UberManager
        @type x: int
        @type y: int
        @rtype: None
        """
        minim = -1;
        closetcar=''
        for car in self._cars.itmes():
            distance = abs(x-car.x)+abs(y-car.y)
            if distance <= car.fuel:
                if (distance <minim)|| (minim==-1):
                    minim = d[istance]
                    closetcar = car.id_

        self.move_car(closetcar, x, y)




class Car:
    """A car in the Super system.
    === Attributes ===
    @type id_: int
        The id of this Car
    @type x: int
        The x-coordinate of this Car.
    @type y: int
        The y-coordinate of this Car.
    @type fuel: int
        The number of fuel units remaining in this Car.
    """

    def __init__(self, id_, fuel):
        """Initialize a new Car, given a car id string and an initial amount
        of fuel.
        @type id_: int
            The id string of the new Car.
        @type fuel: int
            The initial quantity of fuel units in this Car.
        @rtype: None
        """
        self.id= id_
        self.fuel = fuel
        self.x = 0
        self.y = 0


if __name__ == '__main__':
    # Run python_ta to ensure this module passes all checks for
    # code inconsistencies and forbidden Python features.
    # Useful for debugging!
    import python_ta
    #python_ta.check_errors()

    # Uncomment and run before final submission. This checks for style errors
    # in addition to code inconsistencies and forbidden Python features.
    python_ta.check_all()