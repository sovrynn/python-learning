ERR_MSG_BASE = 'Test failed: '
ERR_MSG_WRONG_TYPE = ERR_MSG_BASE + 'Types don\'t match: Expected type %s, but got type %s.'
ERR_MSG_WRONG_STR_VALUE = ERR_MSG_BASE + 'Expected \'%s\', but got \'%s\'.'
ERR_MSG_WRONG_VALUE = ERR_MSG_BASE + 'Expected %s, but got %s.'
SUCCESS_MSG = 'Test passed.'


def test_equals(actual, expected):
    if not actual == expected:
        raise_error(actual, expected)
    else:
        print(SUCCESS_MSG)


def raise_error(actual, expected):
    if not type(actual) is type(expected):
        raise TestFailureException(ERR_MSG_WRONG_TYPE % (type(expected), type(actual)))
    else:
        if isinstance(expected, str):
            raise TestFailureException(ERR_MSG_WRONG_STR_VALUE % (expected, actual))
        else:
            raise TestFailureException(ERR_MSG_WRONG_VALUE % (expected, actual))


class TestFailureException(Exception):
    pass
