# L105 — Joint rational and minus-three quadratic factor at seven

## Hypotheses

Work over Q7 with v7(7)=1 and valuation ring Z7. Put

    phi(t)=(3t²+t+1)^5(1−5t).

A primitive local tuple means nonzero A,B,C in Z7 satisfying
A³+B⁵=C¹¹ and min(v7(A),v7(B),v7(C))=0. Positivity is not a local
condition. The algebra is the entire quotient by phi(t)−s, where
s=B⁵/C¹¹ is distinct from zero and one.

## Conclusion

There is one such tuple with A=7, C=1, B≡1 (mod 7), s=−342, and

    Q7[t]/(phi(t)+342) ≅ Q7 × (Q(sqrt(−3)) tensor Q7) × R8,

where R8 is an explicitly specified étale Q7-algebra of degree eight
below. All three displayed rational factors are disjoint whole factors
of this same fiber, rather than subfields of larger components.

Consequently the joint rational/minus-three factor test at seven cannot
exclude L104's minus-three alternative in the global rational-factor
branch. This does not realize any global algebra or either L095 integer
system, and supplies neither an integer solution nor a signature exclusion.
The minus-eleven alternative and every global lifting gap remain open.

## Proof

We apply simple-root Hensel lifting as stated in Romyar Sharifi,
*Algebraic Number Theory*, online Chapter 5, **Theorem 5.3.30**
([author's chapter](https://www.math.ucla.edu/~sharifi/notes/algnum-ch05.html),
version inspected 2026-10-20, no revision date identified).
Its exact prior coverage is
`drafts/literature/2026-10-20-quadratic-minus-three-seven-adic-test.md`.
The stronger Newton version is Pete L. Clark, *Algebraic Number Theory II:
Valuations, Local Fields and Adeles*, **Theorem 1.79, printed p.58**
([author's notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf)),
as recorded in foundations/17-local-power-hensel-inputs.md. We import
these theorems, without reproof. Below every lifted polynomial is integral,
its seed error has positive valuation and its derivative has valuation zero.

### The entire quadratic completion

The polynomial X²+3 has the two distinct roots 2 and 5 modulo seven.
Its derivative 2X reduces respectively to 4 and 3. The seed errors
are 7 and 28, each of valuation one. Hensel gives two distinct roots
in Z7, so the entire completion is Q7×Q7. In particular the required
degree-three product is Q7³; one rational root alone would not suffice.

### Regular residues and the single branch chosen

The bounded regular test retains all five scalar residues outside {0,1}.
For a compact exact factor record, let [a0,...,an] denote
a0+a1*t+...+an*t^n over F7. The leading unit of phi−s is 3 in
each row. The following monic factors have multiplicity one; their
product times 3 is the entire reduction of phi−s.

| s mod 7 | Complete monic factors, in coefficient notation | Rational roots |
| --- | --- | --- |
| 2 | [1,1]; [6,1]; [5,2,1]; [1,1,6,2,3,2,6,1] | 1,6 |
| 3 | [6,3,1]; [3,2,2,3,3,0,1,4,5,1] | none |
| 4 | [3,1]; [2,0,0,1]; [6,5,6,1]; [6,0,4,6,1] | 4 |
| 5 | [5,1]; [3,5,6,4,5,0,6,0,3,3,1] | 2 |
| 6 | [2,6,0,3,4,1]; [5,6,3,0,6,4,1] | none |

The complete certificate below checks reconstruction, squarefreeness
and irreducibility. For each monic factor h of degree n it records
t^(7^n)−t=0 modulo h and gcd(h,t^(7^(n/q))−t)=1 for every prime
q dividing n. These finite tests prove irreducibility: any irreducible
divisor has degree dividing n by the first relation, and any proper
divisor degree divides n/q for some such q, contradicting the second.
Here we use the elementary finite-field fact that an irreducible
degree-d polynomial divides X^(7^m)−X exactly when d divides m,
obtained by the orbit length of its roots under seventh-power Frobenius.
For the root-count purpose alone, evaluation at all seven residues and
the displayed squarefreeness also suffice independently of irreducibility.

Every rational root at an integral scalar is integral: at a hypothetical
negative root valuation the unit leading degree-eleven term would have
strictly smaller valuation than all lower terms, so could not cancel.
For regular scalars the reductions are squarefree; simple-root uniqueness
therefore makes these the exact rational-root counts throughout each
residue disk. No regular disk has three. Each row also has six common
unit solution tuples modulo seven, all retained in the certificate;
these finite tuples are not asserted to be exact witnesses.

We next test only the A-divisible branch with A=7, C=1. No zero or
infinity branch is needed once an exact witness exists. Let

    fB(X)=X^5+342.

At X=1 its error is 343, of valuation three, and fB'(1)=5 is a unit.
Hensel yields one exact B≡1 (mod 7) with B^5=−342. Consequently
A³+B⁵=343−342=1=C¹¹ and the common valuations are (1,0,0).
This is one primitive tuple, with exact scalar s=−342 and
1−s=A³/C¹¹=343. Subsequent root lifting never changes it.

### Three roots in this same fiber

Exact differentiation gives

    phi'(t)=−165t²(3t²+t+1)^4.

Thus phi has constant coefficient one, no linear or quadratic term,
and cubic coefficient −55. Define the normalized polynomial

    g(u)=(1−phi(7u))/343−1.

This is in Z[u]: the terms below degree three vanish before division,
and each term of degree i>=3 is divisible by 7^i. Its full coefficient
vector in increasing order is

    [−1,0,0,55,1155,29106,377300,5150145,41597325,
     349417530,1467553626,7004233215].

Hence g reduces to 6u³−1. Its three distinct residue roots are
3,5,6, with derivative residues 1,2,4. The actual seed data and the
bounded lifts are:

| seed a | g(a) | v7(g(a)) | g'(a) mod 7 | root mod 49 | root mod 343 |
| --- | --- | --- | --- | --- | --- |
| 3 | 1334598526278206 | 1 | 1 | 24 | 73 |
| 5 | 357034266740513124 | 1 | 2 | 19 | 117 |
| 6 | 2633445196497743831 | 2 | 4 | 6 | 104 |

In all cases v7(g(a))>2v7(g'(a))=0. Hensel gives exact roots
u3,u5,u6 in the respective residue classes. The table entries only
record approximations; existence to all precision follows from the
theorem and these strict inequalities. Put ti=7ui for i=3,5,6.
The identity 343g(u)=−(phi(7u)+342) proves that these are roots of
the same f(t)=phi(t)+342. They are distinct because the ui have
different residues. In fact v7(ti−tj)=1 for i≠j, so their linear
polynomials are coprime in Q7[t], despite identical zero reductions
in the unscaled t coordinate. No factor lifting of repeated linear
reductions is presumed.

### Exact whole complement and separability

Specify the exact polynomial and entire complement by

    P(t)=(t−t3)(t−t5)(t−t6),
    G(t)=f(t)/P(t) in Q7[t],
    R8=Q7[t]/(G(t)).

These definitions use the uniquely specified Hensel roots above,
rather than finite approximations. The factor theorem and distinctness
give exact divisibility by P. Since deg f=11, deg P=3, and the
leading coefficient of f is −1215, G has degree eight with that
same nonzero leading coefficient. This specifies the whole complement,
without selecting or omitting any of its factors.

The derivative identity proves that f has no repeated root over an
algebraic closure: its possible critical roots are t=0, where f=343,
and roots of 3t²+t+1, where f=342. Both values are nonzero in Q7.
Thus f is squarefree. In particular G is squarefree and coprime to P.
More explicitly, at any ti one has q(ti)≡1 (mod 7), ti≠0 and
v7(f'(ti))=2. The denominator
product over j≠i of (ti−tj) also has valuation two, so

    G(ti)=f'(ti)/product(j≠i)(ti−tj)

is a unit. This is an exact coprimality certificate, not a residue
factor count. Chinese remaindering now gives Q7[t]/(f)≅Q7³×R8.
The quadratic-completion computation identifies its first three
factors with the product in the conclusion. R8 is étale of degree
eight because G is squarefree: polynomial Chinese remaindering writes
its quotient as a product of finite separable field extensions, to
which the Stacks Project, **Lemma 10.143.4 (tag 00U3)** applies
([statement and proof](https://stacks.math.columbia.edu/tag/00U3),
version inspected 2026-10-20 in the prior audit assessment).
This is étaleness over Q7, not a claim of étaleness of an integral
power order over Z7. No irreducible decomposition of R8
is needed for this target, which asks for a degree-three direct factor.

The witness decides existence and parks standalone exclusion at seven.
It does not prove that all primitive seven-adic fibers have this factor,
and no classification of the other branches is claimed. L093, L103 and
L104 supply downstream global context only; their global hypotheses
are not assumed for this standalone local construction.

### Certificate and scope

Run `python3 scripts/quadratic-seven/check_joint_fiber.py` to regenerate
`scripts/quadratic-seven/joint-fiber-certificate.json`. All 37 checks
pass. The complete /regular, /branch, /quadratic and /checks values were
inspected, including every residue factor, all multiplicities, common
residue tuples, actual seed errors and lift digits. The script uses
integer and F7 polynomial arithmetic, records its full certificate on
disk, and prints failures, actual/required factor counts, complementary
degree and normalized precision (343, matching the cap). Exact
existence and the complementary algebra follow from the proof above,
not from the precision-three approximations or a preview.

Classification: REPRODUCTION of the assessed elementary lifting methods.
The new local evidence changes this notebook's route, without claiming
a mathematical discovery beyond the sources checked. The independent
critical audit below confirms this existing result without correction.

### Independent critical audit, 2026-10-20

The audit uses the unchanged prior SPECIALIZE assessment
`drafts/literature/2026-10-20-seven-joint-witness-audit.md`. It is a
REPRODUCTION audit, not a stronger theorem or an integer realization.

All complete /regular, /branch, /quadratic and /checks fields of the
original certificate were inspected. The independent replay
`python3 scripts/quadratic-seven/audit_joint_fiber.py` writes
`scripts/quadratic-seven/joint-fiber-audit.json`, retaining the original
certificate's SHA-256. It imports no original script functions:
multinomial expansion recomputes phi and q^4, Newton correction computes
the lift digits, and iterated Frobenius by exponent substitution checks
every recorded irreducibility certificate. It also independently checks
all complete factor products, multiplicities, root lists and unit tuples.
All 87 audit checks pass, including all 37 original checks recomputed;
there are no failures. The actual/required rational-factor count is 3/3,
complementary degree is 8/8, and precision is 343 against the original
343 cap. No higher-precision search was needed.

The arithmetic is subordinate to the following exact application checks.
For X²+3 the two seeds have errors of valuation one and unit derivatives;
degree two and the distinct roots exhaust the entire completion. For
X^5+342 the seed one has error valuation three and unit derivative,
so B is a nonzero unit, while A=7 and C=1 give the same exact scalar
and valuation triple (1,0,0). All normalized coefficients and the identity
343g(u)=−(phi(7u)+342) agree exactly. The three g seeds have strict
Hensel margins 1,1,2 above the required zero, giving unique exact u
in three different nonzero residue classes. Thus each ti has valuation
one and each difference ti−tj has valuation one. Coprimality here is
over Q7; comaximality over Z7 is neither needed nor asserted.

The complete derivative check accounts for t=0 and every root of q
over an algebraic closure, with f-values 343 and 342 respectively.
These are nonzero even though 343 is not a seven-adic unit. The scalar
−165 is nonzero and a seven-adic unit, so no further derivative roots
are omitted. Hence f is squarefree. The exact factor theorem applied
successively to the distinct ti proves divisibility by their monic
degree-three product, and its quotient retains the leading coefficient
−1215 and degree eight. Squarefreeness of f makes that quotient squarefree
and coprime to all three factors. Independently, the displayed formula
for G(ti) has numerator and denominator both of valuation two, verifying
that none of the three chosen roots remains in the complement. Polynomial
CRT and the cited field-level étaleness criterion therefore apply to
the whole complement. Finite lift approximations are never substituted
into this exact quotient definition.

The regular-disk root counts are ancillary and also pass: the unit
leading coefficient forces every rational root to be integral, and
squarefree reductions plus simple-root uniqueness give precisely the
listed counts. No completeness claim about the other singular branches
is needed for an existence witness. No positivity over Q7, global
rationality of the ti, compatibility with larger global fields, or
solution of either L095 integer system is inferred.

The empty L105 DAG row is correct: the polynomial construction uses
the cited standard theorems directly; L093/L103/L104 supply relevance
only. The local stop is confirmed, while all independent global gaps
remain. The argument and its conclusion required no mathematical repair.

## Mathlib

Full matching coverage of this joint-fiber specialization and supporting
Hensel, finite-field and finite-étale declarations: **not checked**.
No absence claim or formal verification is asserted.
