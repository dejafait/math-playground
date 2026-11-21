# Fixed-shift certified overlap test — completed source assessment

TARGET: Test L836(8) at k=6002 and proposed m=9000000000000 using certified indexed endpoint intervals and a separately justified PF_m range.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready residual-envelope and finite-PF comparisons; inspected the step659/667 stop records. Searched FLINT/Arb indexed zeta-zero isolation, Turing completeness, python-flint versioned bindings and verified-height PF terminology; primary API contracts and relevant implementation cases were read as detailed below. No indexed records or overlap computation were produced.
SOURCE_EVIDENCE: Reuse Katkova math/0505174v1 Theorem B p.5/product pp.5–6, Platt–Trudgian 2004.09765v1 Theorem1/Section2 pp.2–3 and Bellotti–Wong 2412.15470v2 Theorem1.1/Section5 pp.1,23–24 via L832/L834/L467 and ready assessments. Read Michałowski https://arxiv.org/html/2607.16795v1#S1.SS2 Section1.2; FLINT v3.3.1 doc/source/acb_dirichlet.rst lines588–656 and relevant native cases; python-flint tag0.8.0 acb.pyx zeta_zero and arb.pyx directed endpoints/log/pi; Arb2.23.0 ball-semantics contract. Direct versioned URLs and ranges below.
COMPARISON: Known indexed isolation/refinement supplies a rigorous way to produce the missing enclosures, with Rosser range covering the requested indices and an independent imported simple ordering below H. The sector source explicitly covers m+1<=pi H; no new general PF theorem is needed. Neither source evaluates L836(8) or supplies stored endpoint records for this target.
GAP: Execute the version-checked indexed algorithm, retain exact outward endpoints and their index provenance, verify all interval domains and proposed PF-order applicability, and certify the sign of the entire L836(8) expression. Only PF6001 remains established locally until the separate applicability argument is written; overlap and growing-shift signs remain open.
REASON: Essential theorem/software coverage now supports one bounded standard-method specialization. Approval concerns the stated test and inspected versions, not its unperformed numerical result; no source blocker remains, while runtime setup is still unpaid.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED identified essential indexed-zero certification and enlarged-order applicability outside the prior symbolic-audit scope; this review closes that source gap without calculating or enlarging PF locally.
SCOPE: One test at k=6002, J=6003, proposed m=9000000000000, exact R and s=(1+q)/2, using L836(5)–(8) and the versioned indexed/ball interfaces below. No parameter sweep, extra shift, omitted costs, general sector reproof, global sign claim or creative mechanism is covered. The separate next turn must perform the applicability argument and mathematical computation.

## Original nomination and stopping conditions

The following nomination's missing-source statements describe its
invocation-start state; the completed comparison below supersedes those
statements, while preserving its mathematical target and qualifications.

The main gap remains L030–L032/C032a all-degree mixed positivity. The
intermediate target would test whether the now-audited actual-quotient
envelope can join an eventual positive ray to a finite nonnegative
range at this one shift. Even successful overlap leaves growing shifts
and other mixed minors open. No sign or numerical threshold is asserted
in this nomination. The integer m above is a proposed test parameter,
not a locally established PF order.

Essential continuation inputs are L836/L835/L834/L832/L467, with the
inherited L018/L021/L776 conventions. Keep k=6002, J=6003,
T=gamma_J, R=(p_k+p_J)/2, p_j=4 gamma_j^2 for the selected packet,
q=p_k/R and exact s=(1+q)/2. The positive-height representatives and
all tail multiplicities remain essential. No cross-notebook input is
proposed. Full matching Mathlib coverage remains unchecked.

The source review should reuse the existing product/count and sector
coverage, identify primary indexed-zero certification evidence or a
rigorous available algorithm, and compare its actual guarantees with
L836's required 4<l<=u<v<=w<H and exact indices 6002,6003. Approximate
ordinates, two unindexed sign changes, or a precision option without
completeness and error guarantees do not supply that input. Any software
route needs its version and theorem-level guarantee assessed before a
mathematical script is authorized. No API key or new service is needed.

