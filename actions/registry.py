from actions.base import GetBatteryAction, GetTimeAction, ListDirectoryAction, OpenFileAction, OpenFolderAction


REGISTERED_ACTIONS = {
   "system.get_time": GetTimeAction,
  "system.get_battery": GetBatteryAction,
  "fs.list_directory": ListDirectoryAction,   
    "fs.open_file": OpenFileAction,
    "fs.open_folder": OpenFolderAction
}

def execute_action(action_name: str) :
    for name, action in REGISTERED_ACTIONS.items():
        if name == action_name:
            return action.execute()

