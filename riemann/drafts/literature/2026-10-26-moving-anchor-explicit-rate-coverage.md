# Moving anchors with a prescribed witness-rate bound — source assessment

TARGET: Assess whether L461 admits a uniform moving-anchor witness cutoff n<=ceil((3/16+C/sqrt(log log T))log T) for T=2+|a| sufficiently large, with one constant C.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read L461's full construction, L266's full general witness proof, L462's hypotheses/conclusions and endpoint qualifications; reused the October 24 construction/audit assessments. Searched notebook-local moving-anchor/shrinking-margin/prescribed-rate terms and external exact witness, Laguerre, moving-anchor and Littlewood uniform-logarithm terms. No inspected matching cutoff theorem was found; queries, source passages and limits are below.
SOURCE_EVIDENCE: Ramachandra, Lectures on the Mean-Value and Omega-Theorems for the Riemann Zeta-Function (1995), Theorems 1.5.1, 1.5.2 and 1.6.1, printed pp. 26–29, explicit statements and the latter two proofs; Dupuy, Hadamard's Theorem and Entire Functions of Finite Order, Theorem 2.2, p. 3, both proof cases; Grava, Complex Function Theory (December 29, 2024), Lemma 4.16, printed p. 42, statement/proof; DLMF 5.11.9 and its bounded-real-part uniformity. Reused inspected Titchmarsh 14.2 and the retained external premise without a new manuscript audit.
COMPARISON: L461's fixed-c conclusion does not imply the prescribed rate and L462 explicitly excludes moving parameters. The newly inspected general inequalities expose their radius dependence and the gamma input covers bounded moving real parts. These cover the tools for one uniform-dependence specialization, not its outcome; neither fixed big-O substitution nor a stronger zero-free premise is authorized.
GAP: Derive and check a single-height-family logarithm bound, a complete circle-to-anchor estimate with controlled prefactors, and L266's integer cutoff with one C and one onset. In particular L461's all-height compact normalizations cannot be left uncontrolled as margins shrink. No uniform moving-anchor estimate or cutoff is proved in this literature turn.
REASON: Essential theorem-level coverage is available with explicit dependence rather than unspecified fixed-parameter constants. Approve one bounded REPRODUCTION attempt using those inequalities and the existing witness interface, with the full uniform transfer and final threshold still to be tested mathematically.
SCOPE: Actual Xi and hypothetical nonreal zeros a+ib under precisely L461's retained external premise, with all multiplicities. One C and one height onset must work for all such centers. No additional zero-free result, initial sign, effective numerical onset or RH conclusion is requested.
LITERATURE_REASON: The target changes fixed anchor, radius and loss parameters to height-dependent ones and requests a prescribed rate; previous coverage explicitly excludes moving anchors. This turn supplies that missing comparison rather than repeating the fixed-margin audit.

## Purpose and bounded source test

The main gap remains initial actual-Xi signs at unbounded heights and
global mixed positivity. The proposed intermediate target would give
a quantified shrinking witness range, usable in a later comparison
with a near-endpoint sign estimate. Those signs and effective overlap
are independent unresolved gaps; merely knowing a witness exists is
not a sign theorem.

Compare, rather than automatically extend, L461 and L462. A possible
parameter family to assess is eta(T)=3/8+1/sqrt(log log T) and
R(T)=3/8+2/sqrt(log log T), restricted to heights with R(T)<1/2.
This family is now within the approved specialization scope, not an
established estimate. All errors and prefactors must be tracked;
substituting these parameters into a fixed-constant big-O statement
is invalid.

Continue to one mathematical attempt because the explicit classical
inequalities below leave the necessary dependencies assessable.
Success requires one C and one sufficiently large height onset for
every hypothetical nonreal zero center, independently of displacement
and central multiplicity. If the logarithm, strip transfer or prefactors
cannot reach the stated rate, preserve that failed threshold and park
this implementation. Do not repeat L462's stopped fixed-anchor
remainder comparison. No success or failure of that test is established
here.

