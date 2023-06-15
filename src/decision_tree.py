from treelib import Node, Tree


def find_court_type(subject, appeal, amount):

    explanation = ""

    if subject == "Private Rent":
        court_type = "Amtsgericht"
        explanation += "Your submitted subject is private rent. The Amtsgericht is responsible for this subject " \
                       "independently from the monetary amount of dispute."

    else:
        explanation += "Your submitted subject is commercial rent. Here, the Amtsgericht is responsible for " \
                       "monetary amounts of dispute up to 5000 Euros. Otherwise, the Landesgericht is responsible. "
        if amount <= 5000:
            court_type = "Amtsgericht"
            explanation += f"For your submitted amount of {amount} the {court_type} is responsible. "
        else:
            court_type = "Landesgericht"
            explanation += f"For your submitted amount of {amount} the {court_type} is responsible. "

    if appeal == "Yes":
        court_type = "Oberlandesgericht"
        explanation = "For cases with an appeal against the decisions of the Amtsgericht or Landesgericht, the " \
                      f"{court_type} is responsible independently of subject and amount. "

    return court_type, explanation
