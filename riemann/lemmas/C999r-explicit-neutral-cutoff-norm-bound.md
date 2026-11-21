# C999r: An explicit norm remainder for the exact neutral endpoint compression

## Hypotheses

Use C744z Sections1-3 and its formula(4), with ell=log(3)/2,
H=L2(0,ell;C), the orthonormal cosine basis e_n, and the two-moment
map C f=(integral exp(x/2)f(x)dx, integral exp(-x/2)f(x)dx).
Let H0=ker(C), P0 its orthogonal projection, and

    V={f in H: sum_n (1+log(2+n)) |f_n|^2<infinity},
    V0=V intersect H0,    f_n=<f,e_n>.

The inner product is linear in the first argument. On V0 the closed
single-cell form is a0(f,f)=sum_n h_n|f_n|^2+<Sf,f>, where

    h_n=Re psi(1/4+i n*pi/(2ell))-log(pi),    S>=0,
    A0>=c I,    c=c_*=8.9*10^-18,    E=A0^-1/2.

Retain the original analytic response identity, arithmetic contracts,
whole-neutral-core qualification, and unreplayed source computation for
c_* from C744z. This result does not independently validate them or
introduce a stronger floor. C744v Sections3-4 supplies bounded positive
S and the diagonal envelope below; C999k Section1 supplies the exact
moment ratios. C744w(8) has the same moment formula, but no numerical
covariance or finite inverse from that certificate is needed here.

Keep C744z's actual separation7 and separation14 operators T,U, with

    K=P0 T|H0,    J=P0 U|H0,    R=E K E,    V14=E J E,
    ||K||<=k=4.71,    ||J||<=u=29.813203120,    ||R||<=1.

The last inequality is C744z's use of the qualified two-cell result;
no sign assumption on the three-cell block S3 is made. The bound on U
includes all334 prime powers, the zero-delay term and the whole
continuous response. The constants k,u are exact terminating decimals
chosen above the inherited bounds, not new floating computations.

Standard inputs are imported from Gerald Teschl, *Mathematical Methods
in Quantum Mechanics*, GSM99, first edition, version12February2009,
[author PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf):
Theorem1.3(iii), printed p41 (Parseval), Theorem1.7, pp43-44 (orthogonal
projection and best approximation), Theorems2.13/2.18, pp71-72/77
(closed-form representation and lower-bound spectral support), and
Theorems3.1/3.2/3.7, pp90-92/96, including (3.25)-(3.27)
(bounded and unbounded spectral calculus and its domains). These general
results are imported, not reproved. Assessment604 and source-gate repair605
cover the original specialization; assessment606, separately approved607,
covers the independent audit in Section5. Neither qualitative compactness
nor Galerkin convergence alone supplies the effective constants below.

## Conclusion

For every integer N>=512 let F_N be the raw cosine projection onto
span(e_0,...,e_(N-1)), let H_N=H0 intersect range(F_N), and let P_N
be the L2 orthogonal projection in H0 onto H_N. Put Pi_N=P_N direct-sum
P_N. The finite compression extended by identity is exactly

    S3_N=I+Pi_N(S3-I)Pi_N,
    S3=[[I-R*R, -(V14+R^2)*], [-(V14+R^2), I-RR*]].

Define the following completely specified constants:

    b=max({0} union {-h_n: 0<=n<512}),
    d_N=log(N/(2ell))-2ell^2/(9N^2),
    a=1+ell^2/(4pi^2),
    eta_N=sqrt(1+a^2/[3(N-1)^3]),    M=c^-1/2,
    delta_N=min{M, eta_N sqrt[(1+b/c)/(d_N+b)]},
    epsilon_N=2 M (u+2k) delta_N.                       (1)

Here b is a finite maximum of512 explicit real special-function
values, not an unspecified bound or a supremum requiring a convergence
certificate. No numerical evaluation of b is needed for this theorem.
All dependence on the qualified c_* is displayed in(1).

Then, on H0 and H0 direct-sum H0 respectively,

    ||(I-P_N)E||=||E(I-P_N)||<=delta_N,
    ||S3-S3_N||<=epsilon_N,    epsilon_N -> 0.          (2)

