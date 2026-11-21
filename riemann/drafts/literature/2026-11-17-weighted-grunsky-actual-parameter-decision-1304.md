# Actual-parameter input for the weighted finite Grunsky test — review1305

TARGET: Assess whether known results or existing rigorous actual-Xi estimates decide C030z's finite test pL(x)=N(x), x<1, p>0, V>0, J>0, H>0, retaining L(x)=0 and all positive-weight branches.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1305 searched secondary/spectral zeta, inverse-zero-power inequalities, actual-Xi/Grunsky and explicit zero-count bounds; reused1303's prescribed-Grunsky comparison and checked the named local stops. Read C030z,L025,L027 and L917's complete enclosure/audit, then its narrowly relevant producer entry points. Queries, inspected sources and limits are below; no novelty inference.
SOURCE_EVIDENCE: Arias de Reyna arXiv2006.04869v1 pp1-2 and Section4 pp9-10; Johansson arXiv1309.2877v1 Section2 Theorem1/(12)-(14), proof pp3-4 and Section3.1 p5; Johansson1611.02831v1 SectionsV/VI; official Arb2.9.0-git acb_poly contracts and Python Decimal exp/adjacent-neighbor/rounding contracts. Reuse1303 for Teo. Exact URLs and applicability below.
COMPARISON: No inspected theorem or certified table decides C030z. The secondary-zeta implementation uses heuristic errors; L917's audited boxes include lambda=0 but its saved S_6 interval crosses zero. Its generic L036/L037 method and degree-twelve tails support a fixed-lambda refinement and finite witness test, not an imported compatibility decision.
GAP: Actual numerical enclosures and a verified witness or an exhaustive obstruction remain missing. A four-point witness search is now source-covered; failure there leaves all other x and L=N=0 branches open. Higher compatibility and analytic realization remain independent.
REASON: Essential coverage now supports one bounded ordinary calculation using existing audited standard-library machinery. This is local source progress, not a mathematical feasibility result or progress beyond the checked sources. The newly ready continuation requires separate next-turn approval.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED concerned actual-parameter information expressly outside1303's finite-sign-only scope; this turn supplies that comparison and reuses adequate formal/enclosure coverage.
SCOPE: Only actual S_2,...,S_6 and C030z's degree-six prescription. No higher degree, extra parameters, univalence application, all-branch decision algorithm or infinite realization construction is approved. The concrete continuation is in assessment1305.

## Completed comparison1305

The main gap remains L030-L032/C032a actual-Xi Q(q)>=0 in every
degree. The intermediate target is rigorous actual parameters for
C030z. A finite compatible jet would allow consideration of further
realization work; it would give no univalence or all-degree sign.
An exhaustive contradiction would stop only this prescription. No
actual compatibility or incompatibility is established in this turn.

### Inspected primary sources and their limits

