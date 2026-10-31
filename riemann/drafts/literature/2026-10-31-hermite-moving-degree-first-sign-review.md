# Romik Hermite remainder: source comparison

TARGET: Review Romik's Hermite coefficient estimates for moving-degree control of Xi and its first two derivatives on [T,2T], with an error budget for Xi'^2-Xi Xi''.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read Romik v3 §§2.1–2.4, including both convergence-integral regions and all coefficient-saddle/tail cases; checked stronger global Hermite bounds in DLMF 18.14.9 and derivative identity 18.9.25. Exact queries and local overlap checks are below. No matching ready effective moving-height discriminant certificate was found in the inspected sources; no novelty inference follows.
SOURCE_EVIDENCE: Dan Romik, arXiv:1902.06330v3, Theorem 2.1, (2.1)–(2.3), Lemmas 2.3–2.6, proof (2.13)–(2.22), Theorem 2.7, (2.23), Corollary 2.8, (2.24), and proof (2.25)–(2.45); NIST DLMF 18.14.9 and 18.9.25, including their domains/normalizations. Source links and qualifications below.
COMPARISON: Romik gives exact actual-Xi coefficients and rapid compact convergence, with unspecified compact constants; his coefficient asymptotics retain unspecified constants/onsets. DLMF supplies a stronger all-real explicit Hermite envelope. These support a bounded effectivization question, not a source import of the requested moving derivative errors or the signed first inequality.
GAP: A numerical coefficient envelope, a summed derivative tail uniform in T and N, and error propagation to the discriminant remain to be proved. Positive truncation margins, multiplicity-compatible sign transfer and higher signs remain independent gaps. No such estimate is derived in this literature turn.
REASON: Direct use of compact convergence or coefficient asymptotics does not meet the target. The exact coefficient integral plus an inspected global Hermite inequality identifies a finite, concrete specialization test; retain that question rather than repeat a criterion audit.
LITERATURE_REASON: Startup coverage was REVIEW_REQUIRED for actual-coefficient derivative tails; this is the first theorem-level comparison of that lead. The global Hermite inequality was checked as the stronger result needed for the same source question.
SCOPE: Source comparison only. The numerical moving-height specialization is nominated in a separate assessment for later approval; no new lemma, mathematical script, sign result or manuscript audit is claimed.

## Exact input and source scope

The central gap is actual-Xi all-degree positivity. L233 and C233a
identify the first necessary signed quantity
D(f)=f'^2-f f''. The present intermediate question concerns actual
coefficients and complete remainder control; it leaves D(P_N)'s sign
and every higher sign unresolved.

