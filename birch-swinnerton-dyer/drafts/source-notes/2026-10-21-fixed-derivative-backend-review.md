# Fixed derivative backend review — step 397

2026-10-21. Literature-only review of the unchanged finite-replay target.
No derivative, new mathematical estimate, lemma or mathematical script
has been produced. This early save preserves the unfinished review.

The main gap is arbitrary-curve rank/order equality for analytic order
at least two. The intermediate target is L101's fixed M=Y=128 finite
certificate. Its downstream use would be independent complex upper-bound
evidence alongside L099; L035 already covers this known fixed order.
Reuse the analytic sources and preserve ATTEMPTS/043 and /045.
Continue only with a source-covered, usable backend and complete outward
export/replay; otherwise park dependent evaluation without changing the
cutoffs or replacing the analytic method in this turn.

## Observed local availability

Read-only environment probes found no `flint` module in the functioning
PATH interpreters: CPython 3.11.16, 3.12.15, 3.13.16, 3.14.8, 3.15.0
and Xcode CPython 3.9.6. The default is Homebrew Python 3.15.0. The
old Framework Python 3.5 executable terminates with exit -9; no package
availability is inferred from that failure. A first broad executable
probe also matched `-config` helpers and an incompatible 32-bit binary;
the corrected probe restricted names to python3 or python3.<digits>.

No `sage`, `gp` or `pkg-config` executable was found. Neither FLINT nor
Arb has an entry in /opt/homebrew/Cellar or /opt/homebrew/opt. The usual
/opt/homebrew and /usr/local FLINT header/library paths were absent.
This is a bounded availability check, not a search of the whole disk.

A read-only request from the execution environment to
https://pypi.org/pypi/python-flint/0.8.0/json failed with
`URLError: [Errno 8] nodename nor servname provided, or not known`.
Web retrieval of official sources works separately; it does not prove
the local interpreter can retrieve or import a wheel. No installation,
system change, API key, binary acquisition or derivative evaluation ran.

## Inspected release-specific primary sources

Candidate source pair: python-flint 0.8.0 and FLINT 3.3.1. Official PyPI
release notes report the 0.8.0 wheels bundle FLINT 3.3.1 and MPFR 4.2.2:
https://pypi.org/pypi/python-flint/json . This is distribution metadata,
not observed installed-library provenance. The release-specific source
`pyproject.toml` declares version 0.8.0 and Python >=3.11:
https://raw.githubusercontent.com/flintlib/python-flint/0.8.0/pyproject.toml .
The official compatibility table lists CPython 3.11–3.14 for that release;
default Python 3.15 is outside the reported tested range. A working 3.13
interpreter is present, but its backend remains absent.

Read python-flint 0.8.0 `src/flint/types/acb.pyx`, callback lines 93–114
and integral implementation lines 2381–2484:
https://raw.githubusercontent.com/flintlib/python-flint/0.8.0/src/flint/types/acb.pyx .
The wrapper passes the order-one analytic flag, rejects unsupported
orders with an indeterminate ball, requires an acb result, and propagates
recorded TypeError/ValueError after the integration. Its call discards
the C integration status: Python returns the resulting ball. Therefore
there is no Python success flag on which to base this certificate.
Full returned containment, finiteness and width remain indispensable.

Read `arb.pyx` lines 202–278 and 304–326:
https://raw.githubusercontent.com/flintlib/python-flint/0.8.0/src/flint/types/arb.pyx .
`lower()` and `upper()` give directed outward exact floating-point
bounds; `man_exp()` requires an exact finite value and exports integer
mantissa/exponent, while `fmpq()` exports an exact finite value as a
rational. These provide a source-covered rational endpoint route
without decimal display parsing or binary64 conversion. Implementation
and actual output validation remain undone.

Read FLINT v3.3.1 `doc/source/acb_calc.rst`, callback and finite-integral
contract (lines 13–163):
https://raw.githubusercontent.com/flintlib/flint/v3.3.1/doc/source/acb_calc.rst .
This pins the general source contract previously read only on mutable
main. It is not evidence of a local binary or a completed callback.

