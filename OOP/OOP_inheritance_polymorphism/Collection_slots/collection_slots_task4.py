class Note:
    _cyrillic_notes = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')

    def __init__(self, name: str, ton: int):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name' and value not in self._cyrillic_notes:
            raise ValueError('недопустимое значение аргумента')
        if key == '_ton' and value not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')
        object.__setattr__(self, key, value)


class Notes:
    __instance = None
    __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'
    _cyrillic_notes = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        Notes.__instance = None

    def __init__(self):
        for k, v in zip(self.__slots__, self._cyrillic_notes):
            setattr(self, k, Note(v, 0))

    def __getitem__(self, item):
        self.__check(item)
        return getattr(self, self.__slots__[item])

    def __check(self, item):
        if type(item) != int or not(0 <= item < len(self.__slots__)):
            raise IndexError('недопустимый индекс')

if __name__ == '__main__':
    notes = Notes()
    nota = notes[2]  # ссылка на ноту ми
    notes[3]._ton = -1  # изменение тональности ноты фа







