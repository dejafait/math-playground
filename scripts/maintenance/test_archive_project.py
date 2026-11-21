import gzip
import hashlib
import io
import json
from pathlib import Path
import tarfile
import tempfile
import unittest
from unittest.mock import patch

import archive_project as archive


class ArchiveTests(unittest.TestCase):
    def test_snapshot_keeps_ignored_evidence_and_logs_but_excludes_credentials(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name in (
                ".git/config",
                ".generated/output",
                ".venv/bin/python",
                ".env",
                "riemann/certificate.json",
                "scripts/loop-codex/stdout.log",
                ".history-backups/original.bundle",
            ):
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("preserve or exclude according to scope")
            included, excluded = archive.files(root)
            names = {path.relative_to(root).as_posix() for path in included}
            self.assertEqual(
                names,
                {
                    "riemann/certificate.json",
                    "scripts/loop-codex/stdout.log",
                    ".history-backups/original.bundle",
                },
            )
            self.assertEqual(len(excluded), 4)

    def test_verify_reads_every_file_across_part_boundaries_and_rejects_corruption(
        self,
    ):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            manifest = root / archive.MANIFEST
            manifest.parent.mkdir(parents=True)
            tag = "test-snapshot"
            with patch.object(archive, "ROOT", root):
                directory = archive.archive_directory(tag)
                directory.mkdir(parents=True)
                content = b"mathematical evidence\x00" * 100
                raw = io.BytesIO()
                with tarfile.open(fileobj=raw, mode="w") as handle:
                    info = tarfile.TarInfo("riemann/evidence.bin")
                    info.size = len(content)
                    handle.addfile(info, io.BytesIO(content))
                writer = archive.SplitWriter(directory, limit=17)
                writer.write(gzip.compress(raw.getvalue()))
                writer.close()
                parts = [
                    {
                        "name": name,
                        "bytes": (directory / name).stat().st_size,
                        "sha256": archive.sha256(directory / name),
                    }
                    for name in writer.parts
                ]
                document = {
                    "tag": tag,
                    "parts": parts,
                    "files": [
                        {
                            "path": "riemann/evidence.bin",
                            "bytes": len(content),
                            "sha256": hashlib.sha256(content).hexdigest(),
                        }
                    ],
                }
                manifest.write_text(json.dumps(document))
                archive.verify(tag)
                self.assertTrue((directory / "verified.json").exists())
                (directory / parts[0]["name"]).write_bytes(b"corrupted archive")
                with self.assertRaisesRegex(ValueError, "Corrupt archive part"):
                    archive.verify(tag)


if __name__ == "__main__":
    unittest.main()
