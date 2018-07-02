import pytest

nums = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

def err_checker(func):
    def wrapper(data):
        data = str(data)
        data = data.split()
        if len(data) == 0:
            return 'wrong args number'
        try:
            data[0] = int(data[0])
        except:
            return 'first arg is not a digit'
        if data[0] < 0 or data[0] > 9:
            return 'first arg is not a digit'
        if len(data) == 2:
            if data[1] not in ['bin', 'oct', 'hex']:
                return 'wrong conversion type'
        if len(data) > 2:
            return 'wrong args number'
        return func(data)
    return wrapper


@err_checker
def handler(data):
    if len(data) == 1:
        return nums[data[0]]
    if len(data) == 2:
        number = int(data[0])
        conv = data[1]
        if conv == 'bin':
            return bin(number)
        if conv == 'oct':
            return oct(number)
        if conv == 'hex':
            return hex(number)

def test_print():
    assert handler('0') == 'zero'
    assert handler(9) == 'nine'
    assert handler('-1') == 'first arg is not a digit'
    assert handler('10') == 'first arg is not a digit'
    assert handler('') == 'wrong args number'

def test_conv():
    assert handler('1 2') == 'wrong conversion type'
    assert handler('1 2 3') == 'wrong args number'
    assert handler('1 bin 3') == 'wrong args number'
    assert handler('10 bin 3') == 'first arg is not a digit'
    assert handler('9 bin') == '0b1001'
    assert handler('0 oct') == '0o0'
    assert handler('8 hex') == '0x8'

if __name__ == '__main__':
    data = input('input digit or number with space-separated conversion type: ')

    test_print()
    test_conv()
    print(handler(data))
