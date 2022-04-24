import argparse
import time
from runROExtractLocal import runServer
from utils import outputTime

def read_args():
    parser=argparse.ArgumentParser(description="squash commits and detect refactoring operations")
    parser.add_argument('repository', help='path for repository to be squashed and detected')
    parser.add_argument('-o', help='path for experiment output', default=".")
    parser.add_argument('-mi', help='minimum coarse granularity, default 1', default=1)
    parser.add_argument('-ma', help='maximum coarse granularity, default 4', default=4)
    parsed = parser.parse_args()
    repoPath = parsed.repository
    output = parsed.o
    mi = parsed.mi
    ma = parsed.ma
    return repoPath, output, mi, ma


if __name__ == "__main__":
    repoPath, output, mi, ma = read_args()
    repositories = [repoPath]

    for each in repositories:
        time_start = time.time()
        runServer(each, ".", output, [int(mi),int(ma)+1])
        time_end = time.time()
        t = time_end - time_start
        tResult = outputTime(t)
        with open((output + repoPath.split("/")[-1]+"/time.txt"), "w") as f:
            f.write(tResult)