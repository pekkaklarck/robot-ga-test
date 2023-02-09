from pathlib import Path

from robot.api import SuiteVisitor
from robot.result import TestSuite


class SummaryGenerator(SuiteVisitor):

    def __init__(self, path: Path):
        self.path = path

    def visit_suite(self, suite: TestSuite):
        stats = suite.statistics
        self.path.write_text(f'''\
| Total | Passed | Skipped | Failed |
|:-----:|:------:|:-------:|:------:|
| {stats.total} | {stats.passed} | {stats.skipped} | {stats.failed} |
''')
