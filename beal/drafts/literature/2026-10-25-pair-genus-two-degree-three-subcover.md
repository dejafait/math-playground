# Degree-three elliptic-subcover continuation — source assessment

TARGET: Determine whether L110's genus-two curve admits a Q-defined degree-three morphism to a genus-one curve, with an exhaustive exact-model test.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched degree-three elliptic subfields, (3,3)-splitting, Kuhn, rational covers and exact sextic coefficient strings; compared local L110/L127/L131, ATTEMPTS/056 and history/471; found complete general base-field methods but no inspected exact-instance answer or duplicate.
SOURCE_EVIDENCE: Read Bröker–Howe–Lauter–Stevenhagen, LMS J. Comput. Math. 18 (2015), Appendix A pp.193–196, (A.1), Lemma A.1, Proposition A.2 and both proof cases, Lemma A.3/Remark A.4, degeneration discussion; Bruin–Doerksen, Canad. J. Math. 63 (2011), Section 2 pp.995–997, Definition 2.3, complementary-cover construction and Lemma 2.6 with proof; Shaska math/0109155v1 Section 2/Main Theorem pp.2–3 and Section 4.1 p.9.
COMPARISON: Known theory supplies complementary covers over Q and a complete base-field normal form including special ramification and twists; it does not evaluate L110. Its rational cubic branch partition supplies an exhaustive necessary-condition obstruction, not a sufficient cover criterion.
GAP: Separately justify and test the branch-partition obstruction on L110's full binary sextic; a certified empty partition set excludes every Q-defined degree-three cover, whereas surviving partitions or exhausted caps leave the target unresolved and require reassessment before solving cover equations.
REASON: Approve one bounded first obstruction within the unchanged target, using complete rational-cover theory instead of a generic complex normal form; no exact-instance exclusion, factorization or new lemma has been derived in this literature turn.
LITERATURE_REASON: Essential primary degree-three and rational-descent coverage was missing at invocation start; the ready degree-two assessment does not cover these hypotheses.
SCOPE: Exactly TARGET through the necessary rational branch-partition test and a bounded good-prime irreducibility certificate described below; no unbounded factor search, parameter solver, invariant-locus transcription, cover construction, rank or point computation.

## Relevance and local scope

Main gap: numerical upper ranks and point control for the actual quotient
factors, before marked lifts and integer recovery. Intermediate target:
exclude, or retain without asserting existence, all Q-defined degree-three
maps by their necessary rational partition of the six branch points.
A positive cover could split Jac(B) into elliptic factors for L127's rank
comparison. A negative would close this cover-degree shortcut only.

Use audited L110's smooth proper genus-two B with

    W²=f(T)=11(T²−4)Q4(T),
    Q4(T)=7+52T−6T²−64T³−25T⁴.

Its rational point (T,W)=(2,0), squarefreeness and proper infinity chart
are already in L110, not new findings. L127 is downstream motivation;
L131 and ATTEMPTS/056 are route evidence only. No cross-notebook input.
Only Q-defined maps are sought: a geometric cover alone is insufficient.

## Primary theorems, hypotheses and essential cases

**Base-field parametrization.** R. Bröker, E. W. Howe, K. E. Lauter and
P. Stevenhagen, *Genus-2 curves and Jacobians with a given number of
points*, LMS J. Comput. Math. **18** (2015), 170–197,
[DOI 10.1112/S1461157014000461](https://doi.org/10.1112/S1461157014000461),
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/3242C20684C520AF0D3DF5C8D78C8355/S1461157014000461a.pdf/genus2_curves_and_jacobians_with_a_given_number_of_points.pdf).
Use the published version, **Appendix A, pp.193–196**. Its model is

    t y²=(x³+3ax+2b)(2dx³+3cx²+1),
    12ac+16bd=1, (a³+b²)(c³+d²)t != 0,

over any field k of characteristic neither two nor three. Lemma A.1
supplies degree-three maps to its two smooth genus-one models.
Proposition A.2 asserts completeness for TWO complementary degree-three
maps with phi2_* phi1^*=0, up to base-field isomorphism and the stated
scalings. That premise must not simply be omitted for a single map.

