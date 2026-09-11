# Lemma 192: coprime density approximation error

**Hypotheses.** Use L191's b,t,M,alpha_m,beta_m and affine H_m,
L190's Z_N=Σ_v Q(v)T_N(v), and L186's bounded real pair profiles.
The inherited scales are h≍N^(3/2), #M=O(h), m≍N²,
R=O(N^(3/2)), and N²≤u,v≤4N². Take N sufficiently large that u>1.
Let phi(u) count the units modulo u, and D(u)=Σ_(d|u)|mu(d)|.
Set I_(u,m,v)=0 when b>t and otherwise set

I_(u,m,v)=(phi(u)/u) ∫_b^t H_m(x) dx
 = (phi(u)/u)[alpha_m(t−b)+beta_m(t²−b²)/2].

The integral uses L191's exact integer endpoints; a singleton has integral
zero. Define the density profile and its signed pairing by

Tbar_N(v)=Σ_u P(u)/u Σ_(m∈M, gcd(m,u)=1) I_(u,m,v),
Zbar_N=Σ_v Q(v)Tbar_N(v).

**Conclusion.** For each nonempty interval the error E_(u,m,v) between
L191's coprime affine sum and I_(u,m,v) satisfies

|E_(u,m,v)| ≤ 2D(u)(|H_m(t)|+|beta_m|(t−b)) = O(D(u)).       (1)

Set E=0 for empty intervals. For every epsilon>0 the actual pair weights
satisfy the absolute accumulated bound

Σ_(u,m,v: m∈M, gcd(m,u)=1) |P(u)Q(v)|/u |E_(u,m,v)|
 = O_epsilon(h N^epsilon).                                 (2)

Consequently Z_N=Zbar_N+O_epsilon(h N^epsilon), and
Z_N=o(Nh) if and only if Zbar_N=o(Nh). The latter decay condition
remains **unproved**.

**Proof.**

For any real x≥b, the number of multiples of d in [b,x] differs from
(x−b)/d by at most 2, by the floor and ceiling formulas. This includes
the closed left endpoint and the case x=b. Möbius inversion gives

A(x)=#{r∈Z: b≤r≤x, gcd(r,u)=1}
    =(phi(u)/u)(x−b)+Delta(x),   |Delta(x)|≤2D(u).          (3)

Indeed Σ_(d|u) mu(d)/d=Π_(p|u)(1−1/p)=phi(u)/u, by
inclusion-exclusion on one full residue period. If zero lies in the
interval, its total Möbius contribution is Σ_(d|u)mu(d)=0 since u>1.
Thus (3) counts exactly the nonzero coprime integers required by L191.

For H(x)=alpha+beta x, finite summation followed by integration of each
indicator 1_{r≤x} yields

Σ_(b≤r≤t, gcd(r,u)=1) H(r)=H(t)A(t)−beta ∫_b^t A(x) dx.

Apply the same identity to the continuous density (phi(u)/u) dx.
Subtracting and using (3) proves the first inequality in (1), also for
b=t. No asymptotic equidistribution is needed.
L185 gives uniformly bounded C_m,G_m; therefore L186's coefficient
formula gives alpha_m=O(1), beta_m=O(N^(−2)). Since |b|,|t|≤R,
|H_m(t)|=O(1) and |beta_m|(t−b)=O(N^(−1/2)). This proves (1).

For fixed u,m, every nonempty integer interval [b,t] contains an integer
r in [-R,R] with v=floor((m²+r)/u). The image of this real displacement
window has length 2R/u=O(N^(−1/2)), so it meets at most two floor cells
for all sufficiently large N. Intersecting the other cutoffs can only
reduce that count. This argument includes singleton and global support
boundary cells, even when their only integer is the excluded zero.
In particular there is no extra factor equal to the number of v values
in their entire support.

The pair definition and the triangle inequality give

Σ_u |P(u)| ≤ (Σ_(a∈[N,2N]∩Z) |p(a/N)|)² = O(N²).

Also |Q(v)|≤C d_2(v) and D(u)≤d_2(u). The elementary divisor bound
proved in L187 gives sup_(u,v∈[N²,4N²]) D(u)|Q(v)|
=O_epsilon(N^epsilon), by choosing its exponent epsilon/4.
Drop gcd(m,u)=1 in the nonnegative error majorant. Using the at most
two cells for each u,m, u≥N² and #M=O(h), (1) now bounds that
majorant by

C_epsilon N^epsilon #M N^(−2) Σ_u |P(u)|
 = O_epsilon(h N^epsilon).

This proves (2). The finite identities in L190 and L191 give the formula
for Z_N. Divide by Nh and fix 0<epsilon<1 to obtain a vanishing error
and the asserted equivalence. ∎

## Qualifications, verification and formalization

This result approximates the displacement sum only. It retains the
coprimality of m and u, the exact floor-dependent integer endpoints,
and the signed P,Q and Fresnel factors. It does not estimate Zbar_N,
L189's nonzero frequencies, other gcd sectors, or prove RH. Replacing
these remaining structures by independent averages is not justified here.
The u>1 condition matters: removing zero for u=1 requires a separate
correction, which is outside the inherited large-N setting.

`python3 scripts/heat/check_coprime_density_error.py` checks (1) and the
finite summation identity on exact rational signed affine examples,
including negative, empty, singleton and zero-crossing intervals, and
checks the two-cell count for short displacement windows. The asymptotic
bound is proved above, not inferred from computation. Formalization
requires lattice discrepancy, finite partial summation, the cell count,
and absolute pair-weight and divisor estimates.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
