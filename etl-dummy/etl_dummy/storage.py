import json
import os
import shutil
from os.path import join
from typing import Dict


class Storage:
    DUMMY_FILE = "dummy_file.json"

    def __init__(self, base_path: str):
        self._base_path = join(base_path, "tmp_store_airflow")
        os.makedirs(self._base_path, exist_ok=True)

    @property
    def dummies(self):
        return self._read_json(self.DUMMY_FILE)

    @dummies.setter
    def dummies(self, value):
        self._write_json(value, self.DUMMY_FILE)

    def cleanup(self):
        shutil.rmtree(self._base_path, ignore_errors=True)

    def _write_json(self, data: Dict, path_to_file: str):
        with open(self._path(path_to_file), "w") as f:
            return json.dump(data, f)

    def _read_json(self, path_to_file: str) -> Dict:
        with open(self._path(path_to_file), "r") as f:
            return json.load(f)

    def _path(self, f):
        return join(self._base_path, f)


class Repo:
    def __init__(self, output_dir: str):
        self.storage = Storage(output_dir)

