# Lemma 186: two-factor residue filter for short sums

**Hypotheses.** Use L185 with rho=N^(−1/2), its set M, sums S0,S1,
and real coefficients C_m,G_m. The inherited weights, as defined in
L180, are w(n)=p(n1/N)p(n2/N)q(n3/N)q(n4/N), with real bounded
profiles and I=[N,2N]∩Z. Define finite pair-product weights

P(u)=Σ_(a,b∈I: ab=u) p(a/N)p(b/N),
Q(v)=Σ_(c,d∈I: cd=v) q(c/N)q(d/N).

Both are zero outside the positive integers in [N²,4N²]. For m∈M put

L_m=max(a−²−m²,−2m rho+rho²),
U_m=min(a+²−m², 2m rho+rho²).

An interval with lower endpoint above its upper endpoint is empty.
For each positive integer u in the support range define

V_m(u)={v∈Z: ceil((m²+L_m)/u)≤v≤floor((m²+U_m)/u), uv≠m²}.

**Conclusion.** The following identities preserve every endpoint exactly:

S0(m)=Σ_u P(u) Σ_(v∈V_m(u)) Q(v),
S1(m)=Σ_u P(u) Σ_(v∈V_m(u)) (uv−m²)Q(v).                 (1)

For sufficiently large N each V_m(u) has at most one element. More
explicitly, write m²=u b+e with b=floor(m²/u), 0≤e<u, and set

j0=ceil((L_m+e)/u),   r0=u j0−e.

The set V_m(u) equals {b+j0} if L_m≤r0≤U_m and r0≠0, and
is empty otherwise. A candidate outside Q's support contributes zero.

Define the real coefficient

H_m(r)=(sqrt(2πm)/N)[G_m−(2πr/m)C_m]

and the signed arithmetic sum

B_N=Σ_(m∈M) Σ_u P(u) Σ_(v∈V_m(u)) Q(v) H_m(uv−m²).

Then

Re A_rho=B_N/(Nh)+O_epsilon(N^(−1/2+epsilon)).             (2)

Consequently the exact remaining cancellation requirement for this
near-square real contribution is B_N=o(Nh). This requirement is
**unproved**; no assertion of its truth is part of the lemma.

**Proof.**

Grouping the first two and last two entries of each ordered quadruple
in L180's weight gives the finite convolution

W(k)=Σ_(uv=k) P(u)Q(v).

There are no conjugations, changes of sign, or divisions by permutation
multiplicities: the pair weights count ordered pairs, as required.
For k=m²+r, L185's conditions on r are precisely L_m≤r≤U_m,
r integral and nonzero. Substituting r=uv−m² with u>0 gives the
ceil/floor conditions in V_m(u). Substituting the convolution into
S0 and S1 and rearranging finite sums proves (1).

The real interval for v has length at most

(U_m−L_m)/u≤4m rho/u=O(N^(−1/2)),

whenever it is nonempty: m≍N² and u≥N². This is strictly less
than one for all sufficiently large N, uniformly in m,u, so it contains
at most one integer. In the Euclidean division m²=ub+e, every
possible displacement equals u(v−b)−e. Its smallest value at least
L_m occurs at v−b=j0. If that value exceeds U_m there is no
candidate; if it is zero the square exclusion removes the sole
candidate. These facts prove the residue-filter formulation, including
closed endpoints, an empty intersection, and exact divisibility u|m².

Finally inserting (1) into L185 (1) gives (2), because the factor N
removed from sqrt(2πm) changes N²h to Nh. Fix any epsilon in
(0,1/2); the remainder tends to zero, proving the stated equivalence.
No independent decay of the G and C terms is required. ∎

## Scope and verification

The unique-candidate rule does not prove cancellation: both the selection
by m² modulo u and Q(b+j0) remain arithmetic, and the real pair weights
need not be positive. The inherited absolute count in L185 gives only
Σ_(m,u,v∈V_m(u)) |P(u)Q(v)|=O_epsilon(h N^(3/2+epsilon)).
Indeed expand each absolute pair weight by the triangle inequality to
recover the same absolute quadruple count. Since H_m(r)=O(1), this
still bounds B_N/(Nh) only by O_epsilon(N^(1/2+epsilon)).
At this scale the residue filter alone supplies no new decay estimate.
Nor does (2) address products outside the near-square window or prove RH.

Verification: the proof uses finite grouping, Euclidean division, exact
integer endpoints, the uniform interval length, and L185's remainder.
`python3 scripts/heat/check_two_factor_short_sums.py` checks the grouping
and residue-filter identities on exact rational finite examples with signed
weights, empty intervals, excluded squares, and closed integer boundaries.
These checks are algebraic regression tests, not asymptotic evidence.
Formalization would require finite convolution, integer ceil/floor and
Euclidean division, the interval-length inequality, and (2)'s normalization.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
