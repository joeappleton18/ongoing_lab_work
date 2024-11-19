import data_wizard

from .models import Board, Label, List, Project, Task

data_wizard.register(Task)
data_wizard.register(List)
data_wizard.register(Board)
data_wizard.register(Project)
data_wizard.register(Label)
