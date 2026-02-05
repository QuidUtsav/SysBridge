
from execution.dry_run import dry_run
from datetime import datetime
from execution.result import ActionResult

class ActionLogger:
    def log(self, *, action, status, message=""):
        timestamp = datetime.utcnow().isoformat()
        entry = f"[{timestamp}] {action.name} | {status} | {message}\n"

        with open("logs/actions.log", "a") as f:
            f.write(entry)

class ActionExecutor:
    def __init__(self, policy_guard=None,logger = None, journal = None):
        self.policy_guard = policy_guard
        self.logger = logger
        self.journal = journal
        
    def execute(self,action,confirm:bool =False):
        
        preview = dry_run(action)
        try:
            if self.policy_guard:
                self.policy_guard.check(action,confirmed=confirm)
                            
            result= action.execute()
            if self.logger:
                self.logger.log(action=action, status="SUCCESS")
            
            if self.journal:
                self.journal.record(action=action,status="SUCCESS")
            return ActionResult(
                action_name=action.name,
                status="executed",
                result=result
            )


        except PermissionError as pe:
            if self.logger:
                self.logger.log(action=action, status="PERMISSION_DENIED", message=str(pe))
                
            if self.journal:
                self.journal.record(action=action, status="DENIED", message=str(pe))

            return ActionResult(
            action_name=action.name,
            status="confirmation_required",
            reason="Action requires user confirmation",
            preview=preview
        )

        except Exception as e:
            if self.logger:
                self.logger.log(action=action, status="FAILED", message=str(e))
                
            if self.journal:
                self.journal.record(action=action, status="FAILED", message=str(e))

            return ActionResult(
                action_name=action.name,
                status="denied",
                reason=str(e),
                preview=preview
            )
                    

