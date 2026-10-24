# C124a — The surviving mask-17 product passes the five-adic filter

## Hypotheses

Use L124's entire degree-eight field K=Q[theta], with the unchanged
marked polynomial

    G(t)=3025t⁸−31460t⁶+76230t⁴−39204t²+2673.

Use its supported generators g0=−3−theta and g4=3−theta and its
mask convention, so mask 17 is delta=g0*g4. Use audited L119's full
five-adic algebra, actual theta transports, six-bit square-class labels
and one common rational scalar quotient. No global class independence,
complete supported group or rational-point hypothesis is assumed.

## Conclusion

The localization of delta=theta²−9 is a square in every factor of
K tensor Q5. Its raw six-bit label and canonical scalar-quotient label
are both 000000, with norm bits (0,0). Its full common-scalar orbit is

    {000000,000010,010100,010110}.

It therefore passes L119's exact point-image filter {1,alpha}. This
fixed test supplies no further pruning of L124's joint-zero fiber,
whose two masks 0 and 17 both survive at five. It does not prove that
mask 17 is globally scalar-square or realized by a rational curve point.

## Proof

### Imported coverage and exact models

The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-10-24-marked-octic-surviving-linear-five-adic.md`.
This is its single fixed-instance specialization, classified REPRODUCTION.
Import Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. **78** (2009), 2347–2370,
[DOI 10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8),
the inspected [arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
21 October 2008: Section 2 p.3 for the even-degree scalar quotient and
norm condition, Section 4 p.6, Lemma 4.4 p.8 and SquareClasses/LocalImage
pp.9–11 for finite-local square classes and their certified bounds.
The assessment's source comparison and L119's audited instance are
reused; no general descent or full image algorithm is reproved.
The unchanged integral squarefree G over Q5 satisfies the source's
general hypotheses; no unit-leading-coefficient shortcut at five is used.

L124 proves support, fixes the mask and certifies that precisely masks
0 and 17 form its joint norm/real/dyadic zero fiber. It does not identify
their global classes. We import that result without recalculating the
bounded family. Only its product g0*g4 is tested here.

For clarity, retain L119's exact transports in full. Put

    H(r)=2673r⁴−39204r³+76230r²−31460r+3025,
    J(v)=66825v⁴−196020v³+76230v²−6292v+121.

Let r0 be the unique root of H in 3+5Z5, let u1 be the unique root
of J in 3+5Z5, and set r1=5u1. Set

    a=−39204/2673+r0+r1,
    b=3025/(2673*r0*r1).

Audited L119 identifies the entire algebra as L4 × L2 × U, where

    L4=Q5(pi), pi⁴=10;
    L2=Q5(lambda), lambda²=15;
    U=Q5(omega), omega²=3.

In L4 let u be the unique root congruent to 1 modulo pi of

    u⁴+(a/pi²)u²+b/10=0,

and set q=pi*u. In L2 set q=lambda*sqrt(r1/15); in U set
q=omega*sqrt(r0/3), using the principal square roots in Q5.
In every factor the actual theta is exactly 1/q. The quantities r1/15
and r0/3 lie in 1+5Z5. These exact root definitions, not a choice of
finite approximants or ramification degrees, fix the localization.
L119 proves the full factorization and these isomorphisms.

Use normalized valuations v4(pi)=1, v2(lambda)=1 and vU(5)=1.
Then q has valuations (1,1,0). At odd residue characteristic every
principal unit is a square by the standard named Hensel lemma applied
to X²−w at X=1, whose derivative 2 is a unit. We use this imported
square-neighborhood fact with explicit strictly positive bounds.

### Exact component evaluations and precision

Multiplication gives

    (−3−theta)(3−theta)=theta²−9=q^(−2)(1−9q²).       (1)

In L4 the relative error −9q² has exactly v4=2; in L2 it has
exactly v2=2, since 9 is a unit and q has valuation one. Thus the
last factor of (1) is a square in both fields. The first factor is
the exact square (q^(−1))². Both delta components are nonzero with
normalized valuation −2. Upon multiplication by pi² or lambda²,
respectively, the unit residues are 1: the quotients q/pi and
q/lambda both have residue 1. Hence the ramified class bits are
(0,0) and (0,0), with strict relative precision 2>0 in each factor.
There is no cancellation that could raise the component valuation:
1−9q² is a unit with residue one.

In U, q²=r0, so the exact component is

    delta=(1−9r0)/r0
         =omega²*w,  w=(1−9r0)/(3r0),
    w−1=(1−12r0)/(3r0).                            (2)

Since r0=3 modulo five, its denominator is a unit, and
1−12r0=1−36=0 modulo five. Therefore vU(w−1)>=1>0
(including infinite valuation if the difference vanishes). Hensel
makes w a square, and omega² is already a square. The delta component
has valuation zero and residue 3=omega_bar² in F25. Its residue
norm to F5 is 3²=4, also consistent with the square character.
Its class bits are (0,0). The strictly positive relative bound is
at least one. Equations (1)–(2) prove the exact classes without any
finite approximation error. Actual lower bounds (2,2,1) all exceed
the required threshold zero; no bound from L119's different point disks
is silently applied to this product.

### Full common-scalar quotient and membership

L119's raw coordinates are (a,b,c,d,e,f), representing

    (pi^a*2^b, lambda^c*2^d, 5^e*(1+omega)^f).

The preceding evaluations give 000000. The norm bits are
(a+c,a+c+f)=(0,0), as required because 3025=55². Under the single
embedded Q5* scalar group the generators two and five have rows

    010100, 010110.

Adding neither, either or both rows to 000000 gives exactly
000000,010100,010110,000010. There are four distinct orbit members;
the unique one with d=e=0 is 000000. All four have norm bits (0,0).
No separate scalar is chosen in an individual component.

L119's exact point-image representatives are 000000 and 101000,
namely identity and alpha. The tested product therefore belongs to
that image. L124's mask 0 is already identity, so neither mask in
its joint-zero fiber is removed by this additional five-adic test.
This comparison does not promote a local square to a global square
or an image membership to a rational point.

### Evidence, scope and stopping decision

Run `python3 scripts/pair-genus-two/surviving_linear_five_adic.py`.
The complete finite certificate is
`scripts/pair-genus-two/surviving-linear-five-adic-certificate.json`.
It retains the exact model definitions, both simple Hensel seeds and
derivative residues, the component identities, all normalized valuations
and residues, strict bounds, full F25 nonzero-square table, raw/norm
bits, complete common-scalar orbit and point-image comparison. All 21
finite arithmetic checks pass, with no failures. The full component
records and full scalar orbit were inspected. The analytic proof above
supplies the exact field and Hensel justification; finite flags alone
do not prove those facts. No independent critical audit is claimed here.

This is an informative negative result for removing this fixed mask,
not a new general theorem beyond the inspected methods. Stop this
specific five-adic removal test. The original dyadic pruning survives,
as do identity and both rational infinity points. Complete supported
units/S-class two-torsion, other supported classes, surviving-cover
point control, degree-nine root recovery, compatible remaining factors,
both L095 integer systems and minus-eleven remain unresolved.

### Independent critical audit, 2026-10-24

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-24-surviving-linear-five-adic-critical-audit.md`.
This separate RESEARCH / REPRODUCTION audit confirms the statement
without correction or strengthening. Its direct mathematical inputs
remain audited L119 and L124. Their full local algebra, actual theta,
final label convention and mask-17 collision are imported; neither the
entire point-image algorithm nor the bounded generator search is rerun.
The precise Bruin–Stoll citation and Hensel applicability above remain
the source coverage for this instance.

