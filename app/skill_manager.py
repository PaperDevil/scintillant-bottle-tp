from scintillant.controllers import ContextUpdater


class States(ContextUpdater):

    def _initial_state_(self):
        """Execute when state is None"""
        super()._initial_state_()
