import string
import random

def gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    
    passion = int(input('Enter the length of the password: '))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    password = ''.join(random.sample(s, passion))
    print(f'Your password is: {password}')
    
if __name__ == "__main__":
    gen()