# Lemma 428: fixed prime correlations exclude uniformly bounded bulk raw densities

## Hypotheses

Write E_H u=H^(-1) integral_[H,2H] u(t) dt, ell=log H, and
chi_p(t)=p^(-it) for each positive prime p. Let f be the real
normalized critical function of L389 (3), so
f(t)^2=|zeta(1/2+it)|^2, including at zeros. Use the audited
order-zero fixed smooth rational-twist moment L381 (7).

For every sufficiently large real H, suppose a proposed conditional
critical-state law has height marginal dt/H and total raw x-second
density q_H(t)=B_H(t)+r_H(t), with measurable nonnegative terms.
Here B_H is the bulk contribution, including its fiber probability
and its conditional mean square; r_H includes every other component.
Assume one constant 0<=C<infinity, independent of H, satisfies

    0<=b_H(t):=B_H(t)/ell<=C almost everywhere,
    E_H r_H=o(ell).                                      (1)

Neither b_H nor the law need be a fixed function of prime phases,
and no consistency between different H is assumed. Matching a fixed
prime correlation means

    E_H[(q_H-f^2) chi_p]=o(ell) as H tends to infinity.     (2)

The little-o and its onset may depend on p. All tests are fixed before
the height limit. No conditional actual critical moment is assumed.

## Conclusion

Such a family cannot satisfy (2) for every fixed prime p. More
precisely, for every proposed C there is a finite fixed set P of
primes with sum_(p in P) 1/p>C^2; the correlations (2) for this
finite set already contradict (1).

