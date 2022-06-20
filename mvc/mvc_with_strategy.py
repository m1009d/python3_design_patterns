#!/usr/bin/env python3

import uuid
from abc import ABC, abstractmethod
import tkinter as tk
import random
import string
from typing import Dict, Callable


class Model():
    uuid = []


class Controller(ABC):

    buttons: Dict[str, Callable]

    @abstractmethod
    def start(self) -> None:
        ...

    @abstractmethod
    def handle_button(self, button_name: str) -> None:
        ...

    @abstractmethod
    def handle_click_clear_list(self) -> None:
        ...


class View(ABC):

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def append_to_list(self):
        pass

    @abstractmethod
    def clear_list(self):
        pass

    @abstractmethod
    def start_main_loop(self):
        pass


class TkView(View):
    # All User Interface stuff

    def setup(self, controller: Controller):
        # setup tkiner
        self.root = tk.Tk()
        self.root.geometry('400x400')
        self.root.title('UUIDGen')

        # create the GUI
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)
        self.label = tk.Label(self.frame, text='Result:')
        self.label.pack()
        self.list = tk.Listbox(self.frame)
        self.list.pack(fill=tk.BOTH, expand=1)
        for button_name in controller.buttons:
            button_name_optimized = button_name.replace(' ', '')
            self.__setattr__(
                button_name_optimized,
                tk.Button(
                    self.frame,
                    text=button_name,
                    command=lambda m=button_name: controller.handle_button(m),
                )
            )
            self.__getattribute__(button_name_optimized).pack()

        self.clear_button = tk.Button(
            self.frame,
            text='Clear List',
            command=controller.handle_click_clear_list
        )
        self.clear_button.pack()

    # Interaction in the user interface
    def append_to_list(self, item):
        self.list.insert(tk.END, item)

    # Interaction in the user interface
    def clear_list(self) -> None:
        self.list.delete(0, tk.END)

    # Show the user interface to the user - start the main loop
    def start_main_loop(self):
        self.root.mainloop()


# Strategy pattern (different strategies)
def generate_uuid1() -> uuid.UUID:
    return uuid.uuid1()

def generate_uuid4() -> uuid.UUID:
    return uuid.uuid4()

def generate_simple_string() -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=30))

def generate_name() -> str:
    names = [
        'John',
        'Michal',
        'Penny'
    ]
    return ''.join(random.choices(names))


class MyController(Controller):

    def __init__(self, view: TkView, model: Model, buttons: Dict[str, Callable]) -> None:
        self.view = view
        self.model = model
        self.buttons = buttons

    def start(self) -> None:
        self.view.setup(self)
        self.view.start_main_loop()

    def handle_button(self, button_name: str) -> None:
        # generate a uuid and add it to the list
        self.model.uuid.append(self.buttons[button_name]())
        self.view.append_to_list(self.model.uuid[-1])

    def handle_click_clear_list(self) -> None:
        # Clear the list of UUIDs in the user interface
        self.model.uuid = []
        self.view.clear_list()


def main() -> int:
    buttons = {
        'Generate UUID1':  generate_uuid1,
        'Generate UUID4':  generate_uuid4,
        'Generate string': generate_simple_string,
        'Generate Name':   generate_name,
    }
    controller = MyController(TkView(), Model(), buttons)
    controller.start()

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
