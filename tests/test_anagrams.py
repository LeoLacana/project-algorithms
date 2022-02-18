from challenges.challenge_anagrams import is_anagram
import timeit


class RequirementViolated(Exception):
    pass


def valida_se_nao_foi_usado_sort_padrao():
    with open("challenges/challenge_anagrams.py", "r") as python_file:
        source = python_file.read()
        if "sorted(" in source or ".sort(" in source or "Counter(" in source:
            raise RequirementViolated(
                "Você deve fazer sua própria implementação "
                "do algoritmo de ordenação!"
            )


def test_validar_se_as_palavras_nao_sao_um_anagrama():
    valida_se_nao_foi_usado_sort_padrao()

    first_string = "pedra"
    second_string = "perdaaa"
    assert is_anagram(first_string, second_string) is False

    first_string = "pedrra"
    second_string = "pedraa"
    assert is_anagram(first_string, second_string) is False

    first_string = "pedra"
    second_string = "pedro"
    assert is_anagram(first_string, second_string) is False


def test_validar_se_as_palavras_sao_um_anagrama():
    valida_se_nao_foi_usado_sort_padrao()
    test_validar_se_as_palavras_nao_sao_um_anagrama()

    first_string = "pedra"
    second_string = "perda"
    assert is_anagram(first_string, second_string) is True


def test_valida_palavra_em_branco_retorna_false():
    valida_se_nao_foi_usado_sort_padrao()

    first_string = ""
    second_string = "perda"
    assert is_anagram(first_string, second_string) is False

    first_string = "perda"
    second_string = ""
    assert is_anagram(first_string, second_string) is False


def test_validar_tempo_anagrama():
    valida_se_nao_foi_usado_sort_padrao()

    setup_import = "from challenges.challenge_anagrams " "import is_anagram"
    first_string = (
        "Lorem ipsum dolor sit amet, consectetur "
        "adipiscing elit, do sed eiusmod tempor "
        "incididunt ut labore et dolore magna aliqua."
    )

    second_string = (
        "Lorem ipsum dolor sit amet, consectetur "
        "adipiscing elit, do sed eiusmod tempor "
        "incididunt ut labore et dolore magna aliqua."
    )
    algorithms_correct = is_anagram(first_string, second_string) is True
    time = timeit.timeit(
        f'is_anagram("{first_string}", "{second_string}")',
        setup=f"{setup_import}",
        number=10000,
    )
    correct_time = time <= 8.2
    assert (
        algorithms_correct and correct_time
    ), f"Falhou, o tempo foi: {time}, algoritmo correto? {algorithms_correct}"
