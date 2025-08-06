import json
import os
from pprint import pprint

import gdb2json


def test_run():
    test_datasets = './tests/test_datasets'
    for gdb_path in os.listdir(test_datasets):
        js = gdb2json.parse(os.path.join(test_datasets, gdb_path))
        js = json.loads(json.dumps(js))
        pprint(js)
