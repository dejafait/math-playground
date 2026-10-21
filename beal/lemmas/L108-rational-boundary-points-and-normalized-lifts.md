# L108 — Rational boundary points and normalized minus-three lifts

## Hypotheses

Let phi(T)=(3T²+T+1)^5(1−5T), and use L107's smooth proper
unmarked quotient Ytilde and its finite map s:Ytilde -> P¹. Its generic
coordinates are a distinguished root r and an unordered pair {a,b} of
other distinct roots of phi(T)−s, with

    u=(a+b)/2,       z=−(a−b)²/12.

Use L107's fixed minus-three double cover Ctilde -> Ytilde. In
particular the rational equation of this cover is v²=z; the unmarked
quotient itself allows arbitrary unordered pairs, including split ones.
Use the audited irreducibility conclusion of L097 for

    h(T)=55+165T+594T²+1100T³+2145T⁴+2475T⁵
                           +2970T⁶+1782T⁷+1215T⁸,
    phi(T)−1=−T³ h(T).

No integer solution, classification of open rational points, or
factorization of the full octic splitting field is assumed.

## Conclusion

There is exactly one rational point of Ytilde above {0,1,infinity}.
It lies above s=1 and is the normalized branch on which r,a,b all
tend to zero. The function r is a local uniformizer there, ord(z)=2,
and the exact normalized residue is

    (z/r²)(P)=1/4.

It therefore has exactly two rational lifts to Ctilde, by L107.
The normalized discriminant residue is −12*(1/4)=−3. There are no
rational points above zero or infinity.

The complete infinity residue fields are Q(zeta_11)^+ once and
Q(zeta_11) four times, each with ramification index eleven.
Below we also give an exact finite-étale algebra presentation of the
whole normalized support over one. We do not split all of those
algebras into individual number fields or compute all nonrational
residue fields over zero. Thus the stronger proposed arithmetic
classification of every boundary residue field remains unfinished,
although the rational-point selection and its lifting value are exact.

This is a model-specific specialization of the cited local-normalization
and descent methods, not a resolution of either L095 integer system or
a claim of progress beyond those general methods.

## Proof

### Local normalization and what must descend

L107 identifies the actual rational quotient, its function field and
its complete geometric ramification. In particular the normalized
geometric fibers have 99 points of index five at zero, 168 of index
one and 109 of index three at one, and 45 of index eleven at infinity.
Those counts alone do not identify arithmetic points.

