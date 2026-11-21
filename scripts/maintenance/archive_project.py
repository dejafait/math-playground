#!/usr/bin/env python3
"""Preserve a stopped research workspace without placing huge blobs in Git.

Release assets contain exact file bytes, including ignored research logs and the
pre-rewrite history backup. A Git bundle preserves every current Git reference.
No credentials, environments, build caches or generated archive output are saved.
"""

import argparse
import fcntl
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import signal
import subprocess
import tarfile
import time
from contextlib import contextmanager

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = Path("scripts/maintenance/research-snapshot-manifest.json")
REPOSITORY = "dejafait/math-playground"
PART_SIZE = 1024**3
SKIP_DIRS = {
    ".git",
    ".generated",
    ".venv",
    "venv",
    "node_modules",
    ".lake",
    "__pycache__",
    ".aws",
    ".codex",
}


def run(*args, **kwargs):
    return subprocess.run(args, cwd=ROOT, check=True, **kwargs)


def sha256(path):
    result = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(8 * 1024**2), b""):
            result.update(block)
    return result.hexdigest()


def supervisors():
    listing = run("ps", "-axo", "pid=,command=", capture_output=True, text=True).stdout
    needle = str(ROOT / "scripts/loop/runner.py")
    return [
        int(line.split(None, 1)[0]) for line in listing.splitlines() if needle in line
    ]


def stop():
    for pid in supervisors():
        print(
            f"Sending graceful SIGINT to this repository's supervisor {pid}", flush=True
        )
        os.kill(pid, signal.SIGINT)
    deadline = time.monotonic() + 60
    while supervisors():
        if time.monotonic() >= deadline:
            raise RuntimeError(
                "Supervisor still alive; refusing to force-kill or snapshot"
            )
        time.sleep(1)
    with workspace():
        print(
            "Supervisor stopped and workspace lock is free; no research files deleted."
        )


@contextmanager
def workspace():
    """Hold both runner locks so research cannot resume during the snapshot."""
    handles = []
    try:
        for relative in (
            "scripts/loop-codex/process.lock",
            "scripts/loop/workspace.lock",
        ):
            path = ROOT / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            handle = path.open("a+")
            handles.append(handle)
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        yield
    finally:
        for handle in reversed(handles):
            handle.close()


def plan():
    with workspace():
        candidates = run(
            "git",
            "ls-files",
            "-m",
            "-o",
            "--exclude-standard",
            "-z",
            "--",
            "riemann",
            capture_output=True,
        ).stdout
        selected, large, size = [], [], 0
        for raw in sorted(set(candidates.split(b"\0")) - {b""}):
            path = ROOT / os.fsdecode(raw)
            length = path.stat().st_size
            if length <= 1024**2:
                selected.append(raw)
                size += length
            else:
                large.append({"path": os.fsdecode(raw), "bytes": length})
        destination = ROOT / ".generated/maintenance"
        destination.mkdir(parents=True, exist_ok=True)
        (destination / "progress.nul").write_bytes(b"\0".join(selected) + b"\0")
        (destination / "large-evidence.json").write_text(
            json.dumps(large, indent=2) + "\n"
        )
        print(
            json.dumps(
                {
                    "git_files": len(selected),
                    "git_bytes": size,
                    "release_files": len(large),
                    "release_bytes": sum(item["bytes"] for item in large),
                },
                indent=2,
            )
        )


def validate_staging():
    planned = set(
        (ROOT / ".generated/maintenance/progress.nul").read_bytes().split(b"\0")
    ) - {b""}
    staged = set(
        run(
            "git", "diff", "--cached", "--name-only", "-z", capture_output=True
        ).stdout.split(b"\0")
    ) - {b""}
    if not staged <= planned:
        raise ValueError("Staging contains unrelated changes; refusing to mix commits")
    for raw in planned:
        if (
            not raw.startswith(b"riemann/")
            or (ROOT / os.fsdecode(raw)).stat().st_size > 1024**2
        ):
            raise ValueError("Progress plan contains an oversized or unrelated path")
    print("Staging contains only planned compact mathematical files.")


