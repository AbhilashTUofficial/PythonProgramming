
def primeAndEven():

    prime = {2, 3, 5, 7, 9, 11}
    even = {2, 4, 6, 8, 10}

    x, = prime.intersection(even)
    print(f"Prime And Even: {x}")

    # * OR

    tmp = prime.intersection(even)
    print(f"Prime And Even: {tmp.pop()}")


def main():

    # * Use this if you know ahead of time
    # * that there will be a single element

    y = [5]
    x, = y
    print(x)

    primeAndEven()


if __name__ == "__main__":
    main()
