"""Contract tests for optional Intermesh authoring integration."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]


class IntermeshOptionalIntegrationTests(unittest.TestCase):
    def test_create_skill_offers_optional_manifest_validation(self) -> None:
        text = (ROOT / "skills" / "skill" / "SKILL.md").read_text()
        self.assertIn("command -v intermesh", text)
        self.assertIn("intermesh manifest validate", text)
        self.assertIn("If Intermesh is unavailable", text)

    def test_audit_reports_manifest_findings_without_requiring_intermesh(self) -> None:
        text = (ROOT / "skills" / "audit" / "SKILL.md").read_text()
        self.assertIn("command -v intermesh", text)
        self.assertIn("intermesh manifest validate", text)
        self.assertIn("If Intermesh is unavailable", text)


if __name__ == "__main__":
    unittest.main()