def files(root):
    included, excluded = [], []
    for directory, dirs, names in os.walk(root, followlinks=False):
        base = Path(directory)
        for name in list(dirs):
            path = base / name
            relative = path.relative_to(root).as_posix()
            if name in SKIP_DIRS:
                dirs.remove(name)
                excluded.append(
                    {
                        "path": relative + "/",
                        "reason": "Git internals, generated output, credentials or rebuildable environment/cache",
                    }
                )
            elif path.is_symlink():
                dirs.remove(name)
                included.append(path)
        for name in names:
            path = base / name
            if (
                name == ".env"
                or name.startswith(".env.")
                and name not in {".env.example", ".env.template"}
                or name == ".DS_Store"
                or name.startswith("._")
                or name.endswith((".pyc", ".pyo"))
            ):
                excluded.append(
                    {
                        "path": path.relative_to(root).as_posix(),
                        "reason": "Credential file or disposable workstation/cache file",
                    }
                )
            else:
                included.append(path)
    return sorted(included), excluded


class SplitWriter:
    def __init__(self, directory, limit=PART_SIZE):
        self.directory, self.limit = directory, limit
        self.handle = None
        self.parts = []
        self.count = 0

    def write(self, data):
        original = len(data)
        while data:
            if self.handle is None or self.count == self.limit:
                if self.handle:
                    self.handle.close()
                name = f"research.tar.gz.part-{len(self.parts):04d}"
                self.handle = (self.directory / name).open("xb")
                self.parts.append(name)
                self.count = 0
            portion = data[: self.limit - self.count]
            self.handle.write(portion)
            self.count += len(portion)
            data = data[len(portion) :]
        return original

    def flush(self):
        if self.handle:
            self.handle.flush()

    def close(self):
        if self.handle:
            self.handle.close()


class HashReader:
    def __init__(self, handle):
        self.handle = handle
        self.digest = hashlib.sha256()

    def read(self, length):
        block = self.handle.read(length)
        self.digest.update(block)
        return block


class JoinedReader(io.RawIOBase):
    def __init__(self, paths):
        self.paths = iter(paths)
        self.handle = None

    def readable(self):
        return True

    def readinto(self, buffer):
        while True:
            if self.handle is None:
                try:
                    self.handle = next(self.paths).open("rb")
                except StopIteration:
                    return 0
            count = self.handle.readinto(buffer)
            if count:
                return count
            self.handle.close()
            self.handle = None

    def close(self):
        if self.handle:
            self.handle.close()
        super().close()


def archive_directory(tag):
    if not tag or any(
        character
        not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_."
        for character in tag
    ):
        raise ValueError("Unsafe release tag")
    return ROOT / ".generated/research-archives" / tag


