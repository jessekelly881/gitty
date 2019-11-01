#!/usr/bin/env bash


for Y in {2018..2019}
do
    mkdir $Y
    for M in {01..12}
    do
        cd $Y
        mkdir $M
        cd ../
        for D in {01..31}
        do
            cd $Y/$M
            mkdir $D
            cd $D
            num=$(./rand.py)
            echo "Committed on $M/$D/$Y" > $num.md
            cd ../../../
            export GIT_COMMITTER_DATE="$Y-$M-$D 12:00:00"
            export GIT_AUTHOR_DATE="$Y-$M-$D 12:00:00"
            # git add $Y/$M/$D/commit.md -f
            # git commit --date="$Y-$M-$D 12:00:00" -m "$M $D $Y"
        done
    done
done
