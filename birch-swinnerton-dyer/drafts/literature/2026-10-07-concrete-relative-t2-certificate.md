# Concrete full-relative T_2 certificate — construction source assessment

TARGET: Construct and verify a full-relative Manin, geometric-reflection and T_2 dual-kernel certificate for E: y^2+y=x^3+x^2-2x, testing L029's dimension-one threshold with independently certified conductor and eigenvalue data.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Checked L029's exact hypotheses, ATTEMPTS/022--023 and the earlier presentation/operator assessments; searched the specified curve and Stein's complete Manin and good-prime algorithms; inspected the primary passages below, not just search snippets.
SOURCE_EVIDENCE: LMFDB 389.a1 equation/invariants/local data/q-expansion; Stein weight-two Proposition 3.10, Proposition 3.11 with both proofs, Theorem 3.13 and Proposition 3.17; Stein general symbols equations (4)--(5) and their full n=2 example; Cremona corrected second edition Sections 3.1--3.2 and 3.9; BCDT Theorem A and Introduction's conductor-level characterization; retrieved 2026-10-07, with L029's existing adjointness/sign coverage reused.
COMPARISON: Standard results cover the complete relative presentation, oriented path reduction and good-prime operator construction; the remaining work is exact implementation and independent checking for this equation, not a new Manin, modularity or multiplicity theorem. No inspected source supplies the requested complete instance certificate or promises that T_2 alone has dimension-one kernel.
GAP: Produce independently checked curve invariants/local conductor and a_2, complete relation saturation and all generator coordinates, geometric path/operator witnesses and exact simultaneous dual-kernel rank; dimension one remains an untested threshold.
REASON: Coverage is ready for one known-source specialization using direct endpoint reduction and exact linear algebra; a citation alone cannot provide this instance's matrices or rank evidence, and no reproof of the source theorems is justified.
LITERATURE_REASON: Changed target from conditional full-relative kernel sufficiency to actual complete presentation and operator evidence for one specified curve; essential curve and construction coverage is unread.

SCOPE: Only the saved equation's full relative Manin presentation, geometric reflection and good-prime T_2 certificate, with independent arithmetic checks; no additional operators, coefficient computation, normalization or uniform termination.

## Primary sources and comparison

