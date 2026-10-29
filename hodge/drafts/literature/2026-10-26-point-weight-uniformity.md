# Point-weight uniformity — source comparison

TARGET: Determine whether L111's fixed Kodaira–Spencer normalization forces L168's weights mu_z to be independent of the reduced split point.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: On 2026-10-26 searched Grothendieck duality residue regular parameters Ext Koszul fundamental local isomorphism trace dx dy residue smooth scheme; Stacks duality regular immersion fundamental class differential forms trace closed point; and Grothendieck duality and transitivity II Verdier residues Koszul; followed Nayak–Sastry II's explicit references to I, Appendix C and section 5.4; checked L111,L168, the prior audit assessment and ATTEMPTS/092–094 for overlap.
SOURCE_EVIDENCE: Inspected Nayak–Sastry I, author PDF dated 2019-05-29, sections C.1–C.2, C.5.3–C.5.4 and 5.3–5.4, including the generator, finite-counit and fraction comparison proofs; II, author PDF dated 2019-05-29, (4.1.2),(4.1.5), Proposition 4.2.2, sections 5.1–5.3 and Theorem 5.4.2, including their regular-section proofs; reuse prior Stacks finite/global duality coverage.
COMPARISON: These sources explicitly cover the determinant-line Ext generator, generalized-fraction conventions and canonical residue normalization for a regular section of a smooth separated map; they do not state uniformity of this notebook's mu_z or identify its particular paired Koszul summand.
GAP: In a separate mathematical turn identify L168's epsilon_{x,y} in the inspected conventions, trivialize the canonical form by the fixed sigma_B, compare with L111 (8)–(9) and retained common kappa, and test whether their ratio is point-independent; neither that identification nor equality of weights is proved here.
REASON: New primary coverage fills the invocation-start normalization source gate and permits the exact saved target as a later REPRODUCTION specialization; no new normalization mathematics, numerical mu_z or exclusion is derived during this literature-only turn.
SCOPE: The same conditional family and fixed forms as L168, general s,t and reduced finite W; test independence of mu_z, without actual section-quartic evaluation, a numerical exclusion or a new F-existence assumption.

The main gap remains primitive realization and F existence. The proposed
intermediate target asks whether the actual point weights have a common
value with the fixed choices. A positive or negative comparison would
settle whether L167's eventual quartic test must retain independent
point coefficients. This does not decide the actual section quadrics or
the complementary operation and is not a repetition of their failed
vanishing arguments.

Essential inputs are L111 and L168, retaining L109,L116,L164,L165 and
L071,L108,L115 through their conditional hypotheses. L167 is downstream
context, not a premise for the trace comparison. There is no
cross-notebook input. Retain identical marked K3 factors, their common
metric/triple/forms and actual connection; hypothetical locally free
rank-two product-polystable F, integral c_1=0 and full character
2-14e_1-21e_2-tau_D+62P; reduced finite W, DW=W^dagger[-2], actual
alpha,j,a,r,gamma, derived theta_z and fixed h_0. Use a single common
relative scalar kappa and the fixed base trace. No equality of weights,
numerical tau_z, generic section positions, F existence or integrability
is assumed. Empty and singleton Z must remain valid cases.

The specific source question is the regular-parameter generator
comparison for Ext^2_{O_{B,z}}(C,O_{B,z}), under the normalized finite
trace and trivialization of omega_B by sigma_B. L168 specifies the
resolution arrows defining epsilon_{x,y}; that orientation cannot be
replaced by a remembered analytic residue sign. Follow primary
regular-immersion duality or residue references from the already read
finite-duality framework. Retrieve the theorem hypotheses and relevant
orientation/proof case first; search for exact and stronger normalized
statements and known sign obstructions. Reuse the general duality
assessment rather than repeating it. No new theorem is derived here.

Continuation/abandonment test: approve a later specialization only when
the source identifies the generator and trace with enough precision to
compare the parameter dependence of tau_z(epsilon_{x,y}) and bar(c_0).
If it already proves the needed conclusion, import it with the necessary
applicability argument. If essential coverage is missing, name that
specific obstruction; do not set tau_z to 1 or infer constancy merely
from a common global scalar. A failed equality would retain the weighted
formula, not disprove F. Persistent source obstruction should park this
normalization target and route to a different independently testable
datum. No repeated L168 audit is proposed. ATTEMPTS/092–094 remain intact.

Full matching Mathlib coverage is unchecked. The proposal above records
the original question and test; the completed review below approves its
source coverage, without carrying out the new mathematics.

## Completed source comparison — step 560

LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED and
the preceding ready assessment expressly excluded analytic residue and
determinant-line normalization. The specific new lead is Nayak–Sastry's
explicit comparison with Verdier's isomorphism, not another audit of
L168's symbolic formula.

The source statements below are inspected inputs for a later proof.
Page numbers are printed pages in the two author PDFs, both dated
May 29, 2019. The arXiv identifiers locate the works, but no identity
between these author copies and every arXiv version is asserted.

### Primary generator and finite-trace comparison