Primary source: Dan Romik, *Orthogonal polynomial expansions for the
Riemann xi function*, [arXiv:1902.06330v3](https://arxiv.org/html/1902.06330v3),
§§2.1–2.4, theorem/equation numbers below. The
[journal record](https://doi.org/10.4064/aa200515-10-3) confirms Acta
Arithmetica 200 (2021), 259–329, under the expanded title ending
*in the Hermite, Meixner–Pollaczek, and continuous Hahn bases*.
The journal manuscript was not compared; theorem citations here are
to v3. An author-final PDF search hit returned 404, which does not
block use of the accessible v3. The manuscript is not independently audited.

Romik (1.1), (1.3), (1.8), (1.11), (2.1), (A.9) fix:

    Xi(t)=xi(1/2+it),
    Phi_R(u)=2 sum_(m>=1) [2pi^2 m^4 exp(9u/2)
                              -3pi m^2 exp(5u/2)] exp(-pi m^2 exp(2u)),
    b_m=(2^m m!)^(-1) integral_R u^m exp(-u^2/4) Phi_R(u) du,
    H_m(t)=(-1)^m exp(t^2) (d/dt)^m exp(-t^2).

On u>=0, Phi_R=K/2 for L019's K; L020's cosine representation
therefore agrees with Romik's full-line Fourier representation.
No height rescaling or Gaussian factor multiplies Xi. In particular
these H_m are polynomials, not normalized Hermite functions.
The coefficients b_(2n)>0 and odd b_m=0 belong to actual Xi,
not an arbitrary moment sequence. Write
P_N(t)=sum_(n=0)^N (-1)^n b_(2n) H_(2n)(t).
These are cited source definitions, not a new expansion.

## What the estimates do and do not supply

Theorem 2.1 gives |Xi-P_N|<=C_1(K) exp(-C_2(K) N log N),
N>=1, uniformly on each fixed compact K in C. Neither constant is
numerical in the statement. Holomorphic compact convergence permits
local derivative convergence, but does not specify useful moving-height
constants. It gives no signed lower bound for D(Xi).

The proof is more informative than that statement. Lemma 2.4 uses
M=2 max_K |t| and N_0=max(128,ceil((2M)^(4/3))); its initial
constant is a finite Hermite maximum. Lemma 2.6, B>=1, controls
integral_0^infinity u^m exp(-B exp(u)) du. The proof locates the
maximum at W(m/B), bounds the part through 2 log m by length times
maximum, and controls the remainder by a concave tangent, (2.18)–(2.19).
Its displayed asymptotic bound still contains an unspecified constant.
Equation (2.22) bounds the Hermite remainder by the entire absolute
coefficient-moment tail before inserting those asymptotics. The last
Stirling step gives O(exp(-N log N/5)) for fixed K, not an effective
uniform assertion with K changing. This is the part worth specializing.

Theorem 2.7, (2.23), gives a Lambert-W coefficient asymptotic with
relative error O(log log n/log n); Corollary 2.8 gives the weaker
logarithmic asymptotic. Neither states a numerical error constant or
onset. Its proof separates the first theta summand Q_n from r_n,
uses a central window of radius n^(-2/5), and treats the left,
central and right regions in (2.38), (2.40), (2.41). The remaining
theta summands are bounded in (2.45), only for sufficiently large n.
Those cases were read; a leading saddle term is not a certified upper
bound for every coefficient. No differentiation of this asymptotic is
justified or needed for the nominated tail question.

A stronger standard bound is explicitly available in
[NIST DLMF 18.14.9](https://dlmf.nist.gov/18.14.E9):

    exp(-t^2/2) |H_m(t)| / sqrt(2^m m!) <= 1,
    m=0,1,..., t real.

The section notes cite Szász (1951). This directly matches Romik's
physicists' H_m; no complex-argument extension is asserted. Also
[DLMF 18.9.25](https://dlmf.nist.gov/18.9.E25) gives
H_m'=2m H_(m-1) for integer m>=1 (H_0'=0).
These are imported standard estimates/identities. Their combination
with an effective actual coefficient bound and an infinite tail sum
has not been performed here. The useful change in route is to avoid
unknown compact-dependent Hermite constants on the real interval.
The elementary numerical coefficient envelope and tail summation,
rather than a reproof of Romik's expansion or sharp saddle formula,
are the remaining specialization work.

## Comparison, searches and recorded failures

Scoped local reads: L018–L020 normalization; L233 and C233a's complete
first-sign requirement; L563's conclusion; the Romik reading-limits
paragraph in `2026-10-30-direct-theta-mixed-positivity-discovery.md`;
mechanism 3 in `2026-10-31-complete-first-sign-mechanism-discovery.md`;
`ATTEMPTS/2026-10-03-complete-parity-positive-definiteness-test.md`
and `ATTEMPTS/2026-10-30-moment-only-pollaczek-preservation.md`.
The two literature filenames in this paragraph are in this directory.
The parity obstruction requires retaining the complete kernel, and
L530 stops moment-only preservation. Neither stops a complete
actual-coefficient remainder estimate. L563 rules out the printed
interface tested there, not this expansion. The finite Giraud–Peschanski
construction was already assessed; it does not provide the missing
actual-kernel remainder. Existing Pollaczek compact convergence and
the Hermite/heat-flow identification are not new leads.

Queries included `Romik Hermite expansion Xi derivative remainder
Theorem 2.1 2.7 moving uniform`, `"xi" "Hermite" "truncation"
"error" Romik`, `"Riemann xi" "Hermite" "remainder"`,
`"Romik" "Hermite" "derivatives"`, `"Riemann xi" "Hermite"
"uniform" "error"`, and `Hermite polynomial Cramer inequality
1.086435 n all real NIST`. Followed the primary Romik and DLMF results.
Search-only Jensen-polynomial and theta Taylor-coefficient hits are not
imports of Hermite b_(2n) derivative tails. Indritz's 1961 AMS paper
was inaccessible (403); no claim is based on its unread proof. DLMF's
explicit bound suffices as the named standard input. Krasikov,
*New bounds on the Hermite polynomials*, arXiv:math/0401310v1,
Theorem 1 p. 1, was inspected as a stronger degree-sensitive lead;
its k>=6 bound has parity-dependent constants. No specialization or
proof audit of it was done; the nominated test needs only DLMF's
simpler bound. No failed search certifies originality or impossibility.

## Decision and bounded test

Direct theorem import does not supply the requested effective derivative
certificate. There is nevertheless an identified bounded gap: make the
coefficient-moment envelope explicit, use the global real Hermite bound
and derivative identity, and sum the complete tail. Nominate the
specific uniform target exp(-2pi T) for derivatives 0,1,2 on [T,2T]
with N=ceil(C(T+1)^2), numerical absolute C, T>=1.
This is an unproved test threshold, not a bound claimed from Romik.
Its purpose is to make absolute errors smaller than the exponential
scale relevant to the discriminant, without asserting a relative
error near zeros. A successful tail estimate would permit a later
signed-margin test. It would not by itself justify any sign.

Continue this specialization only if all constants, initial indices
and derivative interchanges can be justified with the stated polynomial
degree budget. Otherwise save the failed bound and park that budget;
do not repeat compact convergence as evidence. A sign certificate
would additionally require, throughout each intended interval,
|D(Xi)-D(P_N)| below a certified positive D(P_N) margin, or a separate
zero-compatible non-strict argument. Multiple zeros may prevent a
strict margin. Neither that margin nor all-height coverage is supplied.
No creative central-gap proof target is ready until a signed-error test
has actual quantitative inputs; this effective specialization is
reproduction, not a creative or novel sign mechanism.

Mathlib: not checked for the expansion, effective remainder, global
Hermite bound or derivative identity. Availability is unknown. No
formal verification or cross-notebook input is claimed.
