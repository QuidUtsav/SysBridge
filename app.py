from actions.filesystem import OpenFileAction
from execution.executor import ActionExecutor

action = OpenFileAction(filepath="readme.md")

executor = ActionExecutor()
result = executor.execute(action, confirm=True)

print(result)
