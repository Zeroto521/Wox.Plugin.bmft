# -*- coding: utf-8 -*-

import os


def bmft(b_ext: str, l_ext: str, path: str):
    path = os.path.normpath(path)
    for file in os.listdir(path):
        name, suffix = os.path.splitext(file)
        if suffix == b_ext:
            os.rename(os.path.join(path, file), os.path.join(path, name+l_ext))
