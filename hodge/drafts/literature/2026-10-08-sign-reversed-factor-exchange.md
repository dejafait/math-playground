# Changed-sign factor-exchange transfer — source coverage

TARGET: Test whether factor exchange transfers audited L072 to exclude the changed-sign pair (a,b)=(-10,-9).
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped L071/L072 hypotheses and proof, L044's full mixed operator, L003's correspondence convention, L074 and history/151--168 references; searched Stacks Chern pullback and isomorphism pullback, then Cornell Hatcher cup/cross products. No completed exchange application found in these scoped records; no novelty inference.
SOURCE_EVIDENCE: Inspected Stacks Lemma 17.14.3 (01C8), Section 26.24 (01LA), Lemma 42.38.5 statement and full proof (02U4), and Section 42.45 (02UM); inspected Hatcher Algebraic Topology Proposition 3.10/Theorem 3.11 and relevant proof passages pp. 210--212, cross-product definition p. 214 and graded product pp. 215--216; reused the saved L072 audit coverage and history/158 verdict.
COMPARISON: General pullback and cup-product functoriality cover the proposed isomorphism application; audited L072 supplies the five-charge exclusion. Neither source alone states the full changed-sign pair transfer, whose exact tensor and slope hypotheses must still be instantiated.
GAP: A separate research step must verify the full tensor transpose, integral Chern pullback, unchanged marked metric and real product slope-polystability, then test L072's complete integer-domain hypotheses; this review establishes no exclusion.
REASON: Essential coverage is adequate for the unchanged TARGET as a bounded REPRODUCTION application, without redoing GRR or proving a new preservation theorem.
LITERATURE_REASON: The saved factor-exchange continuation was REVIEW_REQUIRED, outside the completed L075 audit; this review supplies its missing functorial coverage and reuses ready L072 sources.
SCOPE: Identical marked K3 factors with identical metric, L071's full integral -tau_D and q-self-adjoint D, integral c_1=0, locally free rank-two F polystable at Omega=p_1^*h+p_2^*h, (a,b)=(-10,-9), unrestricted initial higher characters and K-class. No unequal metrics or non-self-adjoint tensors are covered.

## Gap, use and discriminating test

Universal primitive rational Hodge-class algebraicity is the main gap.
The intermediate target is a conditional exclusion of one residual
product-bundle pair by exchanging factors and using audited L072.
Its plausible downstream use is to remove a construction candidate
from L074's directional non-exclusion list. It supplies no algebraic
cycle, kernel or transport. Continue only if every retained hypothesis
matches; abandon this transfer if the full tensor or polarization changes,
or if the resulting input lies outside L072. Source approval is separate
from that mathematical test.

## Primary inputs inspected and precise scope

[Stacks Lemma 17.14.3, Tag 01C8](https://stacks.math.columbia.edu/tag/01C8)
states that pullback under a morphism of ringed spaces preserves locally
free sheaves; its proof is omitted there. [Section 26.24, Tag 01LA](https://stacks.math.columbia.edu/tag/01LA)
records quasi-coherent pullback and kernels. Isomorphism pullback and
its inverse are the named elementary sheaf functoriality input, not a
restriction-stability theorem. The next step must use the isomorphism
and inverse to account for all coherent subsheaves and stable summands.
No general flat pullback preservation of stability is asserted.

[Stacks Lemma 42.38.5 in Tag 02U4](https://stacks.math.columbia.edu/tag/02U4)
requires a flat morphism of fixed relative dimension and a finite locally
free sheaf, in the locally-finite-type Chow setup. Chern operations commute
with that pullback. Its complete proof uses the pulled-back projective
bundle, its tautological line, flat base change and uniqueness of the
Chern relation. An isomorphism is the relative-dimension-zero case;
the smooth projective complex product meets the setup. Cycle-class
compatibility passes this input to cohomology. [Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM)
defines the rational character as a polynomial in Chern classes. Keep
integral first Chern data distinct from the rational character.

Hatcher, *Algebraic Topology* (Cambridge, 2002), author-hosted
[PDF](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf#page=219),
Proposition 3.10 and Theorem 3.11, printed p. 210, give natural cup
products and graded commutativity over a commutative coefficient ring.
Read the cochain naturality proof and vertex-reversal/chain-homotopy
proof passages pp. 210--212. The cross product is defined using the
projection pullbacks on p. 214; pp. 215--216 retain the graded tensor
multiplication sign. These are primary coverage for the transpose/sign
check; use the actual cohomological degrees and correspondence convention.
They do not establish invariance of this particular tensor by themselves.

## Reuse and remaining application obligations

Reuse [L072 audit coverage](2026-10-08-sign-reversed-five-charge-critical-audit.md)
and history/158: its actual every-fibre concentration, signed relative
GRR and entire integer-slice exclusion were separately audited. The
Stacks 0A1H/0BDH and Fulton Theorem 15.2/Example 15.2.8 inputs need
no reproof or fresh extraction for this application. L071's hypotheses
provide the full self-adjoint operator on H^2, not just its T component.
L044's integral mixed construction and L003's displayed tensor-action
convention were read for comparison; L003's quartic theorem is not being
imported onto this different K3 surface. The next proof must justify its
linear-algebra use on the full cup-product space by Poincare duality.

The separate application must explicitly match factor-point classes,
full mixed class, determinant condition, actual product metric and
polarization, ranks and local freeness. For slope stability use the
retained definition with degree given by c_1 against Omega^3 on this
fourfold: compare every subsheaf via the inverse isomorphism and
integration functoriality, including polystable decompositions. This is
an elementary specialization obligation, not a new theorem proposal.
Higher characters need not be retained from an old K-class: L072 leaves
them initially unrestricted. No opposite-fibre stability, transform
inverse, harmonic-family argument or transport hypothesis is needed.

## Duplicates, stops and limits

Scoped L071/L072/L074 and history/151--168 references contain the
necessary-test region, directional exclusions and audits, but no
completed factor-exchange transfer. L075 addresses different residual
coefficients. Existing ATTEMPTS/043 and 045 preserve compatible
orthogonal/projective index branches; ATTEMPTS/051 stops repetition of
the surface-character filter. This target uses an already proved slice
and is independently testable without reopening those mechanisms.
The persistent flat-index source blocker stays parked.

Essential continuation inputs are L071 and audited L072; L074 motivates
the selected residual pair. Full tensor symmetry and polarization/stability
matching are still application obligations. The flat b=-17 case, larger
charges, other representatives, F existence and transverse transport remain
unresolved. No cross-notebook input is used. Full matching Mathlib coverage
and supporting coverage were not checked; no absence claim is made.

## Outcome

LITERATURE / EXPLORATION / NOVELTY_UNCHECKED: the previously uncovered
TARGET is now SPECIALIZE for a separate REPRODUCTION application.
This is source-scope progress, not a new mathematical result or a
correctness verdict on the transfer. Mathematical exploration usage
is zero; no supervisor-counter reset is claimed. No lemma, mathematical
script, DAG or PROOF change was made.
