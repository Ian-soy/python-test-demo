import random

def generate_question():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    operator = random.choice(['+', '-'])
    if operator == '-':
        if a > b:
            return f'{a} - {b} = ', a - b
        else:
            return f'{b} - {a} = ', b - a
    else:
        if a + b > 10:
            return f'{a} + {10 - a} = ', 10
        else:
            return f'{a} + {b} = ', a + b

def main():
    for _ in range(20):
        question, answer = generate_question()
        print(question)

if __name__ == '__main__':
    main()