The enlarged-order comparison must keep all ordered Toeplitz minors,
the sector index m+1, the closed verified height H, the actual coefficient
normalization, and passage from finite products to fixed minors. Reuse
the existing theorem statement; do not reprove general sector theory
or import the excluded printed PF44 inference. The applicability of the
proposed order is an unpaid obligation, not a conclusion of L836.

The later mathematical test, if approved, must retain every term in
L836(5)–(8), certify an upper bound for the entire expression strictly
below zero, and save all indexed input records and outward arithmetic.
If the evaluated coarse expression misses, that stops this sufficient
majorant at the specified parameters, not actual positivity or RH.
An inconclusive interval is not a miss or a success. Persistent essential
source blockage requires parking this dependent test and selecting an
independently testable target; no repeated access loop is nominated.

The step659 unpaid hybrid ratio and step667 signed-composition stops
remain intact. This quantitative continuation uses standard methods.
No justified creative central mechanism is ready: the audit supplies
neither a signed residual estimate nor a motivated growing-shift bound.
The source gate is essential coverage, not a literature-quota exercise.

## Completed comparison — 6 November 2026

The main gap is actual-Xi all-degree mixed positivity. The single
intermediate target is a certified finite-PF/eventual-ray join at this
one shift. This could settle a remaining rank interval on that ray;
growing shifts and other mixed minors remain independent. No sign,
rank, enlarged PF order or RH conclusion is established in this review.

### Indexed inputs and outward arithmetic

