
class Worker:

    name = None
    surname = None
    position = None
    _income = {}


class Position(Worker):

    def __init__(self, u_name, u_surname, u_position, u_wage, u_bonus):
        self.name = u_name
        self.surname = u_surname
        self.position = u_position
        self._income = {'wage': int(u_wage), 'bonus': int(u_bonus)}

    def get_full_name(self):
        return f'Name: {self.name}\nSurname: {self.surname}\nPosition: {self.position}'

    def get_total_income(self):
        return f'Total income: {sum(self._income.values())}'


# user_input = input('Name, Surname, Position, Wage, Bonus: \n')
# user_input = user_input.split()
user_input = ['Alex', 'More', 'Driver', 1000, 500]
current_user = Position(user_input[0], user_input[1], user_input[2], user_input[3], user_input[4])
print(current_user.get_full_name())
print(current_user.get_total_income())
