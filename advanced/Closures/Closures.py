# Closures
def make_repeater_of(n):
    def repeater(value):
        assert type(value) == str, "Solo utilizar cadenas"
        return value * n

    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Jaiden"))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Riaño"))


if __name__ == "__main__":
    run()
