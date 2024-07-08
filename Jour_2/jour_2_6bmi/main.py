height = input()
weight = input()

weight_as_int = int(weight)
height_as_float = float(height)

#utilisation operateur exposant **
bmi = weight_as_int / height_as_float ** 2

#utilisation multiplication and PEMDAs
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi_as_int)