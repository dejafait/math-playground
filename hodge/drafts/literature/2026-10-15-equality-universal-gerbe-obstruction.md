# Equality kernel — universal-sheaf gerbe obstruction source comparison

TARGET: Assess whether the stable universal-sheaf gerbe pullback is computable from L071's full integral tensor and obstructs the equality kernel.
CHECKED: 2026-10-15
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Bounded exact-statement, stronger-result and nonprimitive stable-locus searches inspected Căldăraru, Krashen–Lieblich and Mattei–Meinsma primary statements; queries and scope failures are recorded below. Local placement, normalization, universal-family and jumping-cycle assessments contain no applicable integral pullback evaluation.
SOURCE_EVIDENCE: Krashen–Lieblich arXiv:0706.1072v3 §1.1, Proposition 1.1.5/Definition 1.1.6; Căldăraru arXiv:math/0108180v1 Theorems 1.1–1.2; Mattei–Meinsma arXiv:2404.16652v2 Theorem 1.2 and §4.1–4.2; Stacks 101.28.3/101.28.6 and 59.28.1 with its cohomology sequence, inspected as detailed below.
COMPARISON: The general G_m-gerbe framework applies on the stable open, but the inspected explicit lattice formulas require a primitive vector; the older formula also requires isotropy. The conditional actual family supplies a lift, not independently computed nonvanishing. Ambient non-fineness, a determinant-fixed mu_2 class and stable-gerbe extension across a polystable point cannot be substituted.
GAP: No inspected primary theorem evaluates the actual stable-gerbe pullback from L071's full integral data at the nonprimitive vector (2,0,-12) and L097's common H; no nonzero pullback is established. The blocker is missing applicable formula coverage, not inaccessible PDFs or a theorem proving impossibility of such a formula.
REASON: Park the gerbe obstruction calculation after a substantive source-scope mismatch; no dependent arithmetic or new lemma is approved. Propose an independent determinant-line positivity review for the existing finite projective classifying map.
LITERATURE_REASON: This changes the target from singular metric extension to an integral universal-family obstruction; the existing equality coarse-moduli assessments do not cover its essential gerbe and pullback formulas.
SCOPE: L071/L093's hypothetical rank-two locally free Omega-polystable equality kernel with integral c_1=0 and ch_2=-14e_1-21e_2-tau_D on the identical marked K3 product, retained Picard rank four, L096's finite possibly empty Z, and L097--L099's actual f restricted to U=B minus Z with v=(2,0,-12). No F existence, gerbe nontriviality, determinant-stack identification or obstruction formula is assumed.

The main gap remains universal primitive rational Hodge realization.
The intermediate target is source feasibility for an integral obstruction
to this particular kernel, using the full mixed tensor rather than only
its holomorphic eigenvalue or rational character. Its plausible downstream
use would be an obstruction to a genuine family lifting the retained
coarse map. Even an exclusion would leave other correction pairs,
representatives, transverse cycle transport and the universal target open.

The completed review follows the original proposal: inspect the
stable-sheaf stack first, distinguish G_m from determinant-fixed mu_2,
and then compare explicit lattice formulas with the nonprimitive vector
and actual stable-open image. L097's polarization and L099's
normalization scopes are retained. No stable gerbe is extended across
a polystable point, and no purity theorem is invoked.

The discriminating test is an evaluable obstruction from the retained
full integral data, with the actual family-to-stack lifting comparison
justified. Continue only if primary coverage supplies that test. Park
the route if it supplies only ambient non-fineness, primitive/isotropic
cases, or a class depending on presently unknown classifying-map data.
An obstruction required to vanish because F was assumed is no
independently computed contradiction. No new theorem or arithmetic
calculation is performed or approved by this proposal.

The metric/degree comparison and its original proposal remain in
2026-10-15-equality-split-metric-extension-degree.md. The normal-curvature
and flat-source product-jet blocks remain preserved; this proposal does
not request their missing analytic data. No cross-notebook input is used.
Mathlib full matching coverage is not checked. The initial proposal's
separate source review is now complete with the calculation parked.

## Inspected primary statements and applicability

