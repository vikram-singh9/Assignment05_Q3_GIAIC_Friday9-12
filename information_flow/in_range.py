def in_range(n, low, high):
    """ Returns True if n is between low and high, inclusive.
        high is guaranteed to be greater than low. """
    return low <= n <= high

if __name__ == "__main__":
    in_range(5, 1, 10) # True