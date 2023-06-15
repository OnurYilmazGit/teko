from decouple import config
import openai


def rephrase_description(situation_description):
    openai_api_key = config("OPENAI_API")
    openai.api_key = openai_api_key

    instruction = f"Reformulate the following text to a natural-sounding and accurate text for legal documents.\n"
    prompt = instruction + situation_description
    print(prompt)

    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].message.content
    print(" ")
    print(message)
    return message


def receive_correct_court(court_type, city):
    openai_api_key = config("OPENAI_API")
    openai.api_key = openai_api_key

    prompt = f"I am living in city corresponding to PLZ {city}. At which {court_type} do I have to file a case for tenancy law? Please give me as an answer only the name of the court."
    print(prompt)

    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].message.content
    print(" ")
    print(message)
    return message


desc = "The crime happened at May 5, 2023. My brother and I were walking down the street. A man in a suit came from the left and destroyed the car's window."
rephrase_description(desc)