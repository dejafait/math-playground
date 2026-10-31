# Lemma 567: complete finite Hermite-band dual specialization

## Hypotheses

Let N>=2 be an integer, q=2N-1, and let H_j be physicists'
Hermite polynomials. Put

    h_j=H_j/sqrt(2^j j!), s_j=h_j^2, 0<=j<=q,
    W={real even polynomials of degree <=2q}.

Let C be the cone of polynomials h^T G h, where G is a real symmetric
PSD matrix indexed by 0,...,q, zero between opposite parities and
whenever |i-j|>2. The normalization is an invertible positive diagonal
congruence of the original H-basis Gram problem.

For the application take F=D(P_N)=P_N'^2-P_N P_N'' with the actual
coefficients and normalization of L564. No sign of F is assumed.

Standard source inputs are Vandenberghe--Andersen, *Chordal Graphs
and Semidefinite Optimization*, DOI 10.1561/2400000006,
[author manuscript](https://www.seas.ucla.edu/~vandenbe/publications/chordalsdp.pdf),
Theorem 9.2, pp. 340--341 (zero-filled chordal PSD decomposition),
and section 10.1, pp. 356--357 (the explicitly stated sufficient
closed-image criterion from Rockafellar, *Convex Analysis*, Theorem
9.1). Finite-dimensional strict conic separation is imported from
[MOSEK Modeling Cookbook 3.4.0, section 8.2, Lemma 8.3](https://docs.mosek.com/modeling-cookbook/duality.html#infeasibility-in-conic-optimization).
The separate source assessment inspected these statements and relevant
proof cases. These are known convex results, not new separation claims.

Use the finite physicists' Hermite formula as stated in O'Sullivan,
*Zeros of Jensen polynomials and asymptotics for the Riemann xi
function*, arXiv:2007.13582v2, opening of
[section 2](https://arxiv.org/html/2007.13582v2#S2), together with
H_j'=2j H_(j-1) as in L564. No source asserts the actual separator
whose existence is being tested here.

## Conclusion

The s_j form a basis of W. Thus specifying d_j=ell(s_j), j=0,...,q,
uniquely specifies a real linear functional ell on W. It belongs to
C* (ell nonnegative on C) exactly when

    d_j>=0, 0<=j<=q,
    d_j d_(j-2)>=e_j^2, 2<=j<=q,
    e_j=((j-1)d_(j-1)-sum_(k=0)^(j-2)d_k)/sqrt(j(j-1)).   (1)

In particular this is a complete list of allowed-square tests, not
only tests of four leading coefficients. If F=sum_(j=0)^q a_j s_j,
the complete pairing is

    ell(F)=sum_(j=0)^q a_j d_j.                           (2)

The cone C is closed. Hence F has no specified sparse PSD Gram
representation iff there is a d satisfying (1) with (2)<0. This
assertion is finite-dimensional for each fixed N, with no uniform
separator, coefficient precision or large-N assertion.

For any real x, the evaluation ell_x(F)=F(x) satisfies every test
(1), including singular cases. A rigorously negative D(P_N)(x)
would therefore separate even the unrestricted SOS cone. The
numerical screen recorded below supplies no such rigorous negativity.

## Proof

**Basis and allowed cone.** The degree of s_j is 2j, and its leading
coefficient is 2^j/j!>0. Distinct even degrees prove independence;
there are q+1 polynomials in the (q+1)-dimensional space W.

The sparsity graph is the disjoint union of the even and odd paths,
with edges {j,j-2}. It is chordal, and its maximal cliques are edges
(or isolated vertices). The cited Theorem 9.2 therefore identifies C
with sums of terms

    gamma_j s_j, gamma_j>=0,
    (h_j,h_(j-2)) B_j (h_j,h_(j-2))^T, B_j PSD, 2<=j<=q.

Including additional individual vertex terms does not change that
cone. Conversely every embedded PSD edge or vertex matrix is PSD
and has exactly the allowed zeros, so its sum is a permitted matrix.
This uses zero-filled PSD decomposition, not PSD completion.

**Cross-products.** A finite identity, for j>=2, is

    sum_(k=0)^(j-1) s_k
       =j s_(j-1)-sqrt(j(j-1)) h_j h_(j-2).              (3)

Here is a direct normalization check and proof. The finite Hermite
formula gives H_j=2t H_(j-1)-2(j-1)H_(j-2). Define

    B_j=[j H_(j-1)^2-(j-1)H_j H_(j-2)]/[2^(j-1)(j-1)!].

B_2=1+2t^2=s_0+s_1. For j>=3, multiplying
B_j-B_(j-1)-s_(j-1) by 2^(j-1)(j-1)! gives

    (j-1)[H_(j-1)^2-H_j H_(j-2)-2(j-1)H_(j-2)^2
                                  +2(j-2)H_(j-1)H_(j-3)].

Insert H_j=2t H_(j-1)-2(j-1)H_(j-2). The remaining expression
is (j-1)H_(j-1)[H_(j-1)-2t H_(j-2)+2(j-2)H_(j-3)]=0.
Induction proves B_j=sum_(k<j)s_k. Replacing both products by
normalized h's gives (3), including j=2 and no negative index.
Applying ell to (3) gives the stated e_j=ell(h_j h_(j-2)).

**All constraints and full pairing.** Nonnegativity on an individual
square is d_j>=0. For every real A,B, nonnegativity on
(A h_j+B h_(j-2))^2 is equivalent to PSD of

    [[d_j, e_j], [e_j, d_(j-2)]].

The complete two-by-two PSD criterion is precisely its two nonnegative
diagonals and nonnegative determinant. It also forces e_j=0 if either
diagonal is zero; no inverse pivot or strict-feasibility premise is
used. Edge decomposition then proves equivalence with ell in C*.
Linearity in the unique full basis expansion gives (2), with every
degree retained. At evaluation, that block is the outer product of
(h_j(x),h_(j-2)(x)), and d_j=h_j(x)^2, so all tests hold exactly.

**Closed image and strict alternative.** In finite-dimensional real
spaces, let K be the product of the nonnegative vertex scalars and
PSD two-by-two edge cones, and let A sum their polynomial terms.
This is a closed convex cone and a linear map, with image C.
If a member of K maps to the zero polynomial, all its summands are
nonnegative at every real t. Consequently each summand vanishes at
every real t. A nonzero s_j cannot vanish identically, so each
vertex scalar is zero. For an edge, factor B_j=R^T R. Every row
of R gives a real linear combination of H_j and H_(j-2) whose
square is zero for every t. The distinct degrees make these two
polynomials linearly independent, so every row of R is zero.
Thus B_j=0 for each edge, and ker(A) intersect K={0}.

The cited closed-image criterion now applies to this particular
map and cone, proving C closed. The cited conic alternative, with
its sign changed to ell(C)>=0 and ell(F)<0, gives strict separation
of every F outside C. Its closure-only infeasibility case cannot
occur here. Conversely such a functional plainly excludes F in C.
No numerical solver status or PSD-completion theorem enters this
argument.

**Initial application and limits of the screen (before C567a).** L564 gives P_N of
degree 2N, so D(P_N) is even of degree <=4N-2=2q and belongs to W.
It is the complete discriminant, including all mixed terms. The
screen `scripts/hermite-gram/global-dual-screen.py` evaluates its
finite Hermite sum and both derivatives, using numerical approximations
of every b_(2n), n<=N. Reproduction uses the pre-existing interpreter:

    /Users/vermeer/Applications/anaconda/bin/python scripts/hermite-gram/global-dual-screen.py

Full numerical diagnostics are saved in
`scripts/hermite-gram/global-dual-screen.json`. Two tanh-sinh meshes
on [0,4], 24 theta terms, and 250-decimal arithmetic suggest negative
pairings at (N,x)=(64,163/4),(128,271/4),(256,447/4). Mesh agreement
is not a quadrature remainder bound; neither omitted theta terms nor
spatial tails have rigorous enclosures in this screen. Accordingly
there are ZERO certified negative pairings, no proved obstruction
at these cutoffs, and no inferred unrestricted or restricted Gram
feasibility. Even certified signs at these three x would not supply
the required unbounded family. No Xi sign, signed transfer through
L564's absolute errors, multiplicity conclusion or RH claim follows.
The specialization above is unaudited; it reproduces the known
finite convex framework in this particular Hermite basis.

The complete allowed-square constraints at these three exact rational
points are separately verified by

    python3 scripts/hermite-gram/global-dual-evaluation-constraints.py

Its full certificate is
`scripts/hermite-gram/global-dual-evaluation-constraints.json`.
For x=p/4 set V_j=2^j H_j(x). The exact integer recurrence is
V_0=1, V_1=p, V_(j+1)=p V_j-8j V_(j-1). The program checks every
V_j against the complete finite Hermite formula and checks all 896
nonnegative diagonal squares and all 890 edge determinants (each
zero). Their unnormalized edge blocks have entries
H_j(x)^2, H_j(x)H_(j-2)(x), H_(j-2)(x)^2; positive diagonal
congruence gives the normalized blocks in (1). Thus every allowed
square constraint is certified for these functionals. The missing
ingredient is their pairing with the actual complete polynomial.

The computed full-pairing approximations are about -2.726842928e-22,
-8.224729367e-38 and -2.005082950e-69, respectively. These are
approximations, not rigorous upper bounds; the required upper bound
is strictly below zero and NONE is supplied. A saved zero mesh
disagreement means equality at saved precision, not exact integration.
These real evaluation points also lie far beyond the corresponding
L564 intervals [T,2T] with T=sqrt(N/16)-1. Even a certified global
obstruction here would leave interval positivity and Xi transfer open.

The later complete rational pairing certification is recorded in C567a.
It resolves this initial screen's three finite sign gaps only; the
unbounded-family, interval and Xi-transfer gaps remain open. The
provisional numerical evidence above is preserved as historical evidence.

## Mathlib

Full coverage of this complete finite Hermite-band dual specialization
has not been checked. Availability is unknown, not absent. General
finite-dimensional separation, PSD matrices and Hermite identities
would be supporting inputs rather than a matching actual-coefficient
separator. Reference: https://leanprover-community.github.io/mathlib4_docs/
