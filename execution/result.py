class ActionResult:
    def __init__(
        self,
        *,
        action_name: str,
        status: str,
        reason: str = "",
        preview=None,
        result=None
    ):
        self.action_name = action_name
        self.status = status
        self.reason = reason
        self.preview = preview
        self.result = result

    def to_dict(self):
        return {
            "action": self.action_name,
            "status": self.status,
            "reason": self.reason,
            "result": self.result,
            "preview": self.preview
        }
        
    def __repr__(self):
        return str(self.to_dict())
    
    def explain(self):
        explanation = {
            "action": self.action_name,
            "status": self.status,
            "result": self.result
        }

        if self.preview:
            explanation["preview"] = self.preview

        if self.result:
            explanation["result"] = self.result

        return explanation
