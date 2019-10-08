import math

class DecisionStructure:

    def verifyManOrWoman(self, info):
        if info == "M" or info == "m":
           print(f"{info} - Mulher")
        elif info == "H" or info == "h":
           print(f"{info} - Homem")
        else:
            print(f"{info} - Não é valido como sexo")

    def verifyLetters(self, phrase):
        phraseNumber = len(phrase)
        letter= phrase[phraseNumber -1]
        vowels = "aeiouAEIOU"
        isVowels = letter in vowels

        if isVowels is True:
            print(f"{letter} - É uma vogal")
        else:
            print(f"{letter} - Não é uma vogal")

    def banknoteCalculator(self, n1, n2, n3):
        nf = (n1+n2+n3)/3
        if nf < 6:
            print(f"Reprovado \nSua nota foi {nf}")
        elif nf >=6 and nf != 10:
            print(f"Aprovado \nSua nota foi {nf}")
        else:
            print(f"Aprovado com Distinção \nSua nota foi {nf}")
    
    def StudentDictionary(self):
        

if __name__ == "__main__":
    decisionStructure = DecisionStructure()
    #decisionStructure.verifyManOrWoman("m")
    #decisionStructure.verifyLetters("é vogal")
    #decisionStructure.banknoteCalculator(10,10,10)
