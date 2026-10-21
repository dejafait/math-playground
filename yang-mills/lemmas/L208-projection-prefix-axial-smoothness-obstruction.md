# L208 — The actual projection-side prefix is not uniformly axial norm-C²

## Hypotheses

Use L187, L196 and L206's actual relative box and full-link matrices,
with even N>=8 and a=8/N. Keep D, P=I-DG_0D^T,
G_0=(D^T D)^(-1), the lower prefix Phi, and the endpoint **sum** q.
Vertex values are zero at every physical face and all normal end
edges are retained. No infinite-grid projection is substituted.

Consider only the direction-1 input/output block of the actual factor
VP=q Phi P occurring in L187(7). Write its transverse layer blocks as

    C_s,b=[VP]_(direction 1, axial tail s; direction 1, axial tail b),

operators on the full three-dimensional interior vertex space, and
fix b=N/2. In the differences below s is interior. Set
x_s=-4+a(s+1/2). No restriction of covariance inputs, residual,
probe modes or other trace factors is made by this factor test.

## Conclusion

There is an actual normalized transverse Dirichlet mode v_N with
Delta_T v_N=6v_N such that

    <v_N,(C_b,b-C_(b-1),b)v_N> >=3/4,                 (1)
    <v_N,(C_b,b-2C_(b-1),b+C_(b-2),b)v_N> >=9/14.   (2)

The comma separates the output and input axial indices; in (2) the
three blocks have input index b throughout. Thus any operator-norm
C² interpolation C_N(x) agreeing with these blocks at their physical
coordinates has, on the corresponding interior interval,

    sup ||C_N'|| >=3/(4a),
    sup ||C_N''|| >=9/(14a²).                        (3)

Even right multiplication by the finite transverse energy inverse
T_N^(-2), T_N=Delta_T+epsilon I, 0<epsilon<=1, leaves the second
lower bound at least 9/(686a²). This last assertion concerns this
finite factor, not a replacement of L207's infinite-grid transition.

Consequently L207 cannot be applied with uniformly bounded c_1,c_2
after absorbing this whole projection-side prefix into its axial
coefficient. This is a quantified obstruction to that specific
norm-Taylor application, including on interior rows and at transverse
energy 6. It is not an obstruction to keeping only deterministic
exterior multipliers in that coefficient, or to evaluating the
Green contraction in its original order.

No lower bound for a response, nonzero actual probe weight, failure
of convergence, or cubic coefficient follows. Multiplication by the
actual exterior columns and the signed residual may change the
estimate. Both actual probes, long plateaus, all four covariance
blocks, finite Green terms, upper jumps, subtractions and complete
heat sums remain in the joint problem. Independent compensation,
finer scales, interacting comparison and continuum/infrared gaps
remain unresolved. This is a standard finite-resolvent specialization,
not a claim of progress beyond the checked sources.

## Proof

### 1. Restrict the actual projection, without deleting its Green part

Let D_A send the N-1 pinned axial vertex values to N axial edges,
(D_A phi)_r=phi_(r+1)-phi_r, 0<=r<=N-1, with phi_0=phi_N=0.
Set L_D=D_A^T D_A and L_E=D_A D_A^T. The latter has diagonal
1 at its two endpoints and 2 elsewhere, with off-diagonal -1.
Let Phi_A be the original lower sum to interior vertices:
(Phi_A w)_s=sum_(r=0)^(s-1)w_r.

L026's exact component spectrum identifies D^T D with
L_D tensor I+I tensor Delta_T on vertices. Fix any normalized
transverse mode of eigenvalue lambda>0. The direction-1 block
of P on that mode is exactly

    P_11(lambda)=I-D_A(L_D+lambda I)^(-1)D_A^T
                 =lambda(L_E+lambda I)^(-1).         (4)

To verify the second equality, multiply by L_E+lambda I, using
(L_E+lambda I)D_A=D_A(L_D+lambda I). The product of the first
expression in (4) with L_E+lambda I is lambda I. This verification
also includes the constant axial edge mode: L_E has a zero mode,
but L_E+lambda I is invertible. No scalar Dirichlet condition is
assigned to the axial edge space.

Write R_lambda=(L_E+lambda I)^(-1), and
B_s=(Phi_A P_11(lambda))_(s,b). For all interior differences,

    B_(s+1)-B_s=lambda (R_lambda)_(s,b).             (5)

