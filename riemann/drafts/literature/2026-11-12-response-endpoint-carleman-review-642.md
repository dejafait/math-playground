# Nomination642 and review643: retain the response endpoint operator analytically

TARGET: Assess whether C744v's two parity response operators admit an explicit Carleman endpoint part plus a quantitatively controlled compact remainder suitable for a full middle-form reference.
CHECKED: 2026-11-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Separate literature-only643 searched exact-response/Carleman/Hankel compact-perturbation and effective Hilbert-Schmidt approximation terminology; checked local532/541, C744v Section3, C999k Sections1-2 and600/603/635/640 stop records. No matching ready-made split with fixed-a constants was found in the inspected sources; queries, access limits and comparison are below, with no novelty inference.
SOURCE_EVIDENCE: Rechecked Hongmin Li paper45 displayed v2 (9November2026),Section2/(2.4)-(2.5),Lemma3.1 and full proof/(3.1)-(3.4), https://rstation.ai/problems/riemann_hypothesis/papers/45 ; bramble_trace paper60 displayed v1 (26October2026),Section2/(2.4)-(2.7) andSection3/(3.1)-(3.7), https://rstation.ai/problems/riemann_hypothesis/papers/60 ; newly inspected Teschl GSM99 (2009),author-hosted317-page PDF,Section6.3 pp139-141,(6.8)-(6.18),Lemma6.9/proof andCorollary6.11/proof, https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf . Exact response and quantitative L2-kernel approximation tools are covered; the requested split is not a cited theorem.
COMPARISON: Li supplies both exact parity vectors for arbitrary a and j>=0; paper60 supplies a majorant and exact full Fourier sums with effective exponential corrections, not a physical-kernel compact split. Teschl supplies a computable operator-error bound from an L2-kernel error once that error is established. Together these justify a bounded standard specialization, not an assertion that this remainder exists, is positive or improves the middle reference. Fixed32 and fixed598 stops remain intact.
GAP: Derive the singular coefficient and exact physical-kernel split at a=log(3)/4, prove complete remainder estimates including both boundary cases and j=0, and give explicit finite-rank approximants with computable error tending to zero in raw L2 operator norm. Compactness without a rate fails the test; lower-reference coercivity, energy-normalized comparison and actual S3 gain remain outside this approval.
REASON: The essential general tools are now inspected and source access is sufficient for one fixed-kernel specialization attempt. Only the explicit algebra, uniform convergence and effective remainder bounds need local proof; reprove neither the Green identity nor Hilbert-Schmidt theory. No mathematical assertion about the proposed split is established643.
LITERATURE_REASON: Changed target asks for a singular-kernel/compact-remainder decomposition and effective approximation scope absent from638/639's shorting coverage and532/541's boundedness comparison.
SCOPE: Review643 is source-only; subsequent reuse permits one standard-specialization attempt for the unchanged TARGET, C744v Section3's complete single-cell response at a=log(3)/4, both complex parity spaces and all j>=0. Determine an exact endpoint split and explicit raw-L2 remainder approximation bound, or record the obstruction. No assumed coefficient/compactness/sign, actual middle-inverse construction, numerical optimization, radius/prefix tuning or600/603/635 restart is covered.

The main gap is still L030-L032/C032a actual-Xi positivity. A response
reference that retains endpoint interactions could help bound the full
middle inverse and its signed induced coupling. This is a plausible use,
not a proved improvement or a complete route to RH. The actual remote
operator U and every T/T* term would still have to be retained later.

The concrete source question uses the known response vectors

    r_j^epsilon(y)=exp(-c_j a)(exp(c_j y)+epsilon exp(-c_j y))
                    /sqrt(1-epsilon exp(-2c_j a)),
    c_j=2j+1/2, epsilon=+1 or -1, 0<y<a.

In coordinates t=a-y and s=a-z, assess whether a source provides an
EXACT split of the full response kernel into an explicitly normalized
Carleman-type kernel and a bounded/Hilbert-Schmidt or otherwise compact
remainder, together with effective constants at this fixed a. Determine
the coefficient from a primary statement or approve its later derivation;
do not infer an equality, positivity or compactness from the upper bound
in C744v. Both parity boundary cases and the j=0 response must be covered.
Raw L2 operator approximation must be distinguished from approximation
after normalization by the logarithmic energy. No assertion of either
kind of compactness is supplied here.

