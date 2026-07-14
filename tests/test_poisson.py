from src.poisson import score_matrix



def test_score_matrix():

    matrix = score_matrix(
        1.5,
        1.2
    )


    assert matrix.shape[0] > 0

    assert matrix.sum() > 0.99