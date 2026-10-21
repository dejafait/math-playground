# Complete ramified dyadic certificate — audit source approval

TARGET: Critically audit L078–L081's complete ramified dyadic Kummer-image certificate, including arithmetic, parameter coverage, realizations and fixed-label comparisons.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready ramified local-image assessment; compared L078–L081's stated methods and the recorded L080 coordinate gap, L081 replacement chart and ATTEMPTS/034–036; bounded exact-field/parameter searches found no usable additional classification.
SOURCE_EVIDENCE: Reused Bruin–Stoll's 14 March 2008 manuscript, Remark 2.1 and Section 4 pp.6–10, and BPT arXiv:2001.02263v3 Section 1, especially Lemma 1.3 p.4; additionally inspected Clark's 161-page author notes, Corollary 1.77/Theorem 1.79 pp.57–58 and Theorem 2.8/Proposition 2.9/Corollary 2.10 pp.64–65.
COMPARISON: The sources cover the general Kummer map, ramified dyadic constancy method, maximal-ring construction, root realization/error estimates and abstract image size; they do not certify these explicit generator maps, labels, disks, comparisons or software. The parameter chart can be audited by its explicit polynomial and Hensel lifting without assuming a literal LocalImage trace.
GAP: Method coverage for the exact audit is ready; independent mathematical and full-evidence verification of L078–L081 remains undone. No global independence, filtered dimension improvement, class-kernel value, rank or integer conclusion is supplied.
REASON: Specialize the inspected general results only as audit inputs; independently check the existing field/model identities, digit induction, strict precision inequalities, exhaustive charts, exact realizations and complete recorded comparisons. Do not reprove general descent theory or enlarge the target.
SCOPE: Independent critical audit of the existing complete local certificate over H=Q2(pi), pi^11=2, with its fixed theta and entire degree-33 J; includes the implicit parameter chart and overlapping standard reciprocal chart, but excludes new global pruning and a claim that the source disk tree was executed.
LITERATURE_REASON: This is the separately requested approval of a newly proposed audit scope. Its implicit parameter chart and inherited maximal-ring/precision obligations needed explicit theorem-level comparison beyond the construction assessment; the unchanged Kummer and local-image coverage is reused.

## Relevance and bounded decision

The main gap is primitive integer emptiness, including the surviving
ordered (3,4,11) branch. The intermediate target is the exact audit in
TARGET. A reliable local membership test could later filter actual
supported global classes. L077's current unit upper bound fourteen
still exceeds the desired eleven, and the localized class contribution
is unknown. Auditing the local list alone changes neither quantity.

Continue with one independent mathematical audit if the named sources
cover all general inputs. This review finds that they do. In that audit,
accept claims only after checking their proofs and complete load-bearing
evidence; correct or isolate a precise failure. Stop an unsupported
assembly rather than using successful shared-code replay as independent
verification. An uncovered new mechanism would require its own review.
This approves the audit, not its mathematical conclusions.

## Reused primary coverage and exact applicability

The already ready
[construction assessment](2026-10-16-ramified-dyadic-two-descent-image.md)
records the primary statements and complete relevant proof cases, and
is reused without new retrieval of unchanged passages:

