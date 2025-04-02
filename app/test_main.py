import pytest
from app.main import get_coin_combination

class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cent_element, expected_list_of_cents",  # Тут має бути кортеж
        [
            pytest.param(
                -1,
                [0, 0, 0, 0],
                id="test should return list of 0 because number is negative",
            ),
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="test should return list of 0 because number is zero",
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],  # corrected this line
                id="test should return first element of list 1 because 1penny = 1cent",
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="test should return first and second element of list 1 because 1penny = 1cent and 1nikel = 5 cent",
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="test should return first element 2 and second third elements 1 because 1penny = 1cent and 1nikel = 5 cent and 1dime = 10cent",
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="test should return fourth element 2 because 1quarter = 25cent",
            ),
        ]
    )
    def test_get_coin_combination(self, cent_element, expected_list_of_cents):
        assert get_coin_combination(cent_element) == expected_list_of_cents

class TestCatchTheRaise:
    @pytest.mark.parametrize(
        "element_error, expected_error",
        [
            pytest.param(
            "1",
            TypeError,
            ),
        ]
    )

    def test_catch_the_raise(self, element_error, expected_error):
        with pytest.raises(expected_error):
            get_coin_combination(element_error)
