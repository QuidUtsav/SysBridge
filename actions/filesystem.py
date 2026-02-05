import subprocess
from pathlib import Path
from abc import ABC, abstractmethod

class Action(ABC):
    
    name:str
    description:str
    risk_level:str  #"low", "medium", "high"
    reversible:bool
    requires_confirmation:bool
    
    
    def __init__(
        self,
        *,
        name:str,
        description:str,
        risk_level:str,
        reversible:bool,
        requires_confirmation:bool,
        params: dict | None = None
    ):
        self.name = name
        self.description = description
        self.risk_level = risk_level
        self.reversible = reversible
        self.requires_confirmation = requires_confirmation 
        self.params = params or {} 
    
    def explain(self)->str:
        param_str= ", ".join(
            f"{key} = {value}" for key, value in self.params().items()
        )
        return param_str
    

    
class GetTimeAction(Action):
    def __init__(self):
        super().__init__(
            name="system.get_time",
            description="Retrieves the current system time.",
            risk_level="low",
            reversible=True,
            requires_confirmation=False
        )
    def execute(self):
        pass
    
class GetBatteryAction(Action):
    def __init__(self):
        super().__init__(
            name="system.get_battery",
            description="Retrieves the current system Battery.",
            risk_level="low",
            reversible=True,
            requires_confirmation=False
        )
    def execute(self):
        pass
    
class ListDirectoryAction(Action):
    def __init__(self):
        super().__init__(
            name="system.list_directory",
            description="Lists the contents of a directory.",
            risk_level="low",
            reversible=True,
            requires_confirmation=False
        )
    def execute(self):
        pass

class OpenFileAction(Action):
    def __init__(self,*,filepath: str):
        super().__init__(
            name="open file",
            description="Opens a specified file.",
            risk_level="medium",
            reversible=False,
            requires_confirmation=True,
            params={"file_path": filepath}
        )
        self.filepath = filepath
    def execute(self):
        path = Path(self.filepath).expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(f"File not found: {self.filepath}")
        
        subprocess.run(
            ["xdg-open", str(path)],
            check=False)
        return f"Opened file: {self.filepath}"

class OpenFolderAction(Action):
    def __init__(self):
        super().__init__(
            name="system.open_folder",
            description="Opens a specified folder.",
            risk_level="medium",
            reversible=False,
            requires_confirmation=True
        )
    def execute(self):
        pass

class LaunchAppAction(Action):
    def __init__(self):
        super().__init__(
            name="system.launch_application",
            description="Launches a specified application.",
            risk_level="medium",
            reversible=False,
            requires_confirmation=True
        )
    def execute(self):
        pass
