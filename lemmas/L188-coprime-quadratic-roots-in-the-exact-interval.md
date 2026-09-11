# Lemma 188: coprime quadratic roots in the exact interval

**Hypotheses.** Use L187 and its inherited notation, with N sufficiently
large, h≍N^(3/2), rho=N^(−1/2), and a−,a+≍N². Choose a fixed
constant C such that every admissible displacement has |r|≤R=C N^(3/2).
For integers N²≤u≤4N² and 0<|r|≤R define the closed real interval
J_(u,r)=[A_(u,r),D_(u,r)], where

A_(u,r)=max(a−−rho, sqrt(a−²−r), sqrt(uN²−r),
                         |r−rho²|/(2rho)),
D_(u,r)=min(a++rho, sqrt(a+²−r), sqrt(4uN²−r)).

All radicands are positive for sufficiently large N. An interval with
A>D is empty. Write T(u,r) for the integers m in this interval satisfying
m²≡−r (mod u) and gcd(m,u)=1. Let omega(u) count the distinct prime
factors of u.

**Conclusion.** The g=1 sector has the exact identity

B_N^(g=1)=Σ_(N²≤u≤4N²) Σ_(0<|r|≤R, gcd(r,u)=1)
 P(u) Σ_(m∈T(u,r)) Q((m²+r)/u) H_m(r).                 (1)

For nonempty J of length ell,

#T(u,r)≤2^(omega(u)+1)(floor(ell/u)+1).                (2)

In particular ell=O(h)<u, and #T(u,r)=O_epsilon(N^epsilon).
Summing this pointwise estimate with absolute weights gives only

Σ_(u,r) Σ_(m∈T(u,r)) |P(u)Q((m²+r)/u)H_m(r)|
                  =O_epsilon(N^(7/2+epsilon)).        (3)

The inherited bound for this same sum is O_epsilon(h N^(3/2+epsilon))
=O_epsilon(N^(3+epsilon)). Thus (2), summed separately over u and r,
does not improve the inherited absolute estimate. This comparison does
not assert that either bound is sharp for the actual weighted sum.

**Proof.**

For g=1 the congruence and coprimality in L187 read m²≡−r mod u
and gcd(m,u)=1. Under the congruence, gcd(r,u)=gcd(m²,u), so
coprimality of either r or m with u is equivalent to that of the other.
The stationary product restriction is a−²≤m²+r≤a+². Positivity
of m turns this into the corresponding two square-root bounds. The
support restriction N²≤(m²+r)/u≤4N² gives the other two square-root
bounds. Finally the displacement restriction is

−2m rho+rho²≤r≤2m rho+rho²,

which is equivalent to m≥|r−rho²|/(2rho). Intersecting these bounds
with M gives precisely J. Keeping r nonzero removes the squares.
The actual support of Q may be smaller than its enclosing interval;
its zero values retain this restriction exactly. This proves (1) by
finite reindexing, without altering signs or endpoints.

Here is an elementary unit-root count. For an odd prime power p^a,
fix one unit root x of x²≡−r. Every other root y satisfies
p^a|(y−x)(y+x). Since their common divisor divides 2x, p cannot
divide both factors. Hence y≡x or −x mod p^a, giving at most two
roots. For 2^a, the cases a≤2 have at most two unit residues. If
a≥3, divide a root by a fixed unit root to reduce to z²≡1 mod 2^a.
The even numbers z−1 and z+1 differ by two; one has exactly one
factor of two. Therefore the other is divisible by 2^(a−1), and
z≡1 or −1 mod 2^(a−1). There are at most four classes mod 2^a.
The Chinese remainder theorem now gives at most 2^(omega(u)+1)
unit roots for every u (also a valid loose bound for odd u).

Each residue class has at most floor(ell/u)+1 representatives in a
closed interval of length ell: distinct representatives are separated
by u. The intersection with M has length at most a+−a−+2rho=O(h),
which is less than u≥N² for sufficiently large N. This proves (2).
The elementary divisor bound proved in L187 implies
2^omega(u)≤d_2(u)=O_eta(u^eta).

The bounded profiles defining P,Q give |P(u)|≤C d_2(u) and
|Q(v)|≤C d_2(v). On their supports u,v=O(N²); also H_m(r)=O(1)
as in L187. For any eta>0 each (u,r) group therefore contributes at
most O_eta(N^(6eta)) in absolute value. There are O(N²) choices of u
and O(N^(3/2)) nonzero r. Taking eta=epsilon/6 proves (3).
L187's absolute bound with G=1 applies also to the restricted g=1
sector, giving the stated stronger inherited estimate. ∎

## Qualification and verification

Replacing the term floor(ell/u)+1 by ell/u is invalid for a short
interval containing a root: one representative can occur even when
ell/u tends to zero. An averaged estimate might recover such a factor,
but none has been proved here. Even the heuristic factor h/u≍N^(−1/2)
would only recover the inherited exponent in (3), not B_N=o(Nh).
No conclusion about signed cancellation or RH follows.

`python3 scripts/heat/check_coprime_quadratic_roots.py` checks the unit
root bound and exact interval regrouping on rational finite cases,
including empty intervals and closed boundaries. The asymptotic bound
is proved above. Formalization would require the finite reindexing,
positive square-root inequalities, prime-power root count, Chinese
remainder theorem, interval spacing and divisor estimates.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
