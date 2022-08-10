#!/bin/bash
. $(dirname $0)/_common.sh

for project in $(ls_projs); do
    (
        cd $(dirname $project)
        hatch run true
        rm -rf venv
        ln -s $(hatch env find) venv
    )
done