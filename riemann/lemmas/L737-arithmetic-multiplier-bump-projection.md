# Lemma 737: vanishing bump projection onto short arithmetic multipliers

## Hypotheses

Use precisely L637's actual Hardy function Z, fixed nonnegative
w in C_c^infinity((0,1)) with integral 1, fixed u0 with w(u0)>0,
and fixed nonzero smooth bump psi supported on [-1/2,1/2]. In
particular psi is the function specified there, not a variable test
function. Set

    L=log T, T<=X<=2T, a=X+u0*T,
    w_XT(t)=w((t-X)/T),
    g(t)=psi(L(t-a))/||psi(L(.-a))||_T,
    <f,h>_T=integral_R w_XT(t) f(t) conjugate(h(t)) dt,
    N=floor(T^(1/10)),
    V=span_C{Z(t)n^(-it):1<=n<=N}.

Pi denotes orthogonal projection onto this finite-dimensional subspace
of the complex Hilbert space L2(w_XT dt). Coefficients are arbitrary
complex numbers and may depend on T,X. All onsets below are existential
and uniform in X. No RH, nonvanishing at a, zero simplicity, Gram
invertibility or diagonal dominance is assumed.

The arithmetic input is S. Bettin, V. Chandee and M. Radziwill,
*The mean square of the product of the Riemann zeta-function with
Dirichlet polynomials*, J. reine angew. Math. 729 (2017), 51–79,
DOI [10.1515/crelle-2014-0133](https://doi.org/10.1515/crelle-2014-0133),
[arXiv:1411.7764v1, Theorem 1, pp. 1–2](https://arxiv.org/pdf/1411.7764v1).
In the source notation, for smooth phi supported in [1,2],
A(s)=sum_(n<=Y^theta) a_n n^(-s), a_n <<_epsilon n^epsilon,
and theta<17/33, it states

    integral |zeta(1/2+it) A(1/2+it)|^2 phi(t/Y) dt
      = sum_(m,n) a_m conjugate(a_n)/lcm(m,n)
          * integral [log(t*gcd(m,n)^2/(2*pi*m*n))+2*gamma]
                          phi(t/Y) dt
        + O_(epsilon,phi)(Y^(3/20+epsilon)(Y^theta)^(33/20)
                           +Y^(1/3+epsilon)).                 (1)

Only theta=1/8 and normalized |a_n|<=1 are used. Uniformity for
our compact smooth-weight family uses the inspected proof operations
in Section 3.1 p. 9, Section 3.2 Cases 1–3 pp. 12–15 and Section
3.3 pp. 15–16: weight truncation/integration by parts and Mellin
separation depend on bounded smooth seminorms on a fixed compact
support. This is a named theorem import, not a reproof of its
arithmetic estimates. Section 1 below checks the window and coefficient
specialization; in particular its error is charged quadratically.

Also use the classical real-axis Riemann–Siegel formula in L637,
Titchmarsh–Heath-Brown, *The Theory of the Riemann Zeta-Function*,
2nd ed. (1986), Section 4.17, (4.17.4), p. 89; see also
[DLMF 25.10.1–3](https://dlmf.nist.gov/25.10#E3). Its
undifferentiated O(t^(-1/4)) remainder includes cutoff crossings.
The exact real-axis identity Z(t)^2=|zeta(1/2+it)|^2 is part of
the Hardy normalization. Neither a derivative moment nor a shifted
moment theorem is used.

The prior SPECIALIZE assessment is
drafts/literature/2026-11-04-dirichlet-multiplier-bump-projection-scope.md.
The elementary finite divisor estimates below are written out because
the checked spectral theorems do not supply this full logarithmic form;
they do not reprove (1). L639 is a comparison, not a mathematical input.

## Conclusion

For all sufficiently large T, uniformly for T<=X<=2T,

    ||Pi g||_T^2 <= C_w N^3/(sqrt(T) L^2)
                 <= C_w T^(-1/5)/(log T)^2 = o(1).             (2)

Constants may also depend on the fixed Hardy normalization; the onset
may depend on u0,psi. The squared distance of g from V is therefore
1-o(1), uniformly in X. More specifically, every complex vector c
satisfies, with U_c(t)=Z(t) sum_(n<=N) c_n n^(-it),

    ||U_c||_T^2 >= (T L/(4N^2)) sum_(n<=N)|c_n|^2.            (3)

This excludes this dictionary at this length as a realization of the
specified microscopic unit bump. It does not exclude longer arithmetic
polynomials, different dictionaries or observers. Signed |W|-weighted
transfer, local signed margins and actual-Xi all-degree mixed positivity
remain open. There is no RH candidate.

This is a local specialization of known moments with a finite arithmetic
estimate. The prior search did not supply this projection conclusion;
no originality beyond the checked sources is claimed. Written on
4 November 2026, step 260; the separate conceptual audit in step 261
below validates the stated specialization under its named imports.

## Proof

### 1. Uniform smooth windows and the charged moment error

Put x=X/T in [1,2]. Choose fixed nonnegative smooth rho_j, j=1,2,3,
whose sum is 1 on a neighborhood of [1,3], with respective supports
compactly contained in (alpha_j,2 alpha_j), where

    alpha_1=3/4, alpha_2=5/4, alpha_3=2.

Such a partition exists since these three open intervals cover [1,3].
Only a neighborhood of that compact interval needs the partition
property; extend all functions smoothly with compact support. For
Y_j=alpha_j*T define

    phi_(j,x)(v)=rho_j(alpha_j*v) w(alpha_j*v-x).

Their supports are fixed compact subsets of (1,2), and every smooth
seminorm is bounded uniformly in x in [1,2]. We have exactly

    w_XT(t)=sum_j phi_(j,x)(t/Y_j).

For all sufficiently large T, N<=Y_j^(1/8) for every j. Pad the
coefficients with zeros up to the source cutoff Y_j^(1/8). This
uses a fixed source exponent, not a T-dependent theta. The bound
in (1) at each scale is

    O_epsilon(T^(57/160+epsilon)),

because 3/20+(1/8)(33/20)=57/160>1/3. All constants are
uniform in x by the common seminorm bounds and the source proof
operations specified above.

For c nonzero set B=max_(n<=N) sqrt(n)|c_n|. In (1) use
a_n=sqrt(n)c_n/B for n<=N, and zero otherwise. Thus |a_n|<=1
with coefficient-bound constant 1. Restore the factor B^2 and
sum the three window formulas. Since B^2<=N||c||_2^2, this gives

    ||U_c||_T^2 = integral w_XT(t) F_(A_t)(c) dt + E(c),
    |E(c)| <= C_(epsilon,w) N T^(57/160+epsilon)||c||_2^2,    (4)

where gamma is Euler's constant and

    A_t=log(t/(2*pi))+2*gamma,
    F_A(c)=sum_(m,n<=N) c_m conjugate(c_n) gcd(m,n)/sqrt(m*n)
                         *[A+2 log gcd(m,n)-log m-log n].     (5)

The zero vector satisfies (4) separately. No unnormalized source
coefficient bound or entrywise-to-operator error inference was used.
All gcd correlations, logarithmic terms and the constant 2*gamma
have been retained.

### 2. Exact divisor factorization of the logarithmic form

Write phi(d) for Euler's totient, mu for the Möbius function and
Lambda(p^k)=log p (k>=1), Lambda(r)=0 otherwise. Define finite sums

    b_n=c_n/sqrt(n),
    B_d=sum_(k<=N/d) b_(dk),
    C_d=sum_(k<=N/d) b_(dk) log k,
    Q=sum_(d<=N) phi(d)|B_d|^2,
    kappa(d)=sum_(p|d) log p/(p-1), with kappa(1)=0.

For real z near 1 put J_z(d)=d^z product_(p|d)(1-p^(-z)).
Expanding the finite product gives
J_z(d)=sum_(r|d) mu(r)(d/r)^z. Hence
sum_(d|q)J_z(d)=q^z by sum_(r|m)mu(r)=1 if m=1 and 0
otherwise. Differentiating this finite identity at z=1 gives

    gcd(m,n)=sum_(d|m,d|n) phi(d),
    gcd(m,n) log gcd(m,n)
       =sum_(d|m,d|n) phi(d)[log d+kappa(d)].

The formula for the derivative follows directly by logarithmically
differentiating the finite product J_z(d), which is positive near 1.
Substitution in (5), using log m=log d+log(m/d), yields exactly

    F_A(c)=sum_(d<=N) phi(d)
       [(A+2*kappa(d))|B_d|^2-2 Re(C_d conjugate(B_d))].        (6)

This is a real Hermitian form for every complex c. In particular, the
two logarithms log m and log n have not been bounded entrywise in a
form with possibly complex coefficients.

### 3. A finite relative bound for the logarithmic cross term

Prime factorization gives log k=sum_(r|k)Lambda(r). Reordering finite
sums therefore gives

    C_d=sum_(2<=r<=N/d) Lambda(r) B_(dr).                      (7)

We prove ||C||_phi<=2 log N ||B||_phi for N>=2, where the squared
norm is sum phi(d)|.|^2. On Euclidean coordinates y_d=sqrt(phi(d))B_d,
the map in (7) has nonnegative matrix entries

    K_(d,n)=Lambda(n/d) sqrt(phi(d)/phi(n)) if d|n, n>d,
    K_(d,n)=0 otherwise.

Take h_d=1/sqrt(phi(d)). The weighted column sums are

    sum_d K_(d,n) h_d/h_n =sum_(r|n)Lambda(r)=log n<=log N.   (8)

The finite Euler product gives phi(dr)>=phi(d)phi(r): the ratio
is the product of p/(p-1) over primes dividing both d and r.
For a prime power r, phi(r)>=r/2. Thus the weighted row sums obey

    sum_n K_(d,n) h_n/h_d
       <=sum_(r<=N/d) Lambda(r)/phi(r)
       <=2 sum_(r<=N) Lambda(r)/r <=4 log N.                 (9)

For completeness the last inequality needs no prime asymptotic.
The exact identity

    log(N!)=sum_(r<=N) Lambda(r) floor(N/r)

follows by summing the divisor formula for log k. Since
floor(N/r)>=N/(2r) for 1<=r<=N and log(N!)<=N log N,
the sum of Lambda(r)/r is at most 2 log N.

Here is the finite Schur argument to preserve the complex norm and
constants. If a nonnegative matrix K has weighted row bound R and
weighted column bound S with positive weights h, Cauchy–Schwarz gives

    |(Ky)_d|^2
      <= (sum_n K_(d,n)h_n)(sum_n K_(d,n)|y_n|^2/h_n)
      <= R h_d sum_n K_(d,n)|y_n|^2/h_n.

Summing in d and using the column bound gives ||Ky||_2^2<=RS||y||_2^2.
With (8)–(9), ||K||<=2 log N. Cauchy–Schwarz in the phi norm now
gives |sum phi(d)C_d conjugate(B_d)|<=2 log N Q.
Because kappa(d)>=0, (6) implies

    F_A(c)>=(A-4 log N)Q.                                   (10)

### 4. Recover arbitrary coefficients and absorb the error

Finite Möbius inversion gives b_n=sum_(k<=N/n)mu(k)B_(nk).
Indeed, after substituting B, the coefficient of b_(nr) is
sum_(k|r)mu(k), equal to 1 for r=1 and zero otherwise.
Using |mu(k)|<=1 and Cauchy–Schwarz gives

    ||c||_2^2=sum_n n|b_n|^2
       <=sum_n n floor(N/n) sum_(k<=N/n)|B_(nk)|^2
       <=N sum_(m<=N) tau(m)|B_m|^2
       <=N^2 sum_(m<=N)|B_m|^2 <=N^2 Q,                     (11)

where tau(m)<=m<=N and phi(m)>=1. This deliberately crude bound
suffices; no uniform positive spectral bound at the endpoint is claimed.

On the support of w_XT, t is in [T,3T], so A_t>=L-C for an
absolute C. Since log N<=L/10, (10) yields, after one onset,

    F_(A_t)(c)>=(3L/5-C)Q >=(L/2)Q.

The integral of w_XT is T. Equations (4), (10) and (11) therefore give

    ||U_c||_T^2
      >= [T L/(2N^2)-C_(epsilon,w) N T^(57/160+epsilon)]
                                                    ||c||_2^2.

The ratio of the error to T L||c||_2^2/N^2 is at most

    C_(epsilon,w) N^3 T^(-103/160+epsilon)/L
      <=C_(epsilon,w) T^(-11/32+epsilon)/L.                  (12)

Fix, for example, epsilon=1/160. This tends to zero; it is eventually
at most 1/4. This proves (3), uniformly for all c and X. It also
proves independence of the generators for sufficiently large T,
rather than assuming independence to form an inverse Gram matrix.

### 5. Local bump numerator and projection

The Riemann–Siegel formula and the elementary bound
sum_(n<=M)n^(-1/2)<=2 sqrt(M) give

    sup_(T<=t<=3T)|Z(t)|<=C T^(1/4).                         (13)

No differentiation, subconvexity, zero exclusion or uniform-strip
assertion is needed. For large T the bump support
I=[a-1/(2L),a+1/(2L)] lies in [T,3T], and its norm denominator
is nonzero since w(u0)>0. Because ||g||_T=1, Cauchy–Schwarz on I
gives

    integral w_XT |g| <= (integral_I w_XT)^(1/2)
                      <=sqrt(||w||_infinity/L).

For every real t, |sum c_n n^(-it)|<=sqrt(N)||c||_2. Hence (13) gives

    |<g,U_c>_T|^2 <= C_w N T^(1/2)||c||_2^2/L.             (14)

For a finite-dimensional subspace, orthogonal projection and
Cauchy–Schwarz imply
||Pi g||_T^2=sup_(0!=U in V)|<g,U>_T|^2/||U||_T^2.
If Pi g=0 both sides vanish; otherwise equality is attained by U=Pi g.
Combining (3) and (14) proves (2), including the supremum over arbitrary
T,X-dependent complex coefficients. Finally ||g-Pi g||_T^2=1-||Pi g||_T^2
by orthogonality. All arguments are finite or use the explicitly
imported uniform moment estimate; no infinite coefficient limit or
unpaid microscopic-window moment interchange occurs.

### Separate conceptual audit — 4 November 2026, step 261

The unchanged approved target was the full uniform projection statement,
not just the finite matrix or a fixed coefficient vector. L637's exact
Hardy normalization, weight, bump and undifferentiated Riemann–Siegel
input were checked. The prior SPECIALIZE assessment was reused. BCR
v1 Theorem 1 and the weight/coefficient operations in Section 3.2
Cases 2–3, printed pp. 14–15, and Section 3.3 p. 16 were reopened to
check the existing import. Its deeper arithmetic estimates remain named
inputs; this is not independent certification of the source manuscript.

**Window and coefficient uniformity.** The interval overlaps are
(5/4,3/2) and (2,5/2), so the three open source windows really cover
the full compact set [1,3], including its endpoints. A fixed smooth
partition subordinate to them exists. Each phi_(j,x) has one common
compact support inside (1,2); differentiating its explicit formula in v
uses only derivatives of fixed rho_j,w and fixed powers of alpha_j.
Consequently every required derivative bound is independent of x.
This alone is a property of this family, not a claim that pointwise
big-O constants are automatically uniform on arbitrary compact families.

The inspected source integrations by parts use finitely many of these
derivatives for fixed epsilon and chosen error decay. Its Mellin
separation uses equally uniform bounds: with v=exp(y), the Mellin
transform on any fixed vertical line is the Fourier transform of
exp(sigma*y) phi_(j,x)(exp(y)), supported in a fixed compact y interval.
Repeated integration by parts gives C_m(1+|tau|)^(-m) there, with C_m
uniform in x,j; all boundary terms vanish. Thus the weight factors in
the source's separated estimates are uniformly bounded. The coefficient
bounds in those estimates use the common size bound on a_n, not the
positions or phases of their nonzero entries. For the normalized vector
that bound is 1. Zero padding to the fixed exponent 1/8 preserves it.
This justifies the uniform specialization of the cited theorem, without
assuming microscopic support for its weight.

Restoring B^2 multiplies both the entire main form and the remainder.
The exact coefficient factor is
sqrt(m*n)/lcm(m,n)=gcd(m,n)/sqrt(m*n), so (5) has the correct
orientation c_m conjugate(c_n). Since B^2<=N sum |c_n|^2,
the error in (4) holds for every vector, even if it varies with T,X.
An error for fixed vectors alone would not establish the claim.

**Full logarithmic form.** Differentiating J_z(d) contributes
log d+sum_(p|d)log p/(p-1), with the plus sign shown in (6).
The log d terms cancel against the two coefficient logarithms; the
uncancelled terms are exactly C_d conjugate(B_d) and its conjugate.
The identity C_d=sum_r Lambda(r)B_(dr) follows by taking the coefficient
of each b_(dk): it is sum_(r|k)Lambda(r)=log k. These are finite
identities for arbitrary complex coefficients.

For the Schur calculation, the weighted column entry is Lambda(n/d),
whereas the row entry is Lambda(r)phi(d)/phi(dr). The totient inequality
therefore goes in the required direction. The factorial identity gives
sum_(r<=N)Lambda(r)/r<=2 log N; combining it with phi(p^k)>=p^k/2
gives row bound 4 log N and column bound log N. Hence the norm bound
is sqrt(4 log^2 N)=2 log N, and the factor 2 in (6) gives exactly
4 log N in (10), not 2 log N. No sign of an individual complex
cross product has been presumed. Finite Möbius inversion counts B_m
once for each divisor n of m in (11); this explains tau(m) and confirms
the claimed N^2 loss. Both crude estimates suffice at the fixed length.

**Absorption and the supremum.** The pointwise main form has margin
A_t-4 log N>=3L/5-C on the support; multiplying by w_XT>=0 and
integrating gives T times this margin. The padded source exponent is
57/160, and after multiplying by N and dividing by T L/N^2 the
error exponent is 3/10+57/160-1=-11/32. For epsilon=1/160 it is
-27/80; thus one X- and coefficient-independent onset makes the error
at most one quarter of T L||c||_2^2/N^2. This leaves (3).

Riemann–Siegel supplies only the real-axis bound (13), for which cutoff
crossings are allowed and no derivative is taken. Since u0 is strictly
inside (0,1), the bump interval lies in [T,3T] at one uniform onset.
Continuity and w(u0)>0 make its norm positive. Its unit normalization
and interval length 1/L give the displayed weighted L1 estimate; no
lower bound on Z or upper bound on the bump's pointwise height is used.
The numerator bound is C_w N T^(1/2)||c||_2^2/L. Dividing by (3)
leaves C_w N^3/(sqrt(T)L^2), hence the exponent -1/5.

Every U in V has such a finite coefficient vector. The lower bound
proves that a nonzero vector gives nonzero U for sufficiently large T;
it does not rely on a presumed inverse Gram matrix. The Hilbert-space
variational formula therefore takes the supremum over all such vectors,
including those depending on T,X. Orthogonality gives the squared
distance exactly as stated. The quotients are zero-safe at individual
zeros of Z, and there is no infinite-dimensional closure or coefficient
limit to justify.

Audit result: no bound, hypothesis or mathematical dependency required
correction. The fixed dictionary fails to realize this unit bump at
any fixed error below 1 for all sufficiently large T. This verifies
the existing local exclusion; it is not a second mathematical discovery
or evidence against RH. The named source proofs, effective constants,
longer dictionaries, signed weighted transfer and mixed positivity have
not been supplied by this audit.

## Mathlib

Full matching Mathlib coverage for (1), its uniform weight specialization,
and this Hardy arithmetic-multiplier projection result has not been
checked and is unknown. No claim of absence is made. Supporting objects
are finite Möbius inversion, Cauchy–Schwarz and orthogonal projection;
no specific Mathlib theorem was checked or invoked. The analytic inputs
are the named BCR theorem and Riemann–Siegel formula with direct links
and exact scopes above. The finite divisor and norm arguments are
included in full here.
