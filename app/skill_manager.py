from http import HTTPStatus

from scintillant.controllers import ContextUpdater
from scintillant.textutils import RandomSentence, RandomPhrase


class States(ContextUpdater):

    def _initial_state_(self):
        """Execute when state is None"""
        self.response.text = RandomSentence(
            "<Welcome|Nice to see you|Hello>, first user of this template :)."
        ).generate()
        self.next_state = self.show_exit

    @ContextUpdater.statefunc
    def show_exit(self):
        """Show exit button"""
        self.response.text = "You can find more information of Scintillant framework in our github: " \
                                 "https://github.com/PaperDevil/scintillant"
        self.next_state = self.choose_counter

    @ContextUpdater.statefunc
    def choose_counter(self):
        """Choose counter"""
        self.response.text = str(RandomPhrase(
            "{parting}, user!", parting=['See ya nex time', 'Goodbye', 'See you soon']
        ))
        self.response.status = HTTPStatus.RESET_CONTENT
        self.next_state = None
