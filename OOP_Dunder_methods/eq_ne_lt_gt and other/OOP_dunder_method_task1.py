from typing import NoReturn, Union, Tuple, Any


class TrackLine:
    to_x: Union[int, float]
    to_y: Union[int, float]
    max_speed: int

    def __init__(self,
                 to_x: Union[int, float],
                 to_y: Union[int, float],
                 max_speed: int) -> NoReturn:

        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:
    start_x: Union[int, float]
    start_y: Union[int, float]

    def __init__(self, start_x: Union[int, float] = 0, start_y: Union[int, float] = 0):
        self.start_x = start_x
        self.start_y = start_y
        self.track_list = []

    def add_track(self, tr: TrackLine) -> NoReturn:
        """Add new track into the track_list"""
        if isinstance(tr, TrackLine):
            self.track_list.append(tr)

    def get_tracks(self) -> Tuple[Any, ...]:
        """Get tuple of TrackLine"""
        return tuple(self.track_list)

    def __len__(self) -> int:
        """Return total track length"""
        tmp_lst = self.track_list[:]
        tmp_lst.insert(0, TrackLine(self.start_x, self.start_y, 0))
        res = 0
        for i in range(1, len(tmp_lst)):
            res += ((tmp_lst[i].to_x - tmp_lst[i-1].to_x) ** 2 +
                    (tmp_lst[i].to_y - tmp_lst[i-1].to_y) ** 2) ** 0.5
        return int(res)

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.__len__() == sc

    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.__len__() > sc

    @classmethod
    def __verify_data(cls, other):
        """Return total track length or Track"""
        if not isinstance(other, (int, Track)):
            raise TypeError("Операнд справа должен иметь тип int или TrackLine")

        return other.__len__() if isinstance(other, Track) else other


def main():
    track1, track2 = Track(), Track(0, 1)
    track1.add_track(TrackLine(2, 4, 100))
    track1.add_track(TrackLine(5, -4, 100))
    track2.add_track(TrackLine(3, 2, 90))
    track2.add_track(TrackLine(10, 8, 90))
    res_eq = track1 == track2
    print(track1 > track2)

if __name__ == '__main__':
    main()