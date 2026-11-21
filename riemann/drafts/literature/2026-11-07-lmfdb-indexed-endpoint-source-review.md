# Indexed endpoint data alternative — completed, record access blocked

TARGET: Assess whether LMFDB's zeta-zero data provide certified indexed rational enclosures for gamma_6002 and gamma_6003 meeting L836's input contract.
CHECKED: 2026-11-07
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Read L836's exact two-index contract, reused the fixed-shift software/product assessment and prior setup stop, searched LMFDB precision/indexing, and inspected LMFDB's three primary provenance pages, release-linked reader/exporter and Platt's primary isolation theorem. Exact list requests were inaccessible, both advertised bulk paths returned HTTP403, and bounded local curl failed DNS; no records were obtained.
SOURCE_EVIDENCE: LMFDB Release1.2.1 Source/Completeness/Reliability pages, checked2026-11-07; reader/exporter commit6ac43f6613bc3ad150712ebcbaa35d113ff941f3, platt_zeros.py lines50–81/92–140/153–160 and zetazeros.py lines51–91; Platt, Isolating some non-trivial zeros of Zeta, Math.Comp.86(2017),2449–2467, accepted manuscript Sections4.1–5, Theorem5.1, printed pp6–8. Direct links and qualifications below.
COMPARISON: Primary sources document one-based ordered data with storage error +/-2^-102 and rigorous Turing completeness; the raw integer/dyadic format could supply L836's finite inputs. This is known data provenance, not a new bound. The exact records remain inaccessible, and the decimal export's complete rounding budget was not verified. No enclosure or overlap is certified.
GAP: Actual records for indices6002/6003, exact rational enclosing endpoints, export-error accounting if decimal transport is used, and every L836(5)–(8) domain/sign check remain missing. The source contract alone supplies none of those values.
REASON: Park this data-dependent overlap route after independently testing the published-data alternative to the failed FLINT setup. Do not infer inaccurate data, a false theorem or a failed overlap from transport failures; reopen only with a materially changed accessible record path and its exact error contract. Select an independent central coefficient-space source target separately.
LITERATURE_REASON: Published-data provenance and certification are essential unread inputs outside the version-pinned FLINT assessment; the symbolic envelope itself already has adequate coverage.
SCOPE: One source-only comparison for the two exact indices. No zero computation, installation retry, numerical overlap test, new analytic bound or approval based solely on displayed digits.

The following nomination paragraphs record the invocation-start scope;
their references to unread evidence are superseded by the completed
comparison below. The proposed calculation is preserved, not executed.

The main gap remains actual-Xi all-degree mixed positivity. This modest
intermediate target could make the fixed-shift overlap test executable;
even a successful join would leave growing shifts and the main gap open.
It is not a proposed creative positivity mechanism.

L836 requires rational intervals [l,u] and [v,w] enclosing the actual
positive-height ordinates with indices 6002 and 6003 and satisfying
4<l<=u<v<=w<H, H=3000175332800. Primary evidence must identify the
index convention, establish completeness/order, and give an error or
rounding rule that proves inclusion. A numerical table, a quoted digit
count without its guarantee, or two isolated sign changes is inadequate.
L834's imported simplicity and total-count argument remains necessary
when identifying critical-line records with all positive-height zeros.

For a subsequent overlap test the essential local inputs remain L836,
L835, L834, L832 and L467, with inherited L018/L021/L776 conventions.
C832a and its completed audit already record the enlarged finite order
m=9000000000000; do not derive it again or infer it merely from PF6001.
No use of that result or numerical sign computation is made in this
nomination. Any later test still owes all of L836(5)–(8), outward
logarithm/pi arithmetic, domain checks and a strict upper bound below
zero. Published endpoint data would not settle those obligations.

Continue only if inspected primary evidence establishes the needed
indexed inclusion contract and an accessible record path. If the data
have no provable error/completeness guarantee, record that specific
source mismatch and park this alternative; do not repeatedly retrieve
the same unsupported digits or retry unchanged setup. Missing or
ambiguous evidence is not a certified negative overlap value.

Preserve the FLINT setup failure, the step659/667 mathematical stops and
the completed L836 audit. The zero-ordinate approval-loop stop concerns
L756's scalar cancellation and supplies neither these records nor a ban
on testing a different data source. No cross-notebook input is proposed.
Full matching Mathlib coverage remains unchecked. This nomination
neither derives mathematics nor approves its own new source scope.

## Review working checkpoint — 7 November 2026

Inspected LMFDB's Source, Reliability and Completeness pages: they give
absolute storage error +/-2^-102, rigorous Turing completeness and the
first 103800788359 positive zeros through height 30610046000. Inspected
the release-linked reader at commit
6ac43f6613bc3ad150712ebcbaa35d113ff941f3: block counts label the zeros
one-based and raw ordinates use an exact integer times 2^-101 plus a
binary block origin. Platt's accepted manuscript, Theorem 5.1 and
Sections 4.1–5, gives the primary isolation/completeness provenance.

Access is unresolved: the exact two-row list endpoint is inaccessible
to the web tool, both advertised bulk-directory paths return HTTP403,
and a bounded local curl request fails DNS resolution. No record,
rational enclosure, rounding certificate or overlap value was obtained.
Do not replace these failures with approximate roots or interpret them
as a mathematical failure of L836. Final disposition and the independent
continuation remain to be recorded; no lemma or script was modified.

