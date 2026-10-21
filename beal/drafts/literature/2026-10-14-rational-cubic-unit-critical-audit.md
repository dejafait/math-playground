# Rational cubic unit witness — critical-audit source coverage

TARGET: Critically audit L071's exact norm-one unit transport and complete rational dyadic nonmembership certificate.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-statement/stronger-result search in the prior rational-cubic-unit-dyadic-pruning assessment; compared L071 with L069/L070, histories 221–222 and ATTEMPTS/032; performed targeted primary-statement lookup for Clark, BPT and Stacks without repeating broad discovery.
SOURCE_EVIDENCE: Simon 2002 Section 1.1 Propositions 1.1–1.2 p.8 reused; BPT arXiv:2001.02263v3 Section 1 p.3 and Lemma 1.3/Remark 1.4 p.4 reinspected, with L070's Theorems 1.8/1.11 coverage reused; Clark 161-page author notes Theorem 2.8 and Proposition 2.9/Corollary 2.10 pp.64–65 statement and relevant proof read; Stacks Lemma 31.18.6 tag 0BD2 statement and entire proof read.
COMPARISON: The inspected named results cover full Kummer evaluation/cardinality, maximal Eisenstein local rings and norm base change; none certifies L071's particular coordinate identities or square obstructions. A positive witness does not require fundamental-unit completeness.
GAP: Essential source coverage for this audit is ready; independent arithmetic, point realization, entire-algebra transport and arbitrary-coordinate nonmembership verification remain research obligations, with no audit verdict supplied here.
REASON: Approve a delimited critical audit by applying known results and independently checking the existing certificate, without new unit discovery, an index reproof or a global rank claim.
SCOPE: Only L071's stated norm-one unit exclusion, its complete rational dyadic nonmembership certificate and the exact applications of L033/L046/L069/L070 needed for that exclusion.
LITERATURE_REASON: The separately saved audit scope was REVIEW_REQUIRED; its maximal-ring citation and full-image-versus-sampled-image comparison needed explicit primary-source approval beyond the ready witness-search assessment.

Essential local inputs are L033, L046, L069 and L070. The approved
audit is of L071 alone and its certificate
`scripts/rational-cubic-unit/witness-certificate.json`, with the
saved prior assessment
`drafts/literature/2026-10-14-rational-cubic-unit-dyadic-pruning.md`.
No cross-notebook input, new unit search, degree-36 class computation,
or independent rank assertion is proposed.

The main gap is primitive integer emptiness across the residual Beal
signatures. The intermediate target is independent certification of
one actual global unit direction removed by the rational dyadic test.
Its plausible downstream use is finite-local pruning of the global
two-descent upper space; that use still needs full unit/class coverage
and a dimension computation. The exact positive witness threshold is
one unit in V outside H, not all norm-one unit classes.

Check the generator identities, inverse,
integrality, norm base change, entire Eisenstein Q2 field and maximal
ring, actual local two-torsion, size-two Kummer image, the realized
point at X=5, and nonsquareness of u,h,uh. In particular review the
two-adic root construction and coefficient obstruction for arbitrary
Z2 coordinates. Check that the same rational place maps D into the
entire local field, so the witness is not lost as a square in D.

The previous hand-entered product coefficient error was corrected
before completion and is disclosed in L071. Mathematical correctness
of the final value, not merely the certificate success flag, needs
independent review. The full filtered ambient space, rank bound and
primitive integer emptiness remain unresolved even if the audit passes.
Mathlib matching/supporting coverage remains not checked.