[LMFDB 389.a1](https://www.lmfdb.org/EllipticCurve/Q/389/a/1),
release 1.2.1 (page reports SageMath 10.5), matches the exact equation and
lists a minimal model, conductor and discriminant 389, no CM, local type
I_1 at 389, and q-expansion beginning q-2q^2-2q^3. These are reference
values, not an independently emitted certificate. Its separate linked
modular-form page returned CAPTCHA; that page was not inspected. Neither
rank nor numerical BSD data is used. No stored Manin matrices were read.

[Stein, online v0.1, Modular Forms of Weight 2](https://wstein.org/books/modform/modform/weight_two.html):
Proposition 3.10 identifies cosets by projective bottom rows. Proposition
3.11 reduces arbitrary oriented cusp paths integrally using convergents;
both its continued-fraction proof and denominator-induction proof were
read, including infinity and the initial formal convergents. Theorem 3.13
gives the complete two/three-term presentation modulo torsion, mapping
[g] to g{0,infinity}. It cites Manin (1972), Section 1.7 for injectivity,
omitted from Stein's proof; import the theorem, not just its proved
surjectivity. The relative interpretation is stated before Theorem 3.7;
that numbered theorem itself concerns the absolute boundary kernel.
Algorithm 3.16/Proposition 3.17 provide a faster good-prime alternative.
Do not confuse all relations with relations only on surviving generators.

[Stein, General Modular Symbols](https://wstein.org/books/modform/modform/modular_symbols.html):
read condition C_n, equations (4)--(5), and the complete determinant-two
example checking each of its three matrix cosets. This provides an
alternative Hecke construction. Reuse the prior assessment's inspected
equations (11)--(12), Remark 1.43 and path adjointness for the geometric
sign and full-relative action. Direct endpoint reduction avoids needing
to re-establish the general Heilbronn construction. No library sign label
is substituted for the reflected endpoints.

[Cremona, corrected second edition (1997), Chapter 3](https://johncremona.github.io/book/fulltext/chapter3.pdf):
read Section 3.1 invariant/change-of-model formulas, Section 3.2
minimal-model algorithm and Tate algorithm through its good and
multiplicative branches, printed pp. 62--67. For a minimal integral
equation the conductor exponent is zero when p does not divide Delta,
and one when p divides Delta but not c4. The multiplicative exit is
explicit in algorithm lines 19--22. Section 3.9, p. 103, lists all rational
CM j-invariants and explains the class-number restriction. These permit
independent minimality, conductor and non-CM checks; none was executed
here. Do not assume minimality from a software model label.

[Breuil--Conrad--Diamond--Taylor, *On the modularity of elliptic curves
over Q: wild 3-adic exercises*, JAMS 14 (2001), 843--939, Theorem A](https://virtualmath1.stanford.edu/~rltaylor/st.pdf):
read the author-hosted prepublication PDF's Introduction, pp. 1--3,
including the equivalent conductor-level weight-two L-function statement.
Import the standard modularity/newform correspondence for E/Q. Once the
equation and conductor are independently checked, its associated
normalized rational newform has good-prime coefficients determined by
point counts. Thus the inaccessible database newform label is not an
essential input to L029; identifying a label or matching only finitely
many coefficients is not a substitute for this theorem.

## Approved instance work and evidence contract

The future step may verify invariants from [0,1,1,-2,0], their exact
factorization, minimality via the cited change-of-model/minimal-model
criteria, all local conductor exponents, and non-CM via the cited CM
criterion. It must enumerate all points over F_2, including infinity,
and certify smooth reduction before using 3-#E(F_2). The source's values
389 and -2 are expectations to compare with, not premises to feed back
into those checks. Modularity identifies the needed form without using
analytic rank, rational rank, finite Sha or a database BSD assertion.

Enumerate every projective coset and an SL_2(Z) lift; include all
two/three-term relation rows. Exact rational row reduction together with
the saturated integer relation lattice must certify the complete
torsion-free presentation. Save all integral-generator coordinates,
basis choices and denominators. Smith normal form with unimodular
witnesses or an independently checked integer-kernel saturation is
acceptable; dimension agreement alone is not presentation evidence.

Preferred implementation: apply L029's three good-prime endpoint maps
to every generator, and separately negate both endpoints for reflection.
Reduce each resulting path using the cited continued-fraction procedure.
Save each exact telescoping chain, unimodular segment and coset reduction,
including negative rationals and infinity. Check all relation images and
all resulting matrix columns. This is a finite implementation of known
algorithms; no new operator theorem is to be derived. The faster Manin
Heilbronn method may be compared, but a returned eigenvector alone is
insufficient evidence. Record explicitly any reversed base-path convention.

Finally save B, its exact kernel basis and reversible rank operations
(or rank-minor witnesses), with actual and required dimensions. L029
requires exactly one dimension on the entire relative dual. A larger
kernel is an inconclusive result for this bounded single-operator test;
do not add primes within this scope. Failures of arithmetic certification,
complete presentation or geometric/operator identification prevent an
application regardless of a reported rank. No instance computation,
new lemma or mathematical script was produced in this source review.

## Relevance, duplicates and remaining limitations

The main gap remains rank E(Q)=m(E) for m(E)>=2. The intermediate target
can provide L029's line premise; L028 could then calibrate it using an
independent nonzero normalized twist value. The test is independent of q.
ATTEMPTS/022--023 stop repeated conditional audits, not this actual-data
construction. Earlier assessments cover conditional sufficiency and
calibration, not the requested instance. No duplicate instance certificate
was found in those targeted local records; no novelty is inferred.

Independent q, period scale, C, b, the other L026 arithmetic premises, F,
divisible Sha, rational membership and complex-order comparison remain
unresolved. There is no BSD candidate. Mathlib matching coverage for this
concrete construction was not checked; software/book algorithms are not
formal-library coverage. The CAPTCHA and failed PARI documentation URL
are nonessential access failures, not persistent blockers: the direct
path algorithm and arithmetic criteria above suffice for this target.

Queries: `site.lmfdb.org EllipticCurve Q 389 a 1 y2+y x3+x2-2x`;
`William Stein modular forms algorithms computing modular symbols
Heilbronn matrices T2 Manin symbols book`; `Breuil Conrad Diamond Taylor
modularity elliptic curves rational Theorem A pdf`. No external code or
database command was executed. The original proposed test is preserved
below as proposal history; its initial pending-source statements describe
the state before this review.

## Original bounded proposed test

Review the exact proposed construction before executing it. Retain the
curve equation as the candidate identifier; do not assume a conductor,
a database label, analytic rank, or one-dimensional T_2 eigenspace from
memory. Essential canonical input is L029; L028 is the downstream use.
Its existing hypotheses still require independent q and normalization
before any C or coefficient certificate. L027, L026 and L004 remain
conditional downstream, not inputs to this matrix test.

A future approved mathematical step should construct only the finite
relative presentation, geometric reflection and good-prime T_2 certificate
for this curve, including complete relation, coordinate and exact rank
witnesses. The discriminating threshold is dimension exactly one for the
entire simultaneous relative dual kernel. A larger kernel is an informative
inconclusive result for this single-operator test, not permission to claim
line identification or silently broaden the operator list. Failure to
certify the complete relative space or the curve/operator assumptions
also prevents an L029 application. No uniform termination is proposed.

Compare available standard algorithms before reimplementing. Prefer an
existing exact certificate if its relative space and geometric sign can
be independently checked. A software plus label or a library command
returning a vector is not the requisite evidence. Identify source scope,
all imported hypotheses, and what remains to be specialized. The old
assessment stays reusable for L029's conditional theorem; it does not
approve this new target. No new calculation or source review of this
concrete target was performed in the completed research step.

Preserve ATTEMPTS/022--023: another conditional enclosure/calibration audit
cannot replace missing inputs. This target is independently testable
without q or any rational-Kummer assertion. Even a successful instance
would leave uniform input production, q, period scale, C, b, the L026
arithmetic assumptions, F, divisible Sha, rational membership and
complex-order comparison unresolved. Mathlib coverage for this concrete
construction is not checked.