We work with complete local branches of that function field, not the
unsaturated invariant equations at a colliding affine image. The
normalization/completion theorem used here is Stacks Project Lemma
33.41.2 [tag 0C1R](https://stacks.math.columbia.edu/tag/0C1R), with
henselian decomposition in Lemma 10.153.4
[tag 04GH](https://stacks.math.columbia.edu/tag/04GH). Our reduced
finite-type curve over Q is Nagata; its finite normalization has
completed local rings which are complete DVRs. The root-label cover
on the punctured formal disk is exactly L107's cover. A local root
with nonzero derivative lifts uniquely as a formal power series:
its successive coefficients are determined by a nonzero linear
coefficient. This gives the expansions used below and proves their
uniqueness, rather than relying on finite-precision approximations.
Their fields and ramification identify the normalized local branches.

For residue descent we import Stacks Lemma 58.2.2
[tag 03QR](https://stacks.math.columbia.edu/tag/03QR): finite étale
schemes over a field are equivalent to finite continuous Galois sets,
and a point's residue field is the fixed field of its stabilizer.
Apply this to the reduced normalized boundary support; its
ramification multiplicities are recorded separately. These primary
inputs and their essential cases were inspected in the prior boundary
assessment on 2026-10-20. We use the complete-local alternative there,
not an unproved monic absolutely irreducible plane presentation for
Duval's algorithm. The expansions and residue descent are the
instance-specific obligations supplied here.

At either finite boundary value all root coordinates are integral in
every local branch. Indeed phi(T)−s divided by its nonzero constant
leading coefficient is monic over Q[[s]] or Q[[s−1]]. Consequently
u,z,r have well-defined finite residues, and their residues at a
rational normalized point belong to Q. Different branches may have
the same residues of all three coordinates; we never identify such
branches solely by their affine images.

### Zero: a necessary fifth root is impossible

Put d²=−11, E=Q(d), alpha=(−1+d)/6 and beta=(−1−d)/6. The root
limits over zero are alpha and beta of multiplicity five, and
gamma=1/5 of multiplicity one. A rational normalized point must
have rational residue of r, so r tends to gamma. Neither member of
its unordered pair can tend to gamma: that local root is unique and
is already the distinguished root. If both pair members tend to
alpha, then u tends to alpha, which is not rational; similarly for
beta. The only possible rational case therefore has one pair member
tending to each of alpha,beta.

Suppose such a rational point P exists, and choose a rational
uniformizer tau of its DVR. Its completion is Q[[tau]]. After the
constant extension to E, the quadratic for the pair has distinct
residual roots alpha,beta and splits uniquely into formal roots

    a=alpha+x,      b=beta+y,       x,y in tau E[[tau]].

This labels the two roots unambiguously by their limits. L107 gives
ord_P(s)=5. Since q(T)=3T²+T+1 satisfies q'(alpha)=d and
q'(beta)=−d, the exact leading expansions are

    phi(alpha+x)=d^5(1−5alpha)x^5+O(x^6),
    phi(beta+y)=(−d)^5(1−5beta)y^5+O(y^6).

Their displayed coefficients are nonzero. Hence ord(x)=ord(y)=1,
and H=y/x is a unit. Equating the two expansions gives, for its
nonzero residue H0 in E,

    H0^5=C,       C=−(1−5alpha)/(1−5beta)
                  =−(11−5d)/(11+5d).

This is impossible. The polynomial D²+11 has the two distinct
roots 1,−1 modulo three, so the embeddings into Q3 obtained by
simple-root lifting give split places of E with normalized valuation
v(3)=1. At the place d=1 modulo three, 11−5d is divisible by three
and 11+5d is a unit. Their exact product is

    (11−5d)(11+5d)=396=4*9*11.

It follows that v(11−5d)=2 and v(11+5d)=0, so v(C)=2. A fifth
power in E has valuation divisible by five at this place. Thus H0
cannot exist and Ytilde has no rational point over zero. This argument
uses a residue of a unit on the normalization, not a slope sampled at
finite precision or a rationality assumption on an affine collision.

For geometric accounting, the 99 inertia branches separate into the
following categories. The two nonrational clusters are interchangeable
in this table; “same” refers to the cluster containing r.

| Distinguished root limit | Pair limits | Geometric branches, each e=5 |
| --- | --- | ---: |
| gamma | both in one cluster | 4 |
| gamma | one in each cluster | 5 |
| a cluster | gamma and same cluster | 8 |
| a cluster | gamma and other cluster | 10 |
| a cluster | both in same cluster | 12 |
| a cluster | both in other cluster | 20 |
| a cluster | one same, one other | 40 |

For example gamma with a mixed pair has 25 labels divided by five;
a cluster r with a mixed pair has 2*5*4*5 labels divided by five.
The other rows follow by choosing the indicated root letters, always
excluding r. These disjoint categories exhaust 495 labels and give
weighted degree 5*99=495. Only the first two rows could even have
rational r; the arguments above exclude both. Individual nonrational
residue fields in this table are not asserted to have been computed.

### One: the unique rational branch and its exact local unit

A rational point over one has rational residue of r. The factorization
phi(T)−1=−T³h(T) and L097's irreducibility of the degree-eight h force
that residue to be zero. We use L097 as a known proved input, with its
Eisenstein-at-eleven argument and precise Milne citation; no new
factorization or octic Galois-group computation is being assumed.

There are three zero-limit roots and eight simple h-roots. If both
members of the pair tend to simple h-roots, rationality of the pair's
symmetric residues would give a rational quadratic factor of h. This
contradicts irreducibility. If exactly one tends to a simple h-root,
its residue is 2u (the other limit is zero), so it would be rational,
again impossible. Thus all three selected roots tend to zero.

The local branch actually exists over Q and is unique. Put T=rX and
form the polynomial, integral in Q[r,X],

    F(r,X)=(phi(rX)−phi(r))/r³.

Its reduction at r=0 is −55(X³−1). Write zeta=zeta_3. The three
simple roots 1,zeta,zeta² lift uniquely in Q(zeta)[[r]] to roots of
F. The first is exactly 1. Denote the other two series A(r),B(r),
with constants zeta,zeta². The pair

    a=r A(r),       b=r B(r)

is unordered and is fixed by Gal(Q(zeta)/Q). Its symmetric functions,
and hence u,z, lie in Q[[r]]. For nonzero formal r the three roots
are distinct, so this is a branch of the actual open quotient.
Its completed branch field is Q((r)): it contains r and all the
symmetric coordinates are in Q((r)). Its completed normalization is
Q[[r]], with residue Q and genuine uniformizer r. The ramification
index is three since phi(r)−1 begins −55r³. The two possible orderings
of A,B give the same unmarked branch. These are all three local
zero-limit roots, so there is no second such branch. This also agrees
with the single inertia orbit on all-three-zero labels.

Its exact leading value is

    z/r² = −(A(r)−B(r))²/12,
    (z/r²)(P)=−(zeta−zeta²)²/12=1/4,

because (zeta−zeta²)²=−3. Therefore ord_P(z)=2. Applying L107's
normalized unit criterion with tau=r gives exactly two rational
lifts. The evaluated normalized unit is 1/4; the discriminant
representative is −3. These are different quantities. There is no
claim that the degenerate affine quadratic at s=1 is a disjoint
quadratic direct factor.

Here is also the entire residue algebra over one, before decomposing
its nonrational factors. Let S be the finite étale Q-scheme h(T)=0.
It is one degree-eight point by L097. Write S^[2] for its ordered
distinct-pair scheme, B for its unordered distinct-pair scheme and
D for its distinguished-root/unordered-other-two scheme. These are
finite étale schemes of degrees 56,28,168 respectively; their
coordinate algebras are defined by the indicated distinct-root
products and permutation invariants, so this specifies exact finite
algebras without an octic Galois-group assumption. The support of
the index-one part is D. The support of the index-three part is

    S^[2] disjoint-union S disjoint-union B
       disjoint-union (S times Spec Q(zeta_3)) disjoint-union Spec Q.

The five parts correspond respectively to r simple/pair mixed;
r simple/pair both zero; r zero/pair both simple; r zero/pair mixed;
and all three zero. In the mixed case with r zero, the other zero
root has leading ratio zeta or zeta², giving exactly the indicated
quadratic tensor factor. With r simple and pair both zero, choosing
the missing zero root as local parameter gives rational symmetric
series for the other two, so its residue scheme is S. The other
cases follow from unique lifting of each simple root. Thus the
geometric counts are 168 of index one and
56+8+28+16+1=109 of index three, with total degree 168+3*109=495.
Every part except B and Spec Q projects to S and hence has no rational
point; B has none because a rational two-element subset would give
a quadratic factor of h. This independently checks rational selection.
The individual field decomposition of B, D, S^[2] and the tensor
factor is not being claimed.

### Infinity: exact arithmetic residue fields

Use tau=1/r. The distinguished root has a pole, and phi(r) has pole
order eleven. Since the quotient's local indices over infinity are
eleven, tau has order one at every normalized branch. Rescale the
other roots as a=r A and b=r B. The exact polynomial

    tau^11*(phi(X/tau)−phi(1/tau))

is integral in Q[tau,X] with reduction −1215(X^11−1). Each of its
eleven distinct roots at tau=0 therefore lifts uniquely over
L=Q(zeta_11) as a formal power series in tau. The distinguished root
is X=1. Consequently the quotient branches over L are precisely
unordered pairs {zeta_11^i,zeta_11^j}, with distinct nonzero exponents
i,j modulo eleven. There are binom(10,2)=45 such branches, already
the complete geometric count. No leading-coefficient radical is
needed: dividing all roots by the actual r removes that common scale.

All coefficients of each pair's symmetric series belong to L, and
Galois acts on exponents by multiplication by m in (Z/11Z)*. Its
stabilizer is exactly the stabilizer of the leading pair: uniqueness
of the formal lifts proves one implication, and distinct leading
pairs prove the other. The leading sum and product can also be read
as residues of 2u/r and (u²+3z)/r² in the normalized branch. They
therefore generate its exact residue field. The local parameter tau
is rational and fixed by Galois, so its completed ring is k[[tau]]
for the fixed field k of that pair's stabilizer. This establishes
arithmetic residue descent on the normalization, not just geometric
inertia counts.

A multiplier fixing the pair either fixes each exponent, and is 1,
or swaps them, in which case m²=1, m=−1 and j=−i. The five inverse
pairs have stabilizer {1,−1} and form one orbit of size five. The
remaining forty pairs have trivial stabilizer and form four orbits
of size ten. Thus the five closed points have residue fields
L^+ once and L four times, all with index eleven. Their weighted
degrees are 11*(5+4*10)=495. None is rational.

### Certificate, qualifications and continuation

Run `python3 scripts/global-fiber-genus/rational_boundary.py`.
The full evidence is
`scripts/global-fiber-genus/rational-boundary-certificate.json`.
The script checks the entire polynomial identity, every zero/one
label and cycle and category, all infinity arithmetic orbits and
stabilizers, the exact valuation arithmetic and the unit 1/4.
All 775 checks pass with no failures; 495 labels meet the cap 1000,
and each weighted fiber degree is exactly the required 495. The
unbounded formal-lifting and rational-exclusion arguments above are
the proof, not the finite enumeration by itself. No old certificate
was modified or used as a preview-based proof.

The rational boundary calculation succeeds. The stronger continuation
test asking for every individual nonrational residue field is not
fully met: the simple-root algebras at one are presented but not
split, and many nonrational zero branches are uncomputed. No complete
arithmetic boundary-field classification is asserted. No open
rational point is excluded, no effective rational-point method is
supplied, and neither L095 power/gcd/positivity system, remaining
global factors, minus-eleven branch nor Beal's conjecture is resolved.
The separate critical application audit is recorded below.

### Independent critical audit — 2026-10-20

Verdict: **PASS without mathematical correction**, for the stated
rational boundary classification, normalized unit and infinity fields.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-rational-boundary-critical-audit.md`.
This audit does not certify the unfinished nonrational decomposition
or add an open-point or integer exclusion. The mathematical inputs
remain audited L097 and L107, with L106 through L107.

The normalization theorem is used on the actual reduced finite-type
curve over Q, which is Nagata, and its finite normalization. The
complete local rings are DVRs, not merely local rings of an affine
collision. For the formal lifts the additional explicit primary
locators are Stacks Lemma 10.153.9
[tag 04GM](https://stacks.math.columbia.edu/tag/04GM) (complete local
rings are henselian), Lemma 10.153.2 and Lemma 10.153.3(2)
[tag 04GE](https://stacks.math.columbia.edu/tag/04GE) (uniqueness and
existence for a simple residual root, including nonmonic polynomials).
Their statements and essential proofs were inspected in the prior
assessment. The hypotheses hold over the characteristic-zero power
series rings used here. In particular a nonzero constant derivative
is a unit; no integrality at a rational-number prime is needed for
these formal lifts. The separate three-adic lift uses derivative
2d, a unit modulo three.

At finite boundary points division by the constant leading coefficient
really gives a monic equation for every root. Thus r,u,z are integral,
and rationality of a normalized point forces their residues to be
rational. At zero, r must tend to gamma, and the unique simple
gamma-root cannot occur again in the pair. The same-cluster cases
have nonrational midpoint. For the remaining case, rationality of P
gives Q[[tau]], and extending the constant field gives E[[tau]];
there is no additional residue extension. The pair polynomial
(T-u)^2+3z has distinct residual roots alpha,beta over E, so unique
simple-root lifting puts a,b in E[[tau]]. Both differences x,y have
order one because their fifth-power leading terms have the same
order five as s. Their ratio therefore has residue in E. This is
the step that justifies testing C for a fifth root in E itself.
At d=1 modulo three the denominator 11+5d is 1 modulo three, whereas
the numerator is zero. The product 396 has exact valuation two,
so the numerator and C have exact valuation two. Divisibility by
five fails. The contradiction excludes a rational point without
asserting any uncomputed nonrational residue field.

At one, h is separable as well as irreducible, by characteristic zero,
and h(0)=55. Its roots are simple in phi(T)-1. A rational unordered
pair of two such roots would yield a degree-two factor of h, not
merely a degree-two subfield of its splitting field. A mixed pair
with one zero root would yield a rational h-root. Both are impossible.
For the remaining branch F(0,X)=-55(X^3-1) has derivative
-165 X^2 at each of its three roots, which is nonzero. The unique
two nontrivial lifts are interchanged by Gal(Q(zeta_3)/Q). Their
symmetric functions give a branch over Q((r)); the completed field
contains Q((s-1)) and r, which already generate Q((r)) since
s-1=-55r^3+O(r^4). Hence it is exactly Q((r)), with uniformizer r,
not a proper subfield or a ramified extension with the same affine
limits. The three choices of distinguished zero root lie in one
inertia orbit; the two orderings of its complementary pair give
the same quotient branch. Finally
(zeta_3-zeta_3^2)^2=-3 gives ord(z)=2 and unit 1/4, independently
of any finite series truncation. L107's full normalized residue
algebra is Q[h]/(h^2-1/4)=Q times Q, so there are exactly two
rational lifts. This is not evaluation of a degenerate quadratic
as a polynomial direct factor.

The entire support presentation over one also passes, including
all cases not needed for rational-point exclusion. To check absence
of hidden coefficient extensions, the following describes each
geometric branch and its descent. Simple roots lift uniquely as
series in delta=s-1 over their residue fields. Write t for a
chosen zero-limit root, so delta=phi(t)-1.

| Root/pair type | Parameter and residue data | Support |
| --- | --- | --- |
| r simple, both pair roots simple | delta and distinguished simple root with unordered other two | D |
| r simple, pair mixed | t is the unique zero root in the pair; the two simple roots retain their distinct roles | S^[2] |
| r simple, both pair roots zero | t is the missing zero root; the other two have rational symmetric series in t | S |
| r zero, both pair roots simple | t=r and the unordered simple pair | B |
| r zero, pair mixed | t=r, the simple pair member, and the ratio of the other zero root to r, with residue zeta_3 or zeta_3^2 | S times Spec Q(zeta_3) |
| all three zero | t=r and the unordered other two zero roots | Spec Q |

For the mixed pair with r simple, the chosen simple pair member
b(delta) belongs to the completion over the residue field; then
t=2u-b(delta) belongs there too. In the case of two zero pair
members, their sum is -t+O(t^2), so it has order one and no further
parameter extension remains. With r zero and a mixed pair,
(2u-b(delta))/r has residue zeta_3 or zeta_3^2, so the quadratic
constant factor is necessary as well as sufficient. In the other
rows the simple-root residues and pair invariants recover precisely
the indicated finite Galois set. The unique series lifts show the
same stabilizer for the whole branch as for these data. This proves
each support identification without assuming a Galois group for h.
The first row has e=1; the other rows have e=3. Their dimensions
168 and 56,8,28,16,1 reproduce all 495 sheets. The possible splitting
of S times Spec Q(zeta_3), or of the other finite étale algebras,
is neither assumed nor computed.

At infinity the distinguished root has no finite residue since
phi(r) has a pole. As its pole order is eleven times that of r,
L107's index eleven implies ord(1/r)=1. In the scaled polynomial
the derivative at a residual eleventh root xi is -13365 xi^10,
which is nonzero. Thus all eleven lifts are unique over
Q(zeta_11)[[tau]], tau=1/r, with no common-scale radical. For each
unordered pair the leading sum and product are residues of actual
invariant functions 2u/r and (u^2+3z)/r^2. Their stabilizer in the
cyclotomic Galois group is exactly the pair stabilizer: they
determine the two roots as an unordered set. Uniqueness of lifting
fixes every subsequent symmetric coefficient under that same
stabilizer. The residue field therefore both contains and is
contained in its fixed field. This establishes the whole field,
not just a lower bound on its degree. There is one inverse-pair
orbit with stabilizer {1,-1} and four trivial-stabilizer orbits,
giving exactly the asserted real degree-five field and four
degree-ten cyclotomic fields. All have e=11 and none is rational.

The independent replay is
`python3 scripts/global-fiber-genus/audit_rational_boundary.py`.
It does not import or execute the producer. It derives phi by
multinomial coefficients, checks every coefficient and exact scalar
record, and reconstructs each zero/one cycle by the closed formulas
for powers of the root permutation. Every stored cycle edge,
canonical start, category, index and histogram is checked; every
one of the 495 labels occurs exactly once at each fiber. At infinity
all 495 labels are independently reduced by translation to the
45 difference pairs, each with multiplicity eleven. All arithmetic
orbits are regenerated. Stabilizers are also computed from the
sum and product in Q[Z]/(1+Z+...+Z^10), independently of the
unordered-label test, and the two computations agree.

All 775 original named check values, every top-level field and the
complete schema are compared, including the honest incomplete-field
flag. The new audit has **2,289 passing checks, no failures**, with
input hashes and complete reconstructed records in
`scripts/global-fiber-genus/rational-boundary-audit-certificate.json`.
The actual label count is 495 against cap 1000, and each actual
weighted degree is 495 against required 495. The zero valuation
is 2 against required divisibility by 5; the normalized square
unit is 1/4; infinity degrees are 5,10,10,10,10. These finite
checks accompany the unbounded local proof above, not replace it.

No mathematical correction or new result beyond the existing
specialization was found. Both L095 integer systems, all open
rational points, remaining global-factor compatibility and the
minus-eleven branch remain unresolved.

## Mathlib

Full matching rational-boundary classification and supporting formal
branch/descent coverage in Mathlib were not checked. No absence claim,
Lean verification, or independent reproof of the imported normalization,
finite-étale descent or Kummer theorems is made.
