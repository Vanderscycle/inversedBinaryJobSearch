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
        pattern1 = {
                1:"I",
                2:"II",
                3:"III",
                4:"IV",
                4:"V",
                6:"VI",
                7:"VII",
                8:"VIII",
                9:"IX"
                }
        pattern2 = {
                10:"X",
                20:"XX",
                30:"XXX",
                40:"XV",
                50:"V",
                60:"VX",
                70:"VXX",
                80:"VXXX",
                90:"XC"
                }
        # seesm that solution could be using 1-9 but being wary of which order (10, 100, 1000) they are placed.

        strValue = str(num)
        sizeNum = len(strValue)
        romans = []
        for i in strValue:
            if int(i)*10**sizeNum in importantNumbs:
                romans.append(importantNumbs[int(i)])



