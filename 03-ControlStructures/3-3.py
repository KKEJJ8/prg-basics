###
# Checking if discount is available
# The discount is available to children under 18,
# or people 65 or older.
#

def check_discount_eligibility(age):
    
    if age < 18 or age >= 65:
     print(f"Person of age {age} is eligible for a discount.")
    else:
        print(f"Person of age {age} is not eligible for a discount.")

ages = [72,65,64,18,17]

for age in ages:
    print(f"Age {age}: {check_discount_eligibility(age)}")
