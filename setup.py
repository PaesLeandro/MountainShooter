from cx_Freeze import setup, Executable
import os

base = "gui" if os.name == "nt" else None
icon_path = "asset/icon.ico"

executable_config = {
    "script": "main.py",
    "target_name": "MountainShooter.exe",
    "base": base,
}

if os.path.exists(icon_path):
    executable_config["icon"] = icon_path

executables = [Executable(**executable_config)]
files = {
    "include_files": [("asset", "asset")],
    "packages": ["pygame"],
    "include_msvcr": True,
}

setup(
    name="MountainShooter",
    version="1.0",
    description="Mountain Shooter app",
    options={"build_exe": files},
    executables=executables
)
