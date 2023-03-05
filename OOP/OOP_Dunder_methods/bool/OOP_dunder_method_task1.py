from dataclasses import dataclass


@dataclass
class Player:
    """Class player containing names age and league points."""

    name: str
    old: int
    score: int

    def __post_init__(self) -> None:
        self.score = int(self.score)
        self.old = int(self.old)

    def __bool__(self) -> bool:
        return self.score > 0


def main() -> None:
    # list of all players
    lst_in = ["Балакирев; 34; 2048",
              "Mediel; 27; 0",
              "Влад; 18; 9012",
              "Nina P; 33; 0"
              ]
    # list of objects player
    players = [Player(*string.split('; ')) for string in lst_in]

    # filtered list of players who have leagues > 0
    players_filtered = list(filter(bool, players)) # Балакирев, Влад

    for i in players_filtered:
        print(i.name)


if __name__ == '__main__':
    main()
