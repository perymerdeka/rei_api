import json
import pandas as pd

from typing import Any
from os.path import join

class Extract(object):

    def to_csv(self, data: list[dict[str, Any]],  filepath: str):
        df = pd.DataFrame(data=data)
        df.to_csv(filepath, index=False)
        return "Excel generated at {}".format(filepath)
    
    def to_excel(self, data: list[dict[str, Any]],  filepath: str):
        df = pd.DataFrame(data=data)
        df.to_excel(filepath, index=False)
        return "Excel generated at {}".format(filepath)
    
    def to_json(self, data: list[dict[str, Any]], filepath: str):
        if filepath.endswith(".json"):
            with open(filepath) as f:
                json.dump(data, f)
            return "JSON generated at {}".format(filepath)
