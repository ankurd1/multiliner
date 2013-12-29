import sys
import os

root_dir = os.path.dirname(__file__) + "/.."
sys.path.append(root_dir)

import multiliner

def test_multiline():
    test_data_file = root_dir + '/tests/data/multiline_data.txt'
    test_data = _read_test_data(test_data_file)
    for inp, out, args in test_data:
        start, ts, extra = args
        start = int(start)
        ts = int(ts)
        extra = extra == 'True'
        assert multiliner.multiline(''.join(inp), start, ts, extra) == out

def _read_test_data(test_data_file):
    result = []
    inp = []
    out = []
    stage = 0
    args = []

    for line in open(test_data_file):
        if len(line.strip()) == 0:
            stage += 1
            if stage == 3:
                result.append((inp, out, args))
                stage = 0
                out = []
                inp = []
        elif stage == 0:
            args = line.strip().split(',')
        elif stage == 1:
            inp.append(line.rstrip())
        elif stage == 2:
            out.append(line.rstrip())

    return result

def test_unmultiline():
    test_data_file = root_dir + '/tests/data/unmultiline_data.txt'
    test_data = _read_test_data(test_data_file)
    for inp, out, _ in test_data:
        assert multiliner.unmultiline(inp) == out