Bounded review test: inspect primary kernel/decomposition statements and
their essential proof cases, starting with the already located paper60
Section2 and paper45 Lemma3.1. Follow only relevant Carleman/Hankel
references. Seek an explicit remainder norm or an assessed derivation
with a computable error tending to zero while the singular part remains
exact. A compactness assertion alone is insufficient for a numerical
lower reference. If all that is available is the old majorant, an
uncontrolled compactness claim, or an assumption of the missing sign,
record that limitation and park this target without repeated retrieval.
If essential access is blocked, do not retry the old numerical supplements;
they are not the requested analytic input.

Three mechanisms compared for next routing:

1. Adding the two-moment correction to unchanged598 is rigorously stopped
   by C999y Section4/642. Its positive rank is too small on the certified
   three-dimensional deficient space; further tail evaluation cannot fix it.
2. Improving common-error centers or residual-stationary proposals remains
   parked by600/603/635. Their failed sufficient allowances are not actual
   sign obstructions, and audit637 is not authority to resume them.
3. Select the entire-response endpoint decomposition. Unlike a finite
   prefix or rank-two addition to M598, it would retain a singular integral
   operator in a new analytic reference. The fixed32-prefix negative
   comparison in C744z Section8 is a warning to retain the full response,
   not evidence that this proposed split exists or succeeds.

Essential continuation inputs: C744v Section3 and its analytic-response
qualification; C744z Section8's prefix stop; C999k Sections1-2 for the
current reference loss; C999y Section4 for the audited fixed repair;
532/541 source passages and600/603/635 stop records. No cross-notebook
input. IEEE754/Decimal, core/c_*, higher endpoints, mixed signs,C744q,H2,
non-neutral coverage and global assembly remain unresolved; none is
validated by this nomination. Full matching Mathlib coverage unchecked.

The nomination required a separate literature-only turn. It was not
approved or derived in audit642; source comparison643 follows below.
A protected creative nomination is not yet justified:
the decomposition may be a standard specialization and no independent
sign-producing mechanism is established. The review should determine
whether it offers materially new usable analytic input before selecting
a bounded mathematical attempt and its proper purpose route.

## Completed source comparison643 — 12 November2026

**Decision and limits.** SPECIALIZE approves a later derivation within the
unchanged TARGET above. No split or bound is proved in this literature
turn. The singular coefficient is deliberately left undetermined: it must
come from the exact summation, not the nonsharp majorant. A full matching
theorem was not found; that observation is not an originality claim.

The source audit read these primary cases before considering broader leads:

