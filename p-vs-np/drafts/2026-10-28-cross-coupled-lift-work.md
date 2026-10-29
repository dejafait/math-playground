# Cross-coupled common-source lift — step 540 working checkpoint

The main gap is uniform worst-case P versus NP. The immediate target is
exactly the pre-invocation EXPLORE target in
`literature/2026-10-27-batched-incidence-zigzag.md`: a bounded incidence
chain for the original wrapped F_r G and G F_r endpoints, with scalar
support plus twice-counted intermediate size at most C*S uniformly.
This could supply the unary sector of the missing fourth comparison;
general F, mixed letters, reception and unrestricted complexity remain
independent unresolved gaps.

The supplied startup snapshot and assessment were used without rereading.
Scoped status shows extensive earlier unfinished notebook work; it is
preserved. Targeted inputs read: L110 §§4,21; L115 §§1–6; L118 §5;
L119 §§1–3; L120 §§1–2; L121's hypotheses/conclusion; L122 §§1–5;
Attempt 056 and history 539. The existing theorem/source assessment is
reused: no new qualitative theorem or source coverage is assumed.

The bounded candidate is a boundary-coupled common source with ordinary
scalar projections, at most two copies of each operand and one charged
2r-edge spine. Unlike Attempt 056 it must change internal functions by
actual cross-copy constant/x incidences. Each proposed projection's row
kernel must be invariant and have zero final value; an elementary reverse
companion is not assumed. These are requirements, not supplied maps.

Continue only after complete r=N=4 path graphs, orders, both maps and all
three oriented equations are checked, including whether L122's forced
residuals have actually changed. If valid, count dyadic growth and then
test the cancellation fixtures before general r/G. A complete failed
equation or a forced superlinear charge stops the particular template.
No valid construction, linear bound or impossibility is yet established.

## Unfinished reasoning

A common-source row must have the same residual after either projection.
Keeping an identity copy of every endpoint coordinate would retain the
other endpoint's binomial conversion; simply making dead branches project
to zero does not address the reachable core. The candidate must therefore
modify accepting cross-copy incidences as well as the initial boundary.
Full maps and an incidence realization are still to be constructed.

## Concrete candidate before replay

Start from L122's literal Q0 solely as a construction recipe. Order its
blocks s, a_F, a_G, b_G, b_F, d, t. Define a scalar incidence H by
a_f_i -> b_f_i and a_h_i -> b_h_i (0<=i<=N),
b_h_j -> d_j and b_f_i -> d_(N+i) (0<=i,j<N), with all other rows zero.
Thus H^3=0. Put T=I+H and U=I+H+H^2. Build NEW literal occurrences by
replacing each old u->v edge with every w->z of the same label for
U[w,u]=1, T[v,z]=1. Retain multiplicities. These edges only go forward
in the displayed block order; this is an actual cross-coupled graph,
not just a polynomial label. There are no additional vertices.

The tentative proof uses C_Q=U C_0 T, D_Q=U D_0 T, fixed raw source/sink,
so M_Q=U M_0 T and alpha_Q=alpha_0 T. At N=4 obtain both full maps by
expanding U times the old finite Q0->A/B maps and checking every entry.
The maps may have long invariant zero-final kernels; no elementary
companion or invertibility of these endpoint maps is required. Only T
is an internal change of basis in this chosen construction, not an
assumed invertible map between the original endpoints.

Potential discriminant: the b_h_j residuals become zero (j<N), while
b_f_i becomes z(1+z)^(N-i-1)+z^(N-i). L122's old unchanged low residual
has therefore changed. In A's independent residual basis its remaining
monomial coefficients may still force 3^k-N entries. This calculation
and its exact finite instances are not yet verified. Full evidence,
invariant kernels, all original occurrences and graph charges are next.

## Finite check and symbolic stopping calculation

The complete N=4 graph, both scalar matrices, both sides of every
transition equation, all boundary coordinates and both full kernel bases
were inspected from `scripts/batched-incidence/output-540/cross-coupled-N4.json`.
Both maps pass; each has rank 9 and the same 21-dimensional invariant
zero-final kernel. Their supports are 42 and 52. The new graph has
30 vertices and 107 edge occurrences, so total charge is 582 against
S=84. These finite numbers are not a universal bound.

The coupling really changes the functions: b_h_j prefixes become
z^(N+j), d_j prefixes become zero for j<N, and b_h_j residuals vanish.
But b_f_i residuals are z[(1+z)^d+z^d], d=N-i-1. A's independent
right-closed residual basis still uniquely forces binom(d,j)+[j=d]
in the columns h_(N-1-j). Their sum over i is 3^k-N. Hence for k>=2
the map-support/S ratio is at least (3/2)^k/72, unbounded, even though
2g(Q)=108N+56<=7S. This stops this exact common-source coupling.
The proof, qualifications and finite matrices are to be made canonical;
it does not stop a different cross-coupling or arbitrary scalar chains.

## Completion

The full proof, two finite matrices, their exact common kernel and the
uniform support obstruction are now canonical in
`lemmas/L123-cross-coupled-spine-projection-obstruction.md`. Attempt 057
records the stop. Dyadic finite checks also pass at N=1,2,8,16; they
confirm the formulas without replacing their symbolic proof. No viable
general-G continuation of this template is claimed. The next mechanism
is only proposed in the separate REVIEW_REQUIRED residual-relation
assessment; no new-target mathematics was performed. The checkpoint
records NEGATIVE / RESEARCH / REPRODUCTION, not a complexity resolution.