- N. Bruin and M. Stoll, *Two-cover descent on hyperelliptic curves*,
  Math. Comp. **78** (2009), 2347–2370,
  [DOI](https://doi.org/10.1090/S0025-5718-09-02255-8);
  [author manuscript, 14 March 2008](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
  Remark 2.1 p.3 and Section 4 pp.6–10. The local algorithm assumes a
  characteristic-zero complete discretely valued field with finite
  residue field and a square-free integral polynomial with its full
  factorization; it permits ramified dyadic bases. Odd degree has no
  scalar quotient. Lemma 4.4 and its proof supply the strict square
  neighborhood; SquareClasses/LocalImage include feasibility, linear
  roots, infinity and reciprocal values. Its odd-residue shortcut is
  inapplicable. The audit must use the actual normalized valuations.
- D. Barrera Salazar, A. Pacetti and G. Tornaría, *On 2-Selmer groups
  and quadratic twists of elliptic curves*, Math. Res. Lett. **28**
  (2021), 1633–1659,
  [DOI](https://doi.org/10.4310/MRL.2021.v28.n6.a1);
  [arXiv:2001.02263v3, 17 September 2020](https://arxiv.org/pdf/2001.02263v3),
  Section 1 pp.3–4. Lemma 1.3 gives
  |E(F)/2E(F)|=[O_F:2O_F]|E(F)[2]| for finite F/Q_p. It is an imported
  standard result, not an independent rerun of its cited Brumer–Kramer
  proof. For the audit it checks abstract completeness only after
  genuine point images and inequivalence have been verified. The
  separate unramified-base good-reduction clause is unnecessary here.

The fixed E0 and monic cubic are exactly those covered in that
assessment. The full-field assertion, nonsingularity, degree and fixed
coordinate maps are existing local inputs to verify, not consequences
of an image count. Simon's Section 1.1, Propositions 1.1–1.2, p.8,
[DOI](https://doi.org/10.1112/S1461157000000668), is the previously
assessed equivalent monic-cubic interface; BPT already supplies the
needed map, so no additional Simon retrieval is essential.

## Added explicit source checks

Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields
and Adeles*, [161-page author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
accessed 2026-10-16 (no dated revision identified). Inspected the
following statements, the Eisenstein proof, and Proposition 2.9's proof:

- Theorem 2.8, Proposition 2.9 and Corollary 2.10, printed pp.64–65:
  for a DVR R and monic f with nonleading coefficients in its maximal
  ideal and constant coefficient outside its square, R[T]/(f) is the
  integral closure, a DVR with uniformizer T and unchanged residue field.
- Corollary 1.77 and Theorem 1.79, printed pp.57–58: for complete
  nonarchimedean K, f in O_K[T], and integral a with
  |f(a)|<|f'(a)|², there is a unique root b with
  |b-a|<|f'(a)|; moreover |b-a|=|f(a)/f'(a)| and
  |f'(b)|=|f'(a)|. Simple residue roots lift. The latter theorem is
  stated without proof there; use the standard named Hensel theorem.

These cover the types of imports used in L078 and L081, conditional on
checking their coefficients and residual inequalities. No formal-group
convergence theorem is required by the written implicit-polynomial
argument. This comparison does not verify that argument's identities,
converse coverage or numerical error bounds.

## What the independent audit must decide

Retain the exact local inputs: L033's E0, L046's H, L069's
X=4x,Y=8y+4, L071's generator, L076's entire compositum, and L078's
fixed theta. Review the needed input proofs narrowly where the
certificate relies on them. No cross-notebook input is authorized or
needed. L074/L075 provide downstream context, not premises for a local
image equality; L077's global restrictions must not be assumed improved.

The remaining checks are specialization/reproduction obligations:

1. L078: verify the mutually inverse field maps, Eisenstein/maximal-ring
   hypotheses, complete basis valuation formula, exact quotient-ring
   operations, digit-66 boundary, generating and independent square
   labels, inverses and fixed-element comparisons. A polynomial order
   without maximality cannot justify labels.
2. L079: verify point existence on every original-integral-x disk,
   fixed-theta evaluation, normalization before reduction, precision,
   every inequivalent label and representative, and the cardinality
   theorem's application. Image size cannot certify unverified images.
3. L080: verify its entire reciprocal feasible/rejected partition,
   realizations, infinity and collisions. Its original-x coverage ends
   at the recorded coordinate gap; retain that correction rather than
   silently identifying x with X.
4. L081: verify the implicit equation, existence/uniqueness for every
   parameter, converse negative-x coverage, zero parameter/O,
   normalization and all strict relative error inequalities. Check
   every stored root residual, unit derivative, class reconstruction,
   affine match and complete coverage/collision data. Its advertised
   minimum 67 must exceed the required 66 after all divisions; those
   values remain unaudited claims here.

Inspect the complete relevant certificates in the later audit, not just
summaries or samples. Replaying a verifier sharing arithmetic with the
constructor is supporting evidence and does not independently validate
that arithmetic. Full point coverage by the parameter chart is a valid
mathematical target distinct from executing the literal cubic-X tree;
no source citation changes that distinction. The present turn ran no
mathematical script and verified no certificate records.

## Search, duplicates, failures and qualifications

This turn searched `"Two-cover descent" "parameter" "LocalImage"` and
`"11a1" "2^(1/11)" Kummer image`. Returned results did not supply a
usable exact-field classification or an audit of this certificate;
irrelevant hits are not evidence of novelty. General and stronger
method comparisons from the construction assessment remain adequate.
The explicit Hensel statement removes any need to pursue an unread
formal-group lead for the written proof. Optional Magma documentation
and Brumer–Kramer's original proof remain uninspected, nonessential
leads; no backend or service is assumed.

The targeted histories 258–259 distinguish the already repaired
coverage gap from the pending critical audit. L079 already claims
abstract full-image equality, so L080/L081's coverage cannot be counted
as a new independent global restriction. ATTEMPTS/034–036 preserve the
exhausted affine, quotient and fixed-ideal searches; this review does
not reopen them. There is no duplicate completed independent audit in
the checked local records.

Mathlib matching and supporting coverage for this exact certificate:
**not checked**, with no absence claim. Canonical mathematical proofs
and their existing citations remain in L078–L081. No lemma, mathematical
script, DAG edge or assembled argument is changed. This is source-scope
approval/local documentation progress, not a mathematical discovery or
completion of the audit. The next action remains exactly TARGET.