Consequently L421/L423's bounded-bulk mechanism, with their retained
lower-order rare second integrals, cannot be extended to match every
fixed single-prime correlation while keeping (1). This includes any
retuning that still has a uniformly bounded normalized bulk raw
density and total rare second integral o(ell). It does not reject
their original selected finite lists, exclude fitting a prescribed
finite prime list with a bound depending on that list, or supply an
actual critical-function law. Actual clipping, capped nondegeneracy,
L413's full-error regulator margin and global mixed positivity remain
unresolved. The separate step-208 critical audit below validates this
known-input specialization without changing its hypotheses or conclusion.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-17-finite-prime-covariance-domination.md`,
whose COVERED_TARGET is the saved target of step 205. This is a local
REPRODUCTION using known moment and Hilbert-space inputs; no novelty
or new zeta moment theorem is asserted. The additional proof is needed
because smooth complex twists do not admit order bracketing, the
finite-height prime characters are not orthogonal, and the proposed
density may depend arbitrarily on H.

### Sharp single-prime moments by nonnegative polarization

Import M. P. Young, *A short proof of Levinson's theorem*, Arch.
Math. 95 (2010), 539--548, DOI 10.1007/s00013-010-0199-9,
[Lemmas 4--5, (4.1)--(4.5), pp. 542--543](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf),
through audited L381 (7). For fixed positive integers h,k and a fixed
rescaled smooth weight 0<=w<=1 supported in [H/2,3H], with
w^(j)=O_j(H^-j), that specialization states

    integral w(t)(h/k)^(-it) f(t)^2 dt
      =gcd(h,k)/sqrt(hk) integral w(t) log(t/(2pi)) dt
         +O_(h,k,w)(H).                                  (3)

The identity for f^2 is L389 (3), which uses no division by zeta.
At Young's scale 2H the support is in [H/2,4H]; the fixed-shape
derivatives meet the weaker (2H/log(2H)) derivative scale. Each fixed
hk satisfies hk<=(2H)^(2theta) eventually for any fixed 0<theta<1/2.
The combined functional-equation diagonals at zero shifts and their
removable singularity are imported from L381, rather than reproved.

Fix one prime p and write rho=p^(-1/2). For each
alpha in {1,-1,i,-i}, the whole function

    Q_alpha(t)=f(t)^2 |1+alpha chi_p(t)|^2

is nonnegative. Expanding its finite square in (3), retaining both
opposite twists, gives

    integral w Q_alpha
       =A_alpha integral w log(t/(2pi)) dt+O_(p,w)(H),
    A_alpha=2+2 rho Re(alpha)>0.                          (4)

For fixed epsilon in (0,1/4), take smooth weights w_minus,w_plus
with 0<=w_minus<=1_[H,2H]<=w_plus<=1. The minorant is supported
inside [H,2H], equal to one except in endpoint strips of length
epsilon H; the majorant is one on [H,2H] and supported in
[(1-epsilon)H,(2+epsilon)H]. Fixed rescaled smooth transitions
give H^(-1) integral w_minus=1+O(epsilon) and
H^(-1) integral w_plus=1+O(epsilon).
The constants in their derivative bounds may depend on epsilon;
their supports lie in [H/2,3H]. On these supports
log(t/(2pi))=ell+O(1), uniformly for epsilon<1/4.

Bracket the integral of each whole nonnegative Q_alpha using these
weights and apply (4). After division by H ell, first let H tend
to infinity at fixed p,alpha,epsilon, then let epsilon decrease to
zero. The upper and lower limits are both A_alpha. Thus

    E_H Q_alpha/ell -> A_alpha.                          (5)

No inequality has been applied to an individual complex twist. The
exact identities, valid for every complex z, are

    |1+z|^2-|1-z|^2=4 Re(z),
    |1+i z|^2-|1-i z|^2=-4 Im(z).

Subtracting the four sharp limits (5) therefore gives

    E_H[f^2 chi_p]/ell -> rho,
    E_H[f^2 conjugate(chi_p)]/ell -> rho.                 (6)

The second identity follows also by conjugation, since f^2 is real.
These are separate fixed-p limits; no growing-twist uniformity is
used or claimed. For any finite fixed prime list they hold jointly.

### Complete-law errors

The other raw second contributions are nonnegative, so for every
fixed prime, without any assumption on their conditional moments,

    |E_H[r_H chi_p]|/ell<=E_H r_H/ell=o(1).              (7)

Combining (2), (6), and (7) yields
E_H[b_H chi_p]->rho and E_H[b_H conjugate(chi_p)]->rho.
The latter follows by reality. All bulk mean and covariance terms
are included in b_H; none have been dropped in this statement.

### Finite Gram limit and Bessel energy

Use the complex Hilbert space L^2([H,2H],dt/H). The named finite
Bessel inequality is the standard projection bound; see P. Garrett,
*Hilbert spaces* (29 October 2016),
[claim 5.2, p. 9](https://www-users.cse.umn.edu/~garrett/m/fun/notes_2016-17/01_hsp.pdf),
and F. Narcowich, *Math 641-600 Orthonormal Sets* (Fall 2014),
[finite projection identities and Bessel paragraph](https://people.tamu.edu/~f-narcowich/m641/m641_notes/orthonormal_sets2014.html).
We specialize this finite-energy principle by Cauchy--Schwarz and an
explicit Gram calculation, rather than apply orthonormal Bessel to
the nonorthogonal finite-height characters.

Fix a finite nonempty prime set P and put

    S_P=sum_(p in P) 1/p,
    v_P(t)=sum_(p in P) p^(-1/2) chi_p(t).

For p=q, E_H[chi_p conjugate(chi_q)]=1. For p!=q, direct integration
of exp(-it log(p/q)) gives

    |E_H[chi_p conjugate(chi_q)]|
       <=2/(H |log(p/q)|) ->0.                          (8)

All denominators are nonzero. Hence, at this fixed P,

    E_H |v_P|^2=S_P+O_P(H^-1),
    E_H[b_H conjugate(v_P)]=S_P+o_P(1).                 (9)

Cauchy--Schwarz and (1) now give the finite-height inequality

    |E_H[b_H conjugate(v_P)]|^2
       <=E_H b_H^2 E_H |v_P|^2
       <=C^2 (S_P+O_P(H^-1)).                          (10)

Taking the height limit in (9)--(10), with P still fixed, yields
S_P^2<=C^2 S_P, hence S_P<=C^2. This argument does not pass b_H
itself to a limit and imposes no phase-only dependence.

Finally import Euler's theorem that the sum of reciprocal primes
diverges; a full elementary proof is in D. Rusin,
*328K Spring 2017 zeta note*,
[unnamed theorem, pp. 1--2](https://web.ma.utexas.edu/users/rusin/328K-17a/zeta.pdf).
For each proposed finite C it supplies a finite P with S_P>C^2.
Choose that P first, then take H to infinity. This contradicts (10).
No rate, growing prime head, infinite product measure, prime number
theorem, or RH is required. This proves the stated obstruction.

### Application to the full L421/L423 bulk

Here x is the first coordinate of X, w is the remaining fiber mass,
and the centered covariance and mean are exactly

    Sigma=ell g_H K+A_H,  K_11=1,
    ||A_H||=O(sqrt(ell)),  |m|=O(1),  0<=w<=1.

L419 supplies the bounded response coefficients and mean calibration;
L421 (8)--(9), and L423 (9)--(10) for its changed weight, retain the
entire matrix correction and give a fixed bound g_H<=G. Thus the
bulk raw density is exactly

    B_H=w(Sigma_11+m_1^2),
    b_H=w g_H+w((A_H)_11+m_1^2)/ell.                    (11)

Positive semidefiniteness of Sigma gives b_H>=0. The full correction
in (11) has absolute value O(ell^-1/2)+O(ell^-1) uniformly, so
b_H<=G+1 eventually after a single larger onset. This verifies (1)
for the raw density, rather than for centered covariance alone.

The high and intermediate components have unnormalized total second
integrals, respectively, O(ell^-2) and O(sqrt(ell)) by L421 (4),(6).
Their nonnegative x-second contributions are bounded by these traces;
their sum is r_H and satisfies (7). The same components are unchanged
in L423. There is no division by small probability or pointwise
rarity assertion. The proof of (11) uses no extension of L423 (9)
from response expressions to prime tests: it uses its actual uniform
bounds, followed by the raw-density theorem just proved.

The finite contradicting list can depend on the law's bound C. This
does not assert that any originally selected correlation fails, or
that a particular prime can be chosen independently of C. It shows
that a full extension matching all fixed prime tests must relax the
bounded normalized bulk raw density or the lower-order rare second
integral assumption (or fail correlation matching). No construction
outside these assumptions has been assessed here.

### Separate critical audit — 2026-10-18, step 208

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-finite-prime-bounded-density-critical-audit.md`.
The obstruction and its complete-law application survive. This is a
REPRODUCTION / proof_audit of the local specialization, not a new
moment theorem or a claim beyond the inspected sources. No repair or
additional mathematical premise is needed.

