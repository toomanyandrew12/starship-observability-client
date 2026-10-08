from __future__ import annotations

import unittest
from unittest.mock import patch

import app


class StatusTests(unittest.TestCase):
    @patch("app.entry_points", return_value=[])
    def test_missing_backend_has_stable_error(self, _entry_points: object) -> None:
        with self.assertRaisesRegex(RuntimeError, "StatusBackend not found"):
            app.load_status()


if __name__ == "__main__":
    unittest.main()
