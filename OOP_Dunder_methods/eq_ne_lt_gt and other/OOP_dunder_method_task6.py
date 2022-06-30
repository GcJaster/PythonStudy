from __future__ import annotations
from dataclasses import dataclass
from typing import Union


class CentralBank:
    """Bank for storing currency wallets."""

    rates: dict = None

    def __new__(cls, *args, **kwargs) -> None:
        return None

    @classmethod
    def register(cls, money: Union[MoneyD, MoneyE, MoneyR]) -> None:
        if isinstance(money, (MoneyD, MoneyE, MoneyR)):
            money.cb = cls


@dataclass
class Wallet:
    """Currency wallet for storage in a bank."""

    __volume: Union[int, float] = 0
    __cb: CentralBank = None
    name: str = None

    @property
    def volume(self) -> Union[int, float]:
        """Return volume of currency wallet."""
        return self.__volume

    @volume.setter
    def volume(self, new_volume) -> None:
        """Set new currency wallet volume."""
        if isinstance(new_volume, (int, float)):
            self.__volume = new_volume

    @property
    def cb(self) -> Union[CentralBank, None]:
        """Return link of the wallet to the bank."""
        return self.__cb

    @cb.setter
    def cb(self, new_cb) -> None:
        """Link wallet to bank."""
        self.__cb = new_cb

    def __eq__(self, other: Union[MoneyE, MoneyR, MoneyD]) -> bool:
        other.__verify_reg_bank()
        return self.__convert_rub(self) == self.__convert_rub(other)

    def __le__(self, other: Union[MoneyE, MoneyR, MoneyD]) -> bool:
        other.__verify_reg_bank()
        return self.__convert_rub(self) <= self.__convert_rub(other)

    def __lt__(self, other: Union[MoneyE, MoneyR, MoneyD]) -> bool:
        other.__verify_reg_bank()
        return self.__convert_rub(self) <= self.__convert_rub(other)

    @staticmethod
    def __convert_rub(obj: Union[Wallet, MoneyE, MoneyR, MoneyD]) -> Union[int, float]:
        """Сurrency conversion into ruble."""
        return obj.volume * obj.cb.rates['rub'] / obj.cb.rates[obj.name]

    def __verify_reg_bank(self) -> None:
        """Verification of wallet registration in the bank."""
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")


@dataclass
class MoneyD(Wallet):
    name: str = 'dollar'


@dataclass
class MoneyE(Wallet):
    name: str = 'euro'


@dataclass
class MoneyR(Wallet):
    name: str = 'rub'


def main() -> None:
    CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
    r = MoneyR(70)
    d = MoneyD(1)
    e = MoneyE(1.25)
    CentralBank.register(r)
    CentralBank.register(d)
    CentralBank.register(e)
    print(r == e)
    print(r < d)
    print(e == d)
    if e == r:
        print("неплохо")
    else:
        print("нужно поднажать")


if __name__ == '__main__':
    main()