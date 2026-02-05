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

    def explain(self):
        explanation = {
            "action": self.action_name,
            "status": self.status,
            "reason": self.reason
        }

        if self.preview:
            explanation["preview"] = self.preview

        if self.result:
            explanation["result"] = self.result

        return explanation
