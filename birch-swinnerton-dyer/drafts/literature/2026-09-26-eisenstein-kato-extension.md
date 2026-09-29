# Eisenstein specialization into the required Kato extension

TARGET: Test whether an Eisenstein specialization of a Beilinson--Flach family gives a class in H^1(Q,W_d) mapping to z_tw for L012's extension 0 -> V -> W_d -> V tensor chi_K -> 0.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Eisenstein degeneration, weight-one Beilinson--Flach/Kato comparison, anticyclotomic extensions, stable lattices, and later degeneration papers; queries and primary statements actually read are recorded below.
SOURCE_EVIDENCE: Loeffler--Rivero, arXiv:2201.02078v2, A1--A2, A4.5, A6.3, C1.4--C1.13; Bertolini--Darmon--Venerucci, author final PDF, Section 1.1, Proposition 4.1 and Theorem 4.2; Burungale--Skinner--Tian--Wan, arXiv:2409.01350v2, Theorems 1.21, 5.19--5.20, 5.26 and Lemmas 4.14--4.16; Alonso--Omil-Pazos--Rivero, arXiv:2509.07564v1, Theorem 1.1, Corollary 5.19 and Conjecture 6.8; Polo--Rivero with appendix by Wu, arXiv:2501.01514v3, Theorem 1.3 and Section 7.
COMPARISON: Known families and lattice comparisons cover useful inputs, but no inspected statement supplies the specified extension with a nonzero z_tw quotient; the direct critical-slope and natural weight-one specializations fail the applicability tests below.
GAP: Identify the inverse anticyclotomic extension, retain a regular global class after changing the coefficient lattice, and prove that its quotient is a nonzero scalar multiple of z_tw under the retained arithmetic hypotheses.
REASON: Stop direct import of the inspected specializations. The known classification of stable CM lattices supports one bounded comparison of a modified lattice and its cohomology class; no construction or division is performed in this literature turn.

## Target, relevance, and threshold

The exact saved target is preserved. Retain all of L012's hypotheses,
including the auxiliary conditions in the
[Castella--Hsieh audit](../../foundations/07-castella-hsieh-nonvanishing.md).
In particular, p > 3 is good ordinary, p splits in K, L(E^K,1) != 0,
and the inert conductor part N^- has an odd number of prime factors.
The coefficient field remains Q_p, with any source's scalar extension
and descent to be accounted for.

The required representation is L012's particular W_d, with inverse
anticyclotomic tangent -d, rather than only its semisimplification.
The threshold is a global class mapping to c z_tw with c != 0;
rescaling would then give the requested quotient. L012 identifies
this with vanishing of its still unknown connecting cup product.
That could settle the mixed lifting obstruction. It would not yet
identify strict lifting with rational Kummer membership.

The main gap remains q(kappa) = 0 and the lower bound r >= 2 beyond
the known r <= 2. Nonvanishing from m(E) = 2, auxiliary existence,
and higher ranks remain independent gaps. No rank bound changes here.

## Search record and reuse

Queries included:

- `Beilinson Flach Eisenstein degeneration Kato classes extension weight one anticyclotomic`
- `Eisenstein specialization Beilinson Flach Kato class Loeffler Rivero critical weight one`
- `"Anticyclotomic diagonal classes and Beilinson"`
- `"Eisenstein degeneration of Euler systems" arxiv`
- `"Bertolini" "Darmon" "Venerucci" "Eisenstein" Kato weight 1`
- `"Beilinson-Flach" "lattice" "weight one" extension`
- `"Beilinson-Flach" "anticyclotomic" "extension" Eisenstein`
- `"Polo" "Rivero" "Eisenstein" "factorization" "Beilinson" sequel`

The [previous review](2026-09-26-current-target.md) already assessed
reciprocity, universal rank-two deformations, and the weighted
two-variable specialization. Those findings are reused. This review
adds the actual Eisenstein coefficient representations, the arithmetic
hypothesis comparison, and the stable-lattice source; it does not
repeat normalization as an advance.

The prior failures of trace continuation, scalar Coleman control,
formal duality, and reciprocity alone remain as recorded in
ATTEMPTS/005--010. The prospective change of lattice must supply
class-level information that those mechanisms did not provide.

