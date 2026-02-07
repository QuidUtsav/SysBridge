import subprocess
import os
from pathlib import Path
from abc import ABC, abstractmethod
from datetime import datetime

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
        return datetime.now().isoformat()
    
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
        with open("/sys/class/power_supply/BAT0/capacity", "r") as f:
            battery_level = int(f.read().strip())
        return battery_level
    
class ListDirectoryAction(Action):
    def __init__(self,*,path: str ):
        super().__init__(
            name="system.list_directory",
            description="Lists the contents of a directory.",
            risk_level="low",
            reversible=True,
            requires_confirmation=False
        )
        self.params["path"] = path
    def execute(self):
        return os.listdir(self.params["path"])

class OpenFileAction(Action):
    def __init__(self,*,path: str):
        super().__init__(
            name="open file",
            description="Opens a specified file.",
            risk_level="medium",
            reversible=False,
            requires_confirmation=True,
            params={"path": path}
        )
        self.path = path
    def execute(self):
        path = Path(self.path).expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(f"File not found: {self.path}")
        
        subprocess.run(
            ["xdg-open", str(path)],
            check=False)
        return f"Opened file: {self.path}"

class OpenFolderAction(Action):
    def __init__(self,*, path: str):
        super().__init__(
            name="system.open_folder",
            description="Opens a specified folder.",
            risk_level="medium",
            reversible=False,
            requires_confirmation=True,
            params={"path": path}
        )
        self.path = path
    def execute(self):
        subprocess.Popen(["xdg-open", self.params["path"]])
        return f"Opened folder: {self.params['path']}"

class LaunchAppAction(Action):
    def __init__(self,*, app: str):
        super().__init__(
            name="system.launch_application",
            description="Launches a specified application.",
            risk_level="medium",
            reversible=False,
            requires_confirmation=True,
            params={"app": app}
        )
        self.app = app
    def execute(self):
        subprocess.Popen([self.params["app"]])
        return f"Launched application: {self.params['app']}"
