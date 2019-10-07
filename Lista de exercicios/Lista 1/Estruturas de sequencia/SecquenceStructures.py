import math

class SecquenceStructures:
    def __init__(self, onNow, params):
        self.exerciseChoices(onNow, params)

    def exerciseChoices(self, choicesNumber, params):
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

if __name__ == "__main__":
    secquenceStructures = SecquenceStructures(5, 70)
