#!/bin/bash
. $(dirname $0)/_common.sh
mkdir -p $ROOT_DIR/dist

for project in $(ls_projs); do
    (
        ls $project/Dockerfile || echo not file
        if [[ -f "$project/Dockerfile" ]] ; then
            cd $ROOT_DIR
            docker build --file  "$project/Dockerfile" --tag "monorepo/$(basename $project)" .
        else
            cd $project
            hatch build
            mv dist/* $ROOT_DIR/dist
        fi
    )
done