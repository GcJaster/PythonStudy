class VideoRating:
    """Class describing video rating """

    def __init__(self, rating: int = 0) -> None:
        self.__check_rating_val(rating)
        self.__rating = rating

    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, new_rating: int) -> None:
        self.__check_rating_val(new_rating)
        self.__rating = new_rating

    @staticmethod
    def __check_rating_val(value):
        if not (0 <= value <= 5):
            raise ValueError('неверное присваиваемое значение')


class VideoItem:
    """Class describing the video"""
    def __init__(self, title: str, descr: str, path: str) -> None:
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


def main() -> None:
    v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
    print(v.rating.rating)  # 0
    v.rating.rating = 5
    print(v.rating.rating)  # 5
    title = v.title
    descr = v.descr
    print(title, descr)
    # v.rating.rating = 6  # ValueError


if __name__ == '__main__':
    main()