## Primary statements inspected

### Critical-slope degeneration

Loeffler--Rivero, *Eisenstein degeneration of Euler systems*,
[arXiv:2201.02078v2](https://arxiv.org/abs/2201.02078v2), 2024-02-14;
published in *J. reine angew. Math.* 814 (2024), 241--282.
Read A1--A2, Theorem A4.5, Corollary A6.3 and Section A6.3
([printed pages 3--8](https://arxiv.org/pdf/2201.02078v2#page=3)),
and [C1, pages 19--23](https://arxiv.org/pdf/2201.02078v2#page=19).

The input is p-decent E_(r+2)(psi,tau), r >= 0, with the
non-criticality condition of A4.5; the companion family is ordinary.
The constituent characters are psi and tau epsilon_cyc^(-1-r).
Corollary A6.3 distinguishes the extension orientations and duals.
C1.4 initially allows a pole; C1.6--C1.7 remove it in a specified
lattice. C1.13 identifies a projected leading term with a Kato
family multiplied by logarithmic and p-adic L-function factors.

Applicability comparison: this character pair has a nonzero relative
cyclotomic twist, unlike the pair 1, chi_K required here. Its
weight-one substitute is outside r >= 0. The theorem cannot be
imported as W_d or as an unweighted quotient. Its lattice analysis
is useful precedent, not a matching lift theorem.

### Weight-one CM comparison

Bertolini--Darmon--Venerucci, *Heegner points and Beilinson--Kato
elements: a conjecture of Perrin-Riou* (2022): read the
[author final PDF](https://www.esaga.uni-due.de/f/massimo.bertolini/publications/BDV-Final.pdf),
Section 1.1, pages 2--4, and Section 4.1--4.3, pages 24--29.
Proposition 4.1 and (23) identify the CM family with an induced
representation; its weight-one fiber is 1 direct-sum chi_K.
Equation (24) and Theorem 4.2 give, with their periods and
nonzero auxiliary factor retained, the weighted class

\[
L_p(f\otimes\chi_K)\,\boldsymbol z_f\otimes v_1
 +L_p(f)\,\boldsymbol z_{f,\chi_K}\otimes v_{\chi_K}.
\]

Section 4 retains Section 1.1's Heegner hypothesis: every prime
dividing pN_f splits in K, as well as its non-exceptionality
restriction. The all-split hypothesis conflicts with the retained
N^- condition. Even in its own setting, the stated fiber is split.
This is a precise source-scope exclusion, not a claim that its
methods cannot be extended.

### General CM lattices and the two-variable class

Burungale--Skinner--Tian--Wan, *Zeta elements for elliptic curves and
applications*, [arXiv:2409.01350v2](https://arxiv.org/abs/2409.01350v2),
2024-09-11. Newly read
[Theorem 1.21, page 9](https://arxiv.org/pdf/2409.01350v2#page=9),
[Section 4.2.8, Lemmas 4.14--4.16, pages 41--42](https://arxiv.org/pdf/2409.01350v2#page=41),
and [Theorems 5.19--5.20, page 52](https://arxiv.org/pdf/2409.01350v2#page=52).
Rechecked [Theorem 5.26, pages 55--56](https://arxiv.org/pdf/2409.01350v2#page=55).

For the elliptic-curve formulation retain p not dividing 2N,
split p, coprime discriminant, and E(K)[p] = 0. The closed CM Tate
lattice is integrally induced and the BF class comes from that
lattice, with relaxed/ordinary local conditions. The lattice lemmas
also control adjacent non-induced lattices and their augmentation
quotients. These are known inputs to cite, not reprove.

The earlier weighted specialization remains the strongest checked
class comparison in this setting. Its twist coefficient vanishes
at the notebook's augmentation. These additional lattice theorems
do not state that a modified specialization has quotient z_tw.
The class's regularity and that quotient remain to be checked.

### Later diagonal/BF comparison

Alonso--Omil-Pazos--Rivero, *Anticyclotomic diagonal classes and
Beilinson--Flach elements*,
[arXiv:2509.07564v1](https://arxiv.org/abs/2509.07564v1), submitted
2025-09-09; PDF dated 2025-09-10. Read the setup and Theorem 1.1,
Proposition 2.4, Assumptions 4.1/4.10, Section 5.2,
[Corollary 5.19, page 22](https://arxiv.org/pdf/2509.07564v1#page=22),
and [Conjecture 6.8/Assumption 6.10, page 26](https://arxiv.org/pdf/2509.07564v1#page=26).

The remaining cuspidal families have coprime tame levels, the stated
character relation, residual irreducibility and p-distinguishedness.
Theorem 1.1 additionally assumes a torsion-free rank-one
H^1_(G union +) and a nonzero triple-product p-adic L-function.
It compares a weighted BF combination to a diagonal class after
specialization. Remark 1.2 explicitly limits this comparison to
the bottom layers.

Conjecture 6.8 asks for division of a BF class by an exceptional
Euler factor; subsequent results assume it. This is neither an
unconditional divisibility theorem nor division by L_p(E).
No displayed conclusion supplies the requested W_d class.

### Follow-up on critical Eisenstein derivatives

Polo--Rivero, with appendix by Wu, *Eisenstein degeneration of
Beilinson--Kato classes and circular units*,
[arXiv:2501.01514v3](https://arxiv.org/abs/2501.01514v3), submitted
2025-10-05; PDF dated 2025-10-07. Read Assumptions 1.1--1.2,
Theorem 1.3 (pages 2--3), and
[Section 7, pages 24--25](https://arxiv.org/pdf/2501.01514v3#page=24).
The main comparison uses critical Eisenstein series, even r and
even characters, with assumptions on the adjoint zero and a
nonzero derivative. It concerns circular units. Question 7.1
and the sequel discussion do not state the weight-one lift needed
here. No theorem from an announced sequel is assumed.

## Access, source scope, and novelty limits

The essential statements above were accessible as primary PDFs;
arXiv mathematical HTML was also used to resolve extracted notation.
Version dates above follow the fixed arXiv records and PDFs, not
the HTML renderings' later generated dates. The author final BDV
copy was accessed on 2026-09-27; its theorem/page numbering is used.

[Rivero's publication list](https://www.oscarrivero.org/publications)
and the sequel query yielded no additional matching theorem read
in this bounded review. Search snippets and automated summaries
were discovery aids only. The cited papers' full proofs, their
uncited references, and peripheral search leads were not exhaustively
audited. No essential inaccessible statement is used as an input.
Absence of a match in this search is not a novelty claim.

## Decision and bounded continuation

**Stop the direct application of the inspected specializations.**
The new coefficient and hypothesis comparisons resolve that
applicability question negatively. This is more than repeating
the previously known weighted formula. It does not prove
nonliftability of z_tw or refute the wider target.

SPECIALIZE retains the original target for a later research turn.
The identified difference is a change of Galois-stable lattice at
the weight-one CM point, followed by a class-level comparison.
Use the cited induced-family and adjacent-lattice results. Test
whether such a lattice has the exact W_d special fiber after
normalizing the cyclotomic direction. Then track the actual BF
class into it and test its regularity and nonzero quotient.
Do not replace the retained K by an all-split Heegner field.

Continue only if this comparison supplies a regular global class
with the required quotient, or an explicit new divisibility claim
with a concrete arithmetic means to test it. Stop this modification
if it gives the opposite extension, the same zero quotient, or
requires unsupported division of global cohomology. A matching
representation alone leaves the arithmetic problem open and is
not an advance on the rank bound. These are prospective tests;
no modified representation or class is constructed in this turn.

The step outcome is NEGATIVE for direct theorem import, with known
source results used for the comparison and no new mathematics.
The review started after two exploration turns and completes the
assessment and route decision on the third bounded turn. Its new
source-scope evidence ends that unproductive run; merely restating
it later would be STALLED. No launcher or research-stop state is
changed. The sole current action and counter are in PROGRESS.md.

## Mathlib

Full coverage of the specified W_d lift: **not checked**.
Supporting coverage for Eisenstein degeneration, stable lattices,
and BF/Kato specialization: **not checked**. The named arithmetic
citations support only the inputs and comparisons stated above;
none is asserted to be a full source or Mathlib match for the lift.
