from challenges.challenge_study_schedule import study_schedule
import timeit


def test_validar_melhor_horario_com_sucesso():
    permanence_periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    assert study_schedule(permanence_periods, 5) == 3
    assert study_schedule(permanence_periods, 4) == 3
    assert study_schedule(permanence_periods, 3) == 2
    assert study_schedule(permanence_periods, 2) == 4
    assert study_schedule(permanence_periods, 1) == 2


def test_validar_permanence_periods_com_entradas_invalidas():
    permanence_periods = [(4, None), ("0", 4)]
    target_time = 4
    assert study_schedule(permanence_periods, target_time) is None

    permanence_periods = [("A", 9), (None, 5)]
    target_time = 6
    assert study_schedule(permanence_periods, target_time) is None


def test_validar_target_time_com_vazio():
    permanence_periods = [(1, 5), (2, 4), (3, 3), (4, 4), (5, 5)]
    target_time = None
    assert study_schedule(permanence_periods, target_time) is None


def test_validar_tempo_schedule():
    permanence_periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    algorithms_correct = study_schedule(permanence_periods, 5) == 3
    setup_import = (
        "from challenges.challenge_study_schedule " "import study_schedule"
    )
    time = timeit.timeit(
        f"study_schedule({permanence_periods}, 5)",
        setup=f"{setup_import}",
        number=10000,
    )
    correct_time = time <= 0.02
    assert (
        algorithms_correct and correct_time
    ), f"Falhou, o tempo foi: {time}, algoritmo correto? {algorithms_correct}"
