def saveFile(buffer: str) -> None: 
    """Saves the buffer as a specified file. The filename, and
    destination is determined by the value of current_path, which is a
    variable located in the backend."""
    ...

def getFileContents() -> str:
    """Returns the contents of a specific file as a string. Uses the value
    of current_path to get it.

    Returns an empty string if current_path is empty."""
    ...

def getCurrentPath() -> str:
    """The current path is a variable within the backend itself. This
    function is for getting it's current value."""
    ...

def setCurrentPath(file_path: str, force: bool = False) -> None:
    """The current path is used as a target for where a file should be
    saved, and what file should be opened. This should only be called
    if the user wants to save the buffer as a new file, or the user want
    to open a file.

    If the file_path is empty, the current path will not change. Unless
    'force' argument is set to True. This is typically done when the user
    wants to create a new file."""
    ...
