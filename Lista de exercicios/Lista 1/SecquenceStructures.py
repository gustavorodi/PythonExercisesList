import math

class SecquenceStructures:
    def __init__(self, onNow, params, field):
        self.exerciseChoices(onNow, params, field)

    def exerciseChoices(self, choicesNumber, params, field):
        if choicesNumber is 1:
            self.conversionInCm(params)
        elif choicesNumber is 2:
            self.circleArea(params)
        elif choicesNumber is 3:
            self.conversionInCelsius(params)
        elif choicesNumber is 4:
            self.conversionInFahrenheit(params)
        elif choicesNumber is 5:
            self.verifyWeight(params)
        elif choicesNumber is 6:
            self.verifysalary(params, field)
        elif choicesNumber is 7:
            self.conversionInFahrenheit(params)
        elif choicesNumber is 8:
            self.verifyWeight(params)
        elif choicesNumber is 9:
            self.conversionInCelsius(params)
        
        else:
            raise Exception("Argumento invalido")

    def conversionInCm(self, conversion):
        conversion = int(conversion * 100)
        print(f"Convertendo fica:{conversion}")

    def circleArea(self, raio):
        resultIs = float(math.pi * (raio ** 2))
        print(f"A area é: {resultIs}")
    
    def conversionInCelsius(self, graus):
        resultIs = int(5*((graus - 32)/9))
        print(f"A temperatura em é {resultIs} Graus Celcius")
    
    def conversionInFahrenheit(self, graus):
        resultIs = int(((graus/5)*9) + 32)
        print(f"A temperatura em é {resultIs} Graus Fahrenheit")
    
    def verifyWeight(self, weight):
        if weight <= 50:
            print(f"Não precisa, pagar imposto")
        else:
            tmp = weight - 50
            resultIs = tmp * 4
            print(f"Você pescou {weight} Kg e precisa pagar {resultIs}")

    def verifysalary(self, salaryH, hours):
        grossSalary = float(salaryH * hours)
        salaryIR    = (grossSalary * 0.011)
        salaryClean =  grossSalary - salaryIR
        salaryINSS  = (grossSalary * 0.08)
        salaryClean =  salaryClean - salaryINSS
        salarySind  = (grossSalary * 0.05)
        salaryClean =  salaryClean - salarySind        
        print(f"Salário bruto: R$ {grossSalary}")
        print(f"IR: R$ {salaryIR}")
        print(f"INSS: R$ {salarySind}")
        print(f"Sindicato: R$ {salarySind}")
        print(f"Salário liquido: {salaryClean}")



if __name__ == "__main__":
    secquenceStructures = SecquenceStructures(6, 160, 27)
