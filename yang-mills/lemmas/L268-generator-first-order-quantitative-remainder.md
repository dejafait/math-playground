# L268 — Quantitative generator-displacement first-order remainder

## Hypotheses

Use exactly L119's Delta_V, V_N, finite stencils A_r(h), C_r(q),
energy kernel e_j, clipped modulus omega_a(d,h), eta_j(a) and eta(a).
In particular retain its unshifted lower-vertex convention, expansion
point (xi_t,xi_x), finite middle projection
Z_(kl;st)=F_l(s)^T P F_k(t), min(s,t), both original exterior
coefficient levels and every signed generator stencil.

The setting is the relative SU(2) cube (-4,4)^4, sufficiently fine
admitted even N, a=8/N, tau=1/16, straight lower-rooted direction-1
forest, ordinary stored coordinates and the bare small-coupling
coefficient taken at each fixed mesh before refinement. Both actual
probes i=3,6, both residual insertion forms, the upper pinned jump,
all source and normal/end rows, constant modes and the complete heat
sums remain as in L119. Import its exact error-row and complete-trace
bounds (13)--(15), with their existing upstream qualifications.

Import L267(1)'s separately audited full-matrix bound for this same
infinite-grid energy kernel:

    ||e_j(z)||_F <= C (1+sqrt(j^2+|z|^2))^(-4)
                      for every j in Z and z in Z^3.          (1)

This is not a replacement of a finite relative covariance by an
infinite scalar Dirichlet covariance. No new upstream audit is made.

## Conclusion

There are constants independent of j and of sufficiently small a>0
such that L119's exact clipped modulus satisfies

    eta_j(a) <= C min(a(1+|j|)^(-1/2),(1+|j|)^(-3/2)),
    eta(a)=sum_(j in Z) eta_j(a) <= C sqrt(a).                (2)

Consequently, for both actual probes and all sufficiently fine
admitted meshes,

    |Delta_V-V_N| <= C_i N^(5/2).                            (3)

This is stronger than the requested N^(5/2)log(eN)^2 budget for
this one difference. It does not estimate
V_N-a^(-3)K_(i,V), the other three transverse-H coefficient
remainders, the full quantitative L011 response or an interacting
remainder. The separate critical audit below accepts this specialization
relative to its imported premises. The continuum construction and finite
positive mass remain unresolved.

## Proof

### 1. Keep the exact shifted modulus

L119(9) is a Taylor remainder for the prescribed smooth displacement,
with delta(a)=O(a^2), uniform C^1 and C^2 bounds and

    omega_a(d,h)=min(C_0,delta(a)+C_0 a(|d|+|h|)).             (4)

