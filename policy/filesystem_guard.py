from pathlib import Path

ALLOWED_ROOT=[
    "/home/utsav/Desktop/python_project/jarvis",
]

class FileSystemGuard:
    def __init__(self,allowed_roots):
        self.allowed_roots = [Path(roots).resolve() for roots in allowed_roots]
        
    def validate_path(self,user_path:str)->Path:
        resolved_path = Path(user_path).expanduser().resolve()
        
        for root in self.allowed_roots:
            if resolved_path.is_relative_to(root):
                return resolved_path
            
        raise PermissionError(
            f"Path {resolved_path} is outside  the allowed filesystem scope."
        )
    