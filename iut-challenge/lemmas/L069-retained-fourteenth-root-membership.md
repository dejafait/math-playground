# L069 — Fourteenth-root membership in the unchanged retained field

## Hypotheses

Retain the same reselected curve E_0/Q, algebraic closure Omega of
Q_3, embedding and places u,w of L045 and L048. Write

F=Q(zeta_60,E_0[30]), K_glob=F(E_0[7]),
H=F_u=Q_3(zeta_60),
N=(K_glob)_w=Q_3(zeta_420,3^(1/7)) subset Omega.

Here zeta_420 is primitive of exact order 420. Division fields use
both coordinates of every geometric torsion point. Full geometric
30-torsion is F-rational and full geometric 7-torsion is
K_glob-rational. Keep the original-cubic precision
M>=max(M_tors,31). L048 gives a pointed Q_3-isomorphism from this
same E_0 to E_(q_0), where q_0 in Q_3 is nonzero and
v_3(q_0)=30, with v_3(3)=1. Reuse L054's s in H with s^2=q_0.

Do not assume q_0=3^30, K_glob=N, an identification with a native
field bearing the name K_w, or a source-marked pilot representative.

## Conclusion

There exist t,rho in the unchanged embedded N such that

t^7=q_0, rho^14=q_0, rho^2=t and rho^7=s.

Every root of X^14-q_0 in Omega belongs to N: the set of roots is
rho mu_14, with mu_14 subset N. Consequently N(rho')=N for every
such root rho', and v_3(rho')=15/7. This closes existential local
radical membership only. It neither assigns a native marking nor
proves native field applicability, image factorization, sufficient
initial data, essentiality or the original finite B>=A comparison.
The separate critical audit below validates this specialization; no
progress beyond the checked known methods is claimed.

## Proof

### Imported results and exact scope

Reuse the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-17-retained-fourteenth-root-membership.md`.
Milne, *Elliptic Curves*, second edition (2021),
[III.3, pp.102–103, finite-extension statement after (26)](https://www.jmilne.org/math/Books/EC2.pdf),
gives Tate's same-field group identification E_q(L)=L^*/q^Z for
finite extensions L/Q_p and q in Q_p^* with |q|_p<1.
Kedlaya, *Introduction: the Tate curve*, fall 2004,
[Theorem 1, p.3 and group-law discussion p.4](https://kskedlaya.org/18.727/tate-curve.pdf),
also states the equivariant surjection with this kernel, including
finite extensions. Import this named theorem without reproof.
Milne, II.6 Proposition 6.3, pp.70–71 of the same book, gives
geometric n-torsion isomorphic to (Z/nZ)^2 when n is prime to field
characteristic. The characteristic is zero here; residue
characteristic three does not restrict n=7 or n=30.

The theorem is not already a statement about this changed curve's
named division-field completion. The following checks its full
torsion and representative hypotheses, then performs only elementary
integer and root algebra. No uniformization or torsion theorem is
reproved. L053's chosen geometric root is not used as an N-valued
representative; its point-group result is not a duplicate membership
proof. L042's old q=3^30 is not substituted for q_0.

### Full seven-torsion in the same field

L045 identifies the full global and local geometric torsion sets
for E_0: the coordinatewise injection from its embedded Q-bar points
to its Omega points is bijective at level seven, since both sets
have 7^2=49 elements by Milne II.6.3. Every coordinate in that full
global list belongs to K_glob by definition. The retained embedding
K_glob -> (K_glob)_w=N therefore places all 49 geometric points in
E_0(N). Conversely every N-rational seven-torsion point is geometric,
so E_0(N)[7] has exactly 49 elements. This is full torsion
rationality, not merely rationality of one cyclic subgroup.

L048 applies L045 to this same reselected E_0. Its pointed
Q_3-isomorphism transports all 49 points to E_(q_0)(N)[7]. The
field N is a finite extension of Q_3 inside Omega, q_0 belongs to
Q_3^*, and v_3(q_0)=30>0. Thus the imported same-field theorem
identifies E_(q_0)(N) with N^*/q_0^Z. In particular each of these
49 classes has an actual representative in N^*.

### Representative exponents give a seventh root

For a class [z] killed by seven, with z in N^*, there is an integer
m such that z^7=q_0^m. The integer is unique because q_0 has
nonzero valuation. Replacing z by z q_0^a changes m to m+7a;
thus m modulo seven is independent of representative choice.

If m=7r, then (z q_0^(-r))^7=1. Hence every class with m divisible
by seven has a representative in mu_7(N). A degree-seven
polynomial over a field has at most seven roots, so there are at
most seven such classes. Since there are 49 seven-torsion classes,
at least one has m not divisible by seven. For that class choose
its same-field representative z. As seven is prime, gcd(m,7)=1;
choose integers a,b with am+7b=1 and put t=z^a q_0^b in N^*.
Then

t^7=(z^7)^a q_0^(7b)=q_0^(am+7b)=q_0.

Only integral powers of nonzero elements already in N are used,
including when the exponents are negative. There is no passage
from a fixed geometric class to a supposedly fixed representative.

### Combining the roots and retaining every choice

By L054, s in H subset N satisfies s^2=q_0. Set rho=s/t^3 in N^*.
Using t^7=q_0 gives

rho^2=q_0/t^6=t,
rho^7=s^7/t^21=s^7/q_0^3=s,
rho^14=q_0.

Put eta=zeta_420^30 in N. For any integer j, eta^j=1 exactly when
420 divides 30j, equivalently 14 divides j. Thus eta has exact
order 14 and its fourteen powers are distinct roots of X^14-1.
That polynomial has degree 14, so these exhaust mu_14(Omega)
and all lie in N. If rho' in Omega satisfies (rho')^14=q_0,
then (rho'/rho)^14=1, whence rho' belongs to rho mu_14 subset N.
Conversely every element of that coset is a root. This proves
every root choice is in the unchanged field, not just one choice.
The absolute valuation of any such root satisfies
14 v_3(rho')=v_3(q_0)=30, hence v_3(rho')=15/7.

The representative ambiguity has therefore been controlled both
in the Tate quotient (integral q_0 powers) and among radicals
(mu_14). It has not been identified with a specified native pilot
or its transported markings. The conditional use in L068 and
foundations/05 still needs its independent native field and image
hypotheses. ATTEMPTS/027's exact-curve stop, ATTEMPTS/031's marked
coordinate stop and ATTEMPTS/032's enclosure-objection stop remain
intact. No mathematical script or numerical certificate is needed
for this finite counting and exact algebra.

### Separate critical audit — 2026-10-17

**Verdict and inputs.** The statement passes the pre-invocation
SPECIALIZE assessment
`drafts/literature/2026-10-17-retained-fourteenth-root-critical-audit.md`.
No correction, additional mathematical hypothesis or new direct input
is needed. Reuse the precisely inspected Milne II.6 Proposition 6.3
and III.3 statement after (26), and Kedlaya Theorem 1, cited above.
The direct inputs remain L045, L048 and L054. L042 is historical
packet context, not permission to replace the changed parameter.

**Complete torsion and the embedded completion.** In L045 the
coordinate inclusion E_0(Q-bar)[7] -> E_0(Omega)[7] preserves the
identity and multiplication by seven and is injective. Both sides
have 49 elements by the cited characteristic-zero torsion theorem;
thus it is onto. Every coordinate of every point in this list is
adjoined to K_glob, and its embedding in N retains those coordinates.
This supplies all 49 points, not just a rational cyclic subgroup.
L045's completion proof uses both inclusions: K_glob=F(S_7) is
contained in N, and its closure contains H, the closure of F, and
S_7, hence contains H(S_7)=N. L048 fixes the stronger precision
before reselection and applies that argument to the same E_0.
It also gives the pointed Q_3-isomorphism with E_(q_0), so all 49
points transport as torsion points over N. No global field is
identified with its completion.

**Actual representatives and counting.** N/Q_3 is finite, q_0 is
nonzero in Q_3, and v_3(q_0)=30>0. These are the hypotheses of
the same-field Tate theorem: its surjectivity over N supplies an
element of N^* for every rational point. For a seven-torsion class,
z^7=q_0^m has a unique integer m, since q_0 has infinite order.
All representatives are zq_0^a, a in Z; their exponents are m+7a.
If m=7r, the same class is represented by zq_0^(-r) in mu_7(N).
The map from this at-most-seven-element root set onto the classes
with zero exponent residue proves the required upper bound; no
injectivity of that map is necessary. Since 49>7, a nonzero residue
occurs. Seven being prime is essential to gcd(m,7)=1. For integers
a,b satisfying am+7b=1, the exact identity
(z^a q_0^b)^7=q_0^(am+7b)=q_0 verifies the Bezout sign.
All inverses exist, so negative m,a,b or r introduce no extension.
Taking fixed points of a geometric quotient is never used in place
of the imported same-field surjectivity.

**Simultaneous identities and every root choice.** Reuse L054's
audited s in H subset N; q_0!=0 implies s!=0 and t!=0. For
rho=s/t^3 the two identities are independently checked:
rho^2=t^7/t^6=t, and rho^7=s^7/(t^7)^3=s^7/(s^2)^3=s.
Consequently rho^14=s^2=q_0. This works for the supplied s and
the t just constructed without a compatibility choice or further
radical extraction. The primitive zeta_420 has its exact order in
N itself. The equivalence 420 | 30j iff 14 | j proves that its
thirtieth power has order fourteen. Its fourteen powers exhaust
X^14-1 by the polynomial degree bound. Dividing any root of
X^14-q_0 by rho therefore puts it in this root set, and conversely
multiplying rho by any of these roots gives a root of X^14-q_0.
Thus all choices, not merely the constructed compatible choice,
lie in N. The simultaneous identities with fixed s,t are asserted
for the constructed rho; they are not asserted for every rho'.
For every rho', valuation gives 14v_3(rho')=30 and v_3(rho')=15/7
in the absolute normalization, without changing the field.

The audit secures existential radical membership only. It selects
neither a native marking nor a comparison map. Native field
applicability, all-image factorization, sufficient initial data,
additional global hypotheses, essentiality and finite B>=A remain
unproved. ATTEMPTS/027,031,032 are unaffected. These are exact
finite counting and algebra checks; no numerical certificate or
mathematical script is needed. Mathlib coverage remains as below.

## Mathlib

Full matching coverage of Tate uniformization and this retained
named-field specialization has not been checked in Mathlib. No
absence claim is made. The proof imports the precisely cited known
theorems and supplies their applicability and elementary root algebra;
it claims no discovery beyond the sources checked.
