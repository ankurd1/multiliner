import sys
import os

root_dir = os.path.dirname(__file__) + "/.."
sys.path.append(root_dir)

import multiliner

def test_multiline():
    test_data = _get_test_multiline_data()
    for inp, out, start, ts, extra in test_data:
        assert multiliner.multiline(inp, start, ts, extra) == out

def _get_test_multiline_data():
    test_data_file = root_dir + '/tests/data/multiline_data.txt'

    result = []
    start = -1
    ts = -1
    extra = False
    inp = ''
    out = []
    stage = 0

    for line in open(test_data_file):
        if len(line.strip()) == 0:
            stage += 1
            if stage == 3:
                result.append((inp, out, start, ts, extra))
                stage = 0
                out = []
        elif stage == 0:
            a, b, c = line.strip().split(',')
            start = int(a)
            ts = int(b)
            extra = c.strip() == 'True'
        elif stage == 1:
            inp = line.rstrip()
        elif stage == 2:
            out.append(line.rstrip())

    return result
