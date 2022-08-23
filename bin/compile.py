#!/usr/bin/env python
from collections import deque
import pathlib
import re
import subprocess
import tempfile
import tomli


REPO_DEP_REGEX = re.compile(r"^([\w-]+) *@ *\{root:uri\}/(.*)")


def get_direct_repo_deps(project_dir: pathlib.Path) -> dict[str, pathlib.Path]:
    project_dir = project_dir.absolute()
    with project_dir.joinpath("pyproject.toml").open("rb") as buffer:
        pyproject = tomli.load(buffer)
    deps = pyproject["project"]["dependencies"]
    dev_deps: str = pyproject["tool"]["hatch"]["envs"]["default"]["dependencies"]
    repo_deps = [
        dev_dep for dev_dep in dev_deps if any(dev_dep.startswith(dep) for dep in deps)
    ]
    results: dict[str, pathlib.Path] = {}
    for dep in repo_deps:
        match = REPO_DEP_REGEX.match(dep)
        if not match:
            continue
        dep_name, path_to_src = match.groups()
        results[dep_name] = project_dir.joinpath(path_to_src).resolve()
    return results


def get_cascade_repo_deps(project_dir: pathlib.Path) -> dict[str, pathlib.Path]:
    q: deque[tuple[str | None, pathlib.Path]] = deque([(None, project_dir)])
    visited: dict[str | None, pathlib.Path] = {}
    while q:
        name, file = q.pop()
        visited[name] = file
        q.extend(get_direct_repo_deps(file).items())
    del visited[None]
    return visited  # type: ignore


def compile() -> None:
    all_deps = get_cascade_repo_deps(pathlib.Path.cwd())
    with tempfile.TemporaryDirectory() as tmp_dir:
        reqs_in = pathlib.Path(tmp_dir) / "requirements.in"
        reqs_out = pathlib.Path(tmp_dir) / "requirements.txt"
        reqs_in.write_text("\n".join([".", *map(str, all_deps.values())]))
        print("Compiling")
        subprocess.check_output(["pip-compile", "-o", str(reqs_out), str(reqs_in)])
        print()


def main() -> None:
    compile()


if __name__ == "__main__":
    main()