Both endpoint/complement mixed blocks and every induced middle product
are retained. In particular S3_N uses the exact full E and full products;
it is not constructed from a finite inverse square root or by squaring
a truncated R.

This is a conditional quantitative specialization, not a sign theorem
or a claim of originality. This particular allowance is ineffective:

    epsilon_N>6*10^6 for 512<=N<=exp(10^6).             (3)

This lower bound concerns the displayed allowance, not the true error.
Finite normalized entries and their errors, any positive finite margin,
c_*/core validation, C744q, H2, non-neutral directions and global
actual-Xi assembly remain open. The separate conceptual audit608 in
Section5 upholds (1)-(3) under exactly the retained contracts, including
the impractical allowance and threshold(13). It is REPRODUCTION of a
standard-method specialization, not an independently validated source
computation, a new sign result, or a complete RH candidate.

## Proof

### 1. Form-domain control of the raw tail of E

C744v(5) gives h_n>=d_n for n>=512. The function
log(t/(2ell))-2ell^2/(9t^2) is increasing for t>0, since its derivative
is 1/t+4ell^2/(9t^3)>0. Its value at512 is positive by C744v's
enclosure (>6.14427654). Thus d_N>0, all h_n>=-b, and h_n>=d_N
when n>=N. For f in V0 and Q_N=I-F_N, positivity of S implies

    a0(f,f)>=d_N||Q_N f||^2-b||F_N f||^2,
    (d_N+b)||Q_N f||^2<=a0(f,f)+b||f||^2.              (4)

The diagonal series exists as a form series on V. It has only finitely
many possibly negative terms, so splitting it here is legitimate.
No raw projection is asserted to preserve neutrality.

For v in H0, spectral calculus gives f=Ev in V0,
a0(Ev,Ev)=||v||^2 and ||Ev||<=M||v||. These are form-domain facts;
they do not assert Ev belongs to Dom(A0). Apply(4) to obtain

    ||Q_N Ev||^2 <= [(1+b/c)/(d_N+b)] ||v||^2.         (5)

This is a bound on the full raw tail for every input, not a fixed-profile
estimate. Positivity of S3 is not used.

### 2. Exact neutral correction and the true orthogonal projection

Write k_n=n*pi/ell, nu_0=ell^-1/2, and nu_n=sqrt(2/ell) for n>0.
C999k Section1 gives, for t=+/-1/2,

    C_t(e_n)=nu_n t[(-1)^n exp(t ell)-1]/(1/4+k_n^2).

For p=n mod2 define

    r_n=(nu_n/nu_p)(1/4+k_p^2)/(1/4+k_n^2).

Then C(e_n)=r_n C(e_p), including r_0=r_1=1. The two columns
C(e_0),C(e_1) are independent: their plus/minus signs are respectively
(+,+) and (-,+), with all four entries nonzero. Consequently f in H0
satisfies the two separate parity identities

    sum_(n even) r_n f_n=0,    sum_(n odd) r_n f_n=0.   (6)

These sums converge absolutely: r_n=O(n^-2), with the explicit bounds
below, and (f_n) is square summable. Continuity of C and Parseval
justify taking moments termwise and grouping by parity.

For n>=2 the ratios obey

    r_n<=sqrt(2)ell^2/(4pi^2 n^2)  (n even),
    r_n<=(1+ell^2/(4pi^2))/n^2     (n odd).

Since ell<1 and pi>3, the even numerator is less than1 and the odd
one is a>1; hence r_n<=a/n^2 in either parity. For f in H0 put

    t_p=sum_(n>=N, n mod2=p) r_n f_n,
    g_N=F_N f+t_0 e_0+t_1 e_1.

Equation(6) proves Cg_N=0 exactly. Since N>=512, g_N lies in H_N
and in V0. The correction is added with a plus sign because the
retained parity sum is -t_p. Raw tails and the two correction modes
are orthogonal. Cauchy--Schwarz on each disjoint parity, followed by
the decreasing-series integral bound, therefore gives

    |t_0|^2+|t_1|^2
      <= max_p(sum_(n>=N,n mod2=p) r_n^2) ||Q_N f||^2
      <= [a^2/(3(N-1)^3)] ||Q_N f||^2,
    ||f-g_N||^2=||Q_N f||^2+|t_0|^2+|t_1|^2
      <=eta_N^2 ||Q_N f||^2.                          (7)

