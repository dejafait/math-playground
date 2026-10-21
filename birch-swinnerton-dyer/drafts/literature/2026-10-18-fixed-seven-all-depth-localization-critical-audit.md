# Fixed all-depth split localization — audit source approval

TARGET: Critically audit L083's fixed all-depth split localization theorem, checking the finite-level identifications, section and cyclic rational Kummer kernel while retaining L034/L081/L082's computational-source qualifications.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the all-depth applicability assessment's recorded exact-curve/localization and Selmer/Kummer searches; read the complete new L083 proof, relevant L034/L081/L082 statements and qualification/audit passages, ATTEMPTS/031/034 and histories 315–317; reread the primary Milne connecting map, localization and finite Selmer diagram and Stacks splitting proof. No fresh discovery search or certificate replay was needed.
SOURCE_EVIDENCE: Milne, Elliptic Curves, second edition (2021), IV Proposition 1.5 p.108, IV.1.9 pp.110–111, IV.2 Lemmas 2.1–2.2 and equations (28)–(29) pp.112–113 inspected; Stacks 10.77.1–10.77.2 splitting/free-module proof inspected 2026-10-18; Silverman (2009) VII.2.1–2.2 pp.188–191 and IV.6.3(b)/6.4 pp.131–132 with author errata 2022-10-13 reused from the ready local-seven and all-depth assessments.
COMPARISON: The exact new audit stays within the already inspected Kummer, reduction, strict logarithm and module hypotheses. L083 supplies the assembly to be tested; none of these sources certifies its correctness automatically. L005's rationalized line is already covered and is not a new target. No new theorem or novelty claim is introduced.
GAP: No essential source gap remains for this fixed proof audit. The audit itself remains undone: both local-quotient containments, torsion exclusions, all-depth primitivity, global/local Kummer matching, section and finite-ring kernel proof must be checked independently against the stated inputs.
REASON: This is the required separate comparison of the new L083 audit target with reusable source coverage. It authorizes a bounded proof audit, retaining the original published-computation qualifications, without redoing L081/L082 or reopening stopped generic routes.
LITERATURE_REASON: The saved critical-audit target had REVIEW_REQUIRED coverage after step 317; this turn supplies its separate scope approval. The underlying source assessments remain adequate, so repeated discovery browsing and upstream computational replays are unnecessary.
SCOPE: Only the existing L083 statement for E=[0,1,1,-2,0], p=7 and every n>=1, with all classical local conditions and the original L034/L081/L082 qualifications. No new point, prime, compatible tower theorem, canonical generator, generic descent interface or arbitrary-curve rank assertion is approved.

## Relevance, downstream use and decision test

The main gap remains rank E(Q)=m(E) for arbitrary analytic order at
least two. The intermediate target is exactly TARGET above. A successful
audit would validate the fixed integral localization application assembled
in L083, giving a checked finite-depth description from actual rank,
primitive-point and Sha inputs. It would not produce those inputs
uniformly or resolve the main gap. Continue with a research audit only
because the exact source scope is covered; stop at the first unmet
hypothesis or incorrect implication and preserve the failed claim.

## Primary theorem coverage and applicability boundaries

[Milne, second edition](https://www.jmilne.org/math/Books/EC2.pdf#page=113),
IV.1.5 p.108 gives the connecting cocycle from a lift; IV.1.9
pp.110–111 gives completion maps. IV.2 pp.112–113 contains multiplication
surjectivity over algebraic closures, the global/local Kummer diagram,
the all-place Selmer definition including R, and equation (29), with
its kernel-cokernel argument. They cover every integer 7^n over Q and
Q_7; no Sha finiteness is required. The audit must check that L083 uses
the inverse local Kummer map only on its image and matches point
localization. IV.3.2's prime-to-residue-characteristic restriction makes
it unsuitable for division by seven here; it is not an input.

Reuse the full primary-hypothesis and proof-case record in
`2026-10-18-known-point-local-seven-test.md` and
`2026-10-18-fixed-seven-all-depth-localization.md` for
[Silverman, second edition](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=150).
VII.2.1–2.2 requires the complete discretely valued field, minimal
integral equation and perfect residue field; good reduction identifies
E_0 with the full local group. IV.6.3(b)/6.4 uses the strict integer
radius r>v(p)/(p-1). The audit stays over Q_7 with r=1>1/6 and the
same formal logarithm throughout. It must distinguish this radius from
coefficient depth n. The
[author errata, 13 October 2022](https://www.math.brown.edu/johsilve/AEC/AECErrata.pdf),
entries for pp.130–133 and 185–191, remain part of the reused assessment;
the erroneous unrestricted integrality wording of IV.6.3(a) is not used.
No general ramified-field extension or logarithm evaluation at P=(0,0)
is within scope.

[Stacks Project, Definition 10.77.1 and Lemma 10.77.2](https://stacks.math.columbia.edu/tag/05CD)
apply over any ring. Their free-module/projective and splitting proof
cases cover the abstract splitting ingredient. They do not alone give
the kernel rank. The audit must test L083's explicit section and
unit-coordinate argument over the local ring Z/7^nZ, including n=1;
no vector-space dimension argument at n>1 is licensed. The existing
proof supplies that elementary specialization, so a new module lemma
or reproof of projectivity is unnecessary.

## Fixed inputs, duplicates and bounded audit obligations

L030 supplies the exact minimal model; only L033's good reduction and
group order thirteen are used here, not its coefficient machinery.
L034 supplies rank two, retaining Cremona's published computational
provenance; the displayed point pair need not be seven-saturated.
L081's completed step-309 audit supplies the actual valuation-one
W=[13]P, and L082's completed step-313 audit supplies the published
seven-primary Sha conclusion from Stein–Wuthrich Theorem 12.3, with
its unreplayed computations. These imports are sufficient in scope;
their cited computations must not be represented as freshly verified.

The audit must check both containments in U/7^nU -> E(Q_7)/7^nE(Q_7),
not replace the full group by U without justification. Test the use of
the order-thirteen reduction group, local and rational seven-torsion
exclusion, and generation at every n by the actual P. Then check global
quotient freeness, all classical local conditions, Kummer naturality,
section well-definedness, cyclic kernel and cardinalities. These are
proof obligations for the next turn, not new deductions in this review.
Quotient-level rational Kummer membership does not assert an actual
rational point of zero local logarithm or a chosen generator across
depths.

The prior exact-target searches and duplicate comparison remain in the
all-depth applicability assessment; unchanged hypotheses justify reuse,
not a claim of novelty from unsuccessful searches. L005 already covers
the rationalized strict line. ATTEMPTS/031's generic semisimplicity
obstruction and ATTEMPTS/034's uninstantiated descent-interface stop
remain intact. Histories 315–317 distinguish the exhausted repeat of
L081's audit from the new L083 assembly. This permits one audit of that
new assembly, not further upstream replay without a specific defect.

Full matching Mathlib coverage and supporting theorem availability are
not checked; no absence claim is made. This literature-only step
approves source scope, not L083's mathematical correctness. It adds no
lemma or mathematical script and changes no argument or DAG edge.