## Primary results and precise scope

Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields and
Adeles*, [author PDF](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
161 pages accessed 2026-10-14; no revision date identified. Theorem 2.8,
printed p.64, requires a prime ideal, leading coefficient outside it,
lower coefficients inside it and constant coefficient outside its square;
its fraction-field conclusion uses a GCD domain. Proposition 2.9 and
Corollary 2.10, p.65, for a monic Eisenstein polynomial over a DVR,
identify the quotient as a DVR with root uniformizer, unchanged residue
field and as the integral closure in the root field. Read the theorem
proof and the complete proposition proof; the corollary is stated as an
exercise. This covers the maximal LOCAL ring invoked by L071. The audit
must verify the translated polynomial and coefficients and identify the
entire cubic algebra. No global maximality of Z[t] follows or is needed.
These general results are imported, not reproved.

Daniel Barrera Salazar, Ariel Pacetti and Gonzalo Tornaría, *On 2-Selmer
groups and quadratic twists of elliptic curves*,
[arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3), 17 September 2020;
published Math. Res. Lett. **28** (2021), 1633–1659,
[DOI](https://doi.org/10.4310/MRL.2021.v28.n6.a1).
Section 1, printed p.3, uses a monic square-free cubic over a field of
characteristic different from two, with the entire cubic algebra and no
scalar quotient. It identifies the full abstract Kummer map and the
nonexceptional evaluation x−T. Section 1.2, p.4, assumes a finite
extension B/Qp. Lemma 1.3 gives full image order
[O_B:2O_B] times |E(B)[2]|, referring to Brumer–Kramer Lemma 3.1 for
its proof; Remark 1.4 uses maximal rings of all algebra factors.
Use B=Q2, not the cubic coefficient field. This cardinality includes
exceptional points. Audit completeness by matching an independently
verified subgroup to that order and checking all local two-torsion.
The prior L070 application of Definition 1.6(iv), Theorem 1.8 and the
first assertion of Theorem 1.11 is reused. Its unramified-base/good-curve
reduction hypotheses concern the original elliptic curve, not smooth
reduction of the changed integral cubic model. No global hypotheses,
separate U4 equality or image enumeration are imported.

Denis Simon, *Computing the rank of elliptic curves over number fields*,
LMS J. Comput. Math. **5** (2002), 7–17,
[DOI](https://doi.org/10.1112/S1461157000000668), Section 1.1,
Propositions 1.1–1.2, printed p.8. Reuse the prior inspected statement
and monic integral irreducible-cubic scope for the Kummer homomorphism,
kernel and norm-square target. BPT's inspected full-algebra formulation
also covers the local evaluation used here. Neither source supplies
the particular unit or its local square comparison.

[Stacks Project, Lemma 31.18.6, tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2),
accessed 2026-10-14, assumes a finite locally free morphism of constant
degree at least one and gives a canonical norm commuting with arbitrary
base change. Its full proof defines the norm by the multiplication
determinant, checks independence of basis and base-change compatibility.
Audit applicability to the same entire rank-three algebra under Q -> K
and K -> Q2; do not replace it by a selected factor or merely a norm
computed in a different cubic presentation.

## Reuse, duplicates and recorded failures

The prior assessment's exact-cubic queries, stronger-result comparison
and Bruin–Stoll full dyadic image algorithm remain adequate for the
unchanged witness mathematics. No new broad searches were needed.
Li's square-free-discriminant Selmer result remains inapplicable;
its smaller-field example is only a lead and supplies no coordinate
isomorphism or local nonmembership theorem. Chung–Li's quadratic-twist
example does not decide this unit test. PARI completeness methods are
unnecessary for the claimed positive witness; absence of a gp backend
is not a source blocker for this audit. These assessments are reused,
not represented as newly inspected stronger conclusions.

L070 alone gives a local index, not a global unit exclusion. L071 is
the result to audit, not an independent premise validating itself.
Histories 221–222 record the source gate and completed witness attempt;
ATTEMPTS/032 parks only the unfiltered ambient bound. It does not ban
testing a genuine local cut. The corrected product coefficient disclosed
in L071 must be recomputed from the final expressions. Checking only
the certificate's success flag or a bounded preview would not suffice.

## Authorized research and continuation test

The next invocation may independently replay the exact certificate and
audit its full load-bearing fields, together with the written arbitrary
Z2-coordinate proof. Verify integral unit/inverse transport, determinant
norm and base change, the maximal local ring, complete local two-torsion,
the actual dyadic point, full-image cardinality, and all three square
comparisons. Justify that the fixed rational place preserves the same
generator and proves nonsquareness in D; subfield nonsquareness alone
does not survive an even-degree extension automatically. A finite
nonmembership obstruction is sufficient only after the full ring and
all possible roots have been covered. An audit rechecks the existing
specialization for correctness; it does not reprove the named general
theorems or initiate a new unit search.

Accept L071 only if these checks certify one genuine class of V outside
the complete H. Any defect requires repair or a precise limitation of
the witness claim while preserving the original work. A failed check
does not refute Beal or justify a rank claim. Full filtered dimension,
other places, units/S-units and ideal-class contributions, rank, indices,
cosets and primitive integer lifting remain independent unresolved gaps.
No new lemma or mathematical script was written or executed in this
literature review. No mathematical audit verdict or novelty claim is made.