The integral used is sum_(n>=N)n^-4<=integral_(N-1)^infinity
t^-4 dt=1/[3(N-1)^3]. It bounds all omitted indices for either parity.
The independence of the two low columns also shows dim(H_N)=N-2;
in particular H_N is a closed finite-dimensional subspace of H0.

Teschl's best-approximation theorem applies to this subspace of the
Hilbert space H0, so ||(I-P_N)f||<=||f-g_N||. Apply(7) and(5) to
f=Ev. The trivial estimate ||(I-P_N)E||<=M supplies the other branch
in delta_N. Since E and P_N are self-adjoint on H0, taking adjoints
gives the equal bound for E(I-P_N). This proves the first part of(2).
No commutation between P_N and E, A0 or F_N is used. Also(7) implies
P_N f->f for every f in H0, though only the quantitative bound on E
is needed below.

### 3. All block products and both sides of the cutoff

For this section write P=P_N and F=I-P on H0. Boundedness of K,J
and the preceding two-sided bound give separately

    ||FR||, ||RF||, ||FR*||, ||R*F|| <= k M delta_N,
    ||F V14||, ||V14 F|| <= u M delta_N.               (8)

For example FR=(FE)KE and RF=EK(EF); the estimates for R* use K*.
Thus neither self-adjointness nor normality of K,R,J is presumed.

For any bounded A define D_N(A)=A-PAP. The exact identity

    D_N(A)=FA+PAF                                     (9)

includes the FAP, PAF and FAF blocks. It omits no endpoint/complement
mixed term. Using ||R||<=1 in(8) bounds both FA and AF by k M delta_N
for each A=R*R, RR* and R^2. For example F R*R=(FR*)R and
R*R F=R*(RF); F R^2=(FR)R and R^2 F=R(RF). The RR* case uses
(FR)R* and R(R*F). Hence

    ||D_N(R*R)||, ||D_N(RR*)||, ||D_N(R^2)||
                                      <=2 k M delta_N,
    ||D_N(V14)||                       <=2 u M delta_N,
    ||D_N(V14+R^2)||                   <=2(u+k)M delta_N. (10)

Every product in these formulas is the full bounded operator product
on H0. In particular the exact retained entries contain

    P R*R P=(PRP)*(PRP)+P R*F R P,
    P RR* P=(PRP)(PRP)*+P R F R* P,
    P R^2 P=(PRP)^2+P R F R P.                        (11)

The extra terms in(11), including the possibly non-Hermitian last
one, have not been dropped, replaced or charged a second time. They
remain in S3_N. Inequality(10) concerns only the difference from that
exact compression; it does not authorize a truncated-middle surrogate.

The difference S3-S3_N has diagonal entries -D_N(R*R), -D_N(RR*)
and off-diagonal entries -D_N(V14+R^2)*, -D_N(V14+R^2). The diagonal
block norm is the maximum of its two entry norms. The self-adjoint
off-diagonal block has norm ||D_N(V14+R^2)||, as follows by squaring
it (or directly from the operator norm definition). Applying the
triangle inequality and(10) proves

    ||S3-S3_N||<=2 k M delta_N+2(u+k)M delta_N
               =epsilon_N.

Since b,c,k,u are fixed, eta_N->1 and d_N->infinity, (1) gives
epsilon_N->0. This completes the proof of(2) for independent complex
endpoints on the entire Hilbert space, with no sign assumption on S3.

### 4. Size of the allowance and the unresolved finite comparison

For 512<=N<=exp(10^6), log(3)>1 gives 0<d_N<10^6. Since
c<10^-16, we have M>10^8. For any b>=0,

    (1+b/c)/(d_N+b)>=min(1/d_N,1/c)>10^-6.            (12)

