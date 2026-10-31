# L519 — Moving-interval eigenvector trace convergence (audited conditional reproduction)

## Hypotheses

Fix A>0 and one common finite real even signed measure mu_A from
L516 (2), with c=log(2pi). In particular it retains nu_rho, every
prime-power atom with log(n)<=2A, including cutoff equality, and the
negative density -2cosh(t/2)1_(|t|<=2A) of the signed pole. The
measure is not chosen separately for each interval.

For 0<ell<2A, put I_ell=(0,ell) and

    A_ell=G_(I_ell)-cI-R_(I_ell)K_(mu_A)E_(I_ell),
    Dom(A_ell)=Dom(G_(I_ell)),
    Psi(xi)=(1/2)log(1+xi^2), n(t)=exp(-|t|)/(2|t|).

Here G_(I_ell) is the zero-extension smooth-core part operator of
the Levy form specified in L513, and K_(mu_A) is whole-line signed
convolution. The Fourier convention is integral f(x)exp(-i xi x)dx.
Translation from L516's centered intervals defines this realization.
Its identification with the full localized Weil form remains the
retained external input, with L516's unaudited-manuscript qualification.
No positivity of this realization is assumed.

Let ell_j->ell_*>0 with ell_j,ell_*<2A. Suppose

    u_j in Dom(A_(ell_j)), A_(ell_j)u_j=lambda_j u_j,
    u_j real, ||u_j||_2=1, lambda_j real and bounded, lambda_j->0.

Assume a real normalized limiting eigenvector, rather than asserting
its existence or selecting it:

    u_* in Dom(A_(ell_*)), A_(ell_*)u_*=0, ||u_*||_2=1.

Put s_j=ell_j/ell_* and assume convergence under the specified unitary
dilation,

    (D_j u_j)(x)=sqrt(s_j)u_j(s_j x), 0<x<ell_*,
    ||D_j u_j-u_*||_(L2(0,ell_*))->0.

The original import used the pre-existing IMPORT assessment
`drafts/literature/2026-10-30-weil-moving-interval-trace-convergence-coverage.md`.
That KNOWN_IMPORTED application is retained below. A separate
2026-10-30 source-proof audit, under the pre-existing SPECIALIZE gate
`drafts/literature/2026-10-30-weil-moving-trace-source-proof-audit-coverage.md`,
now verifies the continuity argument using L513 and L515 as established
fixed-model inputs. This audit is REPRODUCTION, not a new continuity
mechanism or an audit of those inputs' original source proofs.

## Conclusion

Use the continuous representatives and L513-normalized physical traces
provided by L515:

    tau_L(u;ell)=lim_(t->0+) sqrt(log(1/t))u(t),
    tau_R(u;ell)=lim_(t->0+) sqrt(log(1/t))u(ell-t).

Then both signed endpoint traces converge:

    tau_L(u_j;ell_j)->tau_L(u_*;ell_*),
    tau_R(u_j;ell_j)->tau_R(u_*;ell_*).

No simplicity, parity, positive eigenvalue, spectral gap, H1 regularity
or prior trace-topology convergence is a hypothesis. Zero traces are
allowed. The result gives no vanishing of the limiting traces and no
rate in lambda_j. In particular it does not establish L516 (6), a
uniform collar step, full-Weil positivity or RH. The assumed limiting
nullvector and dilated L2 convergence remain independent obligations.

## Proof

### Precise imported assertion

