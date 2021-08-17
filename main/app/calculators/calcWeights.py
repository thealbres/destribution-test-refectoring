from app.utils.constants import weights
from app.utils.calcTime import calcTime
from app.helpers.formatSalary import unmaskSalary

class CalculatorWeights:
    """
    Class responsible for all functions that calculate weights
    """

    def __init__(self):
        pass

    def calcWeights(self, admissionDate, salary, field):
        """
        Receive three arguments (admissionDate, salary, field) and calcute all weights
        """
        admissionDurationWeight = self.calcAdmissionDurationWeight(admissionDate)
        salaryWeight = self.calcSalaryWeight(salary)
        fieldWeight = self.findFieldWeight(field)

        return {
            'admissionDurationWeight': admissionDurationWeight,
            'salaryWeight': salaryWeight,
            'fieldWeight': fieldWeight,
        }

    def calcAdmissionDurationWeight(self, admissionDate):
        """
        Calculate the admissionDuration weight
        """
        admissionDuration = calcTime(admissionDate)

        for weight in range(len(weights['time'])):
            if(admissionDuration >= float(weights['time'][weight]['key'])):
                lowestKey = weight

        return float(weights['time'][lowestKey]['value'])

    def calcSalaryWeight(self, salary):
        """
        Calculate the salary weight
        """
        salaryFormated = unmaskSalary(salary)

        for weight in range(len(weights['salary'])):
            if(salaryFormated >= float(weights['salary'][weight]['key'])):
                lowestKey = weight

        return float(weights['salary'][lowestKey]['value'])


    def findFieldWeight(self, field):
        """
        Calculate the field weight
        """
        for weight in range(len(weights['field'])):
            if(field == weights['field'][weight]['key']):

                return float(weights['field'][weight]['value'])
