# Actual moving-band degree germ: completed source comparison

TARGET: Assess source coverage for an exact locally convergent degree-generating representation of the actual moving-band corrections, retaining all endpoint and compensator terms.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step280 completed bounded exact/stronger-result and moving-cutoff searches below; reused reviews245/249/254/278 and stops244/279. No inspected theorem gives the exact G_r representation or its singularities; no novelty inference.
SOURCE_EVIDENCE: Newly inspected Montgomery-Vaughan MNT I section5.1 Theorems5.1-5.2/Corollary5.3 pp137-140, including near/far/endpoint proof cases, and Lagarias AIF57(2007) AppendixA pp1737-1738. Reused DLMF18.12.13/18.14.8 and the canonical Gorodetsky2211.08973v6 input. Precise links and scope below.
COMPARISON: Truncated Perron inversion and Laguerre extraction cover ingredients for an actual compensated contour representation. They do not state degree-uniform limiting estimates, the four-endpoint resummation or persistence of a zero singularity. Full-Li regularization does not import those conclusions.
GAP: Construct a nonzero analytic disk and an explicitly degree-resummed finite-height contour expression; justify its locally uniform height limit with full jumps and compensators. All-zero singularity detection, signs and main-goal transfers remain separate and unapproved.
REASON: Essential coverage is adequate for one bounded known-tool construction attempt in review280; general Perron/Laguerre reproof is unnecessary. No construction or new lemma is derived in this literature-only step. The newly saved continuation receives separate approval next turn.
LITERATURE_REASON: Moving degree-dependent endpoints and an actual arithmetic generating germ are outside the fixed-argument DLMF and full-Li scopes reused in step279.
SCOPE: Actual Lambda with all prime powers, n>=2, r=1,2, exact L985 kernels and full-right/left-excluded endpoints. No RH, simple zeros, maximal-real-part zero, ordinate nonresonance, good-height clearance or infinite-sum interchange assumption.

## Exact proposed object and bounded review

The step279 nomination below is preserved. Its coverage questions are
answered by the appended step280 comparison; its object and warnings
remain unchanged.

For a real polynomial f use exactly

    T(f;u,v)=sum_(exp(u)<m<=exp(v)) Lambda(m)*f(log m)/m
                                                 -integral_u^v f(t)dt,
    K_m(t)=[L_(m-1)^(2)(t)-1]/(m-1).

Define coefficients, without asserting any estimate or decomposition,

    D_(n,r)=T(K_(n+r);n+r,2*(n+r))-T(K_(n+r);n,2*n),
    G_r(z)=sum_(n>=2) D_(n,r)*z^n,             r=1,2.

The series are formal until a convergence domain is justified.
This definition is a proposed research object, not a derived identity.
The exact J_n, X_n and tilde_X_n are those in review278/L993; no
n-dependent matrix is pulled through a generating function.

Review known moving-cutoff weighted generating transforms and their
endpoint hypotheses. Reuse ready source contracts instead of
reproving Laguerre generating functions or finite explicit formulas.
Compare any proposed interchange with all prime powers, compensation,
arithmetic jumps and finite/infinite spectral cutoffs. Do not infer
uniformity in degree from a fixed-degree formula, or identify G_r
with the ordinary Li germ. Any cross-notebook input needs a separately
recorded reason before its narrow read; none is proposed here.

The plausible downstream use is a later analytic singularity test of
whether an off-line zero can remain visible in the complete actual
correction. That test must address other zeros and endpoint cancellation;
it may not assume a rightmost zero or nonresonance. No such theorem or
RH consequence is asserted. The independent common-interval outputs,
both complements and L984(H) remain unpaid even if this interface works.

Continue only if inspected sources cover a concrete representation
with a justified initial analytic domain and an independently testable
way to track endpoint/spectral terms. An identity merely restating D,
a fixed-argument formal exchange, or repeating the completed quartet
does not pass. If no such interface is justified, stop this mechanism
with its precise obstruction and select an independent target rather
than repeat the direct transport review. Full matching Mathlib coverage
is unchecked. No source passage or new mathematics is derived here.

The central creative prospect is to retain actual signed cancellation
in a degree-generating transform, rather than to sharpen an absolute
prefix bound. Its source/exchange interface is not ready. Recommend
literature_comparison standard/high for this exact nomination; only
after coverage should a concrete creative proof attempt be considered.

## Completed comparison — step280, 10 November 2026

Only source review was performed. L030-L032/C032a actual-Xi positivity
and L966/L968 signed forcing remain the main gap. The intermediate
target is exactly G_r above. Its plausible downstream use is a later
signed singularity/cancellation test, not a prime estimate obtained
from the existence of a small analytic disk.

### Bounded searches, duplicates and stops

Queries included `Laguerre polynomials generating function truncated
sums moving endpoint von Mangoldt`, `Li coefficients generating
function arithmetic expression truncated sums Laguerre polynomials`,
`"Laguerre" "von Mangoldt" "generating"`, `"moving cutoff"
"generating function" primes`, `"Laguerre" "Perron" "generating"
zeta`, `"Li coefficients" "Laguerre" arithmetic generating function`
and `"Perron" "uniform" "complex" truncated formula zeta`.
They located standard tools and full-Li formulas, not an inspected
matching moving-band theorem. Search snippets, self-published RH
claims, the Poisson-Li blog lead and unrelated Laguerre asymptotics
are not imported theorem evidence; their full proofs were not assessed.

