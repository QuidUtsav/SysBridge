from execution.dry_run import dry_run

class ActionExecutor:
    def __init__(self, policy_guard=None):
        self.policy_guard = policy_guard
        
    def execute(self,action,confirm:bool =False):
        
        preview = dry_run(action)
        
        if self.policy_guard:
            self.policy_guard.check(action)
        
        if action.requires_cofirmation and not confirm:
            return{
                "status":"confirmation_required",
                "preview":preview
            }
            
        result= action.execute()
        
        return{
            "status":"executed",
            "result":result
        }
