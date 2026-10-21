# L073 — An auxiliary p=89 family realizes the joint scalar

## Hypotheses

Retain L044's local standard Tate curve E_q, q=3^30, its monic
cubic f in Z_3[x], and its embedded fields
H=Q_3(zeta_60), N=Q_3(zeta_420,3^(1/7)) in Omega. Fix
M>=max(M_tors,31) as in L048 and put h=3^M. Fix the integer c
from L046 with c congruent to 1/4 modulo h. Let d_0,e_0 be
integer representatives of the other two coefficients of f modulo h.
All these choices remain fixed as coefficient boxes grow.

Work in the algebraic closure Q-bar of Q inside Omega. Division
fields use both coordinates of every geometric torsion point. The
curve and global fields below are new auxiliary witnesses; none is
identified with the retained E_0, F or native K_glob.

## Conclusion

There exists an integer cubic

    g_aux=x^3+c x^2+d x+e congruent to f modulo h

whose pointed elliptic curve E_aux/Q has all these properties:

1. Its full local 210-torsion is G_Q_3-isomorphic to E_q[210].
   Its full 30-torsion is H-rational and H(E_aux[7])=N inside Omega.
2. It has split Tate reduction over Q_3, with its own parameter
   q_aux satisfying v_3(q_aux)=30, and its global mod-7 image over
   Q is GL_2(F_7).
3. Set K_aux=Q(zeta_60,E_aux[2]) and
   F_aux=K_aux(E_aux[15])=Q(zeta_60,E_aux[30]). There is one
   tau in G_(K_aux) acting as -Id on E_aux[8] and Id on
   E_aux[15]. In particular this same tau fixes F_aux pointwise.
4. F_aux/Q is Galois of degree dividing 2^14*3^3*5. Its induced
   completion is H; the induced completion of F_aux(E_aux[7]) is N.

The refined short-coefficient family has fixed index
D_aux=89^2*3^(2M+10) in Z^2 and box count
4R^2/D_aux+O_(c,h)(R+1). The result is existential: no effective
M or particular global coefficient pair is claimed. It supplies
the scalar-occurrence condition for this auxiliary family, not for
the retained E_0. The separate critical audit below validates this
known-method specialization; it is not a candidate resolution of the
IUT challenge.

## Proof

### Imported results and scope