This follows without a sign ambiguity by writing the left side as
the convex combination
(d_N/(d_N+b))(1/d_N)+(b/(d_N+b))(1/c).
Both endpoints exceed10^-6 in the stated range. Thus delta_N>10^-3,
as both branches in its minimum exceed10^-3. Since u+2k>30,
epsilon_N>2*10^8*30*10^-3=6*10^6, proving(3).

More generally, to make the displayed epsilon_N smaller than a
specified tolerance tau>0 with tau<2(u+2k)/c, its nontrivial branch
must satisfy the explicit threshold

    d_N+b > [4(u+2k)^2 eta_N^2/(c tau^2)] * (1+b/c).   (13)

This compares the bound obtained with the accuracy required. No value
of b or hidden onset is being used to claim feasible convergence.
A subsequent sign argument would need an independently certified
normalized finite margin gamma_N>0 and all norm/entry errors strictly
below min(1,gamma_N). Neither gamma_N nor finite entry enclosures are
proved here. Replacing E by a finite Galerkin inverse square root is
a separate unproved approximation problem. The free-coordinate finite
margins in C999l/q do not provide this normalized margin.

### 5. Separate conceptual audit — 12 November2026, step608

**Verdict and scope.** Inequalities(1)-(3), convergence in(2), and the
strict threshold(13) are upheld for every integer N>=512 and every
complex input. The audited object is exactly the stated compression
of C744z(4). The audit reuses the approved source assessment606/607
and the specified portions of C744v, C744z and C999k; it does not
replay c_*, the response identity, the two-cell certificate, or the
whole-neutral-core argument. No stronger scalar floor is substituted.

**Restricted form and spectral domains.** In the inherited setting,
H0 is a closed complex Hilbert subspace, V0 is dense in H0, and a0
is closed with lower bound c>0. These are the representation theorem's
hypotheses; the representing operator is A0 on H0. By its spectral
calculus, Dom(A0^1/2)=V0 and a0(f,f)=||A0^1/2 f||^2 there.
For the spectral measure mu_v of any v in H0, support is in [c,infinity)
and the two relevant integrals are

    ||Ev||^2 = integral lambda^-1 dmu_v <= c^-1||v||^2,
    ||A0^1/2 Ev||^2 = integral lambda*lambda^-1 dmu_v
                    = ||v||^2.

This verifies Ev in V0 and the form identity used in(5). It does not
assert finiteness of integral lambda dmu_v, which would be needed for
Ev in Dom(A0). The distinction is essential. No unrestricted inverse
or restriction of an unrestricted square root occurs.

Each h_n is finite: the digamma arguments have positive real part.
C744v(5) and pi>3 imply h_n>=d_n for all n>=512. Monotonicity of d_n
and its positive value at512 give h_n>=d_N>0 for all n>=N.
The remaining finite set is bounded below by -b. On V the diagonal
series has only finitely many possibly negative summands and converges
as a form series, as stipulated by the inherited diagonal form domain.
Thus it can be split at N without a conditional rearrangement. With
S>=0, the exact bookkeeping is

    a0(f,f)+b||f||^2
      >= sum_n (h_n+b)|f_n|^2
      >= (d_N+b) sum_(n>=N)|f_n|^2.

For f=Ev this proves(5). Although Q_N Ev need not be neutral, it is
used only in a coefficient norm, never as an input to the restricted
form or inverse. This removes a possible domain ambiguity in(4).

**Complex moment correction and projection.** C999k's exact moment
formula has C_+(e0),C_-(e0)>0 and C_+(e1)<0<C_-(e1), so its real
two-column determinant is strictly positive. It is also invertible
over C. Since r_n=O(n^-2), Cauchy--Schwarz gives absolute convergence
of each parity sum for every square-summable complex coefficient
sequence. Continuity of the moment map on H, followed by that
two-column invertibility, proves(6) for complex f, without imposing
any relation between even and odd coefficients.

