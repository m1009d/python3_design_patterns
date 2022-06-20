
"""Model-View-Controller python design pattern."""


from typing import Tuple, Union


# data here represent a simple database like object
quotes = [
    "It's not about ideas. It's about making ideas happen.",
    'Always deliver more than expected.',
    'The most courageous act is still to think for yourself. Aloud.',
    'What would you do if you were not afraid?',
    'Nothing will work unless you do.',
    'Surround yourself with only people who are going to lift you higher.'
]


class Model:

    def validate_num(self, num: Union[str, int]) -> Tuple[int, str]:
        try:
            num = int(num)
        except ValueError:
            return 1, 'Invalid output'
        if num == 0:
            return 1, '0 index is not supported'
        if num < 0:
            return 1, 'negative index is not supported'
        if num > len(quotes):
            return 1, f'max number is {len(quotes)}'
        return 0, 'OK'

    def get_quote(self, num: Union[str, int]) -> Tuple[int, str]:
        # model contains also data validation logic
        code, msg = self.validate_num(num)
        if code != 0:
            return code, msg
        try:
            return 0, quotes[int(num) - 1]
        except IndexError:
            return 1, 'Not found'

    def add_quote(self, quote: str) -> Tuple[int, str]:
        try:
            quotes.append(quote)
        except Exception as err:
            return 1, str(err)
        return 0, 'OK'

    def del_quote(self, idx: Union[str, int]) -> Tuple[int, str]:
        code, msg = self.validate_num(idx)
        if code != 0:
            return code, msg
        try:
            del_quote = quotes.pop(int(idx) - 1)
        except ValueError:
            return 1, 'Invalid input'
        except IndexError:
            return 1, 'Not found'
        return 0, f'Quote {del_quote!r} deleted'


class View:

    @property
    def ask_user(self) -> str:
        return input('''
        What would you like to do:

        1 - Select a quote
        2 - Add a new quote
        3 - Delete an already existing quote
        4 - Exit: ''')

    @property
    def select_quote(self) -> str:
        return input('Please provide a quote number: ')

    @property
    def del_quote(self) -> str:
        return input('Please provide a quote number to delete: ')

    @property
    def add_quote(self) -> str:
        return input('Please provide a quote to add: ')

    def show(self, quote: str) -> None:
        print(quote)

    def error(self, error: str) -> None:
        print(f'ERROR: {error}')


class Controller:

    def __init__(self, view: View, model: Model) -> None:
        self.view = view
        self.model = model

    def run(self) -> None:

        while True:

            try:
                user_choice = int(self.view.ask_user)
            except ValueError:
                self.view.error('Invalid input')
                continue

            if user_choice == 1:
                code, msg = self.model.get_quote(self.view.select_quote)
            elif user_choice == 2:
                code, msg = self.model.add_quote(self.view.add_quote)
            elif user_choice == 3:
                code, msg = self.model.del_quote(self.view.del_quote)
            elif user_choice == 4:
                self.view.show('Bye')
                break
            else:
                self.view.error('Invalid input')
                continue

            if code != 0:
                self.view.error(msg)
            else:
                self.view.show(msg)


def main() -> int:
    view = View()
    model = Model()
    controller = Controller(view=view, model=model)
    controller.run()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