def prepare(tag):
    with workspace():
        directory = archive_directory(tag)
        directory.mkdir(parents=True, exist_ok=False)
        bundle = directory / "repository.bundle"
        run("git", "bundle", "create", str(bundle), "--all")
        run("git", "bundle", "verify", str(bundle))
        paths, excluded = files(ROOT)
        paths.append(bundle)
        document = {
            "schema_version": 1,
            "repository": REPOSITORY,
            "tag": tag,
            "git_commit": run(
                "git", "rev-parse", "HEAD", capture_output=True, text=True
            ).stdout.strip(),
            "format": "concatenate parts in listed order, then gzip-decompress and extract tar into an empty directory",
            "files": [],
            "excluded": excluded,
        }
        writer = SplitWriter(directory)
        try:
            with gzip.GzipFile(
                fileobj=writer, mode="wb", compresslevel=1, mtime=0, filename=""
            ) as compressed:
                with tarfile.open(fileobj=compressed, mode="w|") as archive:
                    for index, path in enumerate(paths):
                        name = (
                            ".archive-history.bundle"
                            if path == bundle
                            else path.relative_to(ROOT).as_posix()
                        )
                        before = path.lstat()
                        info = archive.gettarinfo(str(path), arcname=name)
                        if path.is_symlink():
                            archive.addfile(info)
                            item = {
                                "path": name,
                                "type": "symlink",
                                "target": os.readlink(path),
                            }
                        elif path.is_file():
                            info.type, info.linkname = tarfile.REGTYPE, ""
                            with path.open("rb") as source:
                                reader = HashReader(source)
                                archive.addfile(info, reader)
                            item = {
                                "path": name,
                                "bytes": before.st_size,
                                "sha256": reader.digest.hexdigest(),
                            }
                        else:
                            raise ValueError(f"Unsupported special file: {name}")
                        after = path.lstat()
                        if (before.st_size, before.st_mtime_ns) != (
                            after.st_size,
                            after.st_mtime_ns,
                        ):
                            raise ValueError(f"File changed during snapshot: {name}")
                        document["files"].append(item)
                        if index % 1000 == 0:
                            print(
                                f"Archived {index + 1}/{len(paths)} files", flush=True
                            )
        finally:
            writer.close()
        document["parts"] = [
            {
                "name": name,
                "bytes": (directory / name).stat().st_size,
                "sha256": sha256(directory / name),
            }
            for name in writer.parts
        ]
        payload = json.dumps(document, indent=2, sort_keys=True) + "\n"
        (ROOT / MANIFEST).write_text(payload)
        (directory / "research-snapshot-manifest.json").write_text(payload)
        print(
            f"Prepared {len(paths)} exact files in {len(writer.parts)} parts; verify before upload."
        )


def load(tag):
    document = json.loads((ROOT / MANIFEST).read_text())
    if document["tag"] != tag:
        raise ValueError("Manifest tag differs from requested release")
    return document, archive_directory(tag)


def verify(tag):
    document, directory = load(tag)
    paths = [directory / part["name"] for part in document["parts"]]
    for path, part in zip(paths, document["parts"]):
        if path.stat().st_size != part["bytes"] or sha256(path) != part["sha256"]:
            raise ValueError(f"Corrupt archive part: {path.name}")
    expected = {item["path"]: item for item in document["files"]}
    seen = set()
    with io.BufferedReader(JoinedReader(paths)) as joined:
        with gzip.GzipFile(fileobj=joined) as compressed:
            with tarfile.open(fileobj=compressed, mode="r|") as archive:
                for member in archive:
                    item = expected[member.name]
                    if member.name in seen:
                        raise ValueError("Duplicate archived path")
                    seen.add(member.name)
                    if item.get("type") == "symlink":
                        if not member.issym() or member.linkname != item["target"]:
                            raise ValueError("Symlink mismatch")
                    else:
                        result = hashlib.sha256()
                        source = archive.extractfile(member)
                        for block in iter(lambda: source.read(8 * 1024**2), b""):
                            result.update(block)
                        if (
                            member.size != item["bytes"]
                            or result.hexdigest() != item["sha256"]
                        ):
                            raise ValueError(f"Archived file mismatch: {member.name}")
                    if len(seen) % 1000 == 0:
                        print(
                            f"Verified {len(seen)}/{len(expected)} file hashes",
                            flush=True,
                        )
            # Force gzip to validate its trailer, beyond tar's end marker.
            while compressed.read(8 * 1024**2):
                pass
    if seen != set(expected):
        raise ValueError("Archive is missing inventoried files")
    (directory / "verified.json").write_text(
        json.dumps({"manifest_sha256": sha256(ROOT / MANIFEST), "files": len(seen)})
    )
    print(
        f"Verified every one of {len(seen)} archived file hashes and the gzip trailer."
    )


def upload(tag):
    document, directory = load(tag)
    receipt = json.loads((directory / "verified.json").read_text())
    if receipt["manifest_sha256"] != sha256(ROOT / MANIFEST):
        raise ValueError("Archive must pass verification before upload")
    remote = run(
        "git", "ls-remote", "origin", "refs/heads/main", capture_output=True, text=True
    ).stdout.split()[0]
    head = run(
        "git", "rev-parse", "HEAD", capture_output=True, text=True
    ).stdout.strip()
    if remote != head:
        raise ValueError("Push and verify main before publishing the archive")
    # A draft release prevents an interrupted upload appearing to be complete.
    found = subprocess.run(
        ["gh", "release", "view", tag, "--repo", REPOSITORY],
        cwd=ROOT,
        capture_output=True,
    )
    if found.returncode:
        run(
            "gh",
            "release",
            "create",
            tag,
            "--repo",
            REPOSITORY,
            "--target",
            head,
            "--draft",
            "--title",
            "Final research snapshot — 22 November 2026",
            "--notes-file",
            str(ROOT / "scripts/maintenance/research-archive.md"),
        )
    assets = json.loads(
        run(
            "gh",
            "api",
            f"repos/{REPOSITORY}/releases/tags/{tag}",
            capture_output=True,
            text=True,
        ).stdout
    )["assets"]
    existing = {asset["name"]: asset for asset in assets}
    items = list(document["parts"]) + [
        {
            "name": "research-snapshot-manifest.json",
            "bytes": (ROOT / MANIFEST).stat().st_size,
            "sha256": sha256(ROOT / MANIFEST),
        }
    ]
    for item in items:
        asset = existing.get(item["name"])
        if asset:
            if (
                asset.get("digest") != "sha256:" + item["sha256"]
                or asset["size"] != item["bytes"]
            ):
                raise ValueError(
                    "Existing release asset differs; refusing to overwrite"
                )
            print(f"Already uploaded and hashed: {item['name']}", flush=True)
            continue
        print(f"Uploading {item['name']} ({item['bytes']} bytes)", flush=True)
        run(
            "gh",
            "release",
            "upload",
            tag,
            str(directory / item["name"]),
            "--repo",
            REPOSITORY,
        )
    print(
        "All assets uploaded to a DRAFT release; remote-check must download them before publication."
    )


def remote_check(tag):
    document, directory = load(tag)
    downloads = directory / "remote-readback"
    downloads.mkdir(exist_ok=True)
    items = list(document["parts"]) + [
        {
            "name": "research-snapshot-manifest.json",
            "bytes": (ROOT / MANIFEST).stat().st_size,
            "sha256": sha256(ROOT / MANIFEST),
        }
    ]
    for item in items:
        destination = downloads / item["name"]
        if not destination.exists():
            print(f"Downloading independent readback: {item['name']}", flush=True)
            run(
                "gh",
                "release",
                "download",
                tag,
                "--repo",
                REPOSITORY,
                "--pattern",
                item["name"],
                "--dir",
                str(downloads),
            )
        if (
            destination.stat().st_size != item["bytes"]
            or sha256(destination) != item["sha256"]
        ):
            raise ValueError("GitHub readback checksum mismatch: " + item["name"])
        print(f"GitHub readback SHA-256 matches: {item['name']}", flush=True)
    run(
        "gh",
        "release",
        "edit",
        tag,
        "--repo",
        REPOSITORY,
        "--draft=false",
        "--latest=false",
    )
    (directory / "remote-verified.json").write_text(
        json.dumps({"manifest_sha256": sha256(ROOT / MANIFEST), "assets": len(items)})
    )
    print(
        f"Published and independently downloaded every asset: https://github.com/{REPOSITORY}/releases/tag/{tag}"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "action",
        choices=(
            "stop",
            "plan",
            "validate-staging",
            "prepare",
            "verify",
            "upload",
            "remote-check",
        ),
    )
    parser.add_argument("--tag", default="research-snapshot-2026-11-22")
    args = parser.parse_args()
    if args.action in {"stop", "plan", "validate-staging"}:
        globals()[args.action.replace("-", "_")]()
    else:
        globals()[args.action.replace("-", "_")](args.tag)


if __name__ == "__main__":
    main()
