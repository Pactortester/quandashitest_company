import random

def Unicode():
    val1 = random.randint(0x4e00, 0x9fbf)
    val2 = random.randint(0x4e00, 0x9fbf)
    return chr(val1)+chr(val2)


