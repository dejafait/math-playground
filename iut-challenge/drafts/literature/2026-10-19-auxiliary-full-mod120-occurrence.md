# Auxiliary full mod-120 occurrence — source assessment

TARGET: Determine whether L073's fixed-c auxiliary family contains a witness with full mod-120 image and full mod-seven image, retaining its prescribed local 210-torsion and 89-Frobenius data.
CHECKED: 2026-10-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step338 searched fixed-level surjectivity and congruence-family occurrence; inspected the primary composite-level statement and proof cases, compared L073/L046 and their existing assessments, and retained step334's entanglement review and ATTEMPTS/034. Exact queries and read scope are below; no specialized occurrence proof was performed.
SOURCE_EVIDENCE: Zywina https://pi.math.cornell.edu/~zywina/papers/MaximalGalois.pdf, undated 15-page author version retrieved 2026-10-19, section 1.1 pp.1–2, Lemma 2.4 proof p.5, Definition 5.1 p.6, Proposition 5.5/proof pp.7–8, Proposition 5.7/full proof p.8, and Lemmas A.2/A.6/A.8/A.10 with relevant proofs pp.12–14; reuse step334's Jones https://arxiv.org/pdf/math/0611096v1 section 5 Lemma 17/equations (12)–(16), pp.11–13, rereading the conductor and Serre-subgroup passages.
COMPARISON: The inspected fixed-composite-level theorem covers the missing source scope; L073 already supplies the constrained full-rank family and local retention. A separate same-witness counting and applicability argument remains necessary. Neither marginal prime images nor Serre-curve density is used as a substitute for the joint mod-120 condition.
GAP: Source coverage is ready; simultaneous occurrence in this exact family has not been proved here. The old chosen auxiliary witness is not certified, and no unconditional normality or IUT conclusion is claimed.
REASON: Essential composite-level proof cases outside the prior mod-seven assessment were checked; only the identified constrained-family specialization is approved, with the general theorem imported rather than reproved.
SCOPE: Exactly TARGET, with c,h,d_*,e_* fixed as in L073 before boxes grow; retain the entire two-parameter family and its original monic cubics. Permit one later existential count using the assessed bounds at levels 120 and seven on the same member, the existing pointed Q-isomorphism and L044/L046/L048/L073 retention. No effective coefficients, effective M, uniformity in h, identification with either old witness, new field prescription or transfer of later lemmas to a new member is covered.

LITERATURE_REASON: Essential unread coverage is a precise full mod-120 occurrence or obstruction theorem applicable to L073's fixed congruence family over Q, retaining the mod-seven requirement; the ready level-seven and conditional-normality assessments do not cover it.

## Completed comparison — 2026-10-19, step338

The main gap is still original finite B>=A. The intermediate target is
exactly TARGET. Its possible use is to make L085's conditional
nonnormality screen nonvacuous for maximal-image choices, rather than to
demonstrate an essential IUT flaw. No new mathematical result is derived
in this literature-only step.

