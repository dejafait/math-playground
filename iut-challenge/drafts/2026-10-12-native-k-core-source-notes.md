# Native K-core source review — unfinished extraction

The authorized step is literature-only. The main gap remains finite B>=A;
no K-core assertion for the retained curve is derived here.

Recovered primary lead: Mochizuki, *The Absolute Anabelian Geometry of
Canonical Curves*, author PDF `Canonical Liftings.pdf`, 34 pages,
Definition 2.1/Remark 2.1.1, Proposition 2.3 and Definition 2.6/Proposition
2.7. The last result treats exactly punctured hemi-elliptic orbicurves,
reducing coricity to avoidance of four arithmetic classes. Its proof's
Riemann–Hurwitz and triangle cases have been inspected. Need finish the
categorical notation/base-change proof and retrieve explicit exceptions
from Takeuchi/Sijsling before approving a numerical applicability test.

IUT I Definition 3.1(d) concerns C_K=[X_K/{±1}], not terminality of X_K.
Retain the previously qualified May 2020 reproduction. L048's existing
proof supplies v_3(j(E_0))=-30; only later research may compare that input
with an inspected exceptional-value list. No coefficients are to be
reselected and no auxiliary field is to be enlarged.

Uninspected lead: Sijsling, *Canonical models of arithmetic (1;infinity)
curves*, 2019, DOI 10.1090/conm/722/14530. Minamide's slides quote four
j-values, but those excerpts alone are not adequate primary coverage.

## Completed primary extraction

The initial paragraph above is the preserved unfinished checkpoint;
coverage below completes its defining-source and exception-list tasks.
No mathematical application to E_0 is performed.

### Defining category and criterion

Mochizuki, *The Absolute Anabelian Geometry of Canonical Curves*,
Documenta Mathematica, Extra Volume (2003), pp.609–640;
[author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Canonical%20Liftings.pdf),
34 pages, inspected printed pp.8–11,14–15. These are author-PDF page
numbers, not the 32-page journal pagination. No revision date or byte
identity with the journal file is asserted.

Section 2 defines Loc(X) using finite-etale covers, with arrows not
necessarily over X; overline-Loc(X) additionally allows their finite-etale
stack quotients. Definition 2.1/Remark 2.1.1 defines a k-core as X being
terminal in overline-Loc_k(X), with k-morphisms throughout.

Proposition 2.3(i) assumes geometrically normal, geometrically connected,
finite-type X/k: coricity is equivalent after separable closure.
Part (ii) assumes a hyperbolic orbicurve over algebraically closed
characteristic-zero k, and preserves coricity after an algebraically
closed field extension. Its proof uses finite-etale-cover invariance,
isomorphism rigidity and tame compactification.

Definition 2.6(ii) is exactly [ (E minus origin)/{±1} ]. Proposition 2.7
assumes algebraically closed characteristic-zero k and this orbicurve:
non-k-arithmetic implies k-core; exactly four arithmetic classes occur.
Its complete proof checks (2,2,2,2), (2,3,6), (2,4,4), (3,3,3) branch
cases: the first yields the core; the others yield arithmetic triangle
covers, contradicting non-arithmeticity. These are cited inputs, not
reproved here.

### Explicit arithmetic exceptions