J. Arias de Reyna, *Computation of the secondary zeta function*,
[arXiv2006.04869v1](https://arxiv.org/pdf/2006.04869v1), served PDF
internal date22November2021, pp1-2 defines Z(s) for Re(s)>1 using
rho_n=1/2+i alpha_n, positive ordinate and multiplicities, without
assuming RH. These are the positive-real-part Xi representatives of
L025; at s=2k the quantity sought is S_k. Section4 pp9-10 describes
the mpmath implementation: the prime-term bound(46) is not used,
the first omitted term replaces it, the exponential term receives no
error estimate, and the singular expansion/error comparison is
heuristic. Therefore its default outputs or matching digits are not
certified intervals. This rejects that shortcut, not the analytical
definition or the possibility of a separate certified implementation.
The full modular/continuation proof is not imported or audited.

F. Johansson, *Rigorous high-precision computation of the Hurwitz
zeta function and its derivatives*,
[arXiv1309.2877v1](https://arxiv.org/pdf/1309.2877v1), Section2,
Theorem1/(12)-(14), printed pp3-4 and its complete proof; Section3.1
p5: coefficientwise Euler-Maclaurin remainder control requires positive
integers N,M, Re(a)+N>1 and Re(s)+2M>1. The proof bounds the periodic
Bernoulli factor, complex logarithm and argument factor and then the
integrable coefficient tails. Section3.1 adds these bounds to each
coefficient radius and returns infinite bounds if hypotheses fail.
At a=1,s=1/2, every positive N,M meets these conditions. Section2
also permits formal composition. This supplies a known certified
Taylor method for the L018 completed product at this center; no
zero-location premise is required. It does not supply a C030z witness,
any cross-moment inequality, or a guaranteed finite precision margin.

Johansson, *Arb: Efficient Arbitrary-Precision Midpoint-Radius Interval
Arithmetic*, [arXiv1611.02831v1](https://arxiv.org/html/1611.02831v1),
SectionsV,VI and VI-C, explains inclusion-preserving arithmetic,
rigorous truncation bounds and automatic Taylor coefficients, including
zeta and gamma derivatives at1/2. The author's
[Arb2.9.0-git acb_poly documentation](https://fredrikj.net/arb/acb_poly.html)
specifies acb_poly_zeta_series, gamma_series, log_series and exp_series;
zeta uses a=1 and deflate=0 here, and log requires an invertible constant
term. L018 identifies the completion, and L025 supplies the normalized
local-log coefficient identity. This alternative is mathematically
covered, but python-flint is absent in the current interpreter and
the probed standard C include locations/pkg-config did not locate
FLINT/Arb. No installation or library execution was attempted.
This is a local availability observation, not a universal access block.
The revised FLINT3.7.0-dev pages warn of partly generated text; matching
older author documentation and the primary papers were read instead
of treating those pages alone as a theorem proof.

The [Python Decimal reference](https://docs.python.org/3/library/decimal.html)
was checked at exp, next_minus/next_plus, directed rounding, signals
and Context.power. It supports L037's existing contract; power's
almost-always-correct qualification must not replace repeated interval
integer multiplication. L917's audited conditional library assumptions
are retained, not independently verified here.

### Existing rigorous input and a bounded usable difference

L917's full proof and step197 audit were read, including the complete
twelfth-moment tails, closed spatial panels and log polynomials. It
explicitly covers lambda=0. L021/L025 identify the undeformed moments
and their normalized logarithm with actual Xi and actual S_k; no
deformed-zero product or RH hypothesis is needed for that interface.
L036 covers any C8 spatial panel and L037 specifies enclosing
arithmetic. Thus singleton lambda=0 and 256 dyadic spatial panels
use the same inclusion theorem; they are a proposed new computation,
not an already verified numerical certificate. Retain u<=2,n<=4,
100-digit contexts and L917's full positive discarded-mass bound.

The existing certificate was inspected only at its structure and
the complete selected value /panels/0/S/6, using the shared inspector.
That interval has negative lower endpoint -8.8272852928...e-14 and
positive upper endpoint 1.2002978529...e-13; full endpoints remain
canonical in scripts/heat/low-time-h2-uniform-195.json. This confirms
the already recorded sign loss, not a newly discovered numerical
obstruction. L027's E>0 cannot turn that saved box into a strictly
positive lower bound for reciprocal evaluation. No assertion is made
that all consequences of the saved moments fail to decide C030z.

L917's historical stop is the fixed-budget *uniform H2 determinant*
certificate. The proposed output is instead a finite compatibility
witness at the single undeformed parameter, after removing the old
parameter interval width. This does not reopen the uniform determinant
claim or overwrite its evidence. Its general method remains usable.
The inspected prepare/certify_panel entries accept the enclosing
parameter object and use SPATIAL_PANELS for a dyadic partition. No
producer/checker was run, and no lemma or mathematical script changed.

### Search and failure comparison

Queries included `Riemann zeta secondary zeta Z(s) sum zeros inverse
powers Voros values half derivatives`, `Riemann xi Grunsky coefficients
Hankel positive diagonal weights`, `Riemann zeros explicit bound N(T)
Trudgian 2014`, `"secondary zeta" "log-convex"`, `"Grunsky" "Riemann xi"`
and `"Riemann zeros" "inverse powers" inequalities`. These did not
locate a primary statement deciding the positive-weight prescription.
Voros2003 was read only at introductory/admissible-sequence passages;
no formula or numerical table is imported from it. Explicit zero-count
and a newer RH-assuming secondary-zeta preprint were leads only, not
assessed theorem inputs. No new zero-free region or reciprocal-series
continuation is proposed; the local October baseline is not reopened.

Reuse1303's Teo/formal-compatibility comparison; do not browse Grunsky
again for an unchanged identity. C030y stops fixed weights only, while
C030z's two sign-only parameter examples are not actual-Xi models.
Review1303 already compared variable-coefficient/congruence/realization
stops. Stop1248 concerns a global finite-reference measure budget;
stop1302 concerns finite positive-width smoothed laws. Neither decides
the finite actual jet. Preserve stops1297/1302/1200 and all unfinished
work. No cross-notebook input or certified originality claim.

### Decision, test and remaining scope

Assessment1305 records one source-covered singleton quadrature and
four-point witness attempt. Require rigorous positive actual-sum
enclosures before using denominators, and exact p=N/L only when L is
proved nonzero. Strict lower bounds for p,V,J,H must exceed zero.
Zero-containing L is undecided, not equality; exact L=N=0 retains free
p under C030z. A witness gives finite compatibility only. Failure of
all four trials leaves other x and exceptional branches unresolved;
it cannot stop the entire weighted prescription. Stop this fixed
calculation at its saved budget rather than silently refine or switch
to an unassessed all-branch algorithm.

Classification of this source turn is NOVELTY_UNCHECKED. A later
known-method numerical specialization is ordinary calculation, with
no reproof of the cited general tools. Mathlib full matching coverage
and formalization of this finite computation are not checked. No
creative central signing mechanism has been identified: the blocker
is still actual realization and all-degree positivity, and a finite
classical-identity test must not be relabeled creative to fill a quota.

## Original nomination1304 body retained

The original REVIEW_REQUIRED nomination below is historical; the
completed comparison above supersedes its source gate, not its target.

## Input and intended comparison

Use C030z for the precise definitions of A,...,E,k,L,N,V,J,H and
its proof. Canonical mathematical inputs are C030y,L025,L027; L030
explains the intended downstream index shift without supplying a sign.
Reuse assessment1303's source coverage of the formal identities. No
additional general Grunsky browsing is justified without a new lead.

First search narrowly for existing rigorous actual reciprocal-sum
inequalities or enclosures relevant to this exact finite test, and for
known prescribed-Grunsky obstructions that genuinely apply to independent
positive weights. Retrieve primary hypotheses before importing a result.
Do not silently assume RH, log-convexity of every S_k, or positivity of
the actual Hankel matrices. A theorem requiring those properties does
not supply them. The finite sign-only examples in C030z do not decide
what follows from the full inherited zero geometry or theta integrals.

The useful output is an applicability-justified imported decision or
a ready, bounded mathematical target with named rigorous inputs and
thresholds. If numerical bounds are needed, assess their rigorous
derivation before proposing code; arbitrary floating approximations or
sampling x cannot settle the all-branch problem. All L=N=0 cases and
the strict weight inequalities must be accounted for. Finite success
would still leave higher compatibility, analytic extension, disk
univalence, realization and all-degree actual-Xi signs unresolved.

No creative sign mechanism has been established. Do not rebrand this
finite classical-identity specialization as creative. A genuinely new
central construction would require its own independently testable idea
and essential source coverage; none was found within calculation1304.
No cross-notebook input or Mathlib match is claimed.
