# -*- coding: utf-8 -*-

import os
import sys
sys.path.append('../bmft')

import pyperclip

from bmft import bmft
from wox import Wox, WoxAPI

from .constants import *


class Main(Wox):

    def query(self, param: str):
        result = []
        param = param.strip()

        res_format = RESULT_TEMPLATE.copy()

        if param:
            b_ext, l_ext, *path = param.split()
            path = ''.join(path)

            # normal message
            res_format['Title'] = "The path is not folder."
            res_format['SubTitle'] = "Copy the Path to Clipboard."

            # action message
            action = ACTION_TEMPLATE.copy()
            action['JsonRPCAction']['method'] = 'copy2clipboard'
            action['JsonRPCAction']['parameters'] = [param]

            if os.path.exists(path) and os.path.isdir(path):
                bmft(b_ext, l_ext, path)

                # normal message update
                res_format['Title'] = "Done."
                res_format['SubTitle'] = "Open the Path."

                # action message update
                action['JsonRPCAction']['method'] = 'openFolder'

            res_format.update(action)
        else:
            res_format['Title'] = "半亩方塘"
            res_format['SubTitle'] = "Input in keywords, such as `.ext1 .ext2 path`"

        result.append(res_format)

        return result

    def copy2clipboard(self, value):
        pyperclip.copy(value)

    def openFolder(self, path: str):
        os.startfile(path)
        WoxAPI.change_query(path)