The endpoint sum on a direction-1 edge gives
C_s,b v=(B_s+B_(s+1))v on this transverse mode. Consequently

    (C_b,b-C_(b-1),b)v
       =lambda[(R_lambda)_(b,b)+(R_lambda)_(b-1,b)]v,
    (C_b,b-2C_(b-1),b+C_(b-2),b)v
       =lambda[(R_lambda)_(b,b)-(R_lambda)_(b-2,b)]v. (6)

These are identities for the finite pinned projection. Equivalently,
they use L196's Phi P=Phi-G_0D^T from L206(8), with both terms
retained. The rows in (6) lie near the middle of the box, so the
obstruction is separate from the upper pinned jump.

### 2. A finite resolvent lower bound

For completeness the needed bound is elementary and uniform in N.
Write L_E=2I-J, where J has off-diagonal entries 1 and an additional
diagonal entry 1 at each endpoint. J is nonnegative, with every row
sum 2. Thus

    R_lambda=sum_(k=0)^infinity J^k/(lambda+2)^(k+1)

converges in operator norm and has nonnegative entries. It has
strictly positive entries because the path connects every pair.
For w=R_lambda e_b the k=0 term gives w_b>=1/(lambda+2).

Let M=max_(r!=b) w_r. A maximizing off-source row cannot have no
neighbor b: its equation would give lambda M<=0, contradicting
positivity, also at an endpoint of diagonal lambda+1. If the row
is interior and adjacent to b, its equation instead gives
(lambda+2)M<=w_b+M, so M<=w_b/(lambda+1). At an endpoint
adjacent to b the equation is (lambda+1)M=w_b and gives the
same bound. Therefore

    w_b-w_(b-2) >=lambda w_b/(lambda+1)
                    >=lambda/[(lambda+1)(lambda+2)]. (7)

All indices are valid since N>=8 and b=N/2. The proof uses the
entire finite resolvent, with its actual endpoint diagonals.

By L026(6)-(7), the transverse product mode with all three indices
equal to N/2 has

    lambda=4 sum_(mu=2)^4 sin²(pi/4)=6.

Normalize that sine product to obtain v_N. The first identity in
(6), positivity and w_b>=1/8 yield (1). The second identity and
(7) give 6*6/(7*8)=9/14, proving (2). This is an actual mode of
the finite projection, not a synthetic covariance or probe value.

### 3. Compare with the hypothesis needed for coefficient replacement

For any norm-C² interpolation, the fundamental theorem of calculus
gives ||C_N(x+a)-C_N(x)||<=a sup||C_N'||. Its second-difference
integral formula gives

    C_N(x+a)-2C_N(x)+C_N(x-a)
       =integral_(-a)^a (a-|h|)C_N''(x+h) dh,

and hence a norm at most a² sup||C_N''||. Testing these identities
against v_N in (1)-(2) proves (3). Multiplication on the right by
T_N^(-2) multiplies both scalar tests by (6+epsilon)^(-2)>=1/49,
giving the additional second-derivative bound stated above.

L207 assumes bounded derivatives of the operator-valued coefficient
before summing its transition moments. Here even the minimal second
derivative is of order a^(-2). In particular its displayed positive
Taylor allowance a² c_2[epsilon^(-1/2)+eta d^4] does not certify
o(a) for this coefficient by those norms. This is failure of that
estimate, not a lower bound on the actual Taylor error. Smooth
exterior amplitudes, full signed combinations or an exact resolvent
calculation can still supply cancellations that this norm test loses.

The original L187(7) contains this VP factor. A Taylor argument may
keep the deterministic smooth multipliers separate from it; it must
then retain the intervening projection/Green factor in the remainder
and prove an original-order trace bound. Neither (4) nor this local
negative test permits commuting that factor through A or a prefix,
discarding the plateau, or assigning its lower bound to a signed
probe response. No mathematical script is needed: (4)-(7), the full
mode eigenvalue and both interpolation inequalities are exact.

## Mathlib

Full matching projection-prefix obstruction and joint cubic limit:
**not checked**. Supporting finite spectral calculus, Neumann series,
discrete maximum principle and Banach-valued differentiation:
**not checked**; unknown coverage is not absence. The exact finite
recurrence and constants are proved here because the hypothesis
failure concerns this actual relative block and mesh scaling.
No general flow or renormalization theorem is reproved. Reuse the
unchanged [approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
within its exact joint-group target; no literature refresh or
originality claim is made.