Daniel Krashen and Max Lieblich, *Index reduction for Brauer classes
via stable sheaves*, [arXiv:0706.1072v3, 26 December 2007,
§1.1, pp. 2–4](https://arxiv.org/pdf/0706.1072v3#page=2),
assume a proper flat morphism of finite presentation, cohomologically
flat in dimension zero, and a mu_n-gerbe on its source. Definitions
1.1.1/1.1.6 and Lemmas 1.1.2–1.1.4 precede Proposition 1.1.5:
the simple-sheaf stack has scalar inertia and is a G_m-gerbe over
its algebraic-space sheafification, with a universal obstruction class.
The proof uses openness of simplicity and the scalar inertia.

Specialize only this framework to the projective K3 over C, trivial
twisting (n=1), and the fixed-H stable open. Properness, flatness,
finite presentation and H^0(O_S)=C meet the base hypotheses;
stable sheaves are simple. No primitivity assumption is needed here.
This identifies the appropriate obstruction problem, not its value.
The family remains hypothetical: nothing here constructs F.

For base change and neutrality use the Stacks Project,
[Lemma 101.28.3 and Lemma 101.28.6, §101.28](https://stacks.math.columbia.edu/tag/06QB).
A base-changed gerbe is a gerbe; one with a section is equivalent to
the classifying stack of the section's automorphism group. Thus the
retained actual F on S_1 x U, if it exists, is an object over U
lifting f|_U and neutralizes the pulled-back stable gerbe. This is
only the applicability of the cited general result. It is not a
calculation of a nonzero class from tau_D or a contradiction.

Andrei Căldăraru, *Non-fine moduli spaces of sheaves on K3 surfaces*,
[arXiv:math/0108180v1, 27 August 2001, Theorems 1.1–1.2,
pp. 4–5](https://arxiv.org/pdf/math/0108180v1#page=4), requires
a primitive isotropic Mukai vector, compact nonempty stable moduli,
and the quasi-universal Mukai correspondence. Its obstruction is
represented by the transform of an integral vector pairing to one
with v; its Brauer-kernel description is for that K3 moduli surface.
Read §1.9–1.12 and the theorem hypotheses, not only the abstract's
general existence assertion. The present vector is explicitly
2(1,0,-6), so the formula is outside scope already at primitivity;
the local moduli is not the assumed isotropic K3 surface either.
No attempt to adapt or reprove this theorem is made.

Dominique Mattei and Reinder Meinsma, *Obstruction classes for moduli
spaces of sheaves and Lagrangian fibrations*,
[arXiv:2404.16652v2, 21 July 2025, Theorem 1.2, p. 2;
§4.1–4.2, pp. 16–19](https://arxiv.org/pdf/2404.16652v2#page=16),
give a positive-square obstruction/order formula for primitive v
and v-generic H. Read §4's standing scope, Lemma 4.1, Proposition
4.2, Lemma 4.3 and Theorem 4.5, together with the relevant
Lemma 3.16/Proposition 3.17 deformation hypotheses. The proof
uses primitive integral pairing data and deformation to a fine
fibre; the formula is not a nonprimitive stable-open pullback theorem.
Corollary 4.6's shortened wording is read under this standing scope.
Neither replacement of v by v/2 nor changing H is justified for
the retained family. These are hypothesis comparisons, not new
gerbe arithmetic or a critical verification of the paper's proof.

The determinant refinement is a separate issue. The Stacks Project,
[Lemma 59.28.1 and its displayed long exact sequence,
§59.28](https://stacks.math.columbia.edu/tag/03PK), applies with
n=2 invertible over C. It gives the segment
Pic(U)/2 -> H^2_et(U,mu_2) -> H^2_et(U,G_m)[2] -> 0.
Consequently a mu_2 class can contain determinant/line information
lost in its G_m image. No determinant-fixed moduli-stack
identification, chosen refinement or nonvanishing is imported here.

## Search scope, duplicates and stop evidence

Queries included `stable sheaves moduli Gm gerbe universal family
pullback Brauer obstruction nonprimitive Mukai vector`,
`Mattei Meinsma obstruction universal sheaves moduli K3 non primitive
Brauer class`, `K3 Brauer non-primitive moduli universal sheaf gerbe`,
`K3 Brauer group stable locus nonprimitive`, and `universal sheaf
pullback obstruction Mukai nonprimitive`. Follow-up searches used
`K3 nonprimitive Mukai vector Brauer obstruction stable moduli
universal gerbe Perego Rapagnetta` and the exact phrase
`obstruction universal sheaf non-primitive`.
No adequate pullback computation was identified in this bounded
search; this is not a claim of nonexistence or novelty.

The earlier M_H(2,0,-1) assessment treats a different vector and a
coprime universal-family criterion. L097 and L099 give the actual
coarse map and normalization only. The local line-twist/jumping-cycle
assessments fail for missing concentration/effectivity, whereas this
review fails at explicit obstruction-formula coverage. None supplies
the desired independent nonzero pullback. No sibling notebook is used.

Search results also led to Perego–Rapagnetta,
[*The second integral cohomology of moduli spaces of sheaves on K3
and Abelian surfaces*, arXiv:2012.10649](https://arxiv.org/abs/2012.10649).
Its primary theorem and hypotheses have **not** been inspected in this
step. It is an unread lead for the separate determinant-line proposal,
not gerbe coverage or approval of a calculation.

The discriminating test was an evaluable nonvanishing criterion in
the actual nonprimitive/common-H scope. The inspected sources do not
provide it. Ambient order or non-fineness alone would still require
pullback information for f|_U. Passing to U does not supply that data;
extending a Brauer class on the source would not extend a stable
gerbe to a nonsimple polystable target point. No such extension is
asserted. Park this calculation unless a new applicable primary formula
and its evaluable inputs are supplied. This is new source-based
negative route evidence, not exclusion of the equality kernel and
not mathematical progress beyond the sources.
