from enum import Enum

# Read input data
with open("day_2/input.txt", "r") as f:
    games = f.read().splitlines()
games = [game.split() for game in games]


class Moves(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcomes(Enum):
    WIN = 6
    LOOSE = 0
    DRAW = 3


move_codes = {
    "A": Moves.ROCK,
    "B": Moves.PAPER,
    "C": Moves.SCISSORS,
    "X": Moves.ROCK,
    "Y": Moves.PAPER,
    "Z": Moves.SCISSORS,
}

outcome_codes = {
    "X": Outcomes.LOOSE,
    "Y": Outcomes.DRAW,
    "Z": Outcomes.WIN,
}


def rock_paper_scissors(opponent_move: Moves, player_move: Moves) -> Outcomes:
    if player_move == Moves.PAPER:
        if opponent_move == Moves.PAPER:
            return Outcomes.DRAW
        elif opponent_move == Moves.ROCK:
            return Outcomes.WIN
        else:
            return Outcomes.LOOSE
    elif player_move == Moves.ROCK:
        if opponent_move == Moves.PAPER:
            return Outcomes.LOOSE
        elif opponent_move == Moves.ROCK:
            return Outcomes.DRAW
        else:
            return Outcomes.WIN
    else:
        if opponent_move == Moves.PAPER:
            return Outcomes.WIN
        elif opponent_move == Moves.ROCK:
            return Outcomes.LOOSE
        else:
            return Outcomes.DRAW


def compute_game_score(opponent_move, player_move):
    return player_move.value + rock_paper_scissors(opponent_move, player_move).value


def compute_score_part_1(game, move_codes) -> int:
    opponent_move = move_codes.get(game[0])
    player_move = move_codes.get(game[1])
    return compute_game_score(opponent_move, player_move)


def get_move_for_outcome(opponent_move, outcome) -> Moves:
    if opponent_move == Moves.PAPER:
        if outcome == Outcomes.WIN:
            return Moves.SCISSORS
        elif outcome == Outcomes.LOOSE:
            return Moves.ROCK
        else:
            return Moves.PAPER
    elif opponent_move == Moves.ROCK:
        if outcome == Outcomes.WIN:
            return Moves.PAPER
        elif outcome == Outcomes.LOOSE:
            return Moves.SCISSORS
        else:
            return Moves.ROCK
    else:
        if outcome == Outcomes.WIN:
            return Moves.ROCK
        elif outcome == Outcomes.LOOSE:
            return Moves.PAPER
        else:
            return Moves.SCISSORS


def compute_score_part_2(game, outcome_codes) -> int:
    opponent_move = move_codes.get(game[0])
    player_move = get_move_for_outcome(opponent_move, outcome_codes.get(game[1]))
    return compute_game_score(opponent_move, player_move)


# Part 1
print(f"Part 1: answer is: {sum([compute_score_part_1(game, move_codes) for game in games])}")
# Part 2
print(f"Part 2: answer is: {sum([compute_score_part_2(game, outcome_codes) for game in games])}")