import sys
import os
import vim

plugin_path = vim.eval('s:plugin_path')
sys.path.append(plugin_path)

import multiliner

def Multiliner_multiline():
    cb = vim.current.buffer
    cw = vim.current.window
    cur_row, cur_col = cw.cursor
    cur_line = vim.current.line
    ts = cb.options['tabstop']

    result = multiliner.multiline(cur_line, cur_col, ts)

    # if we couldn't break line starting from cur_col, try using 0 instead
    if len(result) == 1:
        result = multiliner.multiline(cur_line, 0, ts)

    del(cb[cur_row - 1])

    for line in reversed(result):
        cb.append(line, cur_row - 1)

def Multiliner_unmultiline():
    pass
