#!/usr/bin/env python

import numpy as np
import os

# Random number generation. Used for num of commits per day

def cleanRandNum(n):
    if(n < 1):
        ret = 0
    else:
        ret = int(round(n,0))

    return ret

def genRand():
    mu, sigma = 8, 10
    s = np.random.normal(mu, sigma)
    return cleanRandNum(s)

# Commit dummy file
def commitDummyFile(year, month, day, num):
    fname = "%s/%s/%s/%s" % (year, month, day, num)

    GIT_COMMITTER_DATE = "%s-%s-%s 12:00:00" % (year, month, day)
    GIT_AUTHOR_DATE = "%s-%s-%s 12:00:00" % (year, month, day)
    GIT_MESSAGE = "%s-%s-%s-%s" % (year, month, day, num)
    GIT_COMMIT_DATE = "%s-%s-%s 12:00:00" % (year, month, day)

    command = "export GIT_COMMITTER_DATE='%s'; export GIT_AUTHOR_DATE='%s'; git add '%s' -f; git commit -m '%s' --date '%s'"% (
    GIT_COMMITTER_DATE,
        GIT_AUTHOR_DATE,
        fname,
        GIT_MESSAGE,
        GIT_COMMIT_DATE
    )
    if not os.system(command) == 0:
        # Check for failure and wait
        return

# Create dummy file
def createDummyFile(year, month, day, num):
    fname = "%s/%s/%s/%s" % (year, month, day, num)
    os.makedirs(os.path.dirname(fname), exist_ok=True)
    with open(fname, "w") as f:
        f.write("DUMMY TEXT")

    return

# Loop through days and create commits

for year in [2015, 2016]:
    for month in range(1,13):
        for day in range(1,32):
            for n in range(0, genRand()):
                createDummyFile(year, month, day, n)
                commitDummyFile(year, month, day, n)