Remaining review at this save: complete the pinned branch/endpoint
contract passages and decide the gate honestly; if blocked, select an
independently testable continuation using existing coverage, without
performing its mathematics this turn. Mathlib remains not checked.

## Completed source comparison and gate decision

Completed the release-specific `acb.pyx` logarithm passage, lines
491–504: `log(analytic=...)` calls `acb_log_analytic` with that flag.
This supplies the branch-check interface required by L101; it does not
certify an unwritten user callback. Read FLINT v3.3.1 `acb_calc.rst`
lines 127–169 and 190–219: requested errors are guidelines, accumulated
error can exceed them, and evaluation limits are not hard execution
bounds. External execution bounds and actual widths must be checked.

Read matching FLINT v3.3.1 `arb.rst`, lines 399–415:
https://raw.githubusercontent.com/flintlib/flint/v3.3.1/doc/source/arb.rst .
It confirms the directed lower/upper routines used by the wrapper.
Read `acb.rst`, lines 5–20 and 43–48:
https://raw.githubusercontent.com/flintlib/flint/v3.3.1/doc/source/acb.rst .
Separate real/imaginary enclosures justify real projection of a valid
complex enclosure for this real integral. These are imported interface
guarantees, not new lemmas. No display or overlap test proves containment.

The search also returned old python-flint 0.3.0 and mutable FLINT
3.7.0-dev documentation; neither specifies the pinned candidate.
Guessed python-flint workflow paths `.github/workflows/build_wheels.yml`
and `wheels.yml` returned 404 and supply no evidence. Successful web-tool
PyPI retrieval does not establish a locally retrievable artifact, wheel
hash, installed version or linkage. The specific integral/endpoint and
callback searches found known machinery, not an original theorem.

Decision: SOURCE_BLOCKED for the exact finite-replay target's essential
concrete executable/interface input. The primary contracts are accessible;
matching them to an actually available backend is blocked. This is not
a missing theorem or mathematical impossibility. The older no-module
observation now has additional interpreter, C-installation and failed
local distribution-request evidence. No whole-disk absence is claimed.
Do not approve a hypothetical binary or repeat this audit without
changed availability evidence. No permissions were requested and no
automatic approval rejection occurred.

The original TARGET and thresholds remain in its assessment. If a
backend becomes available, match its actual version/linkage, whole-set
callback/branch tests, exact outward export and complete independent
128-coefficient/128-kernel replay. Fix execution bounds before invoking
it and retain L101's full signed error B. No finite kernel, parameter
interval or derivative was produced here. Nonfinite, overly wide or
missing outputs fail the certificate; a final interval containing zero
is inconclusive about nonvanishing.

## Independent proposed continuation, not approved mathematics

Park the unavailable-library implementation. Propose a source-only
comparison of published exponential/logarithm Taylor remainder bounds
for rational finite-interval integration. This avoids the absent binary
and has an independently testable output: all 128 L101 finite kernels,
each with radius at most 2^-50, on the unchanged path [1,128]. No new
expansion, quadrature rule, panel count, estimate or feasibility claim
is derived here; that would exceed this turn's target.

Reuse L101's analytic tails and finite-error contract and L031's already
assessed coefficient/parameter rules. Their coverage does not approve
a new rational integration algorithm. The next assessment is
REVIEW_REQUIRED: inspect primary remainder hypotheses and integration
error cases before any proof or script. Continue only if source
comparison supports a finite rational certificate and an explicit
bounded plan; otherwise preserve the source gap. L035 overlap and
ATTEMPTS/043/045 remain unchanged. This proposes a different mechanism;
it neither silently changes the method nor claims attainable widths.

This step is NEGATIVE / LITERATURE / NOVELTY_UNCHECKED: new availability
and interface evidence changes routing, without a new mathematical BSD
result. Mathematical exploration usage remains 0 of 3. Mathlib matching
and supporting coverage remain not checked.
