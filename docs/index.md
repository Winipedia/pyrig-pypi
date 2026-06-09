# pyrig-pypi Documentation

<!-- security -->
[![DependencyAuditor](https://img.shields.io/badge/security-pip--audit-blue?logo=python)](https://github.com/pypa/pip-audit)
[![SecurityChecker](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
<!-- ci/cd -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-pypi/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-pypi/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-pypi/deploy.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-pypi/actions/workflows/deploy.yml)
<!-- code-quality -->
[![MarkdownLinter](https://img.shields.io/badge/markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![TypeChecker](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![VersionControlHookManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)
<!-- testing -->
[![CoverageTester](https://codecov.io/gh/Winipedia/pyrig-pypi/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-pypi)
[![ProjectTester](https://img.shields.io/badge/tested%20with-pytest-46a2f1.svg?logo=pytest)](https://pytest.org)
<!-- tooling -->
[![PackageManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Pyrigger](https://img.shields.io/badge/built%20with-pyrig-3776AB?logo=buildkite&logoColor=black)](https://github.com/Winipedia/pyrig)
[![RemoteVersionController](https://img.shields.io/github/stars/Winipedia/pyrig-pypi?style=social)](https://github.com/Winipedia/pyrig-pypi)
[![VersionController](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)
<!-- documentation -->
[![DocsBuilder](https://img.shields.io/badge/MkDocs-Documentation-326CE5?logo=mkdocs&logoColor=white)](https://www.mkdocs.org)
[![Documentation](https://img.shields.io/badge/Docs-GitHub%20Pages-black?style=for-the-badge&logo=github&logoColor=white)](https://Winipedia.github.io/pyrig-pypi)
<!-- project-info -->
[![PackageIndex](https://img.shields.io/pypi/v/pyrig-pypi?logo=pypi&logoColor=white)](https://pypi.org/project/pyrig-pypi)
[![ProgrammingLanguage](https://img.shields.io/pypi/pyversions/pyrig-pypi)](https://www.python.org)
[![License](https://img.shields.io/github/license/Winipedia/pyrig-pypi)](https://github.com/Winipedia/pyrig-pypi/blob/main/LICENSE)

---

> A pyrig plugin for publishing Python packages to PyPI.

---

## What it does

Drop-in [pyrig](https://github.com/Winipedia/pyrig) plugin that wires
[PyPI](https://pypi.org) into your project:

- Adds a build-and-publish-to-PyPI job to the deploy workflow that runs
  after a successful release.
- Overrides the python badge with a PyPI badge that generates the pyversions badge
  and adds an additional badge for the package's version on PyPI.

No configuration required — installing the package as a development dependency
is the whole setup. Then regenerate your pyrig configs as usual.
The plugin's overrides are picked up automatically.

## Installation

```bash
uv add --group dev pyrig-pypi
uv run pyrig mkroot
```

## Setup

One-time setup before the first publish:

1. Create account at [pypi.org](https://pypi.org)
2. Create an API token
3. Scope: "Entire account" (recommended change to specific project after first
   publish)
4. Click "Add token"
5. **Copy token immediately** (you won't see it again)
6. Add token to your repository secrets as `PYPI_TOKEN`

After that, the deploy workflow will automatically upload your package to PyPI
after every release.

## How it works

The plugin subclasses some pyrig base classes:

- `DeployWorkflowConfigFile` to add the PyPI upload step to the deployment workflow.
- `ProgrammingLanguage` to replace the python badge with a PyPI pyversions badge.
- `PackageManager` to add the args for publishing to PyPI.

And adds its own tool class:

- `PackageIndex` to wrap PyPI information and add the PyPI version badge.
