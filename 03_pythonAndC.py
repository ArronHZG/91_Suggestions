def switch(x):
    return {
        0:"Zero",
        1:"One",
        2:"Two"
    }.get(x)

if __name__ == '__main__':
    print(switch(2))