Read both cases of its proof, **p.195**, rather than relying on the
abstract: two simple ramification points are hyperelliptic conjugates;
one triple ramification point is Weierstrass. The proof treats the latter
with a degree-five model and keeps fields of definition. Section A.3,
**p.196**, explicitly retains d=0 or b=0; generic formulas alone omit
these cases. Use homogeneous cubic factors, retaining infinity when a
factor has affine degree two. Keep t; matching geometric invariants is
not a base-field isomorphism certificate. Lemma A.3 and Remark A.4 also
allow genus-one targets without a prescribed origin. The maps need not
preserve chosen identity points.

Section 5, **pp.182–183**, explains the complementary-map/isogeny
framework. Algorithm 5.4 and Theorem 5.5, **pp.185–187**, solve the
DIFFERENT problem with two elliptic curves supplied as input. Their
polynomial-time assertion does not give an inverse algorithm for B
when both elliptic targets are unknown; no such claim is imported.
The proof's special j=0 and j=1728 cases cannot be discarded in a later
full parameter test.

**Single-map bridge.** N. Bruin and K. Doerksen, *The arithmetic of
genus two curves with (4,4)-split Jacobians*, Canad. J. Math. **63**
(2011), 992–1024,
[DOI 10.4153/CJM-2011-039-3](https://doi.org/10.4153/CJM-2011-039-3),
[published PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9F2CF4B1938C312E140C53BEE3E42F69/S0008414X00006878a.pdf/div-class-title-the-arithmetic-of-genus-two-curves-with-4-4-split-jacobians-div.pdf),
**Section 2, pp.995–997**, Definition 2.3, ensuing complementary-cover
construction, and Lemma 2.6 with its proof. This section concerns general
optimal separable degree n, not only n=4. The construction uses the
connected pushforward kernel and quotient of the Jacobian; for odd n
it explains the rational invariant divisor class and a degree-n
complement over k. Lemma 2.6 includes vanishing of both cross composites.
Do not use the much broader statement that a split Jacobian has a cover
of SOME degree as a claim that the degree remains three.

For applicability next turn, L110 provides a Q-point, whose image makes
any asserted genus-one target an elliptic curve after choosing an
origin. Prime degree three leaves no nontrivial intermediate degree;
a degree-one genus-two/genus-one isomorphism is impossible. Thus the
optimal-cover hypothesis can be checked without assuming an additional
map or any rational Weierstrass point beyond the one L110 already has.
Import this framework; no reproof or new descent theorem is needed.

The older primary R. M. Kuhn, *Curves of genus 2 with split Jacobian*,
Trans. Amer. Math. Soc. **307** (1988), 41–49, Section 4 p.47, was found
in indexed text, including its cubic-factor and odd-degree complement
statements. Its [AMS PDF](https://www.ams.org/journals/tran/1988-307-01/S0002-9947-1988-0936803-3/S0002-9947-1988-0936803-3.pdf)
remained inaccessible on direct opening (403); JSTOR did not supply the
paper and shell download failed DNS. Those indexed extracts do NOT
count as reading its proof. This is a nonessential access limitation:
the accessible published sources above state the required framework
and supply the base-field parametrization and its essential cases.
No further retrieval retry is needed for the approved obstruction.

**Geometric comparison only.** T. Shaska, *Genus 2 fields with degree 3
elliptic subfields*, inspected [arXiv:math/0109155v1](https://arxiv.org/pdf/math/0109155v1),
21 September 2001; published Forum Math. **16** (2004), 263–280.
Section 2/Main Theorem, **pp.2–3**, assumes algebraically closed
characteristic zero. Its invariant relation characterizes geometric
membership in L3. Read the completion argument in Section 4.1,
**p.9**, which uses closedness to include the exceptional locus.
Appendix A's equation (33) was located, but its full large coefficient
list was NOT read or verified and is not an approved input. A zero of
that equation would not prove a Q-defined cover on this twist.

For transport of branch divisors reuse the ready Lercier–Ritzenthaler–
Sijsling assessment `2026-10-25-pair-genus-two-involution-eligibility.md`,
Sections 2A–2B and 2E1 of the primary paper: Q-isomorphisms act by
PGL2(Q) on the branch line. The genus-two branch divisor is intrinsic.
No new automorphism test or rational lift search is required here.

## Separate bounded mathematical attempt

These are obligations to carry out later, not an instance derivation.

1. Import the cited results and justify that any asserted Q-map in the
   target falls under Proposition A.2 via the complementary-cover bridge.
   Homogenize BOTH source factors to degree three, including d=0 and
   b=0. Prove that their disjoint rational branch triples transport to
   the actual binary sextic F(X,Z)=Z⁶f(X/Z). This is a necessary condition
   for every prospective map, including special maps; it is not sufficient.
2. Seek a small exact finite-field obstruction to ANY rational cubic
   factor of F. Scan only primes 3<=p<=97. Require preservation of degree,
   squarefreeness of the entire reduced sextic and nonzero leading
   coefficients before using reduction. For the displayed quartic, test
   irreducibility by exhausting all monic linear and quadratic divisors
   over F_p, saving full exact evidence at any successful prime. Use
   Gauss's lemma (primitive integer polynomial factorization and
   irreducibility by degree-preserving reduction), not a numerical or
   height search. A factorization of the rational binary sextic must
   also be checked projectively; infinity cannot be dropped.
3. If these certificates exclude every rational degree-three branch
   divisor, write the exact-model negative with all hypotheses and an
   independent replay. If no tested prime gives the needed obstruction,
   or if rational branch partitions survive, report the test as
   inconclusive. Do not infer existence or extend the prime bound,
   attempt a generic normal-form solver, or transcribe the unread locus
   polynomial automatically. A new exact-cover-equation target needs
   its own assessment if that becomes necessary.

This tests a necessary condition exhaustively over its finite domain;
an exclusion is exhaustive for all Q-defined degree-three covers only
after Step 1's applicability and transport proof. The review does NOT
promise that the bounded obstruction decides this instance. It approves
a useful intermediate attempt, not a general sufficient test or an
answer for B. No quartic factorization or modular test was run today.

Whole-step caps including preparation, producer, certificate and replay:
**25 primes, 250000 monic divisor trials, 1000000 charged work units,
polynomial degree <=12 and rational/integer bit length <=4096**. One
unit is one polynomial arithmetic operation, candidate check, scalar
check or processed certificate row; instrument these before running.
Do not claim to count library-internal elementary operations. Charge
reruns cumulatively; stop before any cap and save the partial evidence.
An interrupted or exhausted bounded search is never nonexistence.

Continue toward elliptic rank reduction only with actual Q-defined maps;
an exhaustive negative stops the degree-three shortcut. Quotient ranks,
point control, marked lifts, degree-nine recovery, both L095 systems
and other signatures remain. Mathlib coverage of these full results is
not checked; no absence or formal-verification claim is made.

## Duplicates, searches and preserved failures

Local searches were confined to drafts/literature, ATTEMPTS and relevant
recent history, followed by L110's exact model/proper charts and selected
L127/L131 passages. No local degree-three certificate was found. L131's
absence of rational extra involutions closes degree two only; it is not
an obstruction to degree three. Preserve ATTEMPTS/050–056 and unfinished
L108. No prior closed calculation was repeated.

External queries included `Shaska genus 2 degree 3 elliptic subfields
equation locus L3 theorem`, `Kuhn curves genus 2 degree 3 morphisms
elliptic curves rational field criterion`, `Broeker Howe Lauter
Stevenhagen genus 2 curves Jacobians given number points appendix A
pdf`, rational cubic-factor/partition variants and the exact coefficient
strings `275 704 1034 3388` and `7+52`. No inspected exact-instance
answer was found; failed search is not novelty evidence. Other search
leads and software linked by Howe were not inspected or executed.
The AMS Beal page again returned 403; reuse the precise target audit
in foundations/01-target-and-scope.md rather than asserting a new AMS
statement or adding prize-administration hypotheses.
