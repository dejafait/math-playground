# Lemma 958: Xi's finite-rectangle critical-count balance

## Hypotheses

Let f(z)=Ξ(z)=ξ(1/2+iz) be the actual completion in L018. Use the
unconditional growth and Hadamard representation of L023–L024; no
reality of its zeros is assumed. Let 0<a<b satisfy

    a,b outside J(f),             f(a)f(b) != 0,

where J(f) is the union of the closed disks with center Re ρ and
radius |Im ρ| over nonreal zeros ρ of f. L957 supplies such a pair
at sufficiently large positive heights. No effective onset is used.

All zero counts below include full orders. Let 2J and 2J' count the
nonreal zeros of f and f', respectively, in

    R_ab = {z : a<=Re z<=b, |Im z|<=1/2}.

Let N and N' count their real zeros in the closed interval [a,b].
Define K as follows. For each real zero x of f' in [a,b] with f(x)!=0,
let m=ord_x(f'), and assign the integer

    κ(x) = m/2                                      if m is even,
           (m+1)/2  if m is odd and f(x)f^(m+1)(x)>0,
           (m-1)/2  if m is odd and f(x)f^(m+1)(x)<0.

Then K is the sum of these κ(x). Common zeros of f and f' are
excluded from K, but remain in N,N' with their respective orders.
The product in the odd cases cannot vanish. This is Kim's critical
multiplicity, not the count of all stationary points.

Write q=f'/f at the endpoints, let e_a,e_b be the indicators of
f'(a)=0 and f'(b)=0, and set sgn0(0)=0. Define

    E = (sgn0 q(a)-sgn0 q(b)+e_a+e_b)/2.

## Conclusion

All four counts are finite. There are no nonreal zeros of f or f'
on either vertical boundary, and neither function has a zero on
|Im z|=1/2. The two balances, including endpoint contributions, are

    2K = N'-N-E,                         (1)
    N'+2J' = N+2J+E.                    (2)

Consequently

    K=J-J' >= 0.                        (3)

For nonstationary endpoints e_a=e_b=0, E is exactly Kim's endpoint
sign term. If an endpoint is stationary, its f' zero is simple and
has critical multiplicity zero; formulas (1)–(2) use the closed
real counts, including that simple zero. No winding number on a
contour passing through such a zero is asserted.

This is a known-method specialization, accepted by the focused
conceptual audit of 9 November 2026 (step126) recorded below.
It proves no estimate forcing K=0. That is precisely the one-step
no-loss threshold 2J'=2J on this interval, not an established fact
or an RH conclusion. No finite global nonreal-zero census is assumed.

## Proof

### Imported theorem and the scope of the additional work

Import Young-One Kim, *Critical points of real entire functions and
a conjecture of Pólya*, Proc. Amer. Math. Soc. **124** (1996),
819–830, [DOI 10.1090/S0002-9939-96-03083-3](https://doi.org/10.1090/S0002-9939-96-03083-3),
[published PDF mirror](https://scispace.com/pdf/critical-points-of-real-entire-functions-and-a-conjecture-of-3sul01urof.pdf):
critical multiplicities on pp819–820, Theorem1 on p821, Jensen's
Theorem and the complete Theorem1 proof in Section2, pp822–823.
These passages were inspected for this application.

Theorem1 applies to nonconstant real entire functions of genus1*
with endpoints outside J(f), with no assumption of finitely many
nonreal zeros globally. Genus1* means exp(-αz²)g(z), α>=0, with
g real entire of genus at most one. Jensen's Theorem there contains
every nonreal derivative zero in J(f). For endpoints at which ff'
is nonzero, Section2 gives (1)–(2) with E=(sgn q(a)-sgn q(b))/2.
Its real-zero formula is attributed to Pólya, *Some problems connected
with Fourier's work on transcendental equations*, QJM **1** (1930),
21–34, pp29–30. We import it through Kim; Pólya's original proof is
not claimed independently checked or reproved here.

What requires checking locally is the actual-Xi genus, existence of
an allowed pair, equality of rectangle and strip counts, and the
explicit closed-endpoint convention when f' vanishes. The logarithmic
derivative calculation below only justifies that last specialization;
it is not a reproof of Kim's theorem.

### 1. Genus, nonconstancy, and admissible positive endpoints

L018 gives reality, evenness and the strict zero strip |Im z|<1/2.
L023 supplies order at most one. L024 uses its order-one Hadamard
factorization with no quadratic exponential, so f has genus at most
one and belongs to genus1* with α=0. Finite exponential type and
Laguerre–Pólya membership are not being inferred.

Nonconstancy can be checked without zero-location information. For
positive integers n, the completion formula of L018 gives

    ξ(2n)=n(2n-1)π^(-n)(n-1)! ζ(2n).

The defining positive Dirichlet series gives ζ(2n)>1. The ratio of
successive values of n(2n-1)π^(-n)(n-1)! is
(n+1)(2n+1)/(π(2n-1)), which tends to infinity. Hence ξ(2n), and
therefore f, is unbounded. In particular f' is not identically zero.
Also f has a zero: otherwise the even Hadamard representation in
L024 would be the nonzero constant f(0). This fact will ensure a
strict sign in the endpoint calculation below.

Fix one sufficiently large T for L957. Choose a in (T,2T) from its
disk-free complement, excluding real f zeros, and choose b in
(3T,6T) by the same assertion at scale 3T. These choices give one
fixed positive a<b meeting the hypotheses. No new endpoint estimate,
sequence argument, negative-height extension or effective T is needed.
The rest of the proof applies to any a,b satisfying the hypotheses.

### 2. Geometry and finiteness of the counted sets

Every disk of J(f) has radius d<1/2. A vertical line Re z=a meets
such a disk only if |a-Re ρ|<=d, which would put the real point a in
that disk. Thus both vertical boundary lines miss every disk. By
Jensen's Theorem, nonreal f' zeros are in J(f); nonreal f zeros are
there by definition. This excludes their nonreal vertical-boundary
zeros and gives |Im z|<1/2 for every nonreal f' zero. Real zeros
already lie in this strip. Consequently all strip-wide counts in
a<=Re z<=b equal the counts in R_ab, with full multiplicities.
Analyticity and nonconstancy make them finite in that compact set.
Conjugation symmetry of f and f' makes each nonreal count even,
justifying the integers J and J'.

For comparison with Kim's proof contour, any disk meeting the vertical
slab has its entire real diameter strictly inside (a,b). Indeed its
real projection is an interval; if it reached across either endpoint,
that endpoint would belong to J(f). Its radius therefore satisfies
d<(b-a)/2. Every nonreal zero counted here is consequently also
strictly inside Kim's half-height (b-a)/2 rectangle. Both rectangles
count exactly the same zeros; their heights need not agree.

The disk union is locally finite. A disk meeting a bounded real
interval has center within 1/2 of it, and its generating zero lies
in a fixed compact rectangle by the strict strip. There are only
finitely many such zeros. Thus each endpoint outside the closed
union has a real open neighborhood disjoint from every disk. This
also permits the endpoint movements used below; avoidance of a
boundary zero alone would not suffice.

### 3. The nondegenerate boundary formula

First suppose f'(a)f'(b)!=0. Section2 of Kim applies with every
hypothesis now checked. Its argument-principle identity is (2),
and its real-critical-count identity is (1), both with e_a=e_b=0.
Common zeros present no omitted multiplicity: at a zero of f of
order r, f' has order r-1 (zero order 0 when r=1), so the
argument principle for f'/f records their difference -1. Both
source counts retain the original orders, and the definition of K
excludes the common zero. No simplicity assumption is used.

### 4. Stationary endpoints and their exact correction

On a small real neighborhood of an endpoint x with f(x)!=0,
differentiating the genus-one logarithmic derivative of L024 gives

    q'(x) = -sum_{r real zero} m_r/(x-r)^2
            -sum_{u+iv, v>0} 2m_{u+iv}
                  ((x-u)^2-v^2)/((x-u)^2+v^2)^2.             (4)

One term represents each distinct real zero or conjugate pair.
Reciprocal-square summability in L024 gives locally uniform
convergence of the differentiated tail away from zeros, since for
large |ρ| and bounded z its terms are O(|ρ|^(-2)). This justifies
differentiation and conjugate grouping. There is no split divergent
sum of reciprocals and no quadratic exponential term.

At either endpoint outside J(f), |x-u|>v for every nonreal pair.
Every summand in (4) is therefore strictly negative. The series
converges, and f has at least one zero by part1, so q'(x)<0.
If q(x)=0, then f''(x)/f(x)=q'(x)<0. Thus f'(x) is a simple
zero and f(x)f''(x)<0, giving κ(x)=0 by its definition. Moreover
q is positive immediately to its left and negative immediately
to its right.

Take a_ε>a and b_ε<b sufficiently close to the original endpoints,
inside their disk-free neighborhoods. Choose them with ff' nonzero.
Isolation of zeros allows the collars to contain no other real
zeros of either function. They contain no nonreal zeros in the
whole vertical slabs by Jensen containment and disk avoidance.
Hence J,J',N,K are unchanged, while the new real derivative count
is N'-e_a-e_b. This assertion for K also uses the endpoint weight
zero just proved, rather than discarding an endpoint multiplicity.

For all such sufficiently small movements the interior signs are

    s_a=sgn q(a_ε)=sgn0 q(a)-e_a,
    s_b=sgn q(b_ε)=sgn0 q(b)+e_b.

Put e=e_a+e_b and B0=(sgn0 q(a)-sgn0 q(b))/2. The source endpoint
term on the moved contour is B_in=(s_a-s_b)/2=B0-e/2. Applying
part3 there gives

    2K=(N'-e)-N-(B0-e/2)=N'-N-(B0+e/2),
    (N'-e)+2J'=N+2J+B0-e/2.

Rearranging the second equation gives (2) with E=B0+e/2, and
the first gives (1). This is a stabilization on small collars,
not an interchange of an infinite count and a limit. It does not
assign a winding number to the original contour when f' vanishes
on it. Eliminating E yields 2K=2J-2J', proving (3). ∎

**Qualifications.** The boundary corrections cancel; they do not
estimate K. K is a nonnegative integer by its full critical-multiplicity
definition. Thus K=0 is equivalent to no loss of nonreal zero pairs
on this first differentiation in this fixed interval. No method here
shows that this threshold holds. Higher-derivative endpoint geometry,
global count transfer, independent critical signs, and L030–L032/C032a
all-degree mixed positivity remain unresolved. This application does
not invoke Kim's Theorems2–3, a finite global nonreal census, or a
zero-tilt/logarithmic-curvature theorem. The generic endpoint failure
in L956 remains valid; L957 provides the separate actual-Xi input.

### Conceptual audit — 9 November 2026, step126

The stated specialization passes. The audit rechecked Kim's definitions
on pp819–820, Theorem1 on p821 and the complete Section2 proof on
pp822–823 against the actual hypotheses above. It reused the audited
endpoint conclusion of L957; it did not reprove its mollified moment.
No equation or zero-count convention needs correction. This is
verification of an existing known-method input, not a new signed
estimate or a result beyond the sources checked.

**Analytic and geometric checks.** L023–L024 supply genus at most one,
not merely evenness or a zero-strip assertion. The positive-even-integer
completion calculation in part1 proves nonconstancy; L024 then excludes
a zero-free Xi. Thus the degenerate pure-exponential exception to a
strict logarithmic-derivative sign cannot occur. For a bounded complex
neighborhood |z|<=R and a tail zero |ρ|>2R, the complete genus-one
logarithmic-derivative term and its derivative obey

    |1/(z-ρ)+1/ρ| <= 2R/|ρ|²,
    |1/(z-ρ)²| <= 4/|ρ|².

L024's summability includes multiplicities. These estimates verify
normal convergence of both series off the finite head of zeros and
justify (4), with conjugate grouping only after convergence. At each
allowed endpoint every grouped term is strictly negative, and at least
one exists. In particular an endpoint derivative zero really is simple
with critical weight zero; this is not assumed from generic simplicity.

Each closed Jensen disk misses both vertical boundaries. Any disk
meeting the slab has its real diameter wholly inside (a,b), hence has
radius less than both 1/2 and (b-a)/2. This verifies equality of the
strip counts and both rectangle counts, not equality of the rectangles.
The bounded radii and discreteness of the Xi zero set also verify local
finiteness of the disk family and open disk-free collars. Compactness
alone would not give such collars for an arbitrary infinite disk union.

**Independent check of the endpoint orientations.** Move the endpoints
outward instead: choose a_-<a and b_+>b in the same small disk-free
collars, with ff' nonzero. If necessary shrink the collars so that they
contain no f zeros and no f' zeros other than the original endpoint
zeros, and so that a_->0. The original closed counts N,N',J,J',K are
all unchanged on [a_-,b_+]: a stationary endpoint was already included
in N', and its critical weight is zero. Disk avoidance excludes nonreal
zeros throughout the added vertical slabs. The downward crossing gives

    sgn q(a_-)=sgn0 q(a)+e_a,
    sgn q(b_+)=sgn0 q(b)-e_b.

The nonstationary source term on this enlarged interval is therefore

    B_out=(sgn q(a_-)-sgn q(b_+))/2
         =(sgn0 q(a)-sgn0 q(b)+e_a+e_b)/2=E.

Applying the imported nonstationary identities with these unchanged
counts gives (1) and (2) directly. This independently checks both
inward-collar signs and the positive half contribution at each
stationary endpoint. It covers zero, one or two stationary endpoints;
no limiting winding number is assigned on an endpoint zero.

**Multiplicity and scope checks.** At every common zero of order r,
including a nonreal one, f' has order r-1 and f'/f has a simple pole
of residue r. The argument-principle count difference is -1, while
the separate f and f' counts retain r and r-1. Common real zeros are
excluded only from K. At a noncommon real zero of f' the sign in the
odd-m definition is nonzero by the defining order; all critical weights
are nonnegative integers, including even-m and higher odd-m cases.
Thus the subtraction yields exactly K=J-J', not a count of distinct
extrema or of simple critical points. The four existing direct inputs
remain sufficient. The only no-loss threshold here is K=0, still
unproved; neither endpoint avoidance nor this successful audit proves it.

## Mathlib

Full matching coverage for Kim's theorem and this Xi specialization
has not been checked and is unknown. No formal verification is claimed.
Hadamard factorization, locally uniform analytic differentiation and
the argument principle are supporting mathematical inputs, not an
identified Mathlib theorem proving this complete statement.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