**Primary theorem and cases checked.** David Zywina, *Elliptic curves
with maximal Galois action on their torsion points*, Bull. London Math.
Soc. 42 (2010), 811–826, [author version](https://pi.math.cornell.edu/~zywina/papers/MaximalGalois.pdf)
([DOI](https://doi.org/10.1112/blms/bdq039)); numbering refers to that
15-page version. For a fixed number field k, norm and positive integer
m, B_k(R) consists of nonsingular integral short coefficients and
B_(k,m)(R) of failures of SL_2(Z/mZ) containment. Proposition 5.7 gives

    |B_(k,m)(R)| / |B_k(R)| <<_(k,norm,m) log(R)/R^([k:Q]/2).

There is no squarefree-m, minimal-model, good-reduction or non-CM
hypothesis; k=Q is allowed. Lemma 2.4's proof identifies containment
with full image over Q. The full Proposition 5.7 proof uses
determinant-one classes and Proposition 5.5. Lemma A.10 treats composite
m through A.6 and A.2, including the 4/9 cases; A.8's (3,-1)
exception does not affect determinant one. These source statements,
including the 2-power lifting case, are imported without reproof.

**Applicability comparison, not an occurrence proof.** L073's canonical
proof supplies the integral short-coefficient family, its positive
quadratic count with fixed index, its pointed Q-map in both directions,
and its local retention for every member. L046 records the original
source/method application only at level seven. The new assessment
extends the approved source scope to the composite level; it does not
silently relabel L046's conclusion. The future proof must compare the
union of the two fixed-level exceptional sets with that exact family
count, verify both full images on one member over Q, and invoke local
retention for that member. No independence between the two exceptional
conditions is required by this proposed union-bound method. Its full
application and existence conclusion are deferred to research.

The stronger adelic/Serre-density route is unnecessary. Jones,
*Almost all elliptic curves are Serre curves*,
[arXiv:math/0611096v1, 3 November 2006](https://arxiv.org/pdf/math/0611096v1),
section 5 pp.11–13, retains the discriminant-character relation at its
associated conductor. This is a real joint-image obstruction for a
specified curve, not a universal obstruction at every fixed level.
The comparison therefore uses the composite-level exceptional theorem
itself; it assumes no chosen discriminant class, independent radical
signs or absence of entanglement for the old witness. Step334's remaining
Jones coverage is reused; no new discriminant calculation is made.

**Duplicates, failures and source limits.** Read L073's family/count/
retention proof, L046's exact application, L085's hypotheses and
conclusion, and the ready 2026-10-11 mod-seven assessment; searched
the relevant 2026-10-17 auxiliary-family assessments. None claims this
simultaneous occurrence. Step334 explicitly leaves occurrence outside
scope. ATTEMPTS/034 remains stopped: more powers of its single cyclic
Frobenius supply no full-image evidence. No cross-notebook input is used.
The existing challenge scope was rechecked earlier today in step334
against the official announcement/current page and is reused unchanged.

Queries were `Zywina "Proposition 5.7" "m" maximal Galois action torsion
points` and `elliptic curves fixed level m almost all surjective mod m
congruence conditions Jones Serre curves`. Primary theorem and relevant
proof cases above were read, rather than relying on snippets. Other
search leads (Serre constants, explicit Serre families and composite-
modulus surveys) were not inspected or imported. One screenshot fetch
timed out; the complete relevant theorem/proof text was accessible, so
there is no essential source blocker. Full matching and supporting
Mathlib coverage for this constrained occurrence result are unchecked;
unknown coverage is not absence.

**Continuation/abandonment test.** Continue with one known-method
specialization only if both exceptional bounds are dominated by the
unchanged family's count and all original local congruences remain.
Stop this method upon an actual mismatch in theorem hypotheses,
dimension, fixedness of the modulus, base-field isomorphism or
same-member local retention. A marginal-image assertion, another
recorded Frobenius power or a density statement without the constrained
count fails the test. The old E_aux and its unchanged G,H,N are not
reselected by this review. A later existential new member must receive
its own applicability argument before using downstream constructions.

The next mathematical classification is REPRODUCTION, not a claim of
novelty. Actual occurrence, independent initial data, native input/
action, all-image factorization, marked pilot transport, essentiality
and original finite B>=A remain open. PROOF and DAG do not change.

## Preserved invocation-start proposal (historical; superseded by the assessment above)

The main gap remains original finite B>=A. The proposed intermediate
target tests whether the now-audited obstruction has a realizable member
of the prescribed auxiliary family. A positive result would exclude such
maximal-image choices from the exact field prescription's normality
prerequisite. A proved obstruction would prevent treating L085 as an
available example. Either outcome is distinct from an essential IUT flaw.

Keep the fixed c,h,d_*,e_* and the full family
d=d_*+89h u, e=e_*+89h v, u,v in Z from L073. The parameters
c and h are fixed before the boxes grow. The target is existence within
that family, not an assertion about the previously chosen E_aux. No
reselection, alteration of G or replacement of either current witness is
made by this proposal. Any later constructed member would require its
own explicit applicability argument; it is not silently the old curve.

Essential local inputs are L073's family and retained local assertions,
its L044/L046/L048 approximation and image-count methods, and audited
L085's conditional conclusion through L080. Existing step334's Jones
entanglement comparison must be retained. The later review should inspect
precise finite-level theorem hypotheses and relevant proof cases, including
any exceptional primes or discriminant conditions, before importing a
count or a simultaneous-image existence conclusion. The fixed-level-seven
theorem must not simply be relabelled as a level-120 theorem. Check exact
statements, stronger results, duplicates and recorded obstructions; use
the ready source records where their assumptions still match. No new
source theorem is imported here.

The discriminating test, once separately covered, is an actual compatible
existence argument for both images or a precise obstruction under these
fixed congruences. Marginal surjectivity or another power of the recorded
Frobenius does not pass. If essential source coverage remains unavailable,
record the exact blocker and route to an independently testable target;
do not repeat the conditional core calculation or the stopped cyclic test.

Actual full-image occurrence, independent initial data, retained-witness
questions, native input/action, all-image factorization, pilot transport,
essentiality and original finite B>=A remain unresolved. Mathlib coverage
for this proposed simultaneous occurrence result is unchecked. This is a
continuation proposal, not source approval, a new lemma or a second
mathematical attempt in step337.
