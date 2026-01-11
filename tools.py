import os

def list_files(_input=None):
    """List all files in the current directory"""
    return os.listdir(".")

def read_file(filename):
    """Read the contents of a file"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

def calculate(expression):
    """Evaluate a simple mathematical expression"""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Calculation error: {str(e)}"


TOOLS = {
    "list_files": list_files,
    "read_file": read_file,
    "calculate": calculate
}