S. Nayak and P. Sastry, *Grothendieck Duality and Transitivity I:
Formal Schemes*, [author PDF](https://www.cmi.ac.in/~pramath/mypapers/fub1.pdf)
(arXiv:1903.01779). Inspected:

- C.1–C.2, pp. 55–58: a regular sequence in a Noetherian ring gives
  the fundamental local isomorphism from the dual conormal determinant
  (tensored with coefficients) to top Ext. C.1 fixes the tensor-ordered
  Koszul complex and unsigned transpose convention; C.2.4 specifies
  the sign in its generator identification.
- C.5.3 and Lemma C.5.4 with proof, pp. 62–64: the two fraction
  conventions differ by (-1)^r; the fundamental local isomorphism
  followed by the natural Ext-to-local-cohomology map sends
  m tensor 1/t to [m/(t_1,...,t_r)].
- Theorem 5.3.8 and Proposition 5.4.4 with proofs, pp. 14–17:
  for a finite-type Cohen–Macaulay map of relative dimension r,
  a closed subscheme cut out by a quasi-regular sequence of length r
  and finite flat surjective over the base, this residue equals the
  finite trace after the fundamental local and transitivity maps.
  C.2.14–15 also tracks evaluation at 1.

### Primary regular-section residue normalization

The same authors, *Grothendieck Duality and Transitivity II: Traces
and Residues via Verdier's Isomorphism*,
[author PDF](https://www.cmi.ac.in/~pramath/mypapers/fub2.pdf)
(arXiv:1903.01783). Inspected:

- (4.1.2),(4.1.5), pp. 21–22: the Verdier residue agrees with the
  abstract residue under its canonical-bundle isomorphism, and with
  global trace after the support map when the morphism is proper.
- Sections 5.1–5.4 and Theorem 5.4.2, pp. 24–27: for a smooth
  separated morphism of relative dimension r and a closed section,
  the residue of [dt_1 wedge ... wedge dt_r/(t_1,...,t_r)] is 1.
  Remark 5.3.3 gives the coefficient-evaluation formula for a numerator
  f. Proposition 5.3.1 proves independence of the chosen parameters
  by completion; Proposition 5.2.3 proves the power-series case via
  projective-space trace. These proofs and Proposition 4.2.2's
  regular-section argument, pp. 22–23, were read.

The papers' cited older works were not independently opened; they are
references inside these inspected theorem proofs, not separately
verified literature. Lipman's fundamental-local-isomorphism lecture
notes and other search results were discovery leads only and are not
used as theorem inputs. The section-5 statements avoid relying on
the swapped affine-ring labels visible in II's Proposition 4.2.2.

### Applicability and the remaining specialization

Here B is a smooth projective complex surface, z is a C-rational
reduced closed point, and its ideal is generated by two regular
parameters. Work on a sufficiently small smooth affine neighbourhood
with this same closed point and then use the inspected support/open
compatibility (I, Remark 5.3.9, p. 16). The map {z} -> Spec C is the
identity, hence finite flat surjective. These verify the hypotheses
of the section and finite-trace sources; they do not require a split
point to have ordinary middle base change. Fixed sigma_B supplies
the canonical-bundle trivialization. Prior Stacks 0AX4/0DV0/0FVU
coverage supplies the already assessed composite-counit/global pairing
framework and is reused without renewed discovery.

The exact local computation is deliberately deferred. It must use
the resolution arrows in L168, not replace its generator with an
unoriented residue symbol. Track the tensor-Hom and shift comparison
against I, C.1–C.2, then the map of C.5.4; use the same fixed base
trace at every point. Express sigma_B in the chosen regular parameters
before comparing with L111's actual middle pairing. Retain the common
relative scalar kappa and distinguish any single global comparison
scalar for canonical-form conventions from independently chosen point
scalars. No numerical value of such a global scalar is needed merely
to test independence, but its commonness must be justified if used.
No trace has been set to 1 on L168's generator in this review.

The source theorem supplies a normalized residue, not a theorem about
the actual family F, its Kodaira–Spencer map or bracket. A later
specialization is needed precisely to connect these inspected standard
inputs to the two existing canonical formulas. Reproving general
duality or the regular-section residue formula is unnecessary and is
outside the approved work. No claim of novelty follows from this search.

Continue if that explicit comparison settles point-independence, with
any unavoidable common scalar stated. If a genuine mismatch is found,
preserve the weighted formula and record the precise failure; it is
not a disproof of F. Empty Z is vacuous, singleton Z supplies no
between-point comparison, and neither case may be discarded. This
approval adds no control of actual section quadrics, minimum square
length or the complementary operation and does not reopen
ATTEMPTS/092–094. It is source progress only. No essential primary
source for this bounded specialization remains blocked.

Access note: shell PDF download failed at DNS; web PDF text supplied
the theorem statements and relevant proofs. Some PDF screenshots
timed out or were unsupported; no unread image was used as evidence.
No local PDF was successfully downloaded. No mathematical script,
lemma, PROOF.md or DAG.md was changed by this review.
