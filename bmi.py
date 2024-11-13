def bmi(weight, height):
    if weight <= 0 or height <= 0:
        raise ValueError("le poids et la taille doivent etre des valeurs positives")
    index = weight / (height * height)
    return index

def bmi_category(index):
    if index < 18.5:
        return "sous-poids"
    elif 18.5 <= index < 24.9:
        return "poids normal" 
    elif 25 <= index < 29.9:
        return "surpoids"
    else:
        return "obese"
    
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Erreur: la valeur doit etre un nombre positif")
            else:
                return value
        except ValueError:
            print("Erreur: veuillez entrer un nombre valide")
    

weight = get_positive_float("Entrer votre poids en kg : ")
height = get_positive_float("Entrer votre taille en m : ")

try:
    user_bmi = bmi(weight, height)
    user_category = bmi_category(user_bmi)

    print(f"Votre IMC est de {user_bmi:.2f}, ce qui correspond à la catégorie : {user_category}")
except ValueError as e:
    print(e)