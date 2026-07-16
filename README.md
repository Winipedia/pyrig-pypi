# pyrig-pypi

<!-- project-status -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-pypi/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-pypi/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-pypi/deploy.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-pypi/actions/workflows/deploy.yml)
[![ProjectTester](https://codecov.io/gh/Winipedia/pyrig-pypi/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-pypi)
<!-- code-quality -->
[![ByteOrderMarkerFormatter](https://img.shields.io/badge/BOM-fix--byte--order--marker-orange)](https://github.com/pre-commit/pre-commit-hooks)
[![CaseConflictChecker](https://img.shields.io/badge/case--conflict-check--case--conflict-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![DependencyAuditor](https://img.shields.io/badge/security-pip--audit-blue?logo=python)](https://github.com/pypa/pip-audit)
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
[![DocsBuilder](https://img.shields.io/badge/MkDocs-Documentation-326CE5?logo=mkdocs&logoColor=white)](https://Winipedia.github.io/pyrig-pypi)
[![PackageIndex](https://img.shields.io/pypi/v/pyrig-pypi?logo=pypi&logoColor=white)](https://pypi.org/project/pyrig-pypi)
[![ProgrammingLanguage](https://img.shields.io/pypi/pyversions/pyrig-pypi)](https://www.python.org)
[![License](https://img.shields.io/github/license/Winipedia/pyrig-pypi)](https://github.com/Winipedia/pyrig-pypi/blob/main/LICENSE)

---

> A pyrig plugin for publishing Python packages to PyPI.

---

## Overview

pyrig-pypi is a [pyrig](https://github.com/Winipedia/pyrig) plugin that publishes
your package to PyPI automatically as part of your CI/CD pipeline.

## What it adds

- **Automatic publishing** — a build-and-publish step that uploads your package
  to PyPI after a successful release.
- **PyPI badges** — a package-version badge and a PyPI-driven Python versions
  badge.
- **PyPI metadata** — trove classifiers and keywords in `pyproject.toml` for
  discoverability.

## Usage

```bash
uv add pyrig-pypi --dev
uv run pyrig sync
```

Publishing from CI requires a `PYPI_TOKEN` repository secret — see the
documentation for the one-time setup.

## Documentation

Full documentation, including the auto-generated API reference, is available on
the [documentation site](https://Winipedia.github.io/pyrig-pypi).
