import sys
import os
import json

from PyQt5.uic import compileUi


PATH_TO_REG_FILE = './ui-reg.json'

def _warning(msg):
    print ("[WARNING] " + msg)

def _error(msg):
    print("[ERROR] " + msg)
    sys.exit(0)

def compile(reg_file_path, execute_ui = True, create_init=False):
    if os.path.exists(reg_file_path) is False:
        _error("Reg file dont exist {}".format(reg_file_path))

    reg_data = None
    with open(reg_file_path) as reg_file:
        reg_data = json.load(reg_file)

    if reg_data is None:
        _error("Reg data is None")

    PathData = reg_data.get('Path')
    if PathData is None:
        _error("FromDir is None")

    Files = reg_data.get('Files')
    if Files is None:
        _error("Files is None")

    FromDir = PathData.get('FromDirectory')
    ToDir = PathData.get('ToDirectory')

    if FromDir is None:
        _error("FromDir is None")

    if ToDir is None:
        _error("ToDir is None")

    for FileDesc in Files:
        FromFileName = FileDesc.get("From")
        ToFileName = FileDesc.get("To")

        if FromFileName is None:
            _warning("From file name is None in desc {}".format(FileDesc))
            continue

        if ToFileName is None:
            _warning("To file name is None in desc {}".format(FileDesc))
            continue

        FromFilePath = os.path.join(FromDir, FromFileName)
        ToFilePath = os.path.join(ToDir, ToFileName)

        if os.path.exists(FromFilePath) is False:
            _warning("From file path {} dont exists is None in desc {}".format(
                FromFilePath,FileDesc))
            continue

        with open(ToFilePath, "w") as out_file:
            compileUi(FromFilePath, out_file, execute_ui)

    if create_init is True:
        InitPath = os.path.join(ToDir, "__init__.py")
        with open(InitPath, "w") as out_file:
            out_file.write("# ui package")

if __name__ == '__main__':
    compile(PATH_TO_REG_FILE, create_init=True)