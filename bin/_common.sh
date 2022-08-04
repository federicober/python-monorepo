ROOT_DIR=$(dirname $0 | xargs dirname | xargs realpath)

ls_projs() {
    find $ROOT_DIR -name pyproject.toml -type f | xargs dirname
}