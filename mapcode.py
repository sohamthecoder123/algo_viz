def algorithm(setup, update, answer):
    def wrapper(*args, **kwargs):
        state = setup(*args, **kwargs)

        while True:
            if not update(state):
                break            

        return answer(state)
    return wrapper

'''

print(f(5))'''