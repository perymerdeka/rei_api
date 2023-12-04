import pandas as pd

from typing import Any
from os.path import join

class Extract(object):
    def __init__(self) -> None:
        pass

    def to_csv(self, data: list[dict[str, Any]],  filepath: str):
        df = pd.DataFrame(data=data)
        df.to_csv(filepath, index=False)
    
    def to_excel(self, data: list[dict[str, Any]],  filepath: str):
        df = pd.DataFrame(data=data)
        df.to_excel(filepath, index=False)