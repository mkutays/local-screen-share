import os

SCRIPTS_FOLDER = os.path.dirname(os.path.dirname(__file__))
WORKSPACE_FOLDER = os.path.dirname(SCRIPTS_FOLDER)
WORKSPACE_NAME = str(os.path.basename(WORKSPACE_FOLDER))
VENV_FOLDER_NAME = f"{WORKSPACE_NAME}"
VENV_FOLDER = os.path.join(WORKSPACE_FOLDER, VENV_FOLDER_NAME)
REQ_FILE = os.path.join(WORKSPACE_FOLDER, "requirements.txt")