Import bramble_trace, *Boundary traces and support variation for
localized Weil operators*, paper 67, v1, 27 October 2026,
[Section 7](https://rstation.ai/problems/riemann_hypothesis/papers/67),
the **unnumbered trace-continuity assertion after (7.5), its two
integral arguments through (7.6), and the paragraph immediately after
(7.6)**. This is a passage in the proof of Theorem 2.2, not a separately
numbered theorem. It asserts convergence of both physical endpoint
traces for bounded-spectrum eigenfunctions converging after unitary
dilation as the interval radius tends to a positive radius.

The assertion uses the common finite signed-measure class (2.8), the
normalization (2.2), uniform bounded data (7.1), and the full signed
renewal formula (3.19). Its conclusion precedes the simple-branch
application: simplicity is not a premise of this assertion. The
model, coordinates and normalization are checked next. No conclusion
of the source's support law or collar theorem is imported here.

### Common model and bounded-data hypotheses

L516 (2) is precisely the source's (3.4)–(3.5) realization in class
(2.8). All lengths lie below 2A, so the same mu_A supplies every
compression. Retained equality atoms have zero overlap when the
displacement equals the interval length; none is deleted from mu_A.
The convolution kernels and the reference form commute with
translation, so passing between centered and left-anchored intervals
does not change this measure or c.

Write a_j=ell_j/2 and a_*=ell_*/2. Choose a_0=a_*/2>0 and
A_0=(a_*+A)/2<A. After discarding finitely many indices,
a_0<=a_j,a_*<=A_0. Thus the source's eventual compact positive
radius range applies. Let M=||mu_A||_TV and choose a common upper
eigenvalue bound Lambda, also at least zero. L515 gives, for j and *,

    ||u||_infinity<=exp(Lambda+c+M)/sqrt(2),
    ||G_(I_ell)u||_infinity
        <=(|lambda+c|+M)||u||_infinity.

The second right side is uniformly bounded because the eigenvalues
are bounded. These are actual eigenvectors, not arbitrary convergent
L2 data. L515 also supplies both half-line splits and the bounded-data
application of L513. Hence its continuous representatives, trace
limits and both absolutely convergent signed formulas apply. In
particular the left trace retains

    integral_0^ell v(y)(G_(I_ell)u)(y)dy
      -integral_0^ell u(z) integral_ell^infinity v(y)n(y-z)dy dz,

and the right trace retains its reflected version. Neither exterior
integral is truncated at A or omitted. The normalization is the same
V(t)sqrt(log(1/t))->1 as in L513 and source (3.19).

### Unitary coordinates and physical traces

Set f_j(y)=u_j(y+a_j) on (-a_j,a_j), and define f_* likewise.
These translations preserve the eigen-equations, L2 norms and both
physical traces. The source's fixed coordinates on (-1,1) are

    (W_j f_j)(z)=sqrt(a_j)f_j(a_j z)
               =sqrt(a_j)u_j(a_j(z+1)).

The map J:L2(0,ell_*)->L2(-1,1),
(Jg)(z)=sqrt(a_*)g(a_*(z+1)), is unitary by change of variables.
Direct substitution, using s_j a_*=a_j, gives

    W_j f_j=J D_j u_j, W_* f_*=J u_*.

Thus the assumed convergence is exactly the source's unitary-dilation
convergence. No factor from an unnormalized change of variables is
missing.

For clarity, the endpoint traces here are those of f_j in its physical
interval, hence exactly those of u_j. If one instead took the trace
of D_j u_j on (0,ell_*), each trace would be sqrt(s_j) times the
physical trace: the extra logarithmic ratio is
sqrt(log(1/t)/log(1/(s_j t)))->1 as t->0 for each fixed j.
This is only a normalization check, not a continuity assertion for
arbitrary L2 functions. Since s_j->1, it creates no additional factor
in the claimed limits.

All hypotheses of the cited continuity assertion therefore match.
Applying it to f_j,f_* yields both displayed trace limits after
translation back. This finishes the original qualified import. The
following separate audit checks the source's uniform-integral and
forcing-limit arguments; neither part establishes an eigenvalue-relative
flux estimate.

### Separate source-proof audit, 2026-10-30

We verify precisely the unnumbered assertion after source (7.5),
through (7.6), under the hypotheses above. Only L513's fixed-interval
formula and renewal properties and L515's bounded-data application
are imported for the limiting argument. In particular, we do not use
the source's collar law, spectral-branch construction, norm-resolvent
argument or differentiation of an unbounded moving generator.

Discarding finitely many indices, choose fixed 0<m<=L<2A with
m<=ell_j,ell_*<=L. Put M=||mu_A||_TV. L515 and bounded eigenvalues
give finite constants U,H, independent of j and also valid at *, with

    ||u_j||_infinity<=U,  ||h_j||_infinity<=H,
    h_j=G_(I_(ell_j))u_j=(lambda_j+c)u_j+K_(ell_j)u_j,       (1)
    K_ell=R_(0,ell) K_(mu_A) E_(0,ell).

The operator equation in (1) holds in L2 on its stipulated domain;
its right side supplies the bounded representative. The half-line
splits and the continuous representatives used by L513 apply for
each j and for *. No uniform domain identification is being assumed.

#### Moving signed convolution and forcing

Use the fixed space L2(0,1), with unitary map

    (W_ell f)(x)=sqrt(ell)f(ell x),
    g_j=W_(ell_j)u_j,  k_j=W_(ell_j)h_j.

Since W_(ell_j)u_j=W_(ell_*)D_j u_j, the hypothesis gives
g_j->g_*=W_(ell_*)u_* in L2(0,1). Let E be zero extension to R
and R restriction to (0,1). Direct change of variables, with the
measure variable t left unchanged, gives

    C_ell:=W_ell K_ell W_ell^(-1),
    C_ell f=integral_R R[(Ef)(.-t/ell)] mu_A(dt),
    ||C_ell||_(2->2)<=M.                                   (2)

This is a Bochner integral in L2. Translation is strongly continuous
on L2(R): it follows for continuous compactly supported functions
by dominated convergence, then for all L2 functions by density and
translation isometry. Consequently, for each fixed f,

    ||(C_(ell_j)-C_(ell_*))f||_2
      <=integral_R ||(Ef)(.-t/ell_j)-(Ef)(.-t/ell_*)||_2
                                                        |mu_A|(dt)
      ->0.                                                (3)

The integrand is bounded by 2||f||_2 and tends to zero for each t;
the measure has finite total variation. Thus the scalar dominated
convergence theorem justifies (3), including atoms. In particular
a translation passing through a zero-overlap length creates no jump
in this strong topology. No variation-norm continuity of translated
measures, or operator-norm continuity of translations, is asserted.

Using (1)–(3) and lambda_j->0,

    k_j=(lambda_j+c)g_j+C_(ell_j)g_j
       ->c g_*+C_(ell_*)g_*=k_*                  in L2(0,1). (4)

Indeed the convolution difference is at most
M||g_j-g_*||_2+||(C_(ell_j)-C_(ell_*))g_*||_2.
Also ||g_j||_infinity<=sqrt(L)U and
||k_j||_infinity<=sqrt(L)H. Formula (4) proves the source's
forcing-convergence assertion without an interchange involving G.
Every prime-power atom, nu_rho and the signed pole stay inside the
single measure in (2).

#### Interior renewal integral

L513 supplies v positive, continuous and decreasing on (0,infinity),
V(r)=integral_0^r v(y)dy, and V(r)->0 as r->0+. Its first left-trace
integral becomes

    J_j=integral_0^(ell_j) v(y)h_j(y)dy
       =sqrt(ell_j) integral_0^1 v(ell_j x)k_j(x)dx.          (5)

For 0<epsilon<1, its absolute part on x<epsilon is bounded by
H V(ell_j epsilon)<=H V(L epsilon); the same estimate holds at *.
On [epsilon,1], the weights sqrt(ell_j)v(ell_j x) converge uniformly
to sqrt(ell_*)v(ell_*x). This follows from continuity on the compact
positive argument range [m epsilon,L]. Their L2 norms are bounded.
Equation (4) and Cauchy–Schwarz therefore give convergence of the
truncated pairings in (5). It follows that

    limsup_j |J_j-J_*|<=2H V(L epsilon).

Letting epsilon decrease to zero proves J_j->J_*. This uses bounded
forcing to handle the singular weight; L2 convergence alone would
not justify this passage. No L2 integrability of v near zero is used.

#### Entire exterior weight

Write the second left-trace integral, with its positive weight but
signed u_j, as

    F_j=integral_0^(ell_j) u_j(z)
                 integral_(ell_j)^infinity v(y)n(y-z)dy dz.

Its absolute convergence is part of L513. With z=ell_j(1-x) and
y=ell_j+t, the exact transformed expression is

    F_j=integral_0^1 g_j(1-x) Q_(ell_j)(x)dx,
    Q_ell(x)=sqrt(ell) integral_0^infinity
                              v(ell+t)n(t+ell x)dt.         (6)

Thus the square-root factor occurs in BOTH transformed trace terms.
For 0<x<1 and m<=ell<=L, monotonicity gives

    0<=Q_ell(x)
       <=sqrt(L)v(m) integral_(m x)^infinity n(s)ds
       <=sqrt(L)v(m)[C_m+(1/2)|log x|],
    C_m=(log^+(1/m)+exp(-1))/2.                            (7)

For the last bound, split the integral at 1 when m x<1, use
n(s)<=1/(2s) below 1, and bound its tail by
integral_1^infinity exp(-s)/2 ds=exp(-1)/2. If m x>=1,
the tail bound alone suffices. Since integral_0^1 |log x|^2 dx=2,
the right side of (7) is a fixed L2 function.

For each fixed x>0, the integrand in (6) is continuous in ell and
is dominated, uniformly in ell, by v(m)n(t+m x), integrable over
0<t<infinity. Dominated convergence in t proves
Q_(ell_j)(x)->Q_(ell_*)(x). Bound (7) then gives convergence in
L2(0,1), by applying dominated convergence to the squared difference.
Consequently

    |F_j-F_*|<=||g_j-g_*||_2 ||Q_(ell_j)||_2
                +||g_*||_2 ||Q_(ell_j)-Q_(ell_*)||_2 ->0.    (8)

No assumption that v decays at infinity appears: the full tail
t>0 is controlled by n. No exterior truncation, positivity of u_j,
or discarded signed-measure component enters this step.

#### Reflection, physical normalization and disposition

For every j, L513 states the physical left trace as J_j-F_j.
Equations (5)–(8) therefore prove its convergence. Its right-trace
formula replaces u_j(z),h_j(y) by u_j(ell_j-z),h_j(ell_j-y).
On (0,1) this replaces g_j,k_j by g_j(1-·),k_j(1-·).
Reflection is a fixed L2 isometry, preserves the uniform boundedness,
and leaves all the weight estimates unchanged. Repeating the same
two pairings proves right-trace convergence without a parity or
simplicity assumption. L515 supplies the reflected domain split.

These are the physical traces throughout. The sqrt(ell_j) factors
in (5) and (6), and W_(ell_j)=W_(ell_*)D_j, account for every dilation
factor; no boundary limit was inferred by applying an L2 trace map.
The normalization V(t)sqrt(log(1/t))->1 remains L513's precisely
normalized input.

The source's conditional continuity argument passes this independent
audit. No extra hypothesis or change to the conclusion is needed.
It is a reproduction with the moving forcing and full signed limits
made explicit, not progress beyond the inspected source. The proof
does not construct a limiting nullvector, force either limiting trace
to vanish, or bound trace squares by O(lambda_j). Full-Weil
identification and the original fixed-model source proofs retain
their qualifications; no collar or support-variation claim is audited.

## Mathlib

Full matching coverage of moving-interval signed renewal-trace
continuity has not been checked. The source claim and the primary
inputs retained by L513–L515 are external mathematical references;
no Lean declaration or proof was inspected. Unknown coverage is not
evidence of absence. The separate proof above audits only the specified
conditional continuity passage, not the full manuscript or its primary
inputs, and is not a formal verification.
