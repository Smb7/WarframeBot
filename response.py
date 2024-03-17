from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == ' ':
        return "No input"
    elif 'hello' in lowered:
        return 'Hello World'
    elif 'bye' in lowered:
        return 'later'
    elif 'roll dice' in lowered:
        return f'you rolled {randint(1, 6)}'
    else:
        return choice(["I don't understand", "unknow error CPU melting", "Try again"])

