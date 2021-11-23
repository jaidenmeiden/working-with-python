# Closures
def make_division_by(n):
    def division(v):
        return v / n if type(v) == float or type(v) == int else "Solo utilizar número"

    return division


def make_division_by_with_lambda(n: float):
    return lambda x: (x / n) if type(x) == float or type(x) == int else "Solo utilizar número"


def run():
    print("Nested:")
    division_str = make_division_by(5)
    print(division_str("Hola"))
    division_x = make_division_by(5)
    print(division_x(99.7))
    division_5 = make_division_by(5)
    print(division_5(255))
    division_10 = make_division_by(10)
    print(division_10(1577))
    print("Lambda:")
    division_with_lambda_str = make_division_by_with_lambda(5)
    print(division_with_lambda_str("Hola"))
    division_with_lambda_x = make_division_by_with_lambda(5)
    print(division_with_lambda_x(10.97))
    division_with_lambda_5 = make_division_by_with_lambda(5)
    print(division_with_lambda_5(255))
    division_with_lambda_10 = make_division_by_with_lambda(10)
    print(division_with_lambda_10(1577))


if __name__ == "__main__":
    run()
