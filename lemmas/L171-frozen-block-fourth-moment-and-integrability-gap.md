# Lemma 171: frozen block fourth moment and integrability gap

**Hypotheses.** Use L169's frozen sums and equal blocks, with
H=T^(3/4), h=T/ceil(T/H), N=sqrt(T/(2π)), and I the integers in
[N,2N]. Use the positive profile V of L170. Write

Z_j=S_j⁰/sqrt(V(c_j/T)), z_(j,n)=A_n(c_j)/sqrt(V(c_j/T)),
d_(j,k)=Σ_(m,n∈I:mn=k) z_(j,m)z_(j,n), D_j=Σ_k d_(j,k)².

**Conclusion.** With constants independent of T and j, for sufficiently
large T,

c log T ≤ D_j ≤ C log T,
E_j |Z_j|⁴ = D_j + R_j,    |R_j| ≤ C(T/h)D_j.            (1)

In particular E_j |Z_j|⁴ ≤ C T^(1/4)log T uniformly over j.
Together with E_j|Z_j|²=1+O(T^(−1/4)log T), this bound does
not establish uniform integrability of the squares |Z_j|². No lower
bound growing with T is asserted for the full fourth moment.

**Proof.**

L170's compact positive integral implies 0<v_-≤V(u)≤v_+<∞
for 1≤u≤2. Its exact amplitude formula gives, uniformly on I,

c N^(−1/2) ≤ z_(j,n) ≤ C N^(−1/2).                     (2)

Here T=2πN² and all logarithmic Gaussian arguments range over a fixed
compact interval. Consequently D_j is comparable to N^(−2) times
the number E(N) of ordered quadruples m,n,p,q∈I with mn=pq.

Every such quadruple has a unique representation
(m,p,n,q)=(gr,gs,hs,hr), gcd(r,s)=1: take g=gcd(m,p),
and use coprimality in rn=sq. Put v=max(r,s). Necessarily v≤2N,
and each of g,h has at most 2N/v choices. There are at most 2v
ordered positive pairs (r,s) with maximum v. Dropping coprimality,

E(N) ≤ Σ_(1≤v≤2N) 2v(2N/v)² ≤ C N²log(2N).             (3)

For the lower bound take dyadic integers R, sufficiently large and
R≤N/10, and restrict r,s to the integer interval [R,5R/4).
Put L=R/4 (an integer for the chosen large dyadic R). There are L²
pairs. Noncoprime pairs are at most

Σ_(2≤d≤5R/4) (L/d+1)²
 ≤ (3/4)L²+O(R log(2R)).

Indeed Σ_(d≥2)d^(−2)≤3/4, and the remaining two terms are
bounded by a harmonic sum and the number of d. Thus at least
L²/8 coprime pairs remain once R exceeds an absolute threshold.
For each such pair, integers g giving gr,gs∈[N,2N] lie in

[N/min(r,s), 2N/max(r,s)].

This interval has length at least (3/5)N/R. Its number of integers
is at least (3/5)N/R−1≥(1/2)N/R because R≤N/10.
The same holds independently for h. Each dyadic square therefore
supplies at least cN² quadruples. The squares are disjoint and the
parametrization unique, so summing over the order log N admissible
squares gives E(N)≥cN²log N. Together with (2) and (3) this
proves both diagonal bounds in (1), including real noninteger N.

Squaring Z_j and removing a common unit phase gives the finite sum

P_j(t)=Σ_k d_(j,k) exp(i(t−π/2)log k),

whose squared modulus is |Z_j(t)|⁴. Its support has k≤4N².
The exact integrated diagonal is hD_j. For k≠l the integral of
the corresponding exponential is its endpoint difference divided
by i log(k/l). At either endpoint b, apply the finite generalized
Hilbert inequality stated in the foundations to
x_k=d_(j,k)exp(i(b−π/2)log k). Distinct integer log frequencies
have nearest-neighbor gap at least 1/(2k); a subset only increases
the gaps. The whole signed endpoint sum has absolute value at most

C Σ_k k|x_k|² ≤ C N²D_j.

A support with only one element has no off diagonal. Adding the two
endpoint bounds and dividing by h proves |R_j|≤CN²D_j/h,
equivalent to (1). Coefficients are frozen, so no derivative integral
occurs. All expansions are finite. Since h is between H/2 and H,
the asserted uniform upper bound follows.

L170 and the lower bound for V give the displayed second moment.
For X=|Z_j|², the fourth-moment estimate yields only

E_j[X 1_(X>K)] ≤ E_j X²/K ≤ C T^(1/4)log T/K.

This does not tend to zero uniformly in T as K tends to infinity.
The failure is logical as well as quantitative: for T≥e the abstract
nonnegative variable taking value log T with probability 1/log T,
and zero otherwise, has mean one and second moment log T. It obeys
the moment upper bounds just obtained but is not uniformly integrable:
for each K, its tail first moment is one whenever log T>K.
This example is not asserted to describe the actual frozen sum.
Finally R_j is signed and its proved error exceeds the diagonal scale;
the diagonal lower bound cannot be subtracted to give a useful lower
bound for the full fourth moment. ∎

## Scope, verification

This is a uniform bound in block location, not a bound independent of T.
Variance normalization does not remove the multiplicative diagonal's
logarithm. A sharper signed off-diagonal estimate or different tail
information could still prove uniform integrability; its failure for
the actual family is not proved. The cutoff covariance and RH remain
unproved.

Analytic verification checks the four amplitude factors, unique coprime
parametrization, both integer interval endpoint errors, disjoint dyadic
squares, product-frequency support, both Hilbert endpoints, and division
by h. No numerical certificate is needed.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
