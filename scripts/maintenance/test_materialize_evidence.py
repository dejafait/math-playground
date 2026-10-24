import gzip
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from materialize_evidence import materialize


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.content = b'{"exact_interval": ["1/3", "2/3"]}\n'
        self.archive = self.root / 'certificate.json.gz'
        self.archive.write_bytes(gzip.compress(self.content, mtime=0))
        self.item = dict(path='certificate.json', archive=self.archive.name,
                         bytes=len(self.content), sha256=hashlib.sha256(self.content).hexdigest(),
                         archive_sha256=hashlib.sha256(self.archive.read_bytes()).hexdigest())
        self.manifest = self.root / 'manifest.json'

    def save(self):
        self.manifest.write_text(json.dumps(dict(schema_version=1, artifacts=[self.item])))

    def test_restores_exact_bytes_and_reuses_existing_evidence(self):
        self.save()
        self.assertEqual(materialize(self.root, self.manifest), 1)
        self.assertEqual((self.root / 'certificate.json').read_bytes(), self.content)
        self.assertEqual(materialize(self.root, self.manifest), 0)

    def test_never_overwrites_a_changed_file(self):
        (self.root / 'certificate.json').write_bytes(b'user changes')
        self.save()
        with self.assertRaisesRegex(ValueError, 'Refusing to overwrite'):
            materialize(self.root, self.manifest)
        self.assertEqual((self.root / 'certificate.json').read_bytes(), b'user changes')

    def test_rejects_archive_corruption(self):
        self.save()
        self.archive.write_bytes(b'corrupted')
        with self.assertRaisesRegex(ValueError, 'Archive checksum'):
            materialize(self.root, self.manifest)
        self.assertFalse((self.root / 'certificate.json').exists())

    def test_rejects_wrong_expanded_hash_and_cleans_own_temporary(self):
        self.item['sha256'] = '0' * 64
        self.save()
        with self.assertRaisesRegex(ValueError, 'Expanded evidence checksum'):
            materialize(self.root, self.manifest)
        self.assertFalse((self.root / 'certificate.json').exists())
        self.assertFalse(list(self.root.glob('.restore-*')))

    def test_rejects_length_mismatch_and_path_escape(self):
        self.item['bytes'] = 1
        self.save()
        with self.assertRaisesRegex(ValueError, 'declared length'):
            materialize(self.root, self.manifest)
        self.item['path'] = '../outside.json'
        self.save()
        with self.assertRaisesRegex(ValueError, 'escapes repository'):
            materialize(self.root, self.manifest)


if __name__ == '__main__':
    unittest.main()
