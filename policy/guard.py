

class PolicyGuard:
    def __init__(self,fs_guard=None):
        self.fs_guard = fs_guard
    
    def check(self,action,*,confirmed:bool=False):
        if action.risk_level =="high":
            raise PermissionError("High risk actions are not permitted.")
        
        if action.requires_confirmation and not confirmed:
            raise PermissionError("Action requires confirmation before execution.")
        
        if self.fs_guard and action.params:
            path_keys = [ "file_path", "folder_path", "directory", "path"]
            for key in path_keys:
                if key in action.params:
                    self.fs_guard.validate_path(action.params[key])

        return True