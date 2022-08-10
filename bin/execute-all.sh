#!/bin/bash
. $(dirname $0)/_common.sh

$(dirname $0)/venv-all.sh

for project in $(ls_projs); do
    (
        cd $project
        echo $project
        hatch run python -m "$(as_module $project)"
        echo
    )
done