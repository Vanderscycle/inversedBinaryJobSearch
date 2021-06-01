class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        https://www.rapidtables.com/math/symbols/roman_numerals.html
        """
        importantNumbs = {
                1:"I",
                2:"II",
                3:"III",
                4:"IV",
                4:"V",
                6:"VI",
                7:"VII",
                8:"VIII",
                9:"IX",
                10:"X",
                40:"XL",
                50:"V",
                90:"XC",
                10:"C",
                400:"CD",
                500:"D",
                900:"CM",
                1000:"M"
                }
        # seesm that solution could be using 1-9 but being wary of which order (10, 100, 1000) they are placed.
        strValue = str(num)
        sizeNum = len(strValue)
        romans = []
        for i in strValue:
            if int(i)*10**sizeNum in importantNumbs:
                romans.append(importantNumbs[i])



