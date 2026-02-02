

def dry_run(action):
    
    explanation={
        "action": action,
        "description": action.description,
        "risk_level": action.risk_level,
        "reversible": action.reversible,
        "requires_confirmation": action.requires_confirmation
    }
    return explanation