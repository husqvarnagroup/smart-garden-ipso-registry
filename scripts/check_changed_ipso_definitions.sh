#!/usr/bin/env sh

set -u
set -e

to_rev=$1
from_rev=$2

revs=$(git rev-list "$to_rev".."$from_rev")


for rev in $revs
do
    echo Checking commit:
    git log -n1 --oneline "$rev"
    if git diff-tree -r --diff-filter=M "${rev}^!" | awk '/definitions.*\.xml$/{ print $5 }' | grep -q M
    then
        echo IPSO definition file changed!
        git diff --raw "${rev}^!"
        exit 1
    fi
done
