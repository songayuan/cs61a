HW_SOURCE_FILE = __file__


def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if pos < 10:
        return 1 if pos == 8 else 0
    return 1 + num_eights(pos // 10) if pos % 10 == 8 else num_eights(pos // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    """
    "*** YOUR CODE HERE ***"
    def helper(pos):
        if pos == 1:
            return 1
        elif (pos-1) % 8 == 0 or num_eights(pos-1):
            return -helper(pos-1)
        else:
            return helper(pos-1)
    if n == 1:
        return 1
    return helper(n)+pingpong(n-1)


def next_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def coins_partitions(change, coin=25):
        if change == 0:
            return 1
        elif change < 0:
            return 0
        elif not coin:
            return 0
        else:
            return coins_partitions(change, next_smaller_coin(coin)) + coins_partitions(change-coin, coin)
    return coins_partitions(change)


anonymous = True  # Change to True if you would like to remain anonymous on the final leaderboard.


def beaver(f):
    "*** YOUR CODE HERE ***"
    (lambda g: g(g(g(g(g(g(g(f))))))))(lambda f: lambda: f() or f() or f())()


def beaver_syntax_check():
    """
    Checks that definition of beaver is only one line.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> source = inspect.getsource(beaver)
    >>> num_comments = source.count('\\n    #')
    >>> contains_default_line = '"*** YOUR CODE HERE ***"' in source
    >>> num_lines = source.count('\\n') - num_comments
    >>> (num_lines == 2) or (num_lines == 3 and contains_default_line)
    True
    """
    # You don't need to edit this function. It's just here to check your work.


def beaver_run_test():
    """
    Checks to make sure f gets called at least 1000 times.

    >>> counter = 0
    >>> def test():
    ...     global counter
    ...     counter += 1
    >>> beaver(test)
    >>> counter >= 1000
    True
    """
    # You don't need to edit this function. It's just here to check your work.
