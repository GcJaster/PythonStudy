from typing import List


class StringText:
    lst_words: List[str]

    def __init__(self, lst_words: List[str]) -> None:
        self.lst_words = lst_words

    def __le__(self, other) -> bool:
        return len(self.lst_words) <= len(other)

    def __lt__(self, other) -> bool:
        return len(self.lst_words) <= len(other)

    def __len__(self) -> int:
        return len(self.lst_words)

    def join(self) -> str:
        return ' '.join(self.lst_words)

    @staticmethod
    def strip(txt) -> List[str]:
        return ''.join([c for c in txt if c not in "–?!,.;"]).split()


def main() -> None:
    stich = ["Я к вам пишу – чего же боле?",
             "Что я могу еще сказать?",
             "Теперь, я знаю, в вашей воле",
             "Меня презреньем наказать.",
             "Но вы, к моей несчастной доле",
             "Хоть каплю жалости храня,",
             "Вы не оставите меня."]

    stich = list(map(StringText.strip, stich))
    lst_text = [StringText(e) for e in stich]
    lst_text_sorted = sorted(lst_text, key=len, reverse=True)
    lst_text_sorted = [x.join() for x in lst_text_sorted]
    print(lst_text_sorted)

if __name__ == '__main__':
    main()

