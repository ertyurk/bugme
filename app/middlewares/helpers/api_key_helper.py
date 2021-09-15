import random
import string


def generate_api_key():
    random_source = string.ascii_letters + string.digits
    # select 1 lowercase
    key = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    key += random.choice(string.ascii_uppercase)
    # select 1 digit
    key += random.choice(string.digits)
    # generate other characters
    for i in range(36):
        key += random.choice(random_source)
    key_list = list(key)
    # shuffle all characters
    random.SystemRandom().shuffle(key_list)
    key = "".join(key_list)
    final = "pk_" + key
    return final
