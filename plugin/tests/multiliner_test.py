import sys
import os

root_dir = os.path.dirname(__file__) + "/.."
sys.path.append(root_dir)

import multiliner

def test_multiline():
    assert multiliner.multiline(['a']) == ['a']
