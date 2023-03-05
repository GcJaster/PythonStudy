class Morph:
    def __init__(self, *args) -> None:
        self.lst_words = list(args)

    def add_word(self, word: str) -> None:
        if word not in self.lst_words:
            self.lst_words.append(word)

    def get_words(self) -> tuple:
        return tuple(self.lst_words)

    def __eq__(self, other) -> bool:
        return True if other.lower() in self.lst_words else False


def main() -> None:
    dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
                  Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                        'формулах'),
                  Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                        'векторами', 'векторах'),
                  Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                        'эффектами', 'эффектах'),
                  Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')]

    text = 'Мы будем устанавливать связь завтра днем.'
    count = 0
    for i in text.lower().strip('.,!? :').split():
        for j in dict_words:
            if i in j.get_words():
                count += 1
    print(count)


if __name__ == '__main__':
    main()