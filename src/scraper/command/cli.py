from typer import Typer

class ScraperCommand(object):
    def __init__(self) -> None:
        self.app: Typer = Typer()
        