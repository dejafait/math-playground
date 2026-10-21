# Auxiliary native Legendre field prescription — source scope approved

TARGET: Determine whether L074 excludes F_aux=T(sqrt(-1),E_L[15]) for every number field T contained in F_aux and every Legendre descent E_L/T of E_aux.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step293 searched geometric Legendre isomorphism, six parameters and coordinate converses; reused step272/276/289 searches and compared L074, history/292, foundations/05 step272 and ATTEMPTS/033. The arbitrary-descent exclusion is not a duplicate of the six-row test; no novelty claim follows.
SOURCE_EVIDENCE: Reopened Milne (2021) II Theorem 2.4(b) pp.52–53, supporting Theorem 2.1(b) pp.50–51 and Proposition 1.5 p.49; Auer–Top (2002) Introduction p.303, Lemma 2.2 proof pp.304–305 and general-field six-parameter paragraph p.305. Reuse inspected IUT IV Proposition 1.8(i)-(iv),(vi) pp.18–21, Theorem 1.10 p.22 and Corollary 2.2 pp.41–42 from step272; current detailed endpoint retrieval failed, and byte identity remains unverified.
COMPARISON: The converse pointed-coordinate theorem and general-field geometric parameter criterion cover arbitrary literal Legendre descents without assuming rational torsion on a second model. The separate application must match their parameter orbit to L074's rows over the fixed F_aux and check the full-coordinate field predicate.
GAP: No auxiliary native-field exclusion is proved here; the witness-specific exhaustion/base-change argument and its torsion-field consequence remain mathematical work. Actual native T/model identification and independent initial data remain outside this coverage.
REASON: This changed-quantifier source comparison supplies the missing coverage for a separate known-method application; it neither reapproves L074's proof nor reopens parked classification access.
SCOPE: One unchanged L073 auxiliary witness and its F_aux in the fixed Q-bar; arbitrary number field T contained in F_aux and E_L/T given by y^2=x(x-1)(x-lambda), geometrically pointed isomorphic to E_aux. No field enlargement, reselection, retained-witness conclusion or universal IUT flaw claim.

## Exact continuation and approved source scope

Step293's complete comparison is saved in
`drafts/2026-10-18-auxiliary-native-legendre-source-comparison.md`.
It approves source coverage for TARGET, not its mathematical conclusion.
The completed literature step derives no new result and changes no
lemma or mathematical script. The later application is REPRODUCTION.

Essential mathematical inputs are L073 and the separately audited L074;
L048 supplies the already checked nonexceptional-j hypothesis through
those results. The existing native source record is
`foundations/05-native-input-tensor-placement.md`, step272. Preserve its
April 2020 version convention and lack of a byte-identity check. The
conditional T here is not an identification of the actual F_tpd.

The reused primary source locations are
[IUT IV](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf),
Proposition 1.8, Theorem 1.10 and Corollary 2.2 at the pages above;
[Milne, second edition](https://www.jmilne.org/math/Books/EC2.pdf),
II Theorem 2.4(b); and
[Auer–Top](https://pure.rug.nl/ws/portalfiles/portal/14410242/2002JNumberThAuer.pdf),
pp.303–305. Step293 reopened the Milne converse and supporting proof
and the general-field parameter discussion in Auer–Top; no finite-field
proposition is imported. The later application must not assume the
desired exhaustion from the phrase "six models" or from equality of j
alone. Do not assume
full rational 15-torsion on a second descent when invoking a theorem
that requires it on both.

The main gap is still finite B>=A. A possible downstream use is an
admissibility screen: the test could show that this auxiliary witness
cannot meet the native field prescription, forcing a different initial
data construction, or could expose a missing model outside the six-row
test. Either result would concern this witness, not a flaw in IUT.
The exact stated descent category and field predicate now have source
coverage. A mathematical application must separately check all
hypotheses and the original full-coordinate field convention. Continue
only if its parameter-to-row and base-change checks succeed; otherwise
record the specific obstruction and abandon that reduction rather than
silently enlarge the model category. No such application is made here.

Unresolved assumptions include the actual native T/model, exact
generation, retained scalar occurrence and memberships, independent
initial data, source-marked all-image factorization, pilot transport,
essentiality and the original finite B>=A inference. Equal auxiliary
and retained completions identify neither global fields nor parameters.
Keep ATTEMPTS/027,028,031,032,033 and all retained data unchanged.
Full matching and supporting Mathlib coverage is unchecked. This file
approves the saved target's source scope after a separate literature
review; it neither derives its exclusion nor claims mathematics beyond
the sources. The exact Next action is unchanged.