Its scalar calculus input is Taylor's integral remainder, as recorded
in the ready assessment: NIST DLMF, version 1.2.8, section 1.4(vi),
[(1.4.35)--(1.4.37)](https://dlmf.nist.gov/1.4#vi).
The smooth global displacement extensions in L119 satisfy its
line-segment hypotheses. We import (4), without reproving Taylor's
theorem or extending a forest field across the upper pin.

The list of r,h,q with nonzero stencil coefficients is finite and
mesh independent. Put z=d+h+q. For every such pair of shifts,

    |d+h|=|z-q| <= C_1(1+|z|),
    |d|+|h| <= C_1(1+|z|).                                  (5)

For 0<a<=1, delta(a)<=C a^2<=C a(1+|z|). Combining the two
separate bounds supplied by the minimum in (4) therefore gives

    omega_a(d,h) <= C_2 min(1,a(1+|z|)).                      (6)

All constants in (5)--(6) are uniform over the whole finite stencil
list. No axial shift or physical coefficient level has changed.
In particular, the derivative subtracted from the exact kernel is
still evaluated at x, as in L119(2), not at x+h.

### 2. Bound complete spatial square sums at every axial offset

Let M=1+|j|. There are at most C(n+1)^2 lattice points in the
three-dimensional shell n<=|z|<n+1, n=0,1,... . Also

    1+sqrt(j^2+|z|^2) >= c(M+n)

on that shell. Thus (1), (5) and (6) give, for the exact summand
inside L119's eta_j(a), before its stencil matrix norms,

    S_(j,h,q)(a)
      :=sum_(d in Z^3)|d+h|^2 omega_a(d,h)^2
                                      ||e_j(d+h+q)||_F^2
      <= C sum_(n>=0) (n+1)^4 min(1,a(n+1))^2/(M+n)^8.
                                                               (7)

This is a bound on the complete Frobenius matrix norm, including
all mixed entries and their actual shifts. The n=0 and j=0 cases
are included by (1); there is no excluded small-distance region.

For p=4 or p=6 the elementary series estimate is

    sum_(n>=0) (n+1)^p/(M+n)^8 <= C_p M^(p-7).                (8)

Here is a full bound uniform in M>=1. Write u=n+1 and use
M+n>=M and M+n>=u. The terms u<=M have sum at most
M^(-8) sum_(1<=u<=M)u^p <= C_p M^(p-7).
For u>M the sum is at most sum_(u>M)u^(p-8), which is bounded
by C_p M^(p-7) using its first term and the integral of x^(p-8).
That integral converges for both p=4 and p=6. This proves (8),
including M=1.

Apply min(1,a(n+1))<=1 in (7), and then apply
min(1,a(n+1))<=a(n+1) separately. Equations (7)--(8) give

    S_(j,h,q)(a) <= C M^(-3),
    S_(j,h,q)(a) <= C a^2 M^(-1).                            (9)

Both bounds hold simultaneously, so taking square roots yields
sqrt(S_(j,h,q)(a))<=C min(M^(-3/2),a M^(-1/2)).
L119 defines eta_j(a) as the finite sum of these square roots
times ||A_r(h)|| ||C_r(q)||. Summing the fixed stencil norms
therefore proves the first assertion in (2).

The p=6 bound can be viewed as a proved fixed-j fourth spatial
square moment. Its square root has only M^(-1/2) decay, which is
not summable over j. We do not assume or use a globally summable
second spatial moment. The clipping and both bounds in (9) are
essential to the next step. This differs from the separate first
absolute projection/path moment obstructed by L109 and ATTEMPTS/032.

The primary scalar theorem underlying (1) is imported through L267:
Lawler--Limic, *Random Walk: A Modern Introduction* (2010),
Theorem 4.3.1, printed pp. 81--83 of the
[author-hosted text](https://www.math.uchicago.edu/~lawler/srwbook.pdf#page=81).
Its symmetric finite-range irreducible four-dimensional simple-walk
case, including bipartiteness, has H=G_walk/8 for the unnormalized
Laplacian. L267 already justifies the nine mixed matrix differences
and small arguments without differentiating the scalar asymptotic
remainder. No reproof or stronger Green theorem is needed here.

### 3. Sum every signed axial offset before the finite trace

Take L=ceil(1/a), with 0<a<=1. For each integer M>=1 there are
at most two j with 1+|j|=M. For M<=L use the second bound in
(9) after taking its square root, and for M>L use the first.
Then

    eta(a) <= C[a sum_(M=1)^L M^(-1/2)
                         +sum_(M>L)M^(-3/2)]
           <= C'[a sqrt(L)+L^(-1/2)]
           <= C'' sqrt(a).                                  (10)

The middle inequality follows from the first term plus the integral
for the first sum and the decreasing integral tail for the second.
The last uses 1/a<=L<=2/a. Thus all signed offsets, including
offsets larger than the finite box and the zero offset, are bounded
uniformly before any finite level sum. This proves the second
assertion in (2). No fixed-offset convergence or dominated-convergence
rate has been substituted for (10).

### 4. Restore the original complete finite response

To make the normalization explicit, retain L119(13)--(14): the
complete compressed error row matrix at offset j has
Hilbert--Schmidt norm at most C a N^(3/2)eta_j(a), and

    ||Z_(kl;st)||_HS <= C a^2 p(k)p(l) N^(3/2),
    sum_(k,l)|c_(i;kl,a)|p(k)p(l) <= C_i.                      (11)

The finite middle P stays in Z in its original order; only its
imported norm bound is used. The exact response has prefactor
a^(-1)min(s,t). Trace Cauchy--Schwarz and (11), followed by the
complete heat sum, therefore give

    |Delta_V-V_N|
      <= C_i a^2 N^3 sum_(s,t)min(s,t)eta_(t-s)(a)
      <= C_i a^2 N^5 eta(a).                                (12)

For the second inequality, each fixed t has min(s,t)<=N and
sum_s eta_(t-s)(a)<=eta(a); there are fewer than N such t.
No additional unrestricted axial-pair count is taken after (10).
All finite output rows remain in the first Hilbert--Schmidt norm
and all input restrictions are exactly those in L119. In particular
the moved commutator's output is not assumed compact.

Insert (10) into (12), using a=8/N:

    |Delta_V-V_N| <= C_i a^2 N^5 sqrt(a)
                   =64 sqrt(8) C_i N^(5/2).                  (13)

Absorb fixed constants and take a common sufficiently fine mesh
threshold for i=3,6. This proves (3). Since log(eN)>=1, it also
proves the requested weaker threshold. No complete-group outside
factor 3 is inserted. Both generator orientations, insertion forms,
original levels and full heat sums stay in the imported exact trace.

This is a RESEARCH / REPRODUCTION specialization under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-23-generator-first-order-quantitative-remainder.md`.
The added work quantifies its joint clipped lattice sum and restores
the already established trace envelope. It is local standard-method
progress, without a claim of novelty beyond the sources checked.
There is no mathematical script or numerical premise. The separate
critical audit below checks this specialization; the independent
coefficient comparison and construction gaps in the conclusion remain.

### 5. Separate critical audit, 2026-10-24

**Verdict: accepted relative to the imported premises.** This audit
checks the shifted modulus, complete spatial and axial sums and original
response normalization under the prior SPECIALIZE assessment
`drafts/literature/2026-10-23-generator-first-order-rate-critical-audit.md`.
No correction, stronger conclusion or new direct mathematical input is
needed. L119's exact response and L267(1)'s audited kernel estimate remain
imports; this is not a recursive audit of all upstream results.

**Kernel and Taylor conventions.** L110 proof section 2 defines E_j
by the multiplier r_lambda(j) D D*, in the same unshifted transverse
coordinates used in L111 and L119. This is exactly L267(7)--(9)'s
kernel, including both mixed-entry orientations. Its bound (1) therefore
controls the full Frobenius norm in eta_j without a finite-box covariance
substitution. The precise primary Green and Taylor sources cited in
sections 1--2 and their previously inspected coverage are reused; no
fresh retrieval or stronger source claim is made.

L119(8) has displacement difference b(x+h)-b(y) and energy argument
x+h+q-y. Subtracting the continuum gradient at x, not x+h, agrees
with L119(2)--(3). Each segment point is within physical distance
a(|d|+|h|) of x: its relative vector is a[-(1-theta)d+theta h].
The uniform C^2 displacement bound and L028(4)'s O(a^2) C^1
approximation give the second member of the minimum in (4); uniform
gradient bounds give its constant member. The global extension belongs
only to the prescribed displacement, including segments outside the box.
No forest field is extended through its upper pin.

After z=d+h+q, the exact linear weight is |z-q|, and omega's
arguments are z-h-q,h. Maximizing |h|,|q| over the fixed finite
stencil list proves (5) uniformly, including z=0. The two bounds on
omega then give (6), with constants independent of a,j,t and all heat
labels. No axial shift or expansion-point change has been introduced.

**Independent summability check.** Put u=n+1 and M=1+|j|. The full
three-dimensional shell count contributes u^2, the squared linear
weight contributes u^2, and the squared kernel has denominator
comparable to (M+n)^8. The two choices for the minimum consequently
have numerators u^4 and a^2 u^6. For u<=M their sums are bounded
by M^(-8) M^(p+1); for u>M the convergent tails of u^(p-8)
have the same M^(p-7) bound. At p=4 this is M^(-3), and at p=6
it is M^(-1). The u=1 and M=1 cases are included. These estimates
cover every spatial row, not a truncated preview.

Taking square roots and summing the finite stencil norms gives the
two simultaneous allowances in (2). For L=ceil(1/a), the full axial
sum is bounded by a constant times

    a[1+integral_1^L x^(-1/2) dx]
                         +integral_L^infinity x^(-3/2) dx.

The multiplicity is one at j=0 and two for each positive |j|.
Since 1/a<=L<=2/a when 0<a<=1, the bound is O(sqrt(a)). The
a M^(-1/2) allowance is never summed alone to infinity. Its lack of
summability is consistent with the proof, not an omitted sector.
L109/ATTEMPTS/032's separate first absolute moment is not used.

**Finite normalization and both probes.** Trace Cauchy--Schwarz acts
on X_(t,j)-a B_v, not X_(t,j)-B_v: the displacement expansion
contributes one a, canceled only by the original outside a^(-1).
The complete error-row estimate is a N^(3/2)eta_j. L111(13) gives
the closing factor a^2 p(k)p(l)N^(3/2), with the exact middle P
of norm at most one. Including a^(-1), the product is
a^2 N^3 p(k)p(l)eta_j. For each t the weighted s sum is at most
N eta(a); fewer than N levels t give N^2 eta(a). Thus the
response is bounded by a^2 N^5 eta(a), yielding N^(5/2) at a=8/N.
No additional axial-pair count or complete-group factor 3 is inserted.

The first Hilbert--Schmidt norm includes every finite output and allowed
input row, including the moved term's noncompact output. The second
retains both exterior levels and the projection order. No exterior
coefficient is Taylor expanded or commuted, so no extra mode polynomial
is required. L111(13)'s complete heat envelope applies unchanged to
each probe. One common sufficiently fine mesh threshold handles the
finite stencil list and i=3,6. All orientations, residual forms,
end rows, upper jumps and constant modes remain in the imported exact
response and envelope.

This validates an existing local rate by standard methods, without a
claim of a new theorem beyond the sources checked. L120's qualitative
coefficient limit is not assigned a rate: the independent difference
V_N-a^(-3)K_(i,V), the other transverse-H remainders and all interacting
construction gaps remain unresolved.

## Mathlib

Full matching quantitative clipped-modulus/finite-response theorem:
**not checked**. Supporting Taylor integral remainder, lattice shell
counts, positive-series bounds and Hilbert--Schmidt trace estimates:
**not checked**. Unknown coverage is not evidence of absence.
