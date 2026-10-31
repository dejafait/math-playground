# L512 — Conditional audit of the one-prime activation comparison

## Hypotheses

This reproduces a known argument, conditional on explicit analytic
inputs. The source is bramble_trace, *Boundary traces and support
variation for localized Weil operators*, paper 67, v1, 27 October 2026,
[Theorem 2.4 and Sections 5, 8.1–8.2](https://rstation.ai/problems/riemann_hypothesis/papers/67).
The canonical page identifies v1; the version-suffixed URL failed
retrieval during this audit. The source's original renewal and boundary
regularity proofs are not independently certified here.

Fix a prime power n, ell=log(n), a=ell/2, and w=Lambda(n)/sqrt(n)>0.
Use zero extension, Fourier transform integral f(x)exp(-i xi x) dx,
and inner products conjugate linear in the first argument. The complete
Weil form is source (2.1): its Fourier multiplier is
Re psi(1/4+i xi/2)-log(pi), its pole term is
2 Re(hat f(i/2) conjugate(hat f(-i/2))), and its prime term is
-2 sum Lambda(m)/sqrt(m) Re integral f(x+log(m)) conjugate(f(x)) dx.
Retain every source term except the one atom pair explicitly deleted
in the comparison below. No positivity of this form is assumed.

Retain the following source inputs as hypotheses, rather than auditing
their original analytic proofs in this lemma.

1. The closed realization has the zero-extension logarithmic Fourier
   form domain. On a fixed compact range of radii it is the compression
   of G-cI-K_mu with G=(1/2)log(1-D_x^2), c=log(2pi), and the common
   finite real even signed measure in source (3.4). Its old realization
   A on (0,ell) is self-adjoint, bounded below, and has compact resolvent.
   Restriction to old interval and collar gives the operator block
   decomposition with their product domain and bounded cross operator,
   as in source Sections 3.1 and 4, equation (4.1).
2. Every fixed old eigenfunction e has a continuous representative and
   finite traces tau_L(e), tau_R(e), defined by multiplying its endpoint
   values by sqrt(log(1/t)) and letting inward distance t decrease to
   zero. Their existence and normalization, supplied by source (3.19),
   are retained, not proved here. Zero traces are permitted.
3. For the single right collar (ell,ell+delta), put L=log(1/delta),
   H_c=L2(0,1), and (U_delta h)(y)=sqrt(delta)h(ell+delta y).
   Its diagonal block D_delta and the deleted-family cross operator
   C_delta satisfy ||C_delta||<=M, D_delta>z for small delta, and

       R_delta(z)=(D_delta-z)^(-1),
       ||R_delta(z)||=O(1/L),
       L U_delta R_delta(z) U_delta^* -> I strongly.

   The last convergence is uniform for real z in each fixed compact
   set, on each fixed vector; the scaled inverses are uniformly bounded.
   These are the single-collar versions of source (4.1)/(4.5).
   For every fixed old eigenfunction, the right response has source
   (4.7)'s asymptotic

       (C_delta^*e)(ell+s)
         = -tau_R(e)sqrt(log(1/s)) + o(sqrt(log(1/s))).

   Constants and errors can depend on the fixed eigenfunction. No
   uniform bound over all eigenfunctions is assumed.

Let lambda be a fixed simple eigenvalue of A, and let u be its
L2-normalized eigenfunction, with reflection parity p in {+1,-1}.
Thus tau_L(u)=p tau_R(u). The two enlarged operators on (0,ell+delta)
include or delete only the translations of weight -w at displacements
plus/minus ell. Translation identifies this interval with the symmetric
one of radius a+delta/2. The old operator is the same in both families.
All limits below hold for this fixed old operator and fixed eigenvalue.

## Conclusion

For all sufficiently small delta>0 the two operators have unique nearby
simple eigenvalues lambda_full(delta), lambda_del(delta), and

    lambda_full(delta)-lambda_del(delta)
      = -2 w p |tau_R(u)|^2 delta/L + o(delta/L).                 (1)

In each exact scalar Schur reduction, the entire old complementary
spectrum contributes o(delta/L), uniformly on a common closed interval
inside the old complementary spectral gap. The exact scalar derivatives
are -1+o(1) there. These statements verify the conditional calculation
in source (8.1)–(8.8), including its sign, factor two and zero-trace case.

This is REPRODUCTION, not a new activation law or an unconditional audit
of its analytic inputs. It gives neither a uniform remainder as the old
operator varies nor a multiple-cluster matching theorem, effective
collar width, positivity of an enlarged window, or any RH conclusion.
The leading coefficient is strictly signed only when tau_R(u) is nonzero.

## Proof

### One collar and converging response vectors

Choose delta<ell. Translation by ell sends the right collar into
(0,delta), and the reverse translation supplies the adjoint block.
There is no old-old or collar-collar overlap of this atom, up to
measure-zero endpoints. Consequently both diagonal blocks are identical,
and the included cross operator is C_delta+B_delta with

    (B_delta^*e)(ell+s)=-w e(s),  0<s<delta,  ||B_delta||<=w.    (2)

Write C_0=C_delta, C_1=C_delta+B_delta. For any fixed old eigenfunction e,
the response hypothesis gives

    x_delta(e)=U_delta C_0^*e/sqrt(delta L)
        -> -tau_R(e) 1   in H_c.                               (3)

Indeed the relative remainder is uniformly small for 0<s<delta. The
squared L2 norm of sqrt(1+log(1/y)/L) is 1+1/L, and this function
converges to 1 in L2 by dominated convergence. This controls both its
main term and remainder in (3), without any pointwise uniformity in y
away from the endpoint being tacitly assumed.

The trace at the other endpoint and (2) give

    y_delta(e)=U_delta B_delta^*e/sqrt(delta/L)
        -> -w tau_L(e) 1   in H_c.                             (4)

To see the required domination, the trace implies
|e(s)|<=C/sqrt(log(1/s)) for all sufficiently small s. Thus
sqrt(L)|e(delta y)|<=C for 0<y<1. Pointwise convergence for y>0
and dominated convergence prove (4), also when the trace vanishes.
The contribution of B to the normalization in (3) is y_delta(e)/L;
hence (3) holds for C_1 as well. In particular
||C_f^*e||=O(sqrt(delta L)) for f=0,1.

Uniform boundedness and strong convergence in Hypothesis 3 apply to
these converging vectors: if T_delta(z) is the scaled inverse and
x_delta->x, then
||T_delta(z)x_delta-x|| is at most
||T_delta(z)|| ||x_delta-x||+||T_delta(z)x-x||, uniformly in z.
No operator-norm convergence of T_delta is used.

### Exact reduction on a common spectral gap

Let P be projection onto span(u), Q=I-P, and A_Q the restriction of
A to QL2(0,ell). Choose a closed real interval J about lambda with
positive distance g from spec(A_Q). All ensuing uniform estimates
refer to z in J. Define, for f=0,1,

    K_f(z)=C_f R_delta(z) C_f^*,
    S_f(z)=(A_Q-z-QK_f(z)Q)^(-1),
    b_f(z)=QK_f(z)u.

The response bounds imply

    ||K_f||=O(1/L),
    ||K_f u||=O(sqrt(delta/L)),
    <u,K_f u>=delta |tau_R(u)|^2+o(delta).                     (5)

The first bound and the gap ensure that S_f exists with norm at most
2/g for small delta. The inverse is on the whole Q space. At z=lambda
use (A_Q-z)^(-1); writing a full resolvent of A there would be invalid.
Schur elimination of first the positive collar and then this signed
old complement is exact and gives

    F_f(z)=lambda-z-<u,K_f(z)u>-<b_f(z),S_f(z)b_f(z)>.          (6)

Both eliminated blocks are invertible on J. Thus F_f(z)=0 is equivalent
to an eigenvalue of the full enlarged operator in J, and the respective
kernels have the same dimension. This equivalence follows by solving
the collar component and then the Q component in the two block equations;
the bounded cross operators and the stated domains justify the solutions.

### The full complement is smaller than the activation scale

Set alpha=sqrt(delta/L) and v_f(z)=K_f(z)u/alpha. These vectors are
uniformly bounded by (5). For each fixed member e_j of an orthonormal
eigenbasis of A, (3) and the inverse bound give

    |<e_j,K_f(z)u>|
      <= ||C_f^*e_j|| ||R_delta(z)|| ||C_f^*u||=O_j(delta).

Hence sup_z |<e_j,v_f(z)>|=O_j(sqrt(delta L))->0. For an arbitrary
fixed test vector, approximate it by finitely many e_j and use the
uniform norm bound on v_f for the remainder. This proves uniform weak
convergence to zero on J. It does not sum any squared endpoint traces.

By compact resolvent, R_Q(z)=(A_Q-z)^(-1) is compact, and the resolvent
identity gives norm continuity in z on J. A compact operator maps a
uniformly bounded, uniformly weakly null family to norm-zero uniformly:
approximate that operator by a finite-rank operator and test its finitely
many coordinate functionals. Choose a finite operator-norm net for
{R_Q(z): z in J}; applying the preceding fact to each net member proves

    sup_z ||R_Q(z)Qv_f(z)|| -> 0.

The inverse identity gives ||S_f(z)-R_Q(z)||=O(1/L), uniformly on J.
Therefore sup_z ||S_f(z)Qv_f(z)||->0. Multiplication by the remaining
bounded vector proves

    <b_f(z),S_f(z)b_f(z)>=o(delta/L), uniformly on J.           (7)

This is a bound for the complete signed quadratic form. It covers
negative as well as positive old complementary eigenvalues. A gap
estimate alone gives only O(delta/L), which would not prove (1).

### Atom coefficient without subtracting larger remainders

Put T_delta(z)=L U_delta R_delta(z) U_delta^*. Expand the exact
difference K_1-K_0 into C_0 R B^*+B R C_0^*+B R B^*. By (3)/(4),

    <C_0^*u,R B^*u>
      = (delta/L)<x_delta(u),T_delta(z)y_delta(u)>
      = (delta/L)w conjugate(tau_R(u))tau_L(u)+o(delta/L).

Its adjoint is the conjugate for real z. Also
|<B^*u,R B^*u>|<=O(delta/L)O(1/L)=O(delta/L^2).
All errors are uniform on J by the converging-vector argument. Thus

    <u,(K_1-K_0)u>=(delta/L)J_w+o(delta/L),
    J_w=2w Re(conjugate(tau_R(u))tau_L(u)).                    (8)

We have compared the exact operators: subtracting two unspecified
o(delta) errors in (5) would not establish (8). Applying (7) to each
family separately and then (6) yields

    F_1(z)-F_0(z)=-(delta/L)J_w+o(delta/L).                    (9)

### Exact derivatives and the two roots

Differentiation is with respect to real z, with delta fixed. The
resolvent identity, not differentiation of a little-o error, gives

    K_f'=C_f R_delta^2 C_f^*,
    ||K_f'||=O(L^(-2)),
    ||K_f'u||=O(sqrt(delta/L^3)),
    <u,K_f'u>=||R_delta C_f^*u||^2=O(delta/L).

For the complementary inverse,

    S_f'=S_f(I_Q+QK_f'Q)S_f,

