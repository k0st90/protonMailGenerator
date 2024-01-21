import random

#generate password and email
def randomize(_option_, _length_) -> str:
    try:
        character_sets = {
            '-p': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+',
            '-s': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890',
            '-l': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
            '-n': '1234567890',
            '-m': 'JFMASOND'
        }

        if _option_ == '-d':
            return str(random.randint(1, 28))
        elif _option_ == '-y':
            return str(random.randint(1950, 2000))

        characters = character_sets.get(_option_, '')
        return ''.join(random.choice(characters) for _ in range(_length_))
    except:
        return