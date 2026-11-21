# Corollary C030l: separately tilted orbital rank comparison

## Hypotheses

Let n>=1 be finite, let D=diag(q_1,...,q_n) with every q_j real,
and let P_k be any rank-k orthogonal projection on C^n, 0<=k<=n.
All unitary integrals use probability Haar measure on U(n). Set

    A_k(V)=tr(D V P_k V*),
    Z_k(x)=integral exp(-x A_k(V))dV,
    Gamma_k(x)=-(log Z_k(x))',  x real,
    q_-=min_j q_j, Q=max_j q_j.

Repeated, zero and negative rates are allowed. No Xi zero, positive-rate
convolution, simplicity, or RH hypothesis is an input to this statement.

## Conclusion

For every real x and every 0<=k<n,

    q_- <= Gamma_(k+1)(x)-Gamma_k(x) <= Q.                 (1)

The endpoint conventions are Gamma_0=0 and Gamma_n=tr(D). The means
in (1) use two different, separately normalized tilted probability laws.

This is the known result of Suvrit Sra, *On some positivity properties
of the Riemann Xi function*, [author v3, released 2 November 2026](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
Lemma C.7 and Theorem C.8, printed pp25-27, equations (C.14)-(C.16).
The audit below checks that argument relative to its named orbital-law
input. It is a reproduction, not a claim beyond the source or a new RH
criterion. The author's v3 numbering must not be confused with Hub v1.

## Proof

### Imported orbital law and the exact comparison being audited

For a weakly increasing real top row lambda, let X_lambda be
V diag(lambda)V*. Let z_j^(r), 1<=j<=r<n, be the increasingly ordered
eigenvalues of its leading r-by-r corner, and put S_r=sum_j z_j^(r).
The fixed top row is z^(n)=lambda. The constraints are

    z_j^(r+1) <= z_j^(r) <= z_(j+1)^(r+1).

For fixed real numbers c_1,...,c_(n-1), tilt the orbital law by
w(z)=exp(sum_(r<n)c_r S_r), dividing by its own expectation.
Denote this expectation by E_(lambda,c). The needed intermediate
comparison is E_(lambda,c) Phi <= E_(mu,c) Phi for coordinatewise
ordered top rows lambda<=mu and continuous increasing Phi.

For strictly increasing top rows only, import G. Olshanski,
*Projections of Orbital Measures, Gelfand-Tsetlin Polytopes, and Splines*,
J. Lie Theory 23 (2013), 1011-1022,
[Corollary 3.2, p1017](https://www.heldermann-verlag.de/jlt/jlt23/olshla2e.pdf).
It identifies the corner-array law as constant-density Lebesgue measure
on the full interlacing polytope. Its antecedent Proposition 3.1/(10),
pp1015-16, has the same strict-top-row hypothesis. This orbital theorem
is cited, not reproved or claimed independently audited. Its density
constant cancels separately for each tilted boundary. A collapsed
zero/one polytope will not be assigned an ambient Lebesgue density.

### Finite mesh: normalization, connectivity and ordered stationarity

First fix strictly increasing rational lambda<=mu and a common lattice
spacing h containing both top rows. Give each admissible lattice array
weight w(z)>0. There are finitely many such arrays and at least one.
At coordinate (r,j), with all others fixed, the allowed values form
[L,U] intersect hZ. Explicitly L is the maximum of z_j^(r+1) and,
if j>1, z_(j-1)^(r-1); U is the minimum of z_(j+1)^(r+1) and,
if j<r, z_j^(r-1). Both endpoints are increasing in the neighbors
and boundary. The conditional mass is proportional to exp(c_r t).

Here is the normalization check. For ordered intervals [L,U] and
[L',U'] with L<=L', U<=U', take the same positive lattice weights.
At a point inside their overlap, partition the weights into A below
L', C from L' to the test point, D above it through U, and E above
U through U'. The CDF difference has numerator

    (A+C)(C+D+E)-C(A+C+D)=AD+(A+C)E >= 0

and denominator (A+C+D)(C+D+E)>0. At points outside the overlap,
the lower interval's CDF is also at least the upper interval's CDF;
disjoint intervals are immediate. Thus inverse-CDF updates using
one uniform variable preserve order for any sign of c_r. The two
normalizing sums need not coincide.

Connectivity requires more than this conditional comparison. The
coordinatewise minimum admissible array is m_j^(r)=lambda_j:
each entry is bounded below by lambda_j by iterated interlacing,
and this displayed array is itself admissible. If z_v>m_v cannot
decrease by h, a lower neighbor u must have z_u=z_v. Since
m_u<=m_v, that neighbor also satisfies z_u>m_u. A fixed boundary
neighbor cannot block: it would instead have z_u=m_u<=m_v<z_v.
Continue following a blocking lower neighbor. On every oriented
interlacing constraint (r+1,j) to (r,j) to (r+1,j+1), the label
2j-r increases by one. Following lower neighbors therefore cannot
cycle. A legally decreasing coordinate is reached. Decrease it by
h; upper constraints only become easier, and its lower constraints
remain satisfied. The nonnegative integer sum_v (z_v-m_v)/h drops
by one. Repetition reaches the minimum.

Every such step and its reverse has positive probability for a
random-scan single-coordinate conditional-resampling chain. Hence
the finite chain is irreducible. Staying at the current value also
has positive probability, so it is aperiodic. Its separately
normalized weighted law is invariant: resampling from a conditional
distribution preserves the joint law. The standard finite
irreducible aperiodic Markov-chain convergence theorem then gives
convergence to that unique law from every starting state.

Start the lambda and mu chains at their ordered minima, choosing the
same coordinate and uniform variable on every update. The interval
calculation preserves their coordinatewise order at each step.
Consequently the expectation inequality holds at each time for any
increasing Phi. Passing to the two marginal stationary limits proves
it for the separately normalized lattice laws. A common normalizer
or a stationary law inferred solely from an untilted coupling was
not used. For n=1 there are no proper coordinates and this comparison
is the equality of the unique empty-array values.

### Continuum and singular-boundary limits

Keep the strict rational boundaries fixed and let h decrease through
common divisors. Their polytopes have nonempty interior: recursively
choosing strict intermediate entries provides a point where every
constraint is strict. The boundary lies in finitely many hyperplanes,
so has Lebesgue measure zero. The continuous functions w and Phi*w
are bounded on the common compact coordinate box. Thus h^d times
their lattice sums converge to their integrals, d=n(n-1)/2. Each
limiting denominator is positive because w>0 and the polytope has
positive volume. Quotients converge to the corresponding tilted
orbital expectations by the imported orbital law. No uniform limit
of the Markov-chain mixing times is needed: the stationary comparison
was established separately at each fixed h.

For arbitrary weak real boundaries, use one Haar V to realize a
convergent sequence X_lambda. The matrices and the ordered eigenvalues
of each Hermitian corner vary continuously; this also follows from
the usual Weyl eigenvalue perturbation inequality. Bounded top rows
put every corner coordinate in one compact box. On that box w and
Phi*w are bounded, and w is bounded below by a positive constant.
Dominated convergence therefore applies to both weighted Haar
integrals, with strictly positive limiting denominators. This proves
continuity of the tilted expectations at repeated boundaries.

An ordered strict rational approximation exists simultaneously:
for positive rational h tending to zero set

    lambda_j^h = h floor(lambda_j/h)+j h,
    mu_j^h     = h floor(mu_j/h)+j h.

Monotonicity of floor preserves lambda^h<=mu^h. Each row is strictly
increasing and rational, and its j-th approximation error has
absolute value at most j h. Passing the already proved inequality
through Haar continuity proves the desired comparison for all weak
real top rows, including all-zero and all-one boundaries.

### Rank means, identical fields and both rate orderings

The observable A_k is bounded in absolute value by k max_j|q_j|.
On every compact x interval this bounds the integrand and its
derivative. Differentiation under Haar integration gives

    Gamma_k = integral A_k exp(-x A_k)dV / Z_k,

where Z_k>0. Unitary invariance permits the standard projection with
top row lambda^k=(0^(n-k),1^k). For any Hermitian X, telescope its
diagonal entries X_rr=S_r-S_(r-1) to obtain

    tr(DX)=q_n S_n + sum_(r<n)(q_r-q_(r+1))S_r.          (2)

On this rank-k orbit S_n=k. Its constant exp(-x q_n k) cancels
in its own probability normalization. Thus the remaining fields
are exactly c_r=x(q_(r+1)-q_r), identical at ranks k and k+1.
Their top rows are ordered coordinatewise. The comparison just
audited, applied to the increasing function S_r, yields

    Delta_r=E_(k+1,x)S_r-E_(k,x)S_r >= 0 for r<n,
    Delta_n=1.

Simultaneous permutation of the real rates does not change Z_k or
Gamma_k, by Haar invariance. List them increasingly in (2). Then
q_n=Q and all coefficients q_r-q_(r+1) are nonpositive, giving

    Gamma_(k+1)-Gamma_k
      = Q + sum_(r<n)(q_r-q_(r+1))Delta_r <= Q.

List the rates decreasingly for a separate application. Now q_n=q_-
and all these coefficients are nonnegative, giving the lower bound.
The two comparisons may have different fields and different Delta_r;
only their invariant scalar left sides are identified. Neither
argument requires x>=0 or strict rate inequalities. This proves (1).

At rank zero the orbit is {0}; at rank n it is {I}. Hence Z_0=1,
Z_n=exp(-x tr(D)) and the asserted endpoint means follow directly.
The weak-boundary comparison includes both adjacent endpoint cases.
For n=1 the unique increment is q_1, so both bounds are equalities.

### Downstream qualification and audit verdict

The independent checks above pass all cases of the approved audit.
Sra v3 Lemma C.6/(C.10),(C.13), pp23-25, identifies these means
with a different, finite positive-exponential reference. Citing that
identity and (C.17), p27, the source's m-dimensional moving-basis
diagonal, under the finite-reference hypotheses below, obeys

    alpha_i(y)=(n-2i-1)/y-(Gamma_(i+1)(y)-Gamma_i(y))
               >= (n-2i-1)/y-Q,   y>0, 0<=i<m.

That use requires f=Exp(q_1)*...*Exp(q_n) with 0<q_j<=Q.
The exact Grassmannian identification is a cited input for this
downstream remark, not a second theorem audited here. The full
signed-smoothing assertion C.9 additionally retains

    n>=2m,
    (n-2m+1)/2 >= sqrt((m-1)(n-m+1)),
    eta real signed, supported on [0,infinity),
    integral exp(Q u)d|eta|(u) < 1.

Its full proof, infinite-complement closure and finite-height
certificate are outside this audit. Neither an order-independent
shift constant nor (1) removes these finite-core requirements.
The actual Xi squared rates need not all be real; substituting them
into this proof would destroy its positive tilted-law premise.
No comparison with that signed remainder, all-degree L030 sign,
or common-graph realization is proved. L030, C030b and C030k are
scope comparisons only, not mathematical inputs to this result.

## Mathlib

Full matching coverage of the tilted orbital comparison, its orbital
input and its finite-exponential identification is unchecked. No absence
claim is made. Dominated convergence, finite Markov chains and Hermitian
eigenvalue continuity are supporting mathematics; no formalization or
Mathlib theorem-name match for them was checked in this audit.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