**Sharp source specialization and all four squares.** L389 (3) gives
f=-sigma Z with sigma in {1,-1}, hence the squared-modulus identity
holds even at zeros. L381 (7) supplies (3) for h=k=1 and the two fixed
twists (h,k)=(p,1),(1,p). Its separate audit retains both Young
diagonals and both off-diagonal orderings. L381 (9) alone would not
supply the complex coefficient, and is not used in its place. Scale
2H, fixed p, fixed smoothing shape and zero shifts meet the previously
inspected primary hypotheses; no new uniformity in p is imported.

Expansion gives Q_alpha=f^2(2+alpha chi_p+conjugate(alpha chi_p)).
For alpha=1,-1,i,-i the four coefficients in this order are exactly
2+2rho, 2-2rho, 2, 2, all positive since p>=2. The minorant loses
at most 2 epsilon H of area, and the majorant adds at most that much.
Both endpoint strips are within the permitted support. Thus at each
fixed epsilon the normalized sharp integral has lower and upper
limits bounded respectively below and above by
A_alpha(1-2epsilon) and A_alpha(1+2epsilon). The source error is
O_(p,epsilon)(1/ell) after normalization and tends to zero first.
Letting epsilon decrease afterwards proves (5); there is no asserted
uniform error at an H-dependent smoothing width. The real difference
of the alpha=1,-1 limits is 4rho. The alpha=i,-i difference is zero
and equals -4 times the normalized imaginary moment. This checks
both signs and the complete complex limit (6).

