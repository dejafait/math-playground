# Marked-octic S-class execution attempt

The approved target is to compute the ordinary group
Cl(O_K[1/330])[2] with unconditional completeness and representative
certificates. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-marked-octic-s-class-two-torsion.md`.
This is an implementation attempt under that assessment, not a new
literature review or an approval of a different mathematical target.

The main gap remains primitive integer emptiness for residual Beal
signatures. This intermediate group could supply the non-unit part of
supported square classes for L113's marked curve. Essential inputs are
L115's entire degree-eight field, L116's maximal basis and L117's eight
exact ideal kernels; L114 fixes support. Ordinary classes, rather than
narrow classes, are required. Supported units, real/finite point images,
surviving-cover points, degree-nine root recovery, remaining factors,
both L095 integer systems and minus-eleven remain independent gaps.

Continuation requires full unconditional ordinary-class certification,
transport of every supported ideal and a tracked complete quotient with
two-torsion representatives. A partial relation computation or an
uncertified software return cannot meet the threshold. Abandon this
execution attempt if no backend can be obtained within one bounded local
availability/cache/source-acquisition test. Do not repeat backend probes
as a mathematical advance. Preserve all existing work, including L108
and ATTEMPTS/050–051.

Initial observations: `gp`, `pari-gp`, `sage` are absent from PATH;
`cypari2`, `sage`, `sageall`, `sympy`, `flint` are absent from the active
Python. Conventional Homebrew/MacPorts GP locations and PARI libraries
are absent. ATTEMPTS/045 records the analogous backend obstruction for
L098's different octic; it supplies neither a group value here nor a
ban on a concrete new execution attempt. A bounded read-only cache
lookup and official PARI source acquisition are the remaining execution
tests. No class calculation has run at this checkpoint.

## Completed execution test

The bounded lookup found no cached PARI archive or GP executable in the
explicit patterns saved in
`scripts/pair-genus-two/marked-octic-s-class-execution-record.json`.
The attempted source acquisition was

```sh
curl --fail --location --connect-timeout 10 --max-time 30 \
  --output /private/tmp/beal-marked-octic-pari-2.17.2.tar.gz \
  https://pari.math.u-bordeaux.fr/pub/pari/unix/pari-2.17.2.tar.gz
```

It returned code 6: `Could not resolve host: pari.math.u-bordeaux.fr`.
Zero bytes were downloaded. DNS failure occurred before any HTTP request;
the existence of this versioned archive, its contents and any build
feasibility were not tested. No source or binary was installed or run.
The record retains the complete command, stdout, stderr, exit code,
local environment and all bounded cache results. Both the complete
command record and complete cache map were inspected with the shared
JSON inspector. This is execution evidence, not a mathematical
certificate. No `bnfinit`, `bnfcertify`, ideal transport, relation matrix,
Smith calculation or representative extraction occurred.

The actual result is **STALLED**, not a computed group, a bound on it,
or new mathematical negative evidence. Classification REPRODUCTION
describes the intended assessed known-method implementation; no known
theorem or instance calculation was successfully reproduced. The
backend obstruction was already known as a risk and is persistent
across related execution work. This attempt adds a concrete failed
acquisition transcript but does not reset an exploration budget or
justify repeating availability probes. The target is parked pending
an actually executable certified backend and bounded run plan, or
independently checkable complete instance data. The stopping condition
does not reject the underlying method.

No mathematical argument changed, so PROOF.md, DAG.md and every lemma
are preserved. The anticipated independently testable continuation is
the exact real point image for this same marked curve; it needs its own
source approval because support containment did not assess full local
images. No real-image calculation or lemma is attempted here.
ATTEMPTS/052 records the execution stop. Full matching Mathlib coverage
for certified S-class arithmetic remains unchecked; unknown coverage is
not an absence claim. The precise imported general algorithm citations
remain those in the prior SPECIALIZE assessment (Lenstra, Section 2.5,
Theorem 5.4, Theorems 6.1–6.2, and the assessed PARI routine contracts);
this failed run supplies no instance specialization to import.
