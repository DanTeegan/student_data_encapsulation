class Student:

    # Here are the 2 variables of student. They are made private.
    __student_iq = 99
    __name = "BoB"

    def __init__(self):
        self.__bob_iq = 135 # Private variable cannot be called.
        self.__name = "boeing plane" # Again the variable has been made private. it cannot be called.

    # Creating a method called test
    def test(self):
        print("Your IQ" + str(self.__bob_iq))

    # Creating a method called score
    def _score(self):
        print("Great score")

# Here we are creating an object of airplane.
bob = Student()
# bob.test()
bob.__test = 200 # cannot be called as we have used encapsulation (made it private)
