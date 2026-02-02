

class PolicyGuard:
    def __init__(self,fs_guard=None):
        self.fs_guard = fs_guard
    
    def check(self,action,*,confirmed:bool=False):
        if action.risk_level =="high":
            raise PermissionError("High risk actions are not permitted.")
        
        if action.requires_confirmation and not confirmed:
            raise PermissionError("Action requires confirmation before execution.")
        
        if hasattr(action,"path") and self.fs_guard:
            self.fs_guard.validate_path(action.path)
        
        return True