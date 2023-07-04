from treelib import Node, Tree


def find_court_type(subject, appeal, amount, lang):

    explanation = ""
    amount = int(amount)

    if subject in ["Residential Rent", "Private Miete"]:
        court_type = "Amtsgericht"
        if lang == "English":
            explanation += "Your submitted subject is residential rent. The Amtsgericht is responsible for this subject " \
                       "independently from the monetary amount of dispute."
        else: 
            explanation += "Ihr ausgewählter Bereich ist die private Miete. Das Amtsgericht ist zuständig für diesen Bereich" \
                           ", unabhängig von dem Streitwert des Falls."

    else:
        if lang == "English":
            explanation += "Your submitted subject is commercial rent. Here, the Amtsgericht is responsible for " \
                        "monetary amounts of dispute up to 5000 Euros. Otherwise, the Landesgericht is responsible. "
        else:
            explanation += "Ihr angegebener Bereich ist die gewerbliche Miete. Hierfür ist das Amtsgericht zuständig für  " \
                        "Fälle mit einem Streitwert von bis zu 5000 Euro. Andernfalls ist das Landgericht zuständig. "
        if amount <= 5000:
            court_type = "Amtsgericht"
            if lang == "English":
                explanation += f"For your submitted amount of {amount} Euros the {court_type} is responsible. "
            else: 
                explanation += f"Für den angegebenen Betrag von {amount} Euro ist das {court_type} verantwortlich. "
        else:
            court_type = "Landgericht"
            if lang == "English":
                explanation += f"For your submitted amount of {amount} Euros the {court_type} is responsible. "
            else:
                explanation += f"Für den angegebenen Betrag von {amount} Euro ist das {court_type} verantwortlich. "

    if appeal in ["Yes", "Ja"]:
        court_type = "Oberlandesgericht"
        if lang == "English":
            explanation = "For cases with an appeal against the decisions of the Amtsgericht or Landgericht, the " \
                      f"{court_type} is responsible independently of subject and amount. "
        else:
            explanation = "Für Fälle bei denen Revision gegen die Entscheidung eines Amtsgerichts oder Landgerichts eingelegt wurde, ist das " \
                      f"{court_type} zuständig unabhängig von Streitwert und Mietbereich. "

    return court_type, explanation