Narrow local checks reused review245's fixed-argument warning,
review249's endpoint/growing-degree cautions and review278's interval
payment stop. L985 and L989 were read for exact definitions and scope.
Stop244 remains a failure of the specified centered-Vaughan absolute
estimate chain. The contour construction does not repeat that bound,
discard prime powers, pull L993 through a degree series or repeat the
finite quartet. L993 is context only; no cross-notebook input.

### Primary contracts inspected

H.L. Montgomery and R.C. Vaughan, *Multiplicative Number Theory I:
Classical Theory*, Cambridge, 2007, section5.1, Theorems5.1-5.2 and
Corollary5.3, printed pp137-140,
[author-hosted chapter](http://personal.science.psu.edu/rcv4/personal/Publications/MNTI/09.0_pp_137_167_Dirichlet_series_II.pdf#page=2).
For alpha(s)=sum a_m*m^(-s), c>max(0,sigma_a), x>0 and T>=1,
the truncated integral of alpha(s)*x^s/s gives the half-weighted
prefix with remainder bounded by

    sum_(x/2<m<2*x,m!=x) |a_m|*min(1,x/(T*|x-m|))
      +(4^c+x^c)/T *sum_(m>=1)|a_m|/m^c.

The proof covers both far ranges, both near ranges and the s=0
indentation. Theorem5.1 uses symmetric height limits and
c>max(0,sigma_c), not absolute infinite-height inversion. Constants
and uniformity for a new coefficient family need verification.
Import the source proofs without reproof.

Source-integrity qualification: initially returned cached text had a
near sum with m<=x. A fresh author-URL request returned the paginated
PDF: p139 has strict x/2<m<x, and p140 excludes m=x in Corollary5.3.
The cached transcription is not used. Shell download failed DNS;
browser retrieval of the primary chapter succeeded. No essential
source blocker remains.

[DLMF18.12.13](https://dlmf.nist.gov/18.12.E13) states

    sum_(d>=0) L_d^(alpha)(t)*w^d
                  =(1-w)^(-alpha-1)*exp(t*w/(w-1)), |w|<1.

At alpha=2 and real t>=0, Cauchy's coefficient formula is available
on a fixed circle strictly inside this disk. It extracts a polynomial
at a fixed argument; it does not sum moving intervals. The global
bound [DLMF18.14.8](https://dlmf.nist.gov/18.14.E8), d>=0, alpha>=0,
t>=0, and L989's existing normalization are available for domination.
Live statements were inspected. No shifted-kernel or convergence
bound is proved here; no general reproof is needed.

J.C. Lagarias, *Li coefficients for automorphic L-functions*, Ann.
Inst. Fourier57(2007),1689-1740, AppendixA, printed pp1737-1738,
[primary paper](https://www.numdam.org/article/AIF_2007__57_5_1689_0.pdf#page=49),
identifies its Li test polynomial with L_(n-1)^(1)(-x). Its covariance
formula needs cutoff regularization: divergent0/1 terms cancel
against arithmetic terms. The unregularized trace is undefined for
these tests. This warns against dropping compensators but is neither
our alpha=2 moving-band observable nor a degree-uniform theorem for
it. No positivity is imported. Reuse review245's Voros scope unchanged.

Reuse [the canonical finite weighted input](../../foundations/2026-11-10-finite-weighted-landau-input.md)
and L989 without reopening their audit. They retain signed prefixes
and technical endpoint costs; they do not supply resummation or an
infinite-zero exchange.

### Applicability and decision

The actual Mangoldt Dirichlet series is -zeta'/zeta in its absolute
convergence half-plane (also displayed in MNT I section12.1, p397).
Thus complex-coefficient Perron inversion is a concrete interface to
test after Laguerre extraction. First verify a common absolute-
convergence line over the coefficient contour. Do not extend the
notebook's s=1-only Gorodetsky use to complex parameters silently.
Use truncated Perron before any spectral deformation.

This comparison derives no construction. The missing specialization
is explicit degree resummation, normalization by n+r-1, all four
affine endpoints, the constant -1, continuum integrals and uniform
limiting estimates. Start with finite degree and height, restore both
half-jump corrections for full-right/excluded-left endpoints, retain
all powers and assume no clearance. Any later spectral deformation
must keep all crossed residues and the remaining contour.

Continue to the one construction in
[review280](2026-11-10-resummed-perron-cauchy-construction-review-280.md).
Require a nonzero locally uniform domain, an explicitly summed
degree kernel coupled to actual -zeta'/zeta, and complete accounting.
A formal infinite Perron exchange, unevaluated coefficient restatement
or another quartet fails. Record any uncontrolled limit or term
without claiming a general impossibility. All-zero cancellation and
continuation to a zero-sensitive singularity remain unreviewed.
Matching Mathlib coverage is unchecked and unknown.

Outcome EXPLORATION: bounded source comparison prepares a known-tool
attempt; no representation, bound, new mathematical discovery, RH
implication or candidate. No mathematical exploration usage is added.
Creative priority was considered: this interface construction is
development. An explicit signed representation and a justified
remainder-analyticity test still block a central singularity attempt;
routine specialization is not relabeled creative.