so ||S_f'||=O(1). In (6), ||b_f||=O(sqrt(delta/L)) and
||b_f'||=O(sqrt(delta/L^3)); consequently the derivative of its last
term is O(delta/L^2)+O(delta/L)=O(delta/L). It follows that

    F_f'(z)=-1+O(delta/L), uniformly on J.                    (10)

At the two fixed endpoints of J, F_f(z)=lambda-z+O(delta), by (5)/(7).
These endpoint values have opposite signs for small delta. Equations
(10), (6) and the intermediate value theorem give one and only one
simple nearby eigenvalue in each family. Applying (5)/(7) at the root
also shows that its distance from lambda is O(delta); both roots thus
lie in the same J used above.

Let r_f denote those roots. Evaluate (9) at r_0, then use the mean-value
theorem on F_1 between r_0 and r_1:

    0=F_1(r_0)+F_1'(xi)(r_1-r_0),
    F_1(r_0)=-(delta/L)J_w+o(delta/L),
    F_1'(xi)=-1+o(1).

Thus r_1-r_0=-(delta/L)J_w+o(delta/L), with the negative sign as stated.
Reflection gives J_w=2wp|tau_R(u)|^2, proving (1). If the trace is zero,
the same estimates give o(delta/L); no division by the trace occurred.

The common domain, all-eigenfunction response input and fixed gap are
essential hypotheses. Compactness supplies no effective modulus here.
None of these estimates is uniform in a moving interval or collapsing
gap, and no assertion about a first zero of the ground eigenvalue follows.

## Mathlib

Full matching coverage is unchecked. The named spectral theorem,
bounded resolvent identity, compact-operator finite-rank approximation,
dominated convergence and real mean-value theorem support the argument;
no specific Mathlib declaration was inspected. This is not evidence that
the full activation theorem is absent from Mathlib.