Relevant preserved evidence is
[the fixed-anchor stop](../../ATTEMPTS/2026-10-25-interior-anchor-small-tail-comparison.md)
and [its fixed-parameter assessment](2026-10-25-interior-anchor-signed-tail-barrier.md).
The September first-sign and generic associated-kernel stops supply
no new actual-theta sign mechanism. No creative proof target is yet
justified by the present finite-factor audit; the approved work is a
changed-quantifier specialization, not a creative central-sign mechanism.

## Primary inputs and their actual scope

K. Ramachandra, *Lectures on the Mean-Value and Omega-Theorems for the
Riemann Zeta-Function*, TIFR/Springer (1995),
[Theorems 1.5.1–1.6.1, printed pp. 26–29](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr85.pdf#page=36)
(PDF pp. 36–39), was read at the statements and the two interpolation
proofs. Theorem 1.5.1 is the bounded-domain maximum-modulus principle;
its proof is referred elsewhere. Theorem 1.5.2 assumes analyticity on
the closed annulus and gives, for 0<r1<r2<r3,

    M(r2)^log(r3/r1) <= M(r1)^log(r3/r2) M(r3)^log(r2/r1).

Its proof uses rational powers and maximum modulus, then a limit.
Theorem 1.6.1 assumes analyticity on the closed R disk and Re f<=U
on its boundary; equation (1.6.1) gives, for r<R,

    |f(z)-f(z0)| <= 2r(U-Re f(z0))/(R-r), |z-z0|<=r.

The coefficient/geometric-series proof exposes the radius gap; no
fixed lower bound on that gap is a theorem hypothesis. The zero or
constant function needs no logarithm of a zero maximum. The displayed
inequalities are general tools, not a zeta-rate theorem.

Taylor Dupuy, *Hadamard's Theorem and Entire Functions of Finite Order
— For Math 331*, [Theorem 2.2, p. 3](https://tdupu.github.io/complexspring2017/hadamard.pdf#page=3),
was also inspected through both f(0)=0 and f(0)!=0 cases. Its version
requires holomorphy on a neighborhood of the closed disk and displays
both factors 2r/(R-r) and (R+r)/(R-r) in the bound for max |f|.
Use the explicit inequality, retaining the normalized center value;
the notes' informal positivity/conformal-map wording in the proof is
not needed as an additional hypothesis or input.

Tamara Grava, *Complex Function Theory*, December 29, 2024,
[Lemma 4.16, printed p. 42, PDF p. 46](https://people.sissa.it/~grava/cft.pdf#page=46),
assumes an analytic function on a domain containing the closed R disk
and a bound M on its circle. It gives |f^(n)(z0)|<=n! M/R^n for
every nonnegative integer n. The full proof is Cauchy's derivative
formula and the circle-length estimate. It has no unspecified
parameter constant. This supports L266's existing tail argument;
no new tail lemma is needed.

[NIST DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9), including the sentence
immediately following it, gives

    |Gamma(x+iy)| ~ sqrt(2pi)|y|^(x-1/2) exp(-pi|y|/2)

as y tends to either infinity, uniformly for bounded real x.
This directly covers real parts varying within one fixed bounded
interval at large shifted heights. Reuse the previously inspected
5.11.1/5.11.3 sector/remainder coverage if complex Stirling is used.
It supplies no bounded-height nonvanishing minimum uniform in a
shrinking zeta margin.

The [October 24 construction assessment](2026-10-24-fixed-half-plane-witness-cutoff-coverage.md)
and [audit coverage](2026-10-24-l461-witness-cutoff-critical-audit-coverage.md)
are reused for Titchmarsh, second edition revised by Heath-Brown
(1986), Theorem 14.2 and proof, printed pp. 336–337, especially
(14.2.5)–(14.2.6). That theorem assumes RH and fixed interior strips;
its conclusion is not imported under a changed 7/8 hypothesis.
The changed-domain proof in L461 must be developed with explicit
inequalities. The PDF reopened, but label searches failed and the
screenshot supplied no additional readable evidence; no new inspection
of that passage is claimed.

The same assessments retain the pinned September 30 Theorem 1.1 at
commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, strict Re(s)>7/8,
pole at one allowed, boundary unexcluded. Its manuscript and formal
import closure remain locally unaudited. The registered stronger Liu
lead changes the premise and is not used to bypass this exact target.

## Obligations for the single approved attempt

These are prospective checks, not derivations in this source review.

- Keep delta(T)=1/sqrt(log log T), eta=3/8+delta and R=3/8+2delta
  fixed while making each estimate at that T. Restrict to a single
  sufficiently large onset with 0<eta<R<1/2. Track the normalized
  logarithm on neighborhoods inside the strict zero-free half-plane,
  its Euler-series inner disk, explicit Borel factors and the exact
  three-circles exponent. Exponentiate both signs only after obtaining
  a uniform bound. A fixed-epsilon subpower statement is insufficient.
- Verify the upper estimate on the complete complex circle at both
  heights a+/-Im(y), as well as the positive real anchor. All gamma,
  polynomial, exponential and error factors must remain visible.
  L461's constants from extending estimates over all bounded heights
  are not supplied uniformly. Either bound them with their dependence
  or replace that extension by a bounded rectangle around the large
  height, using maximum modulus and separately controlled horizontal
  sides. The general principle is covered; that new application is
  an unresolved part of the mathematical attempt, not a ready bound.
- Use L266's general interface pointwise with b<=3/8<eta<R, retaining
  log(2M/[A(1-p)])/log(1/p), p=eta^2/R^2, including its geometric
  prefactor. Bound the entire expression by the requested cutoff with
  one constant C and one onset. Do not assume L461's B_c is uniform,
  divide by Xi(a), discard central multiplicities, or assert an
  endpoint bound. Allowable analytic losses must be chosen and proved
  small enough for this final comparison rather than declared harmless.

This application reproof is justified by the changed quantifiers and
need to control every constant, not by a claim that the method is new.
No further source theorem is being assumed for the unresolved transfer.
If these elementary tools do not suffice in the attempt, report the
specific missing estimate; approval is not a claim of feasibility.

## Searches, duplicates, failures and Mathlib

Queries actually run included `Riemann zeta zero free half plane
Littlewood log zeta uniform sigma alpha three circles`, `Laguerre Xi
witness logarithmic cutoff`, `Riemann moving anchor`, `zeta logarithm
shrinking zero-free half-plane`, and exact zeta/negative/witness/Laguerre
and Xi/3/16/log combinations. Results did not identify a matching
primary cutoff theorem. The logarithmic-order Laguerre manuscript
appeared as a nearby lead; its already recorded fixed-parameter tail
coverage is reused, with no new inspection or moving-margin inference.
Unrelated zero-free-region expositions and search snippets supply no
theorem input. Failure of these searches is not evidence of novelty.

The notebook-local exact-term search over lemmas/, drafts/literature/
and ATTEMPTS/ found the present nomination and the explicit moving-anchor
exclusions in the L462 assessments; other prescribed-rate hits concern
different objects. L461 and L266 were read in full through their
construction/general comparison. L462's hypotheses, conclusion and
endpoint/signed-remainder qualifications were checked. The saved
interior-anchor stop remains a fixed-parameter stop and is preserved.
No sibling notebook or cross-notebook input was consulted.

[Mathlib's Hadamard documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Hadamard.html)
was inspected: it documents supporting bounded-strip three-lines
results, including
`Complex.HadamardThreeLines.norm_le_interp_of_mem_verticalClosedStrip'`.
This is neither three-circles nor the full moving-anchor witness
theorem. The targeted Borel–Caratheodory documentation search located
no matching API; full matching coverage, Cauchy/gamma API details and
formal quantitative specialization remain unchecked. No absence claim
or local Lean verification is made.

The source decision is SPECIALIZE for the unchanged exact TARGET.
The later attempt should be classified REPRODUCTION. Initial signs,
global mixed positivity, effective numerical overlap and the retained
external theorem audit remain independent gaps. This literature-only
turn changes no lemma, mathematical script, DAG edge or argument in
PROOF.md.