## Completed comparison and disposition

Primary dataset pages inspected, LMFDB Release1.2.1, 7 November2026:
[Source](https://www.lmfdb.org/zeros/zeta/Source),
[Completeness](https://www.lmfdb.org/zeros/zeta/Completeness), and
[Reliability](https://www.lmfdb.org/zeros/zeta/Reliability).
Together they specify all 103800788359 positive-height zeros through
30610046000, absolute storage error +/-2^-102, and rigorous Turing
completeness. Reliability also reports an independent Büthe comparison
and resolution of108 discrepancies in favor of the presented data.
That report is provenance, not a local replay. The
[landing page](https://www.lmfdb.org/zeros/zeta/) states an absolute
decimal precision +/-2.5*10^-31. It is not a raw endpoint certificate.

The deployment's Source link identifies commit
6ac43f6613bc3ad150712ebcbaa35d113ff941f3. Read its
[platt_zeros.py](https://raw.githubusercontent.com/LMFDB/lmfdb/6ac43f6613bc3ad150712ebcbaa35d113ff941f3/lmfdb/zeros/zeta/platt_zeros.py),
especially lines50–81,92–140,153–160. A block header contains binary
origins and N(t) counts; thirteen-byte integer increments accumulate
in an integer, scaled by2^-101. The label increments from Nt0 before
emission and the requested starting index is an inclusive filter.
This supports the one-based interpretation of6002/6003, rather than
an offset guessed from two sign changes. Crossing blocks/files uses
the stored counts and index database. These are reader semantics,
not an independent proof of that database's correctness.

Read the same commit's
[zetazeros.py](https://raw.githubusercontent.com/LMFDB/lmfdb/6ac43f6613bc3ad150712ebcbaa35d113ff941f3/lmfdb/zeros/zeta/zetazeros.py),
lines51–91: /list parses an integer N, calls the indexed reader and
formats mpmath values using nstr. This is decimal transport, with
precision changes in the reader; no directed interval export is
present. No new rounding estimate is proved in this literature turn.
For a future raw-data path, preserve the exact origin/integer encoding
and use the cited storage error, instead of inferring a bound from
the printed digit count. Full nstr/reader arithmetic certification was
not performed, so this review does not approve decimal conversion.

Primary mathematical provenance: D.J.Platt, *Isolating some non-trivial
zeros of Zeta*, Mathematics of Computation86(307)(2017),2449–2467,
[DOI](https://doi.org/10.1090/mcom/3198),
[accepted manuscript](https://research-information.bris.ac.uk/ws/portalfiles/portal/78836669/platt_zeta_submitted.pdf).
Read Sections4.1–5, printed pp6–8: rigorous counts are matched to
observed sign changes, isolation is checked on both sides of the
proposed root, and Section5 records interval arithmetic, the achieved
absolute error +/-2^-102 and the complete103800788359-zero census.
Theorem5.1 gives simplicity and real part1/2 for every nontrivial zero
with |Im rho|<=30610046000. Its next paragraph explicitly identifies
the stored ordinates with Bober's LMFDB distribution. Import that
finite computation by citation; no reproof or manuscript-wide code
audit is claimed. It gives neither zeros above that height nor RH.

LMFDB's Source instead cites Platt's *Computing pi(x) analytically*,
Math.Comp.84(2015),1521–1535, DOI10.1090/S0025-5718-2014-02884-6.
Its publisher link returned403. The accessible
[arXiv:1203.5712v3](https://arxiv.org/pdf/1203.5712v3), Section7,
printed p12, records the same census and points to the isolation
method; it is corroboration, not a replacement error theorem. An
initial guessed arXiv1305.3821 URL was unrelated and discarded. The
guessed main.py reader path returned404; the release-linked actual
reader paths above resolved it. No secondary summary is an input.

### Access test and exact limitation

The inspected indexed route is
https://www.lmfdb.org/zeros/zeta/list?N=6002&limit=2&format=plain .
The web tool could not access it or its download form; the main
query page also failed. This establishes a failure of the available
transport, not nonexistence of the endpoint or records. Both advertised
bulk paths, https://beta.lmfdb.org/data/riemann-zeta-zeros/ and
https://beta.lmfdb.org/riemann-zeta-zeros/ , returned HTTP403. A single
bounded local curl request to the exact list endpoint exited6 with
"Could not resolve host: www.lmfdb.org". No requests used credentials,
installed packages, API keys or a third-party numerical root table.

Thus indexing/completeness/storage-error coverage is substantially
better established than at invocation start, but the combined
continuation test also required accessible exact records. That part
fails in this environment. SOURCE_BLOCKED applies to this provider
route, not to the truth of its documented guarantees. Neither gamma
record, any rational endpoints, the ordering/domain inequality nor a
sign of L836(8) has been certified. The failed setup and original
step659/667 stops remain in force at their original scopes.

Park this dependent computation. The independent nomination is a
[coefficient-Hankel Schur/covariance source comparison](2026-11-07-logarithmic-hankel-schur-covariance-review.md),
which remains REVIEW_REQUIRED. It is not covered by this assessment
and no covariance representation or sign estimate is derived here.
The actual theta-specific signed bridge is still missing, so no
creative mathematical attempt is falsely marked ready. No Mathlib
coverage check was material to data transport; full matching coverage
remains unchecked. PROOF.md/DAG.md and all lemma/script files are
unchanged because this turn changes source status, not the argument.
