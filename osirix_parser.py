import re
import numpy as np
from typing import Any


def index_all(string, substring):
    start = -1
    indice = []
    while True:
        try:
            start = string.index(substring, start+1)
            if start == -1:
                break
            else:
                indice.append(start)
        except:
            break
    return indice


class OsirixSRParser(object):
    def __init__(self, version='13.0.1') -> None:
        self.version = version

    @staticmethod
    def parse(osx):
        decode = osx.EncapsulatedDocument.decode('unicode-escape')
        rois = dict()
        tmp = decode.replace(chr(0), "").replace(chr(14), "").replace(chr(32), "")
        marker = ''.join([chr(i) for i in range(33, 66)])
        roi_loc = index_all(tmp, marker)
        if len(roi_loc) > 0:
            num_roi = len(roi_loc)
            roi_loc.append(len(tmp))

            for i in range(num_roi):
                txt1 = tmp[roi_loc[i]:roi_loc[i+1]]
                abc1 = index_all(txt1, '_')
                abc2 = np.array(index_all(txt1[abc1[0]:], '}Ò')) + abc1[0]
                # abc2 = np.array(index_all(txt1[abc1[0]:-1], '}Ò')) + abc1[0] - 1
                points = []
                for ind2 in range(len(abc1)):
                    txt2 = txt1[abc1[ind2]:abc2[ind2]]
                    endofpoint = abc2[ind2]
                    if len(txt2) > 44:
                        tt = txt2.index('}')
                        txt2 = txt2[1:tt]
                        endofpoint = abc1[ind2] + tt
                    pt = re.findall('\d+\.\d+,\d+\.\d+', txt2)
                    pt = np.array(pt[0].split(','), dtype=np.float32)[None, :]
                    points.append(pt)
                txt3 = txt1[endofpoint-1:abc2[-1]]

                #regex = r"}(.*)+"
                #regex = r"}[a-zA-Z]+|{[^{}]+_"
                # regex = r"(?<=\})([a-zA-Z0-9]+)(?=\_)"
                regex = r"}([a-zA-Z0-9,-\.]+)_"
                matches = re.findall(regex, txt3)
                if len(matches) < 1:
                    raise RuntimeError(f"Cannot parse name of roi\#{i}")
                else:
                    name = matches[0]

                points = np.concatenate(points, axis=0)
                rois[name] = points
        return rois

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.parse(*args, **kwds)