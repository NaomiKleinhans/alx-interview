#!/usr/bin/python3
"""Prime Game - Maria and Ben's prime number removal game."""


def isWinner(x, nums):
    """
    Determines the winner of the game.

    Args:
        x (int): Number of rounds to be played.
        nums (list): List of integers where each represents n for the round.

    Returns:
        str: Name of the player who won the most rounds (Maria or Ben).
        None: If there is no winner.
    """
    def sieve(n):
        """
        Generate a list of prime numbers up to n using the Sieve of Eratosthenes.

        Args:
            n (int): The limit up to which primes are generated.

        Returns:
            list: A list of prime numbers up to n.
        """
        primes = [True for _ in range(n+1)]
        primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n+1, p):
                    primes[i] = False
            p += 1
        return [i for i in range(n+1) if primes[i]]

    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    max_n = max(nums)  # Get the largest n to optimize prime generation
    primes_up_to_max = sieve(max_n)

    # Process each round
    for n in nums:
        primes_in_round = [p for p in primes_up_to_max if p <= n]
        moves = len(primes_in_round)  # The number of moves in this round
        if moves % 2 == 0:
            ben_wins += 1  # Even number of moves -> Ben wins
        else:
            maria_wins += 1  # Odd number of moves -> Maria wins

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    # Main script for testing
    isWinner = __import__('0-prime_game').isWinner

    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