- [Li, paper45 v2](https://rstation.ai/problems/riemann_hypothesis/papers/45),
  Section2/(2.4)-(2.5) and Lemma3.1/(3.1)-(3.4), including its complete
  proof. The unitary half-interval convention fixes the normalization.
  Neumann-Neumann and Dirichlet-Neumann resolvents give the two parity
  responses. Finite digamma sums and monotone limits justify the smooth-core
  identity; compact tests have exponentially decreasing response
  coefficients. This is an arbitrary-a identity, not merely an endpoint
  certificate. It makes no full-response L2 boundedness claim. Import this
  identity; do not reprove it or import its numerical positivity certificate.
- [bramble_trace, paper60 v1](https://rstation.ai/problems/riemann_hypothesis/papers/60),
  Section2/(2.4)-(2.7) and Section3/(3.1)-(3.7). The boundedness/core argument
  uses a constant-plus-Carleman majorant at radius2. The full Fourier matrix
  is instead summed by digamma divided differences; exponential correction
  tails have explicit bounds. These provide an exact-summation precedent,
  not a compact physical-kernel decomposition or transferable radius2
  constants. The separate constant Fourier mode is explicitly qualified.
  The present a differs, so every specialized constant still needs proof.
- [Teschl, GSM99 (2009), Section6.3](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
  printed pp139-141 (PDF pages150-152, zero-based). Read (6.8)-(6.12),
  Lemma6.9 and its proof, (6.15)-(6.18) and Corollary6.11/proof.
  For a square-integrable kernel on the product measure space, (6.9)
  bounds the operator norm by its kernel L2 norm; finite product-basis
  approximations prove compactness. Lemma6.9 identifies the Hilbert-Schmidt
  norm and Corollary6.11 controls bounded conjugations. Apply to the
  proposed remainder/error only after verifying those hypotheses. These
  results give no computable approximation rate without kernel estimates.

**Exact difference to derive later.** Starting from C744v's imported
vectors, one may expand their products, sum the endpoint contribution
exactly, and bound the remaining series with explicit constants. This is
a proposed calculation, not a performed or verified expansion. All four
product contributions, parity denominators and j=0 must remain accounted
for. An alleged removable singularity needs a proved uniform bound on
the closed square, not values sampled away from its corner. If a
remainder is square-integrable, the cited kernel bound permits an
explicit approximation error to be converted into an operator error.
The attempt must exhibit finite-rank approximants and a computable
error tending to zero, for example through justified uniform series or
piecewise-polynomial bounds. Merely invoking density or compactness
does not meet the quantitative target. A new general approximation
theorem is unnecessary; import Teschl and prove only the scalar
estimates and their applicability.

**Relevance and bounded test.** Preserve the singular operator exactly
while approximating only the remainder. This could avoid discarding
endpoint information in a later middle-form lower reference. Success
here is an exact normalized identity in both parity spaces and a full
effective error formula; there is no preset S3 margin claimed. Failure
to isolate all noncompact contributions or produce effective control
ends this attempt. Raw L2 control must be stated separately from any
logarithmic-energy-normalized approximation. No positivity of the
remainder, coercivity of a resulting reference, or improvement over598
follows automatically. Those are separate unapproved targets. Retain
C999k's restricted-form/inverse-order obligations in any downstream use.

**Search and exclusions.** Queries used included:

- `Carleman integral operator kernel 1/(x+y) truncated Hilbert Schmidt perturbation Hankel endpoint kernel exponential series`
- `Hankel integral operator singular kernel compact perturbation 1/t remainder approximation Hilbert Schmidt`
- `Hankel "1/(2 sinh" Carleman operator kernel`
- `Hankel operator "1-e" "Carleman" kernel`
- `Yafaev Carleman operator "Hilbert-Schmidt" perturbation kernel`
- `"Carleman" "exponential" "kernel" "compact" Hankel sinh`
- `"Hankel" "1-e" "kernel" "compact"`
- `Teschl "Hilbert–Schmidt" "integral" "Theorem" kernel pdf mathematical methods quantum`

Local searches were confined to the named response proofs and
12November literature/attempt/history records. Reused532/541's broader
source comparison. Reviewed the600/603/635 failure records: their
finite-radius and allowance failures are not actual-form obstructions,
but none supplies an endpoint decomposition. Audit642 of C999y gives
the fixed598 rank-two stop; this proposal changes the infinite reference
rather than adding that stopped correction. It must not be used to
resume any parked numerical prescription.

The introduction/(1.1)-(1.5) of
[Bertola--Blackstone--Katsevich--Tovbis, arXiv2210.10002v1](https://arxiv.org/pdf/2210.10002v1)
was inspected: its operator couples disjoint multi-intervals through a
finite Hilbert-transform kernel. No theorem or proof from it was read
for this target, and none is imported. Search leads to Perfekt--Pushnitski's
multiplicative Hilbert matrix and Yafaev's whole-half-line Hankel theory
do not establish this two-variable parity split; their theorem hypotheses
and essential proof cases were not fully inspected, so they remain unused
leads. Faris's author-hosted notes timed out on detailed retrieval; the
publisher PDF for Perfekt--Pushnitski returned403. Neither is essential
after the successful Teschl inspection. Shell retrieval was unavailable
because network DNS failed; the web tool supplied the primary passages.
No supplement or API key was used, and no persistent essential source
blocker remains.

This is EXPLORATION in source comparison, not a mathematical advance or
a new decomposition. Full matching Mathlib coverage remains unchecked.
The next use of the same assessed target should be mathematics; no
additional literature is needed unless its hypotheses or scope change.
Its fixed-kernel algebra and estimates are standard specialization,
classified REPRODUCTION and routed as calculation/standard/high. A
protected creative sign-producing mechanism is not yet justified: this
preparatory decomposition could fail or leave the reference sign unpaid.
