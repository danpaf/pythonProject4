import pytest


def multiply(a, b):
    return a * b


def sum(a, b):
    return a + b


def stepen(a, b):
    # Проверяем, является ли base нечетным числом
    if a % 2 != 0:
        # Возводим base в степень exponent
        result = a ** b
        return result
    else:

        return None



@pytest.fixture(params=[(2, 3, 6), (0, 5, 0), (-2, 4, -8)])
def data(request):
    return request.param


@pytest.fixture(params=[(2, 2, 4), (0, 5, 5), (-2, 4, 2)])
def sum_data(request):
    return request.param


@pytest.fixture(params=[(2, 3, 8), (3, 2, 9), (0, 5, None), (-2, 4, None)])
def stepen_data(request):
    return request.param




def test_multiply(data):
    a, b, expected_result = data
    result = multiply(a, b)
    assert result == expected_result


def test_sum(sum_data):
    a, b, expected_result = sum_data
    result = sum(a, b)
    assert result == expected_result


def test_stepen(stepen_data):
    a, b, expected_result = stepen_data
    result = stepen(a, b)
    assert result == expected_result
