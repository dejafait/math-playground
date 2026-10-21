# Primitive full-fiber connecting valuations at eleven — source assessment

TARGET: Determine the complete set of connecting-class valuation vectors modulo five at places above 11 arising from primitive whole-fiber-compatible points in L033's 54a1 branch.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reviewed ATTEMPTS/008-010 and 012 and the local-five assessment; searched X0(11) local five-descent valuations, 54a1 eleven-adic descent, genfermat eleven-adic, and Tate-curve isogeny connecting maps. No inspected result computes this exact restricted vector set; this does not establish novelty.
SOURCE_EVIDENCE: Reused L033-L035 and foundations/15-17; inspected Aoki (2004) Section 3, Proposition 3.1 and proof (6)-(7), pp.212-214; Dokchitser-Dokchitser arXiv:1208.5519v4 Theorem A.1 p.19; Clark Theorem 1.75 p.57 and Proposition 2.9/Corollary 2.10 p.65; rechecked FNS Section 7.2/Table 5 and Schaefer-Stoll Lemmas 4.3-4.4/Section 5.
COMPARISON: Known local descent and Tate theory cover the unrestricted connecting map; Hensel/Eisenstein inputs cover certified factor lifting and ramification when their hypotheses hold. Reused Cohen coverage permits an exact valuation-formula route. None computes the simultaneous primitive whole-fiber image or makes unrestricted spanning certify it.
GAP: The identified specialization is the complete eleven-adic field decomposition, valuation image with all modular-fiber isomorphisms, and common primitive witnesses; every local reduction, ramification, exceptional chart and lifting hypothesis still needs mathematical verification.
REASON: Primary coverage now supports one bounded specialization without a sampled precision assumption or blocked global class data. At eleven the isogeny degree is prime to residue characteristic, but eleventh-power lifting is not a simple-root unit argument; retain it exactly.

## Exact proposed scope and test

Let K and the degree-twelve modular map be exactly L033-L034's. Over
Q11 use the entire algebra A11=K tensor_Q Q11. Consider every
s in Q11 minus {0,1728}, every isomorphism of the entire modular fiber
B_s with A11, and the resulting point P in E0(A11). Require common
nonzero a,b,c in Z11, with min(v11(a),v11(b),v11(c))=0,
a^3+b^4=c^11 and s=1728 a^3/c^11. No positivity or condition at another
place is imposed at this local stage. L036's five-adic characterization
is not imported as an eleven-adic characterization.

For each place w of K above eleven, normalize ord_w by
ord_w(uniformizer)=1. Apply ord_w modulo five to the w-component of
L033's connecting class, interpreted by good divisors at exceptional
points. This is well-defined on K_w^*/K_w^{*5}. The proposed target is
the exact set of these vectors, including an honest empty-set outcome
if appropriate. Whole-fiber isomorphisms and class collisions must all
be retained. No class, field decomposition, common scalar or local
realization is assumed in advance.

Main gap: global emptiness of the five surviving twists for (3,4,11),
as well as infinitely many other residual signatures. Downstream use:
compare the exact vectors with restrictions already forced by L034's
norm and the unrestricted connecting image; any additional restriction
can constrain valuations of global K(S,5) classes. This does not compute
global unit classes or prove global emptiness by itself.

Continuation test after coverage: obtain a complete, proved finite
vector image and determine whether it adds a restriction beyond those
baselines, or isolate a precise essential blocker. If known theorems
already compute the image or show this test is redundant, import that
conclusion and retire the test rather than reproduce it. Mere sampled
points are insufficient for completeness. This different-place,
class-valuation target does not reopen the stopped additional
primitive-scalar filter at five. Preserve ATTEMPTS/008-012.

This assessment was completed in a separate literature-only turn. The
exact target above is preserved. SPECIALIZE supports one later bounded
mathematical attempt, subject to the supervisor's separate approval of
this changed assessment. No eleven-adic result was derived here.

## Primary comparison and inspected cases

