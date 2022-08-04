#!/bin/bash
. $(dirname $0)/_common.sh
mkdir -p $ROOT_DIR/dist
for project in $(ls_projs); do
    (
        cd $project
        hatch build
        mv dist/* $ROOT_DIR/dist
    )
done