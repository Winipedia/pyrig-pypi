"""Explicit references for reviewed dead code false positives."""

from pyrig.rig.configs.base.workflow import WorkflowConfigFile
from pyrig.rig.tools.base.tool import Tool

from pyrig_pypi.rig.tools.packages.index import PackageIndex
from pyrig_pypi.rig.tools.programming_language import ProgrammingLanguage

_CONFIG_FILE_OVERRIDES = (
    WorkflowConfigFile.concurrency_cancel_in_progress,
    WorkflowConfigFile.workflow_triggers,
)
_TOOLS = (
    PackageIndex,
    ProgrammingLanguage,
)
_TOOLS_OVERRIDES = (
    Tool.dev_dependencies,
    Tool.group,
    Tool.image_url,
    Tool.link_url,
    Tool.name,
)
