from actions.registry import create_action_instance

from actions.base import OpenFileAction

action = OpenFileAction()
print(action.name)
print(action.risk_level)
print(action.requires_confirmation)
print(action.reversible)