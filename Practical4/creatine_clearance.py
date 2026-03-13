# 1. Define input variables: age, weight, gender, creatinine concentration (cr)
# 2.  Check each variable in sequence to ensure it meets the range requirements
# 3.  If any variable does not meet the criteria, an error is reported and the result is not computed
# 4.  When all variables are consistent, use the formula to calculate creatinine clearance (CrCl)
# 5.  The female result needs to be multiplied by an additional 0.85
--------------------------------------------------------------------------------
# 1. Input variables
age = 50
weight = 60
gender = "female"
cr = 80
# 2. Check whether all input values are	within the correct ranges
if age >= 100:
  print("age needs corrected")
elif weight <= 20 or weight >=80:
  print("weight needs corrected")
elif gender not in ["male","female"]:
  print("gender needs corrected")
elif cr <= 0 or cr >= 100:
  print("cr needs corrected")
# 3. Calculate the creatine clearance(different in gender)
else:
  crcl = (140 - age) * weight / (72 * cr)
if gender == "female":
  crcl = crcl * 0.85
print("CrCl is: ",crcl)
