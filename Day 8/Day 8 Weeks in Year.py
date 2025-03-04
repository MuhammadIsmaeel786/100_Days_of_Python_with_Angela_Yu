weeks_left = 0
age_remaining = 0
def life_in_weeks(age):
    age_remaining = 90 - age
    weeks_left = age_remaining*52
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(56)