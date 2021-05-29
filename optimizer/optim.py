from itertools import islice
from .data import Data


import pandas as pd
import numpy as np


class Optim:
    def __init__(self) -> None:
        pass

    # = = = = = = = = = = = = = = = = = = = = = = = = = =
    #                     FIT DATA
    # = = = = = = = = = = = = = = = = = = = = = = = = = =

    def fit(self, df: pd.DataFrame):
        """

        It catches all groups which is the same numbers of candles.

        @params:
            - df : Dataframe

        @return:
            - None

        """

        fitted_ranges = []

        i = 0

        size = len(df.index)

        while i < size - 2:

            row = df.iloc[i]

            change = row["change"]

            cd = []

            if change <= 0:
                i += 1
                continue

            cd.append(row)

            a = 0

            for idx, sr in islice(df.iterrows(), i + 1, None):

                i = idx

                if sr["change"] < 0:
                    a += 1

                if sr["close"] > cd[0]["close"]:

                    if a <= 1:

                        cd.append(sr)

            for r in reversed(cd):
                if r.change < 0:
                    cd.pop(len(cd) - 1)
                else:
                    break

            if len(cd) > 2:
                fitted_ranges.append(cd)

        return fitted_ranges

    # = = = = = = = = = = = = = = = = = = = = = = = = = =
    #                   OPTIMIZE DATA
    # = = = = = = = = = = = = = = = = = = = = = = = = = =

    def optimize(self, df: pd.DataFrame) -> dict:
        """

        it collocates by how many candle to going up.
        It calculates avg of all the same candle groups

        @params:
            - df : Dataframe

        @return:
            - None

        """
        fitted_ranges = self.fit(df)

        for fr in fitted_ranges:

            size = len(fr)

            flag = fr[0]

            cgo = Data.cgo[size] if Data.cgo[size] != None else Data.gm

            for idc in Data.idc:
                cgo[idc][idc].append(flag[idc])
                cgo[idc]["scores"].append(flag[f"{idc}_score"])

            cgo["sma"]["sma1"].append(flag["sma_9"])
            cgo["sma"]["sma2"].append(flag["sma_21"])
            cgo["sma"]["sma_score"].append(flag["sma_score"])

            Data.cgo = cgo

        for g in Data.cgo:

            cgo = Data.cgo[g]

            for idc in Data.idc:
                cgo[idc]["optim"] = np.average(cgo[idc][idc])
                cgo[idc]["score_optim"] = np.average(cgo[idc]["scores"])

            cgo["sma"]["sma1_optim"] = np.average(cgo[idc]["sma1"])
            cgo["sma"]["sma1_optim"] = np.average(cgo[idc]["sma2"])
            cgo["sma"]["sma1_optim"] = np.average(cgo[idc]["scores"])

            Data.cgo[g] = cgo

    # = = = = = = = = = = = = = = = = = = = = = = = = = =
    #                   OPTIMIZE DATA
    # = = = = = = = = = = = = = = = = = = = = = = = = = =

    def max_optim(self, dfs: dict):
        
        for pair in dfs:

            df = dfs[pair]

            self.optimize(df)

        return Data.cgo
