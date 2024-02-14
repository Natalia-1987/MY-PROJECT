import allure
import pytest

"""Пишем обычный тест с параметризацией"""


@allure.parent_suite('parent_suite - Browser')
@allure.feature('Simple additional func')
@pytest.mark.parametrize("a, b, expected_result", [(1, 2, 3), (5, 5, 11), (0, 0, 0)])
def test_addition_parametrization(a, b, expected_result):
    result = a + b
    assert result == expected_result, f"Expected result: {expected_result}, but got {result}"






