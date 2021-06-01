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
        a,b,c = ["","",""] # e.g. 0-10 -> a="I",b="V"c="X"
        importantNumbs = {
                1:a,
                2:2*a,
                3:3*a,
                4:a+b,
                5:b,
                6:b+a,
                7:b+2*a,
                8:b+3*a,
                9:a+c
                }
        importantNumbs2 = ["I","V","X","L","C","D","M"] #1,5,10,50,100,500,1000
        # seesm that solution could be using 1-9 but being wary of which order (10, 100, 1000) they are placed.

        strValue = str(num)
        index = len(strValue) - 1
        romans = []
        for i in strValue:
            a,b,c = [index,index +2]
            romans.append(importantNumbs[int(i)])
        return ''.join(romans)


