def get_coin_combination(cents: int) -> list:
    values = [1, 5, 10, 25]
    coins = [0, 0, 0, 0]

    for i in range(3, -1, -1):
        if cents < 0:
            return [0, 0, 0, 0]
        else:
            coins[i] = cents // values[i]
            cents -= coins[i] * values[i]

    return coins
