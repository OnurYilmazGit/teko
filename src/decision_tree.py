from treelib import Node, Tree


def find_court_type(subject, appeal, amount):

    explanation = ""
    amount = int(amount)

    if subject in ["Residential Rent", "Private Miete"]:
        court_type = "Amtsgericht"
        explanation += "Your submitted subject is residential rent. The Amtsgericht is responsible for this subject " \
                       "independently from the monetary amount of dispute."

    else:
        explanation += "Your submitted subject is commercial rent. Here, the Amtsgericht is responsible for " \
                       "monetary amounts of dispute up to 5000 Euros. Otherwise, the Landesgericht is responsible. "
        if amount <= 5000:
            court_type = "Amtsgericht"
            explanation += f"For your submitted amount of {amount} Euros the {court_type} is responsible. "
        else:
            court_type = "Landgericht"
            explanation += f"For your submitted amount of {amount} Euros the {court_type} is responsible. "

    if appeal in ["Yes", "Ja"]:
        court_type = "Oberlandesgericht"
        explanation = "For cases with an appeal against the decisions of the Amtsgericht or Landgericht, the " \
                      f"{court_type} is responsible independently of subject and amount. "

    return court_type, explanation