**Aoki.** Noboru Aoki, *On the Tate–Shafarevich group of semistable elliptic curves with a rational 3-torsion*, Acta Arithmetica **112.3** (2004), 209–227, [publisher PDF](https://www.impan.pl/shop/publication/transaction/download/product/82298). Section 3, pp.212–214, is not restricted to the title's degree three: it takes a finite extension k/Q_p, a Tate curve E_q, a prime n, a chosen q1=q^(1/n) in k and a rational point S of order n. For the dual map psi:E/<S> -> E, Proposition 3.1 gives the whole Kummer image if nu(S) is nonzero and the trivial image otherwise. The inspected proof constructs theta-function evaluations in (6), checks f composed with [n] is an nth power, and obtains delta(tau(u))=[u^(-nu(S))] in (7). Both nu cases were read. This is a conditional unrestricted-image theorem, not the target's restricted set. For any application at n=5, first verify split Tate reduction, q1 in k, the torsion coordinate, and agreement with L033's pairing/normalization. Exceptional evaluation remains through L033's good divisors. No degree-three global conclusion or Proposition 3.3 torsion-valuation formula is imported.

**Tate applicability.** Tim and Vladimir Dokchitser, *Local invariants of isogenous elliptic curves*, Trans. AMS **367** (2015), 4339–4358; inspected [arXiv:1208.5519v4](https://arxiv.org/pdf/1208.5519v4), 28 October 2013, Appendix A, Theorem A.1 and proof, printed p.19. For a finite extension of Q_l with split multiplicative reduction, it gives Tate uniformization, valuation of q, and both degree-p isogeny directions (power map or lattice enlargement). A root-lattice isogeny requires the selected pth root in the field. Split reduction and the relevant direction must be proved for each completion; the theorem does not certify them for this K. The j here is the elliptic invariant, distinct from the modular scalar.

**Local algebra certificates.** Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields and Adeles*, [author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf), accessible 161-page version, no identified revision date. Inspected the separable tensor-product/CRT argument on printed p.53, Hensel factor-lifting Theorem 1.75 and Remark 1.76 p.57, and Proposition 2.9 with proof and Corollary 2.10 p.65. Coprime residue blocks lift over a complete valuation ring; internal repeated factors do not become irreducible merely from that statement. An Eisenstein polynomial over a DVR gives a totally ramified field, with its root a uniformizer and the quotient its integer ring. These are supporting criteria, not a decomposition of the displayed degree-twelve polynomial. The attempt must prove irreducibility of every lifted factor and the total dimension, ramification indices and residue degrees. Reuse foundation 17's strong Hensel theorem only with its derivative inequality checked. No prime-ideal decomposition inferred from reduction at a possibly nonmaximal order is approved.

**Descent source reuse.** Schaefer–Stoll's June 13, 2001 [long manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf), Lemmas 4.3–4.4 pp.6–7 and Section 5 pp.8–10, applies away from the isogeny prime, including places above eleven for degree five. Inspected the smooth-reduction unramified argument, local quotient-size statement and good-divisor interface; canonical qualifications remain in foundation 15 and L033. Its subgroup spanning/cardinality method verifies the unrestricted image only. Neither that size nor independent points certify a set cut out by a common scalar and whole-fiber condition. Ramification of K must enter the normalization; rational-field Tamagawa data cannot be transferred without checking local minimal models. The general connecting theorem is imported, not reproved.

**FNS reuse.** [Final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf), internally June 10, 2019, Section 7.2, printed pp.25–27: rechecked the complete twelve-subgroup transport and Table 5's 54a1 polynomial against L033. The field and map are essential inputs; the adjacent two-Selmer dimensions use GRH and are excluded. The source's later two-adic computation is not an eleven-adic image theorem. Neither the inspected transport nor this table supplies the complete decomposition or restricted fifth-descent valuations at eleven.

**Effective fallback, unchanged source.** Reuse foundation 16's inspected Cohen (1969), Theorem 3.1 pp.144–145 and Section 4 p.146, [primary scan](https://math.uchicago.edu/~shmuel/lg-readings/Cohen-1969-Communications_on_Pure_and_Applied_Mathematics.pdf). Its complete discretely valued characteristic-zero scope covers Q11, not only Q5; the residue-ring decisions are finite. It offers an exact decision route after a faithful field/valuation encoding, with no practical complexity or small-precision guarantee. L037 is a Q5 encoding example, not an already proved Q11 specialization. No encoding or elimination is performed here.

## Exact specialization obligations and route decision

Retain the proposed scope above verbatim. L033 and L034 supply the curve, field, dual connecting map and complete modular map. L035 supplies a comparison framework over Q5 only: its norm-deformation argument must be checked anew at eleven, not cited as an eleven-adic theorem. L037 may guide chart and generation guards but is not an input asserting their eleven-adic applicability. L036 and L040 supply no eleven-adic scalar characterization or equality. No cross-notebook input is used.

A complete result must certify all places w above eleven and order the vector components by explicit factors/embeddings. Normalize ord_w by a uniformizer, verify residue degrees for any norm comparison, and retain every whole-algebra isomorphism, including permutations of isomorphic factors. Use the actual finite modular fiber, with the x=16 removable chart and good divisors at T. O is excluded by the finite scalar condition, not by deleting it from unrestricted descent. A finite residue preview, unverified factorpadic output, or reduction of the scalar alone cannot establish the image.

Keep the common nonzero a,b,c in Z11 and the exact original sum equation in the test. Cube/fourth unit conditions and eleventh unit conditions are different at this prime. In particular an eleventh-power equation has derivative divisible by eleven: foundation 17's simple-root lifting at five cannot be copied. An exact scalar-domain proof or a faithful formula retaining these witnesses is needed; no new scalar domain is derived in this review.

Aoki's theorem may simplify the unrestricted baseline after its hypotheses are checked. It cannot replace the restricted vector calculation. Similarly L034's constant norm is a baseline, not new power filtering. Compare an achieved complete vector image with both baselines; if it supplies only inherited restrictions, record redundancy honestly and retire this test. If completeness requires a missing precision or component argument, save that specific obstruction and do not identify sampled vectors with the full image. Global S-unit/class data, global intersections, the other four twists and infinitely many signatures remain independent gaps.

SPECIALIZE approves only one bounded REPRODUCTION attempt at the exact TARGET after separate supervisor approval of this changed assessment. Citations cover general theory; the identified local arithmetic difference still requires proof. No adequate exact match was found among the inspected statements, without any claim of originality. This review adds source coverage, no mathematical restriction, no new lemma and no mathematical script. Mathlib matching and supporting declarations remain not checked. Preserve ATTEMPTS/008–012.
