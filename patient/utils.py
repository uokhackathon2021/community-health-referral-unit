from datetime import datetime
import random


def create_referal_code():
    val = "123456789qwertyuioplkjhgfdsazxcvbnm".upper()
    v = ""
    for x in range(7):
        v += val[random.randint(0, len(val) - 1)]

    return "REF/" + v + "/" + str(datetime.now().year)
