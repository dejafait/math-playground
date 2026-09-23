# Lemma 190: zero-mode floor cells and signed profile

**Hypotheses.** Use L189's floor extension and notation, and the real
pair weights P,Q of L186. All u,v,r,m indices below are integers;
u,v range over [N²,4N²], and r ranges over 0<|r|≤R with gcd(r,u)=1.
N is sufficiently large that all square roots below are positive.
Write J_(u,r)=[A_(u,r),D_(u,r)] as in L188.

Define the finite set

K_(u,r,v)={m∈Z: A_(u,r)≤m≤D_(u,r),
          sqrt(uv−r)≤m<sqrt(u(v+1)−r), gcd(m,u)=1}.

Equivalently its integers satisfy gcd(m,u)=1 and b≤m≤d, where

b=max(ceil(A_(u,r)), ceil(sqrt(uv−r))),
d=min(floor(D_(u,r)), ceil(sqrt(u(v+1)−r))−1).

Empty integer intervals contribute zero. Define the real profile

T_N(v)=Σ_(u,r) P(u)/u Σ_(m∈K_(u,r,v)) H_m(r).

**Conclusion.** The exact zero mode of L189 is

Z_N=Σ_v Q(v)T_N(v)
   =Σ_(c,d∈I) q(c/N)q(d/N)T_N(cd),  I=[N,2N]∩Z.        (1)

Thus the precise signed-profile condition for this zero mode is

Σ_(c,d∈I) q(c/N)q(d/N)T_N(cd)=o(Nh).                   (2)

Condition (2) is necessary and sufficient for Z_N=o(Nh), and is
**unproved**. In particular it is a condition for the actual profile q
and the actual P-dependent T_N, not a uniform assertion for arbitrary
bounded test profiles.

Every individual floor cell contains O(1) integers, uniformly. Nevertheless
the established absolute estimate remains only

Σ_v |Q(v)| Σ_(u,r) |P(u)|/u
                    Σ_(m∈K_(u,r,v)) |H_m(r)|
                  =O_epsilon(N^(3+epsilon)).           (3)

No cancellation or improvement of that bound is asserted.

**Proof.**

For a positive integer u, floor((m²+r)/u)=v is equivalent to
uv≤m²+r<u(v+1). All m in J are positive, so taking square roots
gives exactly the half-open cell in K. A strict real upper bound x
on an integer m is equivalent to m≤ceil(x)−1, including when x is
itself an integer. Intersecting with the original closed J proves the
integer endpoint formula. In particular the global closed cutoff
m²+r≤4uN² is retained: at v=4N² the surviving cell may consist
of the equality m²+r=4uN². There is no permission to replace the
strict upper cell boundary with a closed one.

The cells are disjoint as v varies and exhaust all m in J, since
N²≤(m²+r)/u≤4N² there. Coprimality of m and u is retained in
every cell independently of gcd(r,u)=1; the two conditions are not
interchangeable off the congruence. Insert this partition into L189's
definition of Z_N and group the finite sum by v. This proves the first
identity in (1). Expanding Q(v) into its ordered pair definition from
L186 proves the second, without absolute values or assumptions on signs.
Dividing the exact identity by Nh proves the stated equivalence.

The untruncated real cell has length

sqrt(u(v+1)−r)−sqrt(uv−r)
 =u/[sqrt(u(v+1)−r)+sqrt(uv−r)]=O(1),

because u≍N², v≍N² and |r|=O(N^(3/2)). A real interval of
bounded length contains a bounded number of integers. This does not
allow one to count a fractional number of representatives in any cell.
For (3), sum over v first: the partition gives at most O(h) integers
for each (u,r), using J's length bound. The bounded H and pair divisor
bounds used in L189 bound each |P(u)Q(v)H_m(r)| by O_epsilon(N^epsilon).
There are O(N²) choices of u and O(N^(3/2)) of r, and 1/u≤N^(−2).
The resulting bound is O_epsilon(N^(3/2+epsilon)h), which is (3).
All operations are finite; no integral approximation is used. ∎

## Scope and verification

The profile T_N retains the exact r-dependent m intervals, both
coprimality restrictions, signed P, and the Fresnel coefficient H.
Boundedness of q alone bounds (1) by an absolute sum, and does not
establish (2). Even (2) would leave L189's nonzero frequencies and the
other gcd sectors unresolved; this is not a proof of RH.

`python3 scripts/heat/check_zero_mode_floor_cells.py` verifies the floor
partition and signed ordered-pair identity with exact rational arithmetic,
including empty intervals and integral floor boundaries. Artificial rational
H values test finite grouping only; asymptotic estimates have the proof
above.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
