#!/bin/bash
. $(dirname $0)/_common.sh

for project in $(ls_projs); do
    (
        cd $project
        hatch run cov
    )
done