Use the prior SPECIALIZE assessment
`drafts/literature/2026-10-17-auxiliary-89-frobenius-family-test.md`.
Import J.S. Milne, *Elliptic Curves*, second edition (2021),
[II.6 Corollary 6.2/proof, pp.70–71; IV.9 Theorem 9.4/proof,
p.150; V.7 Proposition 7.5/(46), p.217; V.8 Propositions 8.1
and 8.3/proofs, pp.220–221](https://www.jmilne.org/math/Books/EC2.pdf).
For good reduction at p and torsion primes different from p,
reduction identifies the unramified torsion action of an arithmetic
Frobenius lift with the p-power Frobenius of the reduced curve.
The latter satisfies pi^2-[a_p]pi+[p]=0, with
a_p=p+1-#E(F_p). We import the endomorphism identity and reduction
theorems, rather than infer a scalar from trace and determinant alone.

For the exceptional count and cyclotomic determinant use David
Zywina, *Elliptic curves with maximal Galois action on their torsion
points*, Bull. London Math. Soc. 42 (2010), 811–826,
[author version, section 1.1 pp.1–2, Definition 5.1 p.6,
Proposition 5.7/proof p.8, and Lemma 2.4 proof p.5](https://pi.math.cornell.edu/~zywina/papers/MaximalGalois.pdf).
For k=Q and fixed level 7, among nonsingular integral short models
in the maximum-norm box the number failing SL_2(F_7) containment
is O(R^(3/2) log R); containment gives full GL_2 image over Q.
The determinant of the full torsion representation is the cyclotomic
character. Reuse L046's inspected sieve and coordinate coverage.
No general source theorem is reproved. The finite-field, fixing and
refined-family calculations below are the required specialization.

### Compatible congruences and good reduction

In F_89 prescribe

    d=c^2/3, e=c^3/27+1.

Here 3 and 27 are inverted only in F_89. Since gcd(h,89)=1,
the Chinese remainder theorem gives integers d_*,e_* with

    d_*=d_0 mod h, d_*=c^2/3 mod 89,
    e_*=e_0 mod h, e_*=c^3/27+1 mod 89.

The full compatible family is
d=d_*+89h s, e=e_*+89h t, s,t in Z. Every original cubic is
monic and congruent to f modulo h. Modulo 89 its equation becomes

    y^2=(x+c/3)^3+1.

The translation z=x+c/3 is invertible over F_89 and preserves the
point at infinity. The discriminant of y^2=z^3+1 is -432,
which is 13 modulo 89, hence nonzero. Equivalently its cubic has
discriminant -27, also nonzero. Thus every member has good reduction
at 89. There is no good-reduction assertion at 3.

### Exact point count and one actual lift

Since 89-1=88 and 3*59=177=1+2*88, the map z -> z^3 is a
bijection of F_89: its inverse on nonzero elements is z -> z^59,
and it fixes zero. For each of the 89 values y, exactly one z
satisfies z^3=y^2-1. Consequently the reduced curve has exactly
89 affine points and its unique rational point at infinity, so
#E_aux(F_89)=90 and a_89=0. This is a complete elementary count,
not numerical evidence or a supersingular-classification import.

Choose a place of Q-bar above 89 and one element sigma of its
decomposition group lifting arithmetic Frobenius, whose residue
action is x -> x^89. The decomposition group surjects onto the
residue Galois group, so such a lift exists. All primes dividing
120 are different from 89. The imported good-reduction theorem
therefore identifies the action on each prime-power part of the
entire E_aux[120] with the reduced Frobenius action; inertia is
trivial on those modules. The imported endomorphism identity is
pi^2+[89]=0. Hence, for tau=sigma^2,

    rho_120(tau)=[-89]=[31] mod 120.

In particular -89=-1 mod 8 and -89=1 mod 15. These are actions
of the same actual element, not independently lifted marginal
matrices. We use arithmetic, not inverse geometric, Frobenius.

The restriction to E_aux[2] is identity. Also
det rho_120(tau)=(-89)^2=7921=1 mod 120. By the cyclotomic
determinant theorem tau fixes every 120th root of unity and hence
the chosen zeta_60. It thus fixes both generators of K_aux and
belongs to its actual absolute Galois group in this Q-bar.
Identity on E_aux[15] then puts the same tau in G_(F_aux).
The equality F_aux=Q(zeta_60,E_aux[30]) follows because
E_aux[30]=E_aux[2]+E_aux[15] equivariantly: multiplication and
the group law express each side's full points from the other.
Fixing means pointwise fixing of both coordinates, not just setwise
preservation or fixing x-coordinates.

### Full-rank count and the mod-7 requirement

Use L046's pointed Q-coordinate change

    X=9x+3c, Y=27y,
    A=81d-27c^2, B=729e-243cd+54c^3.

It gives Y^2=X^3+AX+B and is an invertible pointed Q-isomorphism.
Let A_*=81d_*-27c^2 and B_*=729e_*-243cd_*+54c^3. The refined
short coefficients are exactly

    (A_*,B_*)+(81*89h s,-243c*89h s+729*89h t).

The triangular parameter matrix has determinant
(81*89h)(729*89h)=89^2*3^(2M+10)>0. Its first coordinate
determines s and its second then determines t; there is no loss
of dimension from fixing c or adding the two independent congruences.

For |A|<=R, the number of s is 2R/(81*89h)+O(1). For each
such s, |B|<=R allows 2R/(729*89h)+O(1) integers t, with an
error uniformly bounded in the center of its interval. Multiplying
and summing gives

    #family in [-R,R]^2=4R^2/D_aux+O_(c,h)(R+1).

All these models are nonsingular: their original discriminants are
already units at 89, and the pointed Q-isomorphism preserves
nonsingularity. The imported exceptional bound holds for the whole
short-coefficient box, hence bounds exceptions within this family.
For fixed c,h and 89, the ratio of that bound to the leading family
count is O(D_aux log R/sqrt(R)), tending to zero. The family error
divided by its leading term also tends to zero. Thus for all
sufficiently large R there is a family member whose mod-7 image
contains SL_2(F_7), and hence is GL_2(F_7) over Q. Its pointed
Q-isomorphism transfers that image to the original cubic. There is
no uniformity claim in M and no effective coefficient-size bound.
Every such chosen member also has the same Frobenius-square property
proved above, since it was proved for the entire refined family.

### Retention for that same auxiliary witness

Apply L044 to this member's original monic cubic: its full local
210-module agrees with E_q[210], since the required precision and
all coefficient congruences persist. Restricting the equivariant
isomorphism to G_H and to levels 30 and 7 gives full H-rational
30-torsion and equality of the full 7-coordinate fixing kernels.
Thus H(E_aux[7])=N as embedded fields, exactly as in L044/L046.

L048 applies to every original cubic in this fixed neighborhood,
independently of the new congruences: the discriminant valuation is
30, c4 is a unit, the characteristic-3 node is split, and the
unique changed Tate parameter q_aux has v_3(q_aux)=30. Local
constancy alone is not being used to infer this geometric property.

Finally apply L045 to E_aux with
F_aux=Q(zeta_60,E_aux[30]). Its hypotheses have just been verified
for this same witness. It gives the stated Galois degree divisibility
and the embedded completions H and N, with the places induced by
the unchanged local embedding. These are new global fields and
places; equal completions do not identify them with the retained
ones. No equality q_aux=q_0 or q_aux=3^30 is inferred.

All three continuation tests pass: exact reduction/Frobenius,
one actual joint fixing element, and a positive full-rank family
surviving the exceptional bound. L071/L072 are possible downstream
applications, not inputs or claims about the retained curve here.
Native T/model, exact generation, independent initial data, marked
all-image factorization, pilot transport, essentiality and original
finite B>=A remain unresolved. ATTEMPTS/027,028,031,032 are intact.

### Separate critical audit — 2026-10-17, step 288

The pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-17-auxiliary-89-family-critical-audit.md`
covers this audit. The imported theorems and their hypotheses are those
cited above; the relevant complete applications in L044, L045, L046
and L048 were checked. No new source theorem, effective approximation
precision or downstream radical conclusion is used. All claims in the
Conclusion pass, with no change to their mathematical hypotheses.

**Complete reduction and count.** Expanding (x+c/3)^3 gives
x^3+c x^2+(c^2/3)x+c^3/27. Thus both prescribed congruences,
with arbitrary fixed c modulo 89, give exactly the stated translated
curve. Its discriminant is -16*27=-432=13 modulo 89, so the
original integral equation defines a smooth elliptic model at 89;
the infinity section is smooth as well. No minimal-model assumption
at another prime enters this good-reduction check. For every nonzero
z, z^(3*59)=z^177=z by z^88=1, and zero is fixed. Hence each
y in F_89 determines exactly one z with z^3=y^2-1. This counts
every affine point once, and homogenization gives exactly the one
rational infinity point. The total is 89+1=90, and a_89=0.

**One element at the complete finite level.** The three primary parts
of level 120 are E[8], E[3] and E[5]. Good reduction and
89 not dividing 120 make the respective reduction maps isomorphisms
on geometric torsion, equivariant for one chosen decomposition group.
Its quotient onto Gal(F_89-bar/F_89) permits an actual lift sigma
of the 89-power arithmetic automorphism. Inertia acts trivially on
each of these three parts. The cited identity pi^2+[89]=0
therefore gives, simultaneously, sigma^2=[-89] on each part.
Their direct-sum decomposition is the complete E[120], so
tau=sigma^2 acts there by [31]. This invokes the endomorphism
identity itself, not just a matching characteristic polynomial or
separately chosen lifts. In particular 31=7 modulo 8 and 31=1
modulo 3 and 5, giving exactly (-Id on E[8], Id on E[15]).

The Weil-pairing determinant comparison at level 120 is applicable
in characteristic zero; it gives chi_120(tau)=(-89)^2=7921
=1+66*120. Thus tau fixes mu_120 pointwise, including the chosen
zeta_60. Its scalar action on E[2] is identity. These facts put
tau in the actual G_(K_aux), not merely in a conjugate or abstract
image. Identity on E[15] then fixes F_aux pointwise. To check
the displayed equality of division fields explicitly, for P in
E[30] write P=[15]P+[16]P: the first summand is killed by 2,
the second by 15, and [31]P=P. Conversely both smaller torsion
groups lie in E[30]. The group law is defined over Q, so this
is an equality of fields generated by full coordinates, including
the rational identity, rather than an equality of x-coordinate fields.

**Family dimension and required count.** The two coefficient CRT
conditions are independent because gcd(3^M,89)=1 and d,e vary
independently while c is fixed. In the original coefficients the
step is 89h in each variable. Substituting X=9x+3c,Y=27y in
the short equation gives exactly 729(y^2-x^3-cx^2-dx-e)=0;
the projective change is invertible over Q and preserves infinity.
Consequently the lattice of short coefficients has triangular
steps a=81*89h and b=729*89h, and determinant ab=D_aux.
There is one parameter pair per coefficient pair. Both steps and
all offsets remain fixed as R grows.

For each admitted s the interval for t has length 2R/b, independent
of its center. Using integer-count error at most 2 for each closed
interval gives the explicit sufficient lower bound

    #family >= 4R^2/D_aux - 4R/a - 4R/b - 4.

All family members are nonsingular by the unit discriminant at 89.
For some fixed C and sufficiently large R the cited whole-box
exceptional bound is at most C R^(3/2) log R. Hence a sufficient
threshold for at least one nonexceptional member is

    C log R/sqrt(R) + 4/(aR) + 4/(bR) + 4/R^2 < 4/D_aux.

The left side tends to zero, and the right side is a fixed positive
number. This verifies existence at fixed M without requiring an
effective C or M_tors. Whole-box exceptions bound the subfamily's
exceptions even if a curve has multiple integral models. Zywina's
Q-case criterion then supplies GL_2(F_7), and the pointed map
transfers it to the original cubic. No sieve theorem for a newly
restricted family, uniformity in M or disjointness is being assumed.

**Retention uses that same member.** Every refined member, before
any short coordinate change, is a monic degree-three polynomial
congruent to f modulo 3^M. Thus L044's squarefree finite-torsion
neighborhood at m=210 applies, including its 3-primary part.
Restriction to G_H preserves the full pointwise kernels, giving
the embedded H-rational 30-torsion and H(E_aux[7])=N. The
choice from the sieve does not alter any of these universal facts.
Likewise L048's integer invariant congruences apply to every such
original member: M>=31 preserves v_3(Delta)=30 and unit c4,
and its reduced node has the two distinct F_3-rational tangents.
Its minimality and split Tate conclusion therefore give the chosen
member's own q_aux with v_3(q_aux)=30. Constancy of finite
torsion is not substituted for this reduction argument.

Finally these are precisely L045's curve hypotheses. The full global
and local torsion sets agree in Omega, so adjoining all 30-torsion
globally gives F_aux contained in H and containing Q(zeta_60),
whose closure is H. Adjoining all 7-torsion then has closure N.
L045's Galois-compositum divisibility proof applies to this same
curve and yields 2^14*3^3*5, without a disjointness assumption.
Neither identical completions nor these degree constraints identify
the auxiliary global fields, places or parameter with the retained
ones. No use of L047 or a restricted mod-7 image conclusion is
needed here; the direct DAG inputs remain unchanged.

The audit validates only the auxiliary family and scalar occurrence
by known methods. It establishes no retained radical membership,
ordered-root Legendre torsion verdict, native T/model, minimal
generation, independent initial data, all-image factorization, marked
pilot transport, essentiality or original finite B>=A comparison.
The elementary exact arguments suffice; there is no numerical or
finite-preview certificate standing in for an infinite assertion.

## Mathlib

Full matching and supporting Mathlib coverage of this auxiliary
family specialization has not been checked. No absence or formal
verification claim is made. The general reduction, Frobenius,
determinant and sieve results are imported with precise citations;
the finite count, fixing field and refined lattice are explicit
specializations. No new general theorem beyond the checked source
methods, or numerical certificate for an explicit global curve,
is claimed. The separate audit above validates the informal specialization;
it does not claim formal verification.
