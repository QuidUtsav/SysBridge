
def dry_run(action):
    preview = {
        "action": action.name,
        "description": action.description,
        "risk_level": action.risk_level,
        "reversible": action.reversible,
        "requires_confirmation": action.requires_confirmation,
    }

    if action.params:
        preview["parameters"] = action.params

    return preview
