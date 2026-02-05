from datetime import datetime

class ActionJournal:
    def __init__(self):
        self.entries = []

    def record(self, *, action, status, message=""):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "action": action.name,
            "risk_level": action.risk_level,
            "reversible": action.reversible,
            "status": status,
            "message": message
        }
        self.entries.append(entry)

    def last(self):
        return self.entries[-1] if self.entries else None
