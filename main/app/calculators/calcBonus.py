from app.helpers.formatSalary import unmaskSalary
from app.helpers.formatSalary import maskSalary

class CalculatorBonus():

    def __init__(self):
        pass

    def calcBonus(self, employer, weights):
        salaryFormated = unmaskSalary(employer['salario_bruto'])

        bonus = (((salaryFormated * weights['admissionDurationWeight']) + 
            (salaryFormated * weights['fieldWeight'] )) /  
            (salaryFormated * weights['salaryWeight'] )) * \
            1000

        return bonus
