from pathlib import Path
from FriendlyHandbook_kobSK import sort_folder
from FriendlyHandbook_kobSK.adbook import run_addressbook
from FriendlyHandbook_kobSK.note_book import run_notebook
from FriendlyHandbook_kobSK.calculator import main
import FriendlyHandbook_kobSK.sort_folder


def run_folder():
    folder_path = input("Введіть шлях до теки для сортування: ")
    FriendlyHandbook_kobSK.sort_folder.main(Path(folder_path))
    return "Сортування завершено успішно"

def run_adbook():
    run_addressbook()
    return "Книга контактів завершено успішно"
def calc():
    main()
    return "Калькулятор завершено успішно"

def run_nbook():
    run_notebook()
    return "Нотатки завершено успішно"



bot_command_dict = {
    "1": run_adbook,
    "2": run_nbook,
    "3": run_folder,
    "4": calc,
}


def assistant_bot():
    print("Вас вітає персональний помічник FriendlyHandbook")
    print(
        """
    Виберіть одну з наступних опцій:
    - Книга контактів (PhoneBook) -> Натисніть '1'
    - Нотатки (NoteBook) -> Натисніть '2'
    - Сортувач папок (CleanFolder) -> Натисніть '3'
    - Калькулятор (Calculator) -> Натисніть '4'
    - Вийти з помічника -> Натисніть '0'
    """
    )

    while True:

        command = input("Введіть номер опції (від 0 до 4): ")

        if command == "0":
            raise SystemExit("\nДо побачення!\n")

        elif command in bot_command_dict.keys():
            handler = bot_command_dict[command]
            answer = handler()
            print(answer)

        else:
            print("Некоректне число. Будь ласка, введіть число від 0 до 4")


if __name__ == "__main__":
    assistant_bot()

