import os
import platform
from typing import Text


def root_path():
    """ 获取 根路径 """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path


def ensure_path_sep(path: Text) -> Text:
    """兼容 windows 和 linux 不同环境的操作系统路径 """
    if path is not None:
        if "/" in path:
            path = os.sep.join(path.split("/"))

        if "\\" in path:
            path = os.sep.join(path.split("\\"))

        if path.startswith("\\"):
            return path[1:]
        elif path.startswith(".\\"):
            return path[2:]
        else:
            return path
    else:
        return None


def fix_full_path(path: Text, root_of_path=None) -> Text:
    if path is not None:
        path = ensure_path_sep(path)
        if platform.system() == 'Windows' and ":" not in path:
            if root_of_path is None:
                root_of_path = root_path()
            else:
                root_of_path = ensure_path_sep(root_of_path)
            return os.path.join(root_of_path, path)
        else:
            return path
    else:
        return None

# if __name__ == '__main__':
#     print(fix_full_path("./logs\log.log","D:/download"))
