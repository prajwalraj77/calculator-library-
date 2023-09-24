from calci import  Calculator

num=Calculator()

addition=num.add(5,7)
print(f"sum of two no is {addition}")

subtraction=num.sub(5,15)
print(f"subtraction of two no is {subtraction}")

multiplication=num.mul(4,5)
print(f"multiplication of two no is {multiplication}")

division=num.div(22,7)
quotient, remainder = division
print(f"division of two no , quotient= {quotient} and remainder= {remainder}" )