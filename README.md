# pyrig-pypi

<!-- security -->
[![SecurityChecker](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![DependencyAuditor](https://img.shields.io/badge/security-pip--audit-blue?logo=python)](https://github.com/pypa/pip-audit)
<!-- tooling -->
[![VersionController](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)
[![RemoteVersionController](https://img.shields.io/github/stars/Winipedia/pyrig-pypi?style=social)](https://github.com/Winipedia/pyrig-pypi)
[![ContainerEngine](https://img.shields.io/badge/Container-Podman-A23CD6?logo=podman&logoColor=grey&colorA=0D1F3F&colorB=A23CD6)](https://podman.io)
[![Pyrigger](https://img.shields.io/badge/built%20with-pyrig-3776AB?logo=buildkite&logoColor=black)](https://github.com/Winipedia/pyrig)
[![PackageManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
<!-- documentation -->
[![DocsBuilder](https://img.shields.io/badge/MkDocs-Documentation-326CE5?logo=mkdocs&logoColor=white)](https://www.mkdocs.org)
[![Documentation](https://img.shields.io/badge/Docs-GitHub%20Pages-black?style=for-the-badge&logo=github&logoColor=white)](https://Winipedia.github.io/pyrig-pypi)
<!-- code-quality -->
[![VersionControlHookManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![MarkdownLinter](https://img.shields.io/badge/markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![TypeChecker](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
<!-- project-info -->
[![PackageIndex](https://img.shields.io/pypi/v/pyrig-pypi?logo=pypi&logoColor=white)](https://pypi.org/project/pyrig-pypi)
[![ProgrammingLanguage](https://img.shields.io/pypi/pyversions/pyrig-pypi)](https://www.python.org)
[![License](https://img.shields.io/github/license/Winipedia/pyrig-pypi)](https://github.com/Winipedia/pyrig-pypi/blob/main/LICENSE)
<!-- testing -->
[![ProjectTester](https://img.shields.io/badge/tested%20with-pytest-46a2f1.svg?logo=pytest)](https://pytest.org)
[![CoverageTester](https://codecov.io/gh/Winipedia/pyrig-pypi/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-pypi)
<!-- ci/cd -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-pypi/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-pypi/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-pypi/release.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-pypi/actions/workflows/release.yml)

---

> A pyrig plugin for publishing Python packages to PyPI.

---

## What is pyrig-pypi

pyrig-pypi is a plugin for [pyrig](https://github.com/Winipedia/pyrig) that
integrates PyPI publishing into a pyrig project.

## Features

### PyPI Integration

Integrates PyPI publishing into the deployment workflow, by uploading Python packages
to the Python Package Index (PyPI)

### PyPI Badges

Replaces the python badge with a PyPI badge that generates the pyversions badge
and adds an additional badge for the package's version on PyPI.

## Usage

To use pyrig-pypi, add it as a development dependency in your pyrig project
and run `pyrig mkroot` to generate the project structure. This will adjust all
necessary files.

```bash
uv add --group dev pyrig-pypi
uv run pyrig mkroot
```

If you are using pyrig with its Github workflows, you will need a
[PyPI](https://pypi.org) account and get an API token there
and add this token as `PYPI_TOKEN` to your repository secrets.
This is necessary for the PyPI upload step in the deployment workflow to work.