The primary software contract is FLINT **v3.3.1**,
[acb_dirichlet.rst](https://raw.githubusercontent.com/flintlib/flint/v3.3.1/doc/source/acb_dirichlet.rst),
“Riemann zeta function zeros”, lines588–656. Isolation returns the
**n-th** Hardy-Z zero and no other zero: Gram's-law range is1..126,
Rosser's-rule range1..13999526, Turing's-method range n>=2, and the
default requires n>=1. Refinement encloses that isolated zero; the
consecutive-zero routine requires positive n. N(t) counts all positive
ordinates through t with multiplicity. This is index/completeness
coverage, not merely a root near an initial guess. The frozen
[Arb2.23.0 API](https://arblib.org/acb_dirichlet.html#riemann-zeta-function-zeros)
has the same contracts. No independent reproof of Rosser/Turing theory
or rerun of its underlying verified finite range is claimed.

Relevant native cases were inspected in
[v3.3.1 isolate_hardy_z_zero.c](https://raw.githubusercontent.com/flintlib/flint/v3.3.1/src/acb_dirichlet/isolate_hardy_z_zero.c):
constants/comments lines16–48; the Rosser block-separation loop
889–920; dispatch, index counting and isolation1002–1044 (with dispatch
959–997); and isolation followed by refinement1287–1322. The selected
indices use the documented Rosser branch, rather than the first126
Gram-law case. Blocks extend to good Gram endpoints and subdivide
until sign changes match Gram intervals. The documentation's certified
index contract is imported; code inspection is a consistency check,
not a proof of the whole library. Nontermination/failure is not evidence.

[v3.3.1 zeta_zeros.c](https://raw.githubusercontent.com/flintlib/flint/v3.3.1/src/acb_dirichlet/zeta_zeros.c),
lines13–38, calls the Hardy-Z routine and attaches real part1/2.
That assignment alone proves no global zero exclusion. For this target,
L834's imported sign-change/total-count equality supplies simplicity
and identifies the ordered Hardy-Z roots below H with the ordered
positive-height zeta roots; the future records must also check w<H.
This retains the independent height theorem instead of assuming RH
from the software output.

The inspected binding is python-flint **tag0.8.0** (release commit
4920921), [acb.pyx](https://raw.githubusercontent.com/flintlib/python-flint/0.8.0/src/flint/types/acb.pyx),
`zeta_zero`, lines2327–2346: positive n is converted to an exact fmpz
and passed with working precision to the native routine. Thus the
later computation may request precisely6002 and6003; no zero-finding
call was made in this turn. Pin this binding and native version3.3.1,
or assess a changed implementation before dependent work.

For data export, the same tag's
[arb.pyx](https://raw.githubusercontent.com/flintlib/python-flint/0.8.0/src/flint/types/arb.pyx),
`man_exp` lines211–239 and `lower`/`upper`304–326 provide exact finite
dyadic decomposition and directed endpoints. `log`753–770 and
`pi`2137–2148 call the native ball routines. Save exact endpoints,
not decimal midpoints. The
[Arb2.23.0 ball-semantics contract](https://arblib.org/using.html#ball-semantics)
requires output inclusion for every input point and includes rounding
error in the radius. Precision alone is not an accuracy certificate;
nonfinite balls or unpaid denominator/log domains fail the test.

Availability is a separate execution obligation: neither default
Python3.15.2 nor the inspected Python3.13 environment has python-flint
metadata installed. Python3.13/3.12/3.11 and uv executables are present.
No install or numerical evaluation was attempted. A future isolated
setup must report actual binding/native versions; a setup failure must
be saved, never replaced by approximate mpmath roots. Current FLINT
3.7.0-dev documentation carries a revision warning; it was a discovery
lead, not the authority for this version-pinned approval. The failed
`v0.8.0` wrapper URL was corrected to the actual tag `0.8.0`; the
separate nonexistent hardy_z_zeros.c lead was resolved by the definitions
in isolate_hardy_z_zero.c. Neither is a persistent access blocker.

### Enlarged-order scope and prior failures

Reuse `2026-11-05-verified-height-pf6001-scope.md` and L832's precise
Katkova Theorem B/product-limit comparison, without repeating its
discovery or proving sector theory. Fresh inspection of Michałowski
[2607.16795v1 Section1.2](https://arxiv.org/html/2607.16795v1#S1.SS2)
confirms the sufficient condition m+1<=pi H and the stated finite-order
region through floor(pi H)-1. All ordered minors are covered by the
PF theorem; its displayed consecutive-minor consequence does not
restrict the theorem to that subfamily. The later applicability
argument must verify the proposed integer against this condition,
the actual ordinary normalization, closed verified height, real
conjugate-grouped products and fixed-minor limits. No simplicity or
strictness is part of the PF import. No proposed larger order is
established here and Katkova's excluded printed PF44 inference stays
excluded. This is specialization/reproduction of known results.

The named step659 hybrid-ratio and step667 signed-composition records
were read. The former lacks quantitative determinant/nonvanishing
input; the latter lacks paid signs for growing residual minors. Neither
supplies this test, and neither forbids a test of the audited actual
quotient with new indexed evidence. Existing pole-ray existence and
symbolic-envelope results do not duplicate the unperformed evaluation.
No full matching Mathlib coverage was checked; no absence claim.

### Bounded implementation and decision test

The separately approved mathematical step must keep the continuation
inputs L836/L835/L834/L832/L467, inherited L018/L021/L776, and all
positive-height representatives/tail multiplicities. It must save the
two exact indexed enclosures and algorithm/version provenance, check
4<l<=u<v<=w<H, and record exact R and s as definitions rather than
replace them by approximate midpoints. The interface's rational
outward R_+,q_+,a_+,s_+,V_+,B_+,C_+ must retain all L836(5)–(8)
terms, including -J/T^2 in V and exponent m+k+2. Positive denominators
and logarithm arguments require explicit checks. The proposed order
needs its own cited applicability argument before any overlap claim.

Continue on a certified strictly negative upper bound for the entire
expression in (8); save full arithmetic and input evidence to a local
certificate and print only result, bounds, failures and paths. A
certified positive lower bound for the chosen coarse expression stops
that majorant at these parameters only. A nonnegative upper bound by
itself, or a straddling interval, is inconclusive. Permit precision
refinement only to resolve enclosure width in this one test, not a
parameter search. No numerical sign is forecast by this source review.
On persistent source/setup blockage park the dependent computation;
preserve the original stops. A later result needs its own critical
review and cannot settle growing-shift signs or RH.

Coverage is ready for this exact continuation; there is no justified
new central creative mechanism here. The missing input for such a
nomination is a concrete signed residual or growing-shift mechanism
with an independently payable bounded test, not more source repetition
or relabeling this standard specialization.
