from actions.filesystem import GetBatteryAction, GetTimeAction, ListDirectoryAction, OpenFileAction, OpenFolderAction


REGISTERED_ACTIONS = {
   "system.get_time": GetTimeAction,
  "system.get_battery": GetBatteryAction,
  "fs.list_directory": ListDirectoryAction,   
    "fs.open_file": OpenFileAction,
    "fs.open_folder": OpenFolderAction
}

def create_action_instance(action_name: str, **kwargs) :
    if action_name not in REGISTERED_ACTIONS:
        raise ValueError(f"Action '{action_name}' is not registered.")
    
    action_class = REGISTERED_ACTIONS[action_name]
    return action_class(**kwargs)
    