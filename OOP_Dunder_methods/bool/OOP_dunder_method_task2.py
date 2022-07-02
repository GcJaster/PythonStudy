from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class MailBox:
    """Reception of the list of lines and turning them into objects of the MailItem class"""
    inbox_list: List[MailItem] = field(default_factory=list)

    def receive(self, lst: [str]):
        """Creating a MailItem list from a lines list and return."""
        mails = lst
        for mail in mails:
            address, title, content = map(str.strip, mail.split(';'))
            self.inbox_list.append(MailItem(address, title, content))
        return self


@dataclass
class MailItem:
    """Class for creating a letter."""

    mail_from: str
    title: str
    content: str
    is_read: bool = field(default=False, init=False)

    def __bool__(self) -> bool:
        return self.is_read

    def set_read(self, fl_read: bool) -> None:
        """Set the status of the letter - read or not."""
        self.is_read = fl_read


def main() -> None:
    test_lst = ["sc_lib@list.ru; От Балакирева; Успехов в IT!",
                "mail@list.ru; Выгодное предложение; Вам одобрен кредит.",
                "mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить."
                ]

    # get list of MailItem
    mail = MailBox().receive(test_lst)

    for i in (0, -1):  # set read for first and last message
        mail.inbox_list[i].set_read(True)
    inbox_list_filtered = list(filter(bool, mail.inbox_list))

    for mail in inbox_list_filtered:
        print(mail.content)


if __name__ == '__main__':
    main()
