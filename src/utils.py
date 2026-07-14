from math import factorial, exp


def poisson_probability(lmbda, goals):

    return (
        exp(-lmbda)
        *
        (lmbda ** goals)
        /
        factorial(goals)
    )


def clamp(value, minimum, maximum):

    return max(minimum, min(value, maximum))