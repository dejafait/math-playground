# Version proof evidence; ignore disposable workspace

Proof evidence belongs in Git even when a program can regenerate it. The saved
certificate identifies the actual output used by a lemma or review; rerunning a
program with changed inputs, dependencies or arithmetic does not necessarily
reproduce that evidence. Size and file extension do not decide its status.

A recommended per-topic layout is:

```text
riemann/scripts/laguerre/
  certify_finite_witness_band.py
  audit_finite_witness_band.py
  inputs/                         tracked intentional inputs
  certificates/                   tracked results used by proofs and audits
    finite-witness-band-certificate.json
    exterior-ordering-certificate.json
  reports/                        tracked verification/provenance notes
  .generated/                     ignored temporary/intermediate results
  .scratch/                       ignored experiments not used as evidence
```

Keep certificate producers and verifiers, exact input data or immutable source
identities, proof-linked outputs, meaningful failed-run evidence and source
snapshots required for replay. A concise topic README should identify generation
and verification commands, relevant code/dependency versions, input/output
hashes and implementation assumptions. Regeneration is an additional check,
not a substitute for versioning the certificate that was actually reviewed.

Ignore caches, temporary candidates, duplicate exploratory dumps, ordinary raw
logs and unfinished intermediates only when they are not part of a proof,
failure decision, provenance chain or reproducibility contract. If a temporary
result becomes evidence, promote the required file and its provenance into a
tracked folder before citing it. Failed evidence can also deserve promotion.

The revised proposed ignore policy excludes explicit ephemeral directories,
not all JSON, text, binary files or output-* directories. Legacy certificate
paths are included by default; no relocation is necessary just to retain them.

A later organizational move should be its own maintenance commit: inventory
all references, retain certificate bytes where possible, update producers,
verifiers and Markdown paths together, and run the affected checks. If embedded
paths or source hashes require changed certificate bytes, regenerate/review
those changes explicitly; do not silently transplant metadata or change the
mathematical conclusion. The history rewrite must preserve original evidence
and record any path mapping.

No certificates were moved or deleted for this proposal. In particular, the two
large Laguerre certificates remain at their existing paths and stay versioned.
The previous 79.6 MB hypothetical filtered tree is withdrawn as a proposed
storage target because it discarded evidence we intend to retain.
