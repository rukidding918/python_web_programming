class CountFromBy:
    def __init__(self, val: int=0, incr: int=1) -> None:
        self.val = val
        self.incr = incr

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)