def convert_gender(gender: str):
    gender = gender.upper()
    if gender == "M":
        return "MALE"
    if gender == "F":
        return "FEMALE"
    else:
        return "GENDER_UNKNOWN"
