import sys
import pytest
from challenges.challenge_palindromes_recursive import is_palindrome_recursive


@pytest.fixture
def is_recursive():
    sys.setrecursionlimit(100)
    try:
        word = "A" * 200
        is_palindrome_recursive(word, 0, len(word) - 1)
    except RecursionError:
        pass
    else:
        pytest.fail("O algoritimo deve ser recursivo.")


def test_validar_se_a_palavra_e_um_palindromo_retorna_true(is_recursive):
    word = "I"
    assert is_palindrome_recursive(word, 0, len(word) - 1) is True
    word = "GG"
    assert is_palindrome_recursive(word, 0, len(word) - 1) is True
    word = "ANA"
    assert is_palindrome_recursive(word, 0, len(word) - 1) is True
    word = "ESSE"
    assert is_palindrome_recursive(word, 0, len(word) - 1) is True
    word = "SOCOS"
    assert is_palindrome_recursive(word, 0, len(word) - 1) is True
    word = "REVIVER"
    assert is_palindrome_recursive(word, 0, len(word) - 1) is True


def test_validar_se_a_palavra_nao_e_um_palindromo_retorna_false(is_recursive):
    word = "AGUA"
    assert is_palindrome_recursive(word, 0, len(word) - 1) is False


def test_validar_se_nao_passar_palavra_retorna_false(is_recursive):
    word = ""
    assert is_palindrome_recursive(word, 0, len(word) - 1) is False
