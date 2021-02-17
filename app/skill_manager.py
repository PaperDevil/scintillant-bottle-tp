from scintillant.controllers import ContextUpdater


class States(ContextUpdater):

    def _initial_state_(self):
        """Execute when state is None"""
        super()._initial_state_()
        self.response.out_text = "Напишите что-то, чтобы перейти на следующий шаг"
        self.next_state = self.show_exit

    @ContextUpdater.statefunc
    def show_exit(self):
        """Show exit button"""
        self.response.out_text = "Вы можете закончить общение нажав на кнопку"
        self.response.choices = [
            ['Выход', 'exit'],
            ['Выбрать счётчик', 'choose_counter']
        ]
        self.next_state = self.choose_counter

    @ContextUpdater.statefunc
    def choose_counter(self):
        """Choose counter"""
        self.response.out_text = "Выберите счётчик"
        self.response.choices = [
            ['312', '312'],
            ['581', '581']
        ]
        self.next_state = None
