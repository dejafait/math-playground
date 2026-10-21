# Relative local seven-divisibility: source assessment

TARGET: Certify the full local seven-divisibility congruence for Q=(1,0) relative to P=(0,0) on the conductor-389 curve using exact formal parameters.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped local searches of lemmas, literature assessments, relevant local histories and ATTEMPTS find P's certificate and L083's abstract quotient theorem but no explicit Q-relative residue; exact-curve logarithm/divisibility queries and the primary overlap checks below supply no matching inspected value.
SOURCE_EVIDENCE: Reuse the inspected Silverman (2009) III Algorithm 2.3 pp.53–54, VII Propositions 2.1–2.2 pp.188–191, IV Lemma 6.3(b)/Theorem 6.4 pp.131–132 and author errata from the ready 2026-10-18 known-point assessment; compare the complete relevant L081/L083 arguments and step-319 audit. Inspect Wuthrich (2006) Section 3 pp.3–5 and Section 4 opening p.5, author's publication-status entry, and Sage's logarithm algorithm/precision/exact-model examples on 2026-10-20.
COMPARISON: Known reduction, strict-radius logarithm and exact group-law results cover this unchanged curve and prime for any supplied rational point; audited L083 supplies full quotient generation by P. The missing difference is exact Q-specific scalar arithmetic and the resulting unique relative residue, not a new general local theorem.
GAP: No Q scalar coordinates, formal parameter, relative residue or explicit congruence is computed in this turn; a separate finite arithmetic certificate and full-group applicability proof are required. Nonzero global kernel membership remains independent.
REASON: The changed-point coverage gap is resolved by primary-source comparison and reuse; a single bounded known-method specialization is justified independently of the parked order chain, without claiming novelty.
SCOPE: Exact model [0,1,1,-2,0], Q=(1,0), P=(0,0), prime seven and depth one only; exact scalar/addition chains, projective reduction, formal-parameter valuations and full local quotient interpretation. No higher-depth lifting, new point search, saturation, descent enclosure or BSD implication.
LITERATURE_REASON: The saved changed-point target was REVIEW_REQUIRED; this turn compares its missing exact-arithmetic and full-quotient scope with existing ready primary coverage rather than repeating an assessment for an already approved target.

## Gap, relevance and duplicates

The main unresolved claim is rank E(Q)=m(E) for arbitrary analytic
order at least two. The intermediate target is a complete description
of which integer combinations aP+bQ belong to 7E(Q_7), through Q's
coordinate relative to P modulo seven. A concrete relative residue could
supply explicit rational representatives in the local Kummer kernel.
It would not show that a displayed representative is nonzero in the
global quotient, or supply a rational point of zero local logarithm.

L081 already certifies P's valuation-one witness; its separate audit
passes. L083 already proves generation of the entire local quotient by
P and split classical localization at every depth; its step-319 audit
passes. This target must compute the missing Q coordinate rather than
repeat either theorem. L034 supplies the published pair and independence,
with computational-source qualifications. The local calculation needs
only Q's exact membership on the curve, not a strengthened saturation
claim. A future global-nonzero claim would require separate justification.

The scoped duplicate search used `Q-relative`, `[13]Q`, and
`relative.*congruence|congruence.*relative` in lemmas, literature,
history and ATTEMPTS; the only prior relative proposal located was
history/371 and this assessment. The relevant P-local source notes,
L081/L083 proofs, step-319 history and ATTEMPTS/045 were inspected.
ATTEMPTS/041/042/044 and the step-371 stop remain preserved. In
particular the source-adaptation failure gives no arithmetic obstruction;
this target does not repair, retry or iterate the parked order route.
No global novelty or exhaustive absence conclusion follows from searches.

## Primary comparison and precise imports

Joseph H. Silverman, *The Arithmetic of Elliptic Curves*, second edition,
GTM 106, Springer (2009), DOI 10.1007/978-0-387-09494-6:

- [III Algorithm 2.3, pp.53–54](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=71) covers identity, inverse, chord and tangent branches on the general Weierstrass equation. Retain a_2=1 and a_3=1, prove every denominator nonzero where division is used, and certify scalar labels as well as curve membership. The prior assessment read the preceding intersection derivation and all branches.
- [VII Propositions 2.1–2.2, pp.188–191](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=204) assume a complete discretely valued field, perfect residue field and minimal integral equation. Good reduction identifies E_0 with the full group; the formal parameter on E_1 is t=-x/y. The prior assessment inspected reduction/Hensel proof cases and the complete parameter proof. The parameter at affine P or Q, each with y=0, is not an input.
- [IV Lemma 6.3(b) and Theorem 6.4, pp.131–132](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=150) apply to a formal group over the valuation ring of a characteristic-zero complete discretely valued field at integer radius r>v(p)/(p-1). Q_7 and radii one and two are unchanged; the same logarithm and its valuation estimate are used on both filtrations. Reuse the inspected statements and proofs, including both directions of the isomorphism.

