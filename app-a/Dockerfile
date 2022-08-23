ARG INSTALL_PATH=/opt/python-monorepo
ARG PIP_VERSION=22.2.2

FROM python:3.9-slim-bullseye
ARG INSTALL_PATH
ARG PIP_VERSION

RUN apt-get update \
    # && apt-get install -y build-essential \
    && apt-get clean \
    && python3 -m venv "${INSTALL_PATH}" \
    ;

COPY common-lib-pypi /tmp/src/common-lib-pypi
COPY dep-of-common-lib /tmp/src/dep-of-common-lib

RUN --mount=type=cache,target=/root/.cache/ \
    "${INSTALL_PATH}"/bin/pip install pip=="${PIP_VERSION}" \
    && "${INSTALL_PATH}"/bin/pip install --no-deps \
    /tmp/src/common-lib-pypi \
    /tmp/src/dep-of-common-lib \
    ;

COPY app-a /tmp/src/app-a

RUN --mount=type=cache,target=/root/.cache/ \
    "${INSTALL_PATH}"/bin/pip install /tmp/src/app-a \
    ;
