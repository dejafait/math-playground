"""Step 459 focused shared-helper authorization tests; archives are read only."""
import hashlib
import io
import json
from pathlib import Path
from unittest.mock import patch
import parameterized_input as p
import receive_parameterized as r

HERE = Path(__file__).resolve().parent
OUT = HERE/'output-459'
BASE = HERE/'output-457/old-nonzero'


def main():
    source = BASE/'source.jsonl'
    raw = source.read_bytes()
    changed = raw.replace(b'"format":', b'"format" :', 1)
    assert changed != raw
    original_open = Path.open
    reads = 0

    def altered_second_open(path, *args, **kwargs):
        nonlocal reads
        if path == source and args and args[0] == 'rb':
            reads += 1
            if reads == 2:
                return io.BytesIO(changed)
        return original_open(path, *args, **kwargs)

    records = []
    with patch.object(Path, 'open', altered_second_open):
        try:
            p.request(source, BASE/'request.json')
        except p.Rejected as error:
            assert str(error) == 'source changed during checking' and reads == 2
            records.append(dict(test='second-source-read-changed', accepted=False,
                                reason=str(error), reads=reads,
                                original_sha256=hashlib.sha256(raw).hexdigest(),
                                second_read_sha256=hashlib.sha256(changed).hexdigest()))
        else:
            raise AssertionError('changed second source read accepted')
    assert source.read_bytes() == raw

    # An internally valid certificate for a different caller cannot replace the
    # certificate authorized by these two original paths.
    try:
        r.receive(HERE/'output-457/singleton/certificate.json', source, BASE/'request.json')
    except p.Rejected as error:
        assert str(error) == 'source retention'
        records.append(dict(test='valid-other-caller-certificate',accepted=False,reason=str(error)))
    else:
        raise AssertionError('valid unauthorized certificate accepted')
    result = dict(checks=records, failures=[], archive_source_unchanged=True,
                  assumptions=['caller chooses trusted source/request paths',
                               'SHA256 collision resistance for separate source reads'],
                  limitation='Second checker read is not separately byte/depth capped; no total hostile-race resource bound is claimed.',
                  code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    p.write_json(OUT/'authorization-checks.json',result)
    print(json.dumps(dict(checks=len(records),failures=[],evidence=str(OUT/'authorization-checks.json'))))


if __name__ == '__main__':
    main()
