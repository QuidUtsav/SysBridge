from actions.base import GetBatteryAction, GetTimeAction, ListDirectoryAction, OpenFileAction, OpenFolderAction


REGISTERED_ACTIONS = {
   "system.get_time": GetTimeAction,
  "system.get_battery": GetBatteryAction,
  "fs.list_directory": ListDirectoryAction,   
    "fs.open_file": OpenFileAction,
    "fs.open_folder": OpenFolderAction
}

def execute_action(action_name: str) :
    if action_name in REGISTERED_ACTIONS:
            return REGISTERED_ACTIONS[action_name]()