The product has coefficients (-9,0,1) and mask 2^0+2^4=17. Reading
the exact transports, q/pi and q/lambda have residue one and q has
normalized valuation one in both ramified fields. Hence 9q² has
valuation exactly two. In (1) the principal factor has residue one,
so no cancellation can change its valuation zero. Thus delta has
valuation -2, and multiplication by the square of the chosen
uniformizer gives unit residue one. Hensel for X²-(1-9q²) at 1 has
unit derivative 2 and positive error valuation 2. This proves both
ramified components square in the actual fields, with no approximant
or precision extrapolation.

In U, equation (2) is an exact rational-function identity. At r0=3
modulo five, 1-9r0 has residue 4 and 3r0 has residue 4. In particular
delta is nonzero, its valuation is zero, and w has residue one. The
error numerator 1-12r0 has residue zero; the denominator is a unit.
The bound vU(w-1)>=1 is all that is required, and is not asserted to
be equality. Unit-derivative Hensel makes w a square. The multiplying
element omega² is an explicit square in U, although 3 is nonsquare
in Q5. Independent enumeration of all 24 nonzero F25 elements gives
exactly the twelve saved squares and verifies omega_bar²=3 and its
residue norm 4. The residue field is not replaced by F5.

These arguments determine all six bits as zero before quotienting.
The norms of L119's six generators give (a+c,a+c+f); the leading
coefficient 3025=55² retains norm bits (0,0). The scalar-two row is
010100, since 2 is nonsquare in both ramified residue fields and square
in F25. The identities 5=pi^4/2=lambda²/3 give row 010110: both
inverse units are nonsquare, while U contributes valuation one.
The two rows are independent. Their four sums are precisely the
displayed orbit; all have square norm and only 000000 has d=e=0.
L119's actual point-image list contains that representative. No
componentwise scalar adjustment or subgroup premise for the point
image is used. L124's other joint-zero mask, 0, is the empty product.

The independent arithmetic auditor is
`scripts/pair-genus-two/audit_surviving_linear_five_adic.py`; run it with
`python3 scripts/pair-genus-two/audit_surviving_linear_five_adic.py`.
It imports and executes no producer code. Its complete output is
`scripts/pair-genus-two/surviving-linear-five-adic-audit-certificate.json`.
All 49 comparisons pass, with no failures. They reconstruct reciprocal
and scaled coefficients, product and cleared-denominator identities,
Hensel seed residues, complete component records, all residue squares,
norm/scalar comparisons, and every one of the 21 producer check records.
Every field of the producer certificate, including exact model
definitions and failure list, was also inspected in full against the
analytic proof. Those model definitions and the full point image are
audited inputs, not assertions established merely by these finite flags.
The strict bounds remain (2,2,1)>0 in the three actual fields.

The first auditor launch failed before calculation because system
Python lacked SymPy. Replacing its small symbolic operations by exact
standard-library coefficient arithmetic removed that execution
dependency; no source or mathematical failure was concealed.

ATTEMPTS/054's fixed-test stop is confirmed. This audit establishes
reliability of the local input only; it gives no new mathematical
conclusion beyond C124a or the inspected methods. Global scalar-square
status, full supported arithmetic and all point/integer gaps above
remain unresolved. The mathematical assembly and DAG are unchanged.

## Mathlib

Full matching Mathlib coverage of this fixed localization and the
Bruin–Stoll algorithm is not checked. Standard Hensel and residue-square
facts support the proof; specific supporting Mathlib identifiers have
not been checked. Unknown availability is not evidence of absence.