The retained moment is -t0 C(e0)-t1 C(e1), so adding the two low
modes cancels it exactly. The error is Q_N f-t0 e0-t1 e1; its three
summands are orthogonal. On each parity apply Cauchy--Schwarz, then
sum the two inequalities using the maximum of the parity weights.
This gives the first line of(7), rather than an additional factor2.
The even numerator sqrt(2)ell^2/(4pi^2) is less than1, the odd one
is exactly a, and the integral from N-1 bounds the entire omitted
sum. Thus eta_N is valid for every N>=512. The two independent
moment constraints leave H_N of dimension N-2, and it is closed in
H0. Teschl's best-approximation theorem applies to g_N in this
subspace. Combining it with(5), the trivial bound M, and
((I-P_N)E)*=E(I-P_N) verifies both sides and both branches of(1)-(2).
No equality of these projections with a form-orthogonal projection,
or commutation with E, has been used.

**Full nonnormal block products.** Write F=I-P_N only in this paragraph;
it is not the raw projection complement Q_N. The four endpoint
factorizations are FR=(FE)KE, RF=EK(EF), FR*=(FE)K*E,
and R*F=EK*(EF). The corresponding factorizations with J give the
two V14 bounds in(8). All factors are bounded operators on H0.
For the three quadratic terms, the complete two-sided list is

    A=R*R:  FA=(FR*)R,   AF=R*(RF),
    A=RR*:  FA=(FR)R*,   AF=R(R*F),
    A=R^2:  FA=(FR)R,    AF=R(RF).

In every case ||R||=||R*||<=1 bounds both norms by k M delta_N.
The algebra A-PAP=FA+PAF is exact, including FAF. It yields(10)
by the triangle inequality, with no self-adjointness of R or J.
Inserting I=P+F between the two R factors verifies each equality
in(11). In particular PRFRP has no presumed sign and remains in
the retained off-diagonal entry. These are the exact full products,
not products of finite compressions.

Because P=P*, D_N(A*)=D_N(A)*. The error's diagonal block has norm
at most 2k M delta_N. Its self-adjoint off-diagonal block has norm
||D_N(V14+R^2)||, at most 2(u+k)M delta_N. Their sum is exactly
the allowance 2(u+2k)M delta_N. This verifies the coefficient of
epsilon_N with neither a missing mixed block nor a second charge
for the retained crossing products. With b,c fixed and finite,
d_N tending to infinity and eta_N tending to1 imply delta_N and
epsilon_N tend to zero. No positivity of S3 enters this argument.

**Allowance and threshold.** For N in(3), 2ell=log3>1 implies
d_N<log N<=10^6, strictly, while d_N>0. Also c<10^-16.
The two weights in(12) are nonnegative and sum to1, even when b=0.
Both endpoints 1/d_N and 1/c are strictly larger than10^-6;
therefore the nontrivial delta_N branch exceeds10^-3, as does M.
Since M>10^8 and u+2k>30, (3) follows strictly. This proves no
lower bound on ||S3-S3_N||.

For completeness put alpha=2M(u+2k). The constant branch of
epsilon_N is alpha M=2(u+2k)/c. For 0<tau<alpha M,
epsilon_N<tau is equivalent to

    alpha eta_N sqrt((1+b/c)/(d_N+b)) < tau.

Every factor is positive. Squaring and rearranging gives exactly(13),
so it is both necessary and sufficient for this displayed allowance
in the stated tolerance range. It is not necessary for the true
error to be below tau. A separate finite-entry perturbation would
have to be added to the cutoff error before comparison with
min(1,gamma_N); none is paid by this audit.

**Research consequence.** This establishes the conditional cutoff
input as audited, with unchanged hypotheses, constants and direct
inputs. It is local verification of a standard-method specialization;
no progress beyond the sources checked is claimed. The finite-margin
stops537/598/600/603 remain intact and concern different sufficient
certificates. C999l/q's free-coordinate margins still do not furnish
gamma_N on the exact P_N subspace of this theorem. A different choice
of endpoint projection would need a new comparison and its own tail
control; neither this error bound nor those finite margins transfer
automatically. The main actual-Xi positivity gap remains unresolved.

## Mathlib

A full matching theorem for this neutral cutoff remainder has not
been checked. Parseval, Hilbert orthogonal projection, bounded operator
norms and positive-form spectral calculus are supporting mathematics;
their availability would not supply the local constants or S3 positivity.
No assertion of absence from Mathlib or mathematical novelty is made.
