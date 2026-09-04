# Home

<!-- project-status -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-pypi/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-pypi/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-pypi/release.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-pypi/actions/workflows/release.yml)
[![ProjectTester](https://codecov.io/gh/Winipedia/pyrig-pypi/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-pypi)
<!-- code-quality -->
[![ByteOrderMarkerFormatter](https://img.shields.io/badge/BOM-fix--byte--order--marker-orange)](https://github.com/pre-commit/pre-commit-hooks)
[![CaseConflictChecker](https://img.shields.io/badge/case--conflict-check--case--conflict-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![DependencyChecker](https://img.shields.io/badge/dependencies-deptry-blue)](https://github.com/osprey-oss/deptry)
[![EndOfFileFormatter](https://img.shields.io/badge/EOF-end--of--file--fixer-orange)](https://github.com/pre-commit/pre-commit-hooks)
[![EndOfLineFormatter](https://img.shields.io/badge/EOL-mixed--line--ending-orange)](https://github.com/pre-commit/pre-commit-hooks)
[![JSONFormatter](https://img.shields.io/badge/JSON-pretty--format--json-orange)](https://github.com/pre-commit/pre-commit-hooks)
[![JSONLinter](https://img.shields.io/badge/JSON-check--json-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![LargeFileChecker](https://img.shields.io/badge/large--files-check--added--large--files-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![MarkdownLinter](https://img.shields.io/badge/Markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![MergeConflictChecker](https://img.shields.io/badge/merge--conflict-check--merge--conflict-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![ModuleTestNamingChecker](https://img.shields.io/badge/test--naming-name--tests--test-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![SecretsChecker](https://img.shields.io/badge/secrets-detect--secrets-blue)](https://github.com/Yelp/detect-secrets)
[![SecurityChecker](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![ShellFormatter](https://img.shields.io/badge/shell-shfmt-orange)](https://github.com/mvdan/sh)
[![ShellLinter](https://img.shields.io/badge/shell-shellcheck-blue)](https://github.com/koalaman/shellcheck)
[![SpellChecker](https://img.shields.io/badge/spell--check-typos-blue)](https://github.com/crate-ci/typos)
[![TOMLLinter](https://img.shields.io/badge/TOML-tombi-blueviolet)](https://github.com/tombi-toml/tombi)
[![TrailingWhitespaceFormatter](https://img.shields.io/badge/whitespace-trailing--whitespace--fixer-orange)](https://github.com/pre-commit/pre-commit-hooks)
[![TypeChecker](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![YAMLLinter](https://img.shields.io/badge/YAML-ryl-red)](https://github.com/owenlamont/ryl)
<!-- tooling -->
[![PackageManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Pyrigger](https://img.shields.io/badge/built%20with-pyrig-3776AB?logo=buildkite&logoColor=black)](https://github.com/Winipedia/pyrig)
[![RemoteVersionController](https://img.shields.io/github/stars/Winipedia/pyrig-pypi?style=social)](https://github.com/Winipedia/pyrig-pypi)
[![VersionControlHookManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)
[![VersionController](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)
<!-- project-info -->
[![DocsBuilder](https://img.shields.io/badge/Documentation-zensical-326CE5)](https://Winipedia.github.io/pyrig-pypi)
[![PackageIndex](https://img.shields.io/pypi/v/pyrig-pypi?logo=pypi&logoColor=white)](https://pypi.org/project/pyrig-pypi)
[![ProgrammingLanguage](https://img.shields.io/pypi/pyversions/pyrig-pypi)](https://www.python.org)
[![License](https://img.shields.io/github/license/Winipedia/pyrig-pypi)](https://github.com/Winipedia/pyrig-pypi/blob/main/LICENSE)

---

> A pyrig plugin for publishing Python packages to PyPI.

---

## Overview

Drop-in [pyrig](https://github.com/Winipedia/pyrig) plugin that wires
[PyPI](https://pypi.org) into your project:

- Adds a build-and-publish-to-PyPI job to the deploy workflow that runs
  after a successful release.
- Replaces the static Python badge with one sourced from PyPI's pyversions
  endpoint, and adds a badge for the package's current version on PyPI.

No pyrig configuration to write by hand — installing the package as a
development dependency and regenerating your pyrig configs as usual is enough
for the plugin's overrides to be picked up automatically. Publishing itself
needs a one-time trusted publisher setup on PyPI before the first release.

## Installation

```bash
uv add pyrig-pypi --dev
uv run pyrig sync
```

## Setup

One-time setup before the first publish. Do not create a PyPI API token.

### New PyPI project

If the project does not exist on PyPI yet, configure a pending trusted
publisher from your account:

1. Sign in at [pypi.org](https://pypi.org)
2. Open **Your account** and select **Publishing** in the account sidebar
3. Under the **GitHub** section, add a pending publisher
4. Enter the PyPI project name exactly as it appears in `pyproject.toml`
5. Enter the GitHub organization or user, repository name, and workflow
  filename: `deploy.yml`
6. Click **Add**

The pending publisher creates the project when the workflow publishes its first
release, and then becomes a regular trusted publisher.

### Existing PyPI project

If the project already exists on PyPI, add the trusted publisher to that
project:

1. Open [Your projects](https://pypi.org/manage/projects/)
2. Select **Manage** for the project
3. Select **Publishing** in the project's sidebar
4. Under the **GitHub** section, add a publisher
5. Enter the GitHub organization or user, repository name, and workflow
  filename: `deploy.yml`
6. Click **Add**

For both paths, the values must match the publishing workflow exactly. The
package job already has the required `id-token: write` permission in the
generated workflow. The deploy workflow will then obtain a short-lived OIDC
credential and upload the package without a PyPI token or repository secret.

See PyPI's guides for
[new projects](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/)
and
[existing projects](https://docs.pypi.org/trusted-publishers/adding-a-publisher/)
for the current UI and publisher form.

## How it works

The plugin subclasses some pyrig base classes:

- `DeployWorkflowConfigFile` to add the PyPI upload step to the deployment workflow.
- `ProgrammingLanguage` to replace the python badge with a PyPI pyversions badge.
- `PackageManager` to add the args for publishing to PyPI.
- `PyprojectConfigFile` to add PyPI trove classifiers and keywords to the
  project metadata.
- `RepositorySettingsConfigFile` to mirror the project's PyPI keywords as
  GitHub topics in `.github/settings.json`.
- `ConfigureRepositoryConfigFile` to sync those topics to the repository via
  the GitHub API in `.github/configure.sh`.

And adds its own tool class:

- `PackageIndex` to wrap PyPI information and add the PyPI version badge.

## API Reference

For class- and method-level details, see the [API Reference](api.md), generated
automatically from the source.
