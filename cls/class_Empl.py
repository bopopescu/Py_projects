class Employee:
    def __init__(self, first_name, last_name, e_ID, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = e_ID
        # private attibute, start with 2 understore, __
        self.__salary = salary

    def show_employee(self):
        print("First Name is", self.first_name)
        print("Last Name is ", self.last_name)
        print("ID is ", self.user_id)
        print("Salary is ", self.get_salary())
        
    def get_salary(self):
        return self.__salary


def main():
    test_engineer = Employee("Jack", "Wallace", "747612", 10000)
    test_engineer.show_employee()
    my_salary = test_engineer.get_salary()
    print("the salary is called by get_salary ", my_salary)


if __name__ == "__main__":
    main()
