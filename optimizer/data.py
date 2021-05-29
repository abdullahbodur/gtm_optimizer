import numpy as np


class Data:

    gm = {
        "macd": {
            "scores": np.array(),
            "macd": np.array(),
        },
        "rsi": {
            "scores": np.array(),
            "rsi": np.array(),
        },
        "sma": {
            "scores": np.array(),
            "sma1": np.array(),
            "sma2": np.array(),
        },
        "cci": {
            "scores": np.array(),
            "cci": np.array(),
        },
    }

    cgo = {}

    go = {}

    idc = ["macd", "rsi", "cci"]

    pass