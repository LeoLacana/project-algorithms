from challenges.challenge_palindromes_iterative import is_palindrome_iterative
import timeit


def test_validar_se_a_palavra_e_um_palindromo_iterativo_retorna_true():
    word = "I"
    assert is_palindrome_iterative(word) is True
    word = "GG"
    assert is_palindrome_iterative(word) is True
    word = "ANA"
    assert is_palindrome_iterative(word) is True
    word = "ESSE"
    assert is_palindrome_iterative(word) is True
    word = "SOCOS"
    assert is_palindrome_iterative(word) is True
    word = "REVIVER"
    assert is_palindrome_iterative(word) is True


def test_validar_se_a_palavra_nao_e_um_palindromo_iterativo_retorna_false():
    word = "AGUA"
    assert is_palindrome_iterative(word) is False


def test_validar_se_nao_passar_palavra_iterativa_retorna_false():
    word = ""
    assert is_palindrome_iterative(word) is False


def test_validar_tempo_iterative():
    setup_import = (
        "from challenges.challenge_palindromes_iterative "
        "import is_palindrome_iterative"
    )
    word = "ANA"
    algorithms_correct = is_palindrome_iterative(word) is True
    time = timeit.timeit(
            'is_palindrome_iterative("ANA")',
            setup=f"{setup_import}",
            number=10000,
        )
    correct_time = time <= 0.005
    assert (
        algorithms_correct and correct_time
    ), f"Falhou, o tempo foi: {time}, algoritmo correto? {algorithms_correct}"
