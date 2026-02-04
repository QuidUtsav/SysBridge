from click import confirm
from execution.dry_run import dry_run
from datetime import datetime

class ActionLogger:
    def log(self, *, action, status, message=""):
        timestamp = datetime.utcnow().isoformat()
        entry = f"[{timestamp}] {action.name} | {status} | {message}\n"

        with open("logs/actions.log", "a") as f:
            f.write(entry)

class ActionExecutor:
    def __init__(self, policy_guard=None,logger = None):
        self.policy_guard = policy_guard
        self.logger = logger
        
    def execute(self,action,confirm:bool =False):
        
        preview = dry_run(action)
        try:
            if self.policy_guard:
                self.policy_guard.check(action,confirmed=confirm)
                            
            result= action.execute()
            if self.logger:
                self.logger.log(action=action, status="SUCCESS")
                
            return{
                "status":"executed",
                "result":result
            }
        except PermissionError as pe:
            if self.logger:
                self.logger.log(action=action, status="PERMISSION_DENIED", message=str(pe))
            return{
                "status":"permission_denied",
                "message":str(pe),
                "preview":preview
            }
        except Exception as e:
            if self.logger:
                self.logger.log(action=action, status="FAILED", message=str(e))
            raise
        

