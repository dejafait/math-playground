# L117 — Fixed-lattice first moment meets the actual pole budget

## Hypotheses

Retain L089's fixed congruence family, algebraic closure, domains and
local conditions. In its notation set

    a=81*89h, b=729*89h, D=ab, m=-243c*89h,
    (A,B)=(A_*+a u, B_*+m u+b v), u,v in Z.

All these integers are fixed before R tends to infinity; a,b are
positive and b is odd. Let P_R be the set of these pairs with

    R/2<=A<=R, |B|<=R, B odd, R>=2.

A good pair has both full images at levels 120 and seven, as in L089.
For good pairs retain L090's six ordered-root parameters t_o, literal
E_o and full-coordinate fields F=G_o and C_o=G_o^nor. Fix any finite
exceptional parameter set Exc in U(Q-bar) before R grows. Retain
L101's d=6, delta=3317760 and absolute source constant xi>=5.
Use the qualified April 2020 IUT IV source and explicit Legendre
adjunction interpretation of L101; its authentication limitations
are not removed.

For any pair in P_R, good or otherwise, define

    f(A,B)=4A^3+27B^2,
    j=6912 A^3/f(A,B),
    H0=log Q, where j=N/Q, gcd(N,Q)=1, Q>0.

This definition is numerical for nongood pairs; it assumes no
semistability or native field for them. For good pairs L101 identifies
H0 with the actual all-place G_o-normalized height H for every ordering.
All logarithms are natural.

## Conclusion

Put x=R/(2a), y=R/b and, writing |P_R| for the pair count, set

    K=log(31R^3), Y=10 delta sqrt(K) log(2 delta K),
    E_fix=sum_(p prime, p divides 6ab) log p,
    W_R(A,B)=sum_(p prime, p<=Y, p divides f(A,B)) log p.

The following explicit first-moment upper bound holds:

    sum_(P_R) W_R <= F_R,
    F_R=E_fix |P_R|+3xy(log Y)^2
           +6(x+y)Y log Y+12Y^2 log Y.                 (1)

For all sufficiently large R (with every family constant, Exc and xi
fixed), at least R^2/(8D) good pairs in P_R have all six parameters
outside Exc and satisfy

    q_R=(log R)/8 <= H <= K,
    W_R<=B_R=delta sqrt(q_R) log(2 delta q_R)<=M(H),
    M(H)=3 delta sqrt(H) log(2 delta H)
                       -(delta+2)sqrt(H)-xi.          (2)

In particular, for each such pair and any one ordering, its actual
interval-pole cost T from L116 satisfies T<=M(H). L116 therefore
supplies a prime ell>=7 for that same member and literal F with
P1+, P2, P3 and v_ell(j)>=0. This supplies L098's extra premise.
The prime may depend on the ordering; no common prime is asserted.

This is an existential known-method specialization validated by the
separate step480 critical audit below. It is no essential IUT flaw, full initial-data repair,
selected-ell large-image assertion, or original finite B>=A result.
No effective R or estimate uniform in the lattice constants is claimed.

## Proof

