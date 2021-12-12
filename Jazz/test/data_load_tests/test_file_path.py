
import unittest
from pathlib import Path


class TestFilePath(unittest.TestCase):
    def test_file_path(self) -> None:
        p = Path("working/directory/fileName.ext")
        self.assertEqual(str(p.parent), "working/directory")
        self.assertEqual(str(p.with_name("newFile.py")), "working/directory/newFile.py")
        self.assertEqual(p.stem, "fileName")
        self.assertEqual(p.name, "fileName.ext")
        self.assertEqual(p.suffix, ".ext")
