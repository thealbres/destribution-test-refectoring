from app.calculators.calcWeights import CalculatorWeights
from app.calculators.calcBonus import CalculatorBonus
from app.helpers.parsers import buildPayload

async def calcDistributions(employees: str):

    employeesWithBonus = list()
    weightsCalculator = CalculatorWeights()
    bonusCalculator = CalculatorBonus()

    for employer in employees.funcionarios:

        weights = weightsCalculator.calcWeights(employer['data_de_admissao'], employer['salario_bruto'], employer['area'])
        employer['bonus'] = bonusCalculator.calcBonus(employer, weights )
        
        employeesWithBonus.append(employer)

    return buildPayload(employeesWithBonus)