The [author's errata dated 13 October 2022](https://www.math.brown.edu/johsilve/AEC/AECErrata.pdf), entries for pp.130–133 and 185–191, were inspected in the reused assessment. Its convergence qualification for IV.6.3(a) must persist; do not replace the strict-radius theorem with unrestricted integrality. No changed field, ramification, model or radius requires a fresh source theorem. Reuse `drafts/literature/2026-10-18-known-point-local-seven-test.md` for the full source/proof-case record, rather than claim fresh rereading of the book.

External queries on 2026-10-20 were `Wuthrich p-adic elliptic logarithms
389 7 (1,0) (0,0) lattice`, `"389a1" "log" "7" "(1" "(0"`,
and `"389a1" "local" "divisibility"`. Search-only results included
software examples and purported BSD arguments; none is imported as a
theorem or treated as an inspected competing proof.

Christian Wuthrich's [author text dated 26 April 2006](https://www.maths.nottingham.ac.uk/plp/pmzcw/download/logs.pdf), Section 3 pp.3–5, uses this exact curve and pair, gives a formal-subgroup basis at three and plots lattice minima including seven. The Section 4 opening discusses logarithmic linear forms. These inspected passages do not state Q's required residue. The [author's publications entry](https://www.maths.nottingham.ac.uk/plp/pmzcw/) describes this text as no longer intended for publication. Its asymptotic assertions and subsequent lattice theorems are not mathematical inputs here. The nearby error notice concerns a different paper; it is not attributed to this text.

The [Sage reference](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_point.html#sage.schemes.elliptic_curves.ell_point.EllipticCurvePoint_number_field.padic_elliptic_logarithm), algorithm/precision note and examples (HTML lines 3588–3629), multiplies into the formal group before evaluating. Its P example is at three; seven occurs in ratios for another point. The stated precision limitation prevents treating a default output as a certificate. No Sage computation was executed. Silverman's theorem, rather than software precision behavior, is the mathematical input.

## Approved next attempt and discriminating test

The saved target is unchanged. Perform one exact finite computation of
Q's coordinate in the depth-one local quotient, with no residue guessed
or built into the verifier. One sufficient certificate plan is:

1. Certify [13]Q by exact rational group law, with a distinct scalar-chain replay. Retain every branch, intermediate coordinate, curve identity and nonzero division denominator. Compare [13]P with L081's audited exact value.
2. For the seven candidates c=0,...,6, certify A_c=13Q-c(13P) by exact addition and a separate replay. Record primitive projective reduction and reduced numerator/denominator valuations of t(A_c), treating O separately with t(O)=0. Seek exactly one c with A_c=O or v_7(t(A_c))>=2; each other candidate must have valuation exactly one. This is an intended threshold, not an arithmetic result of this review.
3. Give the full-group interpretation using L081/L083's proved reduction-quotient comparison, equality [7]E_1=E_2 and invertibility of multiplication by 13 modulo seven. Use P's proved generation to justify uniqueness and the asserted condition for every aP+bQ. Do not replace the exact parameter tests with an unproved truncated-logarithm congruence. No general theorem reproof is needed.

The source theorem hypotheses do not depend on which rational point
is multiplied. L030/L033 supply the minimal good-reduction model and
complete reduction order 13; L081 supplies the fixed nonzero P input;
L083 supplies the quotient identification. These are the essential
local inputs; L034 is retained for the published pair/provenance and
possible later Kummer interpretation. L082 is already an input of
L083's Selmer conclusions, but Sha vanishing is unnecessary for the
local arithmetic test itself.

Continue only if the complete certificate meets the seven-candidate
threshold and the full-group proof. Stop and preserve the actual failure
if arithmetic replay, reduction, a source hypothesis or uniqueness fails;
do not change prime, depth, point or enlarge the task. Failure of a
candidate or implementation is not a rank or BSD counterexample.
Even success leaves global nonzero-class membership, uniform rational
witness production, all descent/order arithmetic and arbitrary-curve
complex-order/rank comparison unresolved. No lemma or mathematical
script is written in this literature-only turn.

## Mathlib

Full matching result and supporting exact Weierstrass, reduction,
strict-radius formal logarithm and Kummer coverage: not checked. No
absence is inferred. The proposed calculation is reproduction of known
methods; the searches do not certify originality.
