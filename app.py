from actions.filesystem import GetTimeAction,GetBatteryAction,ListDirectoryAction,OpenFileAction,OpenFolderAction,LaunchAppAction
from execution.executor import ActionExecutor
from policy.guard import PolicyGuard
from policy.filesystem_guard import FileSystemGuard
fs_guard = FileSystemGuard(
    allowed_roots=[
        "/home/user/Desktop/allowed_folder",
        "/home/user/Documents"
    ]
)

policy_guard = PolicyGuard(fs_guard=fs_guard)

executor = ActionExecutor(policy_guard=policy_guard)

executor = ActionExecutor(policy_guard=policy_guard)

action = LaunchAppAction(app="firefox")
result = executor.execute(action, confirm=True)
print(result)