**Strict finite contradiction and the order of choices.** Fix any
C>=0 and then, using the cited Euler divergence, choose one finite
nonempty P with S=S_P>C^2. For this fixed set, the error in its Gram
norm is bounded in absolute value by

    (2/H) sum_(p,q in P, p!=q)
                 1/(sqrt(pq) |log(p/q)|),

which tends to zero. The finite sum of the matching errors and (7)
also tends to zero, even if the separate onsets depend on p and even
if b_H varies arbitrarily with H. Write
m_H=E_H[b_H conjugate(v_P)] and G_H=E_H|v_P|^2. Then m_H->S,
G_H->S>0, while Cauchy--Schwarz gives |m_H|<=C sqrt(G_H) for
every large H. To see the strict finite-height failure explicitly,
put d=S-C sqrt(S)>0. Choose one onset so that

    |m_H-S|<d/3,  C |sqrt(G_H)-sqrt(S)|<d/3.

For C=0 the second inequality holds identically. These inequalities
give |m_H|>S-d/3>C sqrt(S)+d/3>C sqrt(G_H), a contradiction.
Every choice of primes precedes this height onset. There is no
infinite Bessel family on a finite interval, limit of b_H, assumed
prime-phase independence, or uniform growing-twist estimate.

**Raw law, complete matrix and rare fibers.** In L421 (8) and L423
(10), Sigma is the centered covariance, not the raw second matrix.
The conditional bulk raw x-second moment is Sigma_11+m_1^2 and
its contribution to the full law is multiplied by w. Consequently
(11) is exact, with K_11=1. The uniform lower bound on |b| and
W_H=Ew bounded away from zero make m uniformly bounded. The complete
A_H=-(Q+E[w m m^T])/W_H has norm O(sqrt(ell)); all its entries
remain in Sigma. The bounded positive weight and its normalization
N_H=1+O(H^-1+ell^-5/2) give a fixed upper bound G for g_H.
Positive semidefiniteness of Sigma supplies b_H>=0; retaining the
absolute correction in (11) gives b_H<=G+1 eventually. No centered
moment has been substituted for a raw moment.

The other raw density is exactly
r_H(t)=p(t)Y_1(t)^2+k(t)(Z_mid(t)_1)^2. Its nonnegative integral
is at most tr Q_hi+tr Q_mid=O(ell^-2)+O(sqrt(ell))=o(ell).
This uses L421 (4),(6), unchanged in L423, and remains valid on
fibers where p=1/2. It neither divides by a rare probability nor
requires a pointwise upper bound on r_H. Thus every prime-weighted
rare error is o(ell) by modulus one, and both parts of (1) hold.
The response-average identities of L423 are not promoted to new
prime-weighted actual moments: only its uniform bounds are used.

The actual moment uses L381 (7) with the normalization in L389 (3);
the raw-law check uses L419's bounds with the complete constructions
in L421 and L423. The primary finite-energy and divergence inputs
have their precise citations above. The audit
validates a stop for the bounded-bulk extension to all fixed prime
tests. It preserves L423's finite selected-list feasibility and does
not strengthen L427's separate W^3 stop. A bound depending on a
prescribed finite list is not excluded. No actual clipping,
realization, capped nondegeneracy, L413 margin or RH conclusion follows.

## Mathlib

Full matching coverage for the zeta fixed-prime obstruction has not
been checked; no absence is asserted. The analytic moment is imported
by the precise Young citation above and the audited L381 specialization.
Finite Bessel / Cauchy--Schwarz and Euler prime-reciprocal divergence
are named standard inputs with the inspected references above.
Supporting Mathlib theorem names and a formalization of the complete
specialization were not checked. No computational certificate or
mathematical script is used: the strict threshold is supplied by
Euler divergence and all finite-height errors are explicit or follow
from the cited fixed-test moment.
