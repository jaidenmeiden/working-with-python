# Delete repeat elements
def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def remove_duplicates_with_sets(some_list):
    return list(set(some_list))


def run():
    random_list = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 7, 7, 8, 8, 9, 9, 9, 9]
    print(remove_duplicates(random_list))

    random_list1 = remove_duplicates_with_sets(random_list)
    print(random_list1)


if __name__ == '__main__':
    run()
