biological_gender = str(input("Enter the biological gender (male/female): "))
if biological_gender == "male":
    hemoglobin_value = float(input("Enter the hemoglobin value (in g/l): "))
    if hemoglobin_value >= 117 and hemoglobin_value <= 155:
        print("The hemoglobin value is normal.")
    elif hemoglobin_value < 117 :
        print("The hemoglobin value is low.")
    elif hemoglobin_value > 155:
        print("The hemoglobin value is high.")
if biological_gender == "female":
    hemoglobin_value = float(input("Enter the hemoglobin value (in g/l): "))
    if hemoglobin_value >= 134 and hemoglobin_value <= 167:
        print("The hemoglobin value is normal.")
    elif hemoglobin_value < 134:
        print("The hemoglobin value is low.")
    elif hemoglobin_value > 167:
        print("The hemoglobin value is high.")