Sijsling, *Canonical models of arithmetic (1;infinity)-curves*,
[arXiv:1707.01158v2](https://arxiv.org/pdf/1707.01158v2), submitted
6 July 2017; PDF dated July 7, 2017, 19 pages. Read introduction
pp.1–3, Lemma 1.1.1/Table 1 pp.3–4, section 3.1 pp.10–11 and
[Table 4 in experimental HTML](https://arxiv.org/html/1707.01158v2#S3.SS1).
The HTML displays a generated 2026 date; retain the versioned PDF's
2017 date, not an inferred theorem revision.

The four arithmetic groups of signature (1;infinity) exhaust the list.
Table 4 gives their pointed genus-one models, cusp at infinity:

| Case | Model | j-invariant |
| --- | --- | --- |
| I | y^2=x^3-44x^2-16x | 2^14 * 31^3 / 5^3 |
| II | y^2=x^3-4x^2-384x-2304 | 2^2 * 73^3 / 3^4 |
| III | y^2=x(x^2-256) | 1728 |
| IV | y^2=x^3-1728 | 0 |

Section 3.1 distinguishes intermediate covers/isogenies from the final
X(Gamma), including case III's intermediate Q(i)-model. Use the final
table, not an intermediate isogenous curve. PDF extraction flattened
exponents; HTML confirms their exact grouping. Models/classification
are imported, not reproduced by numerical Belyi computation. Neither
the Magma implementation nor all of sections 1,2,3.2,4 were audited.

Takeuchi, *Arithmetic Fuchsian groups with signature (1;e)*,
J. Math. Soc. Japan 35(3) (1983), pp.381–407,
[DOI/publisher](https://doi.org/10.2969/jmsj/03530381), is the reference
in CanLift Proposition 2.7 (Theorem 4.1(i)) and Sijsling Lemma 1.1.1
(Proposition 3.1/Theorem 3.4). The publisher PDF eventually supplied
27-page metadata; subsequent statement extraction failed. No direct
Takeuchi theorem/proof inspection is claimed. CanLift and Sijsling
already supply the matching statements and complete exception table;
Takeuchi's unread proof is not an essential missing hypothesis for
importing those two results. Minamide's slides were search leads only.

### Native object and applicability obligations

Reuse the native source/version qualification from
`drafts/literature/2026-10-12-native-selected-place-model-comparison.md`.
Read the full May 2020 IUT I Definition 3.1(c,d), reproduced printed
p.62 [here](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf#page=62).
The unadorned C_K=C_F times_F K is the specified core, distinct from
its level-l covering orbicurve. K is the full l-division field.

A future application should retain l=7 and K=D=F(E_0[7]), already
present in L045/L048. It must check the characteristic-zero orbicurve
hypotheses, use the classification to exclude arithmeticity of the
same punctured elliptic curve, preserve it under its finite-etale
quotient, apply Proposition 2.7 to the quotient, and transfer via
Proposition 2.3 to the actual number field. Categorical arithmeticity
must not be replaced by rationality of coefficients or non-CM alone.
If needed, cite CanLift's defining category and Remarks 2.1.2,2.1.3
for the common-cover/category identification, rather than asserting
an ordinary coarse-space etale map. The quoted classification and
criterion suffice for this routine specialization; no new universal
criterion or classification reproof is proposed.

L048, section “The changed curve's geometric parameter”, explicitly
supplies v_3(j(E_0))=-30. A separate application can compare it with
all four exact values above; this review performs no such comparison
or K-core conclusion. No exact q_0, effective coefficient tuple or
new curve selection is needed as a source hypothesis.

The downstream use is one native initial-data prerequisite. Covering,
cusp, complete selected places, actual inputs/actions, pilot,
essentiality and finite B>=A remain separate. L051 is a reduction
input only, L049 background, L050 a different predicate, and the
recorded packet stops remain preserved. Full matching Mathlib
coverage is unchecked; no absence claim is made.

### Retrieval record

Queries included exact `Mochizuki K-core`, `K-coric`, `Canonical Curves
core`, `punctured hemi-elliptic j arithmetic`, `K-core j-invariant`,
`Sijsling arithmetic punctured`, and the exact Sijsling title on arXiv.
Scoped duplicate/failure checks used the native selected-place assessment,
foundations/02, history/167 and the packet-field-role assessment; their
K-core gap was explicit. Only L045's hypotheses/conclusion and L048's
relevant existing proof were loaded for retained-data comparison.

Author CanLift text was accessible through the web tool. Direct shell
curl to arXiv failed DNS; no downloaded PDF was inspected. Web screenshots
returned references without visible image data, so no visual inspection
is claimed. Readable PDF text and Sijsling's HTML supplied the necessary
statements/cases/notation; the latter also identifies overline-Loc.
The journal CanLift file and EtTh PDF were accessed as secondary
reference endpoints but did not supply usable defining passages.
The existing native reproduction/byte-identity qualification remains.
