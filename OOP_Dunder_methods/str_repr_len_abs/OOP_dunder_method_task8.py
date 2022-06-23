from typing import NoReturn, Tuple


class Ingredient:
    def __init__(self, name: str, volume: float, measure: str) -> NoReturn:
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self) -> str:
        return f"{self.name}: {self.volume}, {self.measure}"


class Recipe:
    def __init__(self, *args) -> NoReturn:
        self.lst_ingrs = list(args)

    def add_ingredient(self, ing: Ingredient) -> NoReturn:
        self.lst_ingrs.append(ing)

    def remove_ingredient(self, ing: Ingredient) -> NoReturn:
        self.lst_ingrs.remove(ing)

    def get_ingredients(self) -> Tuple[Ingredient, ...]:
        return tuple(self.lst_ingrs)

    def __len__(self) -> int:
        return len(self.lst_ingrs)


def main() -> NoReturn:
    recipe = Recipe()
    recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
    recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
    recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
    ings = recipe.get_ingredients()
    n = len(recipe)  # n = 3
    print(n)


if __name__ == '__main__':
    main()