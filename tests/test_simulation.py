from src.simulation import simulate_matches



def test_simulation():


    result = simulate_matches(

        1.5,

        1.2,

        1900,

        1850,

        simulations=10000

    )


    assert (
        result["home_qualification"]
        +
        result["away_qualification"]
    ) == 1