### Coverage, imports and the bounded test

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-25-average-lattice-first-moment-specialization.md`
and its completed step476 source record. The present calculation is
the approved explicit application, not a new general sieve theorem.
Import the named Schwartz–Zippel lemma in Dana Moshkovitz,
[*An Alternative Proof of the Schwartz-Zippel Lemma*](https://eccc.weizmann.ac.il/report/2010/096/revision/1/download),
ECCC TR10-096 revision 1, 8 July 2010, sections 1–3, pp.1–2:
a nonzero total-degree-d polynomial in two variables over F_p has
at most dp zeros. Its trivial d>=p case is included. Here d=3 and
the application below has p>=5.

The relevant counting source is Cremona–Sadek,
[*Local and global densities for Weierstrass models of elliptic curves*](https://arxiv.org/pdf/2003.08454v3),
v3, 18 October 2021, Proposition 3.1 and proof, printed p.11.
Use its prelimit residue-block method. Its fixed-modulus density
asymptotic does not supply uniformity in p. The explicit translated
row bounds below are the needed application to this skew lattice.

For height coverage, Zywina,
[*Elliptic curves with maximal Galois action on their torsion points*](https://pi.math.cornell.edu/~zywina/papers/MaximalGalois.pdf),
15-page author version, Lemma 5.9 and proof, printed p.8, supplies
an upper logarithmic height bound in a coefficient box, not a lower
bound. The explicit denominator inequality below specifies the
envelope needed here and checks cancellation in the correct direction;
it does not reprove that general number-field theorem. Reuse L089's
audited application of the same source's Proposition 5.7 at the fixed
levels, giving a union of image exceptions of size at most
C R^(3/2) log R for fixed C. No conditional independence is imported.

The main gap remains original finite B>=A. The intermediate target
is a joint actual-family survivor with the sufficient budget of L116;
its downstream use is only the additional integrality premise of L098.
The test is whether the low-height, finite-parameter and weighted losses
are o(R^2) relative to the fixed positive lattice density. ATTEMPTS/036's
height-only obstruction is retained: the present argument needs
arithmetic counting beyond its scalar bound.

### A uniform envelope and actual-pole containment

For every pair, A>0 and B is nonzero, so f>0 and 0<j<1728.
The reduced denominator Q divides the positive integer f. Thus

    0<=H0=log Q<=log f<=log(4R^3+27R^2)<=K.            (3)

For H0>0, every prime with negative valuation of j divides f;
the converse is not asserted. Cancelling numerator factors can only
remove denominator primes and decrease H0. On H>=q_R with q_R>=1,
the function sqrt(z) log(2 delta z) is increasing: its derivative
is (log(2 delta z)+2)/(2sqrt(z))>0. Consequently the actual upper
endpoint U(H)=10 delta sqrt(H) log(2 delta H) is at most Y.
Every prime counted by the actual T of L116 therefore occurs in W_R,
and all its summands are nonnegative. Hence

    T<=W_R                                                   (4)

on good pairs in this height slice, for every ordering. W_R may
overcount primes outside the interval, primes already excluded by
S1–S3, and divisors cancelled in j. All are harmless for (4).

### Counts uniform in each moving prime

Choose integers v0,k solving

    B_*+b v0=1 mod 2, m+b k=0 mod 2.

They exist because b is odd. Odd B is exactly the condition
v=v0+k u+2w, with u,w in Z. In these variables the map to (A,B)
has linear part

    (u,w) -> (a u, (m+bk)u+2b w)

and determinant 2ab. The permitted u form one interval of length x;
for each permitted integer u the permitted w form an interval of
length y, with a center depending on u. No assertion that this
is a Cartesian rectangle in (u,w) is needed.

If p does not divide 6ab, this affine map is invertible modulo p.
The polynomial 4A^3+27B^2 over F_p is nonzero, with total degree
three, since p>=5. Its pullback is likewise nonzero, of degree at
most three. The named zero bound gives at most 3p root residue pairs
(alpha,beta) for (u,w) modulo p. For one root pair, the u interval
contains at most x/p+2 integers congruent to alpha. For each such
u, its translated w interval contains at most y/p+2 integers
congruent to beta. These elementary interval bounds hold for every
translation and both endpoint conventions. Therefore

    N_p=#{(A,B) in P_R:p divides f(A,B)}
       <=3p(x/p+2)(y/p+2)
       =3xy/p+6(x+y)+12p.                              (5)

The shear and offsets do not affect this bound. For primes dividing
6ab, instead use N_p<=|P_R|. Their number and E_fix are fixed;
we make no nonzero-reduction claim for them.

Sum (5) with weights log p for p<=Y; all sums are finite. For Y>=2,

    sum_(p<=Y) log p/p <= (log Y)^2,
    sum_(p<=Y) log p <=Y log Y,
    sum_(p<=Y) p log p <=Y^2 log Y.                    (6)

For the first inequality, put n=floor(Y) and bound by
log Y times sum_(k=2)^n 1/k. On each [k-1,k], 1/t>=1/k,
so this harmonic sum is at most log n<=log Y. The other
two inequalities use at most Y integers, each with log p<=log Y
and p<=Y. Adding the exceptional-prime contribution proves (1).
No prime-distribution result or growing product modulus is used.

### Low reduced height and fixed parameter exceptions

Let Z=R^(1/8). If H0<q_R, then the reduced denominator satisfies
1<=Q<Z. Since 0<N/Q<1728, for each such Q there are at most
1728 Q positive numerator choices. Counting also noncoprime choices
only enlarges the count, so the possible rational j-values number
at most 1728(Z+1)^2. L089's exact invariant equation permits at
most 2(floor(R)+1) pairs for each fixed j. Thus the number of
low-height pairs, including any good ones, is at most

    L_R=3456(R+1)(R^(1/8)+1)^2=O(R^(5/4)).             (7)

This uses the reduced denominator, not coefficient height. It
allows arbitrary numerator cancellation. For the fixed finite set
Exc, let n_Exc be the number of rational values in J(Exc).
Every ordered parameter equal to a point of Exc forces the rational
invariant into this finite set. The same fiber bound therefore
excludes at most

    E_R=2 n_Exc(R+1)=O(R)                               (8)

pairs, simultaneously for all six orderings. No stability of Exc
under Galois or under permutation of the roots is needed.

### The actual minimum budget dominates the weighted loss

Take R so large that q=q_R>=xi^2>=25. For s>=1 the derivative
with respect to s of M(s^2) is

    3 delta log(2 delta s^2)+5 delta-2>0.

Thus for H>=q, M(H)>=M(q). Also xi<=sqrt(q), and

    M(q)-delta sqrt(q) log(2 delta q)
      =sqrt(q)[2 delta log(2 delta q)-(delta+2)]-xi
      >=sqrt(q)[2 delta log(2 delta q)-(delta+3)]>0,    (9)

since log(2 delta q)>1 and delta>3. This justifies B_R in (2)
as a uniform lower bound on the actual residual budget over the
entire retained slice, without needing an upper-height replacement.

For explicit comparison, the L089 count also gives

    |P_R|<=xy+2x+2y+4, |P_R|=O(R^2).

Put t=log R. With all constants fixed,

    Y=O(sqrt(t) log t), log Y=O(log t),
    B_R asymptotic to (delta/sqrt(8)) sqrt(t) log t.

These follow directly from K=3t+log31 and q_R=t/8. In particular
B_R tends to infinity and

    F_R/(B_R R^2)
      =O(1/B_R+(log Y)^2/B_R
                  +Y log Y/(R B_R)+Y^2 log Y/(R^2 B_R))
      ->0.                                             (10)

For the only potentially large ratio,
(log Y)^2/B_R=O(log t/sqrt(t))->0. The remaining moving-prime
errors are bounded respectively by O(log t/R) and
O(sqrt(t)(log t)^2/R^2), and also tend to zero. Constants may
depend on the fixed lattice; no uniformity in a,b or h is claimed.

By the finite first-moment inequality, the number of pairs with
W_R>B_R is at most F_R/B_R=o(R^2). This estimate holds on the
whole P_R before any image restriction. L089 gives at least
R^2/(4D) good pairs for all sufficiently large R after subtracting
its two full-image exception sets. Removing from that good set
the pairs in (7), (8) and the weighted bad set leaves at least

    R^2/(4D)-L_R-E_R-F_R/B_R.                          (11)

The actual required threshold is

    (L_R+E_R+F_R/B_R)/R^2 <=1/(8D).

Its left side tends to zero by (7), (8), (10), whereas the right
side is fixed and positive. Hence (11) is at least R^2/(8D)
for all sufficiently large R. No statistical independence of
image, divisibility, height or parameter conditions is assumed.

Choose any surviving member. All original congruences, full images
and domains are unchanged. For each ordering L101 gives the same
actual H=H0, while L090 gives that member's literal F=G_o and C_o.
Equations (4), (9) and W_R<=B_R give T<=M(H), with sqrt(H)>xi
after enlarging R so q_R>xi^2. L116 now applies with its unchanged
delta, source sets and interval. The resulting ell has P1+, P2,
P3 and is outside the rational pole set, supplying precisely L098's
extra integrality premise for this member. This is the stated
consequence, not an assertion of all initial-theta-data conditions.

Full (a)–(c)/initial data/III/P7, directed-cover hypothesis (*),
generation/full repair, factor-four excess, actual action/factorization/
pilot, authentication/def=, essentiality and finite B>=A remain
unresolved. L105's large-image retention for this selected ell is
outside this estimate. No U/B descent, full B[ell] rationality or
global theta splitting is assumed. The separate audit below checks this scope only.

### Separate critical audit — 2026-10-25, step480

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-25-fixed-lattice-first-moment-critical-audit.md`.
Reuse its primary theorem coverage and the precise citations above.
This audit checks (1)–(11) and the application to the actual fields;
it neither reproves those general theorems nor extends the target to
L105's selected-prime image assertion. The established inputs are
L089, L090, L101 and L116 with their recorded source qualifications.

**Parity, moving primes and the finite sum.** Since b is odd, the
two parity congruences defining v0 and k are solvable. Substitution
v=v0+ku+2w is a bijection between Z^2 and the permitted parameter
pairs. Its composition with the coefficient map has determinant
2ab, which is nonzero modulo every p not dividing 6ab. An invertible
affine substitution is an automorphism of F_p[u,w]; hence it cannot
send the nonzero polynomial 4A^3+27B^2 to zero. Here p>=5 and the
degree is at most three, below p, so the inspected nontrivial case
of Schwartz–Zippel applies. There are at most 3p root residue pairs.

For each fixed root pair, there are at most x/p+2 allowed u values.
For each such u separately there are at most y/p+2 allowed w values
of the required residue. The center can depend on the actual u,
not merely its residue; the same interval bound still applies.
Multiplying and then summing over root pairs proves (5) without
assuming a rectangular parameter region or independent residues.
For the finitely many excluded primes, N_p<=|P_R| gives the E_fix
term even if some lie above Y. All weights are nonnegative. The
harmonic integral in (6) and the two integer-count bounds therefore
give exactly (1). In particular, no asymptotic with a prime-dependent
implicit constant was summed over moving primes.

**Cancellation and both discarded parameter sets.** A>0 and odd B
give 0<j<1728 and f>0. In lowest terms Q=f/gcd(6912A^3,f), so Q
divides f and every rational pole divides f. The envelope (3) is
valid also on nongood pairs. If Q<R^(1/8), enumerating each integer
Q and the fewer than 1728Q possible positive numerators gives at
most 1728(R^(1/8)+1)^2 invariant values, even before imposing
coprimality. For each value in (0,1728), the invariant equation in
L089 gives at most two B for each integer A. There are at most
floor(R)+1 such A. Thus (7) is valid with its displayed constant,
including for nongood pairs. No lower bound on Q is inferred from
large coefficients. For a fixed finite Exc, an excluded ordering
forces j into J(Exc) intersect Q. One union over these invariant
values handles all six orderings and proves (8), without a hidden
sixfold or Galois-stability requirement.

**Uniform actual budget and the limiting comparison.** On the
retained slice H>=q>=xi^2>=25, the derivative of M(s^2) is
3 delta log(2 delta s^2)+5 delta-2>0 for s>=1. Also xi<=sqrt(q).
Subtracting B_R from M(q) consequently gives at least
sqrt(q)[2 delta log(2 delta q)-(delta+3)]>0, since delta>3 and
log(2 delta q)>1. This verifies (9) in the needed direction;
an upper bound for H has not replaced H in the minimum budget.
The increasing interval endpoint and H<=K give U(H)<=Y, so actual
poles counted in T are a subset of the primes counted in W_R.

With t=log R, the four contributions to F_R/(B_R R^2) are bounded
respectively by constants times

    1/(sqrt(t) log t), (log t)/sqrt(t),
    (log t)/R, sqrt(t)(log t)^2/R^2,

for all sufficiently large R. Each tends to zero; the constants
depend only on the fixed data. The last two come from the explicit
6(x+y)Y log Y and 12Y^2 log Y errors, respectively. Thus the
finite first-moment inequality removes o(R^2) pairs. Equations
(7) and (8) remove O(R^(5/4)) and O(R) pairs. Subtracting these
sets from L089's at-least-R^2/(4D) good pairs is legitimate whether
or not the sets overlap or correlate with the image exceptions.
Their total divided by R^2 eventually falls below the fixed
positive threshold 1/(8D). This verifies (10), (11) and the claimed
at-least-R^2/(8D) survivor bound, not an effective value of R.

**Same-member selection and verdict.** L101's proof of H=log Q
applies before prime selection to every good member and ordering;
it is not limited to that lemma's existentially chosen witness.
It uses semistability and all actual F-places, and needs neither
P2 nor initial theta-data to identify this height. L090 defines
the literal F=G_o and C_o for each of these same members. On a
survivor enlarge the fixed R threshold to ensure q>xi^2; then
T<=W_R<=B_R<=M(H) and sqrt(H)>xi hold with L116's exact delta,
sets and interval. Its conditional theorem gives one ell outside
A union S_I, hence P1+, P2, P3 and v_ell(j)>=0 for this ordering.
The cited finite-set theorem is used with an enlarged set, not
with a different field or a separately selected member. L098 is
downstream only; its integrality premise was not assumed here.

The audit passes without changing any estimate or direct mathematical
input. It validates the stated known-method application, not new
mathematics beyond the checked sources. It does not combine this
prime with L105's image witness or with the later native assembly.
Authentication/def= qualifications, full initial data, generation,
the directed module, actual action/pilot and finite B>=A remain
unresolved. No candidate essential flaw is obtained.

## Mathlib

Full matching coverage for this constrained first-moment and joint
survivor statement has not been checked. Supporting coverage for
finite-field zero counts, rational heights and finite-sum inequalities
has not been checked either. No absence claim or Lean verification
is made. General inputs are imported at the precise primary locations
above; the explicit moving-prime, cancellation and joint-count
specializations are proved here.
