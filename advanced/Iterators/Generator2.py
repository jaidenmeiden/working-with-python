# Iterator (Fibonacci)
import time


def fibonacci_gen(limit=None):
    n1 = 0
    n2 = 1

    if not limit:
        counter = 0
        while True:
            if counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                aux = n1 + n2
                # swapping:
                n1, n2 = n2, aux
                counter += 1
                yield aux
    else:
        for counter in range(0, limit):
            if counter == 0:
                yield n1
            elif counter == 1:
                yield n2
            else:
                aux = n1 + n2
                # swapping:
                n1, n2 = n2, aux
                yield aux


if __name__ == "__main__":
    fibonacci = fibonacci_gen(100)
    for element in fibonacci:
        print(element)
        time.sleep(0.05)
