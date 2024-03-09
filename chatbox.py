import re

questions_answers = [
    (r'hello', "Hello, Can i help u?"),
    (r'who are you', "I'm AI"),
    (r'i need help finding a hospital, can you help me', "I'm always willing to help. Based on your location through positioning, the hospitals near you are Bach Mai Hospital and An Viet Hospital."),
    (r'can you give me the address of bach mai hospital', "78 Giai Phong"),
    (r'does bach mai hospital have consultations on saturdays', "Yes."),
    (r'what are the operating hours of bach mai hospital', "24/7"),
    (r'is bach mai hospital good', "Yes"),
    (r'what diseases does an viet hospital treat', "An Viet Hospital is general hospital"),
    (r'does the hospital have consultations on saturdays', "yes"),
    (r'where does dr. Nguyen Thi Hoai An work', "Dr.An work Bach Mai hospital."),
    (r'Is dr.Nguyen Thi Hoai An good', "She must be good."),
    (r'what are dr. nguyen thi hoai an\'s consultation hours', "She consultation at 15h-18h"),
    (r'which is a good hospital for musculoskeletal diseases in hanoi', "Bach Mai Hospital."),
    (r'do you sell baby clothes', "I'm a chatbot?"),
    (r'do you work on sundays', "yes, of course.")
]

def get_response(input_str):
    input_str = input_str.lower()
    for pattern, response in questions_answers:
        if re.search(pattern, input_str):
            return response
    return "I'm sorry, I don't have a response for that."


while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Bot:", response)