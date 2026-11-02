# Lemma 644: simultaneous dimension and small full vertical Pick trace

## Hypotheses

Use the actual Xi and multiplicity-preserving zero correspondence of
L018. All logarithms are natural. For sufficiently large real T put

    N=floor(log T), a=3/2, u_j=j/N-1/2 (0<=j<N),
    Q_N(z)=product_(j<N)(z-u_j+ia),
    H_N={P/Q_N: deg P<N}, ||h||^2=integral_R |h(x)|^2 dx/(2pi).

Use L641's fixed concentration space E_N: the spectral subspace of
P_N 1_[-1,1] P_N restricted to H_N for eigenvalues >=1-N^(-1/2).
Here P_N is the boundary orthogonal projection onto H_N. For every
X in [T,2T] put c_X=X+1/2 and ell_X=log(X/(2pi)). Define

    M_T(X)=#{zeta: |Re(zeta)-c_X|<=1},
    U_X={h in E_N: h(zeta-c_X)=0 for all these zero occurrences},
    r_X=dim U_X,
    tau_X=sum_(zeta: |Re(zeta)-c_X|>1)
                    k_U(zeta-c_X,conjugate(zeta)-c_X).

Every zero is an actual Xi zero. Counts and sums retain all orders,
both ordinate signs and both horizontal displacements. The constraints
are values, including repeated rows, not derivative constraints. The
finite kernel k_U uses the inherited norm. Import L642's absolutely
convergent mixed trace and uniform entire tail, and L643's audited
fixed-E_N mean. The relevant L641/L642 proofs are checked for this
application below; L641's unrelated countervectors are not inputs.

Standard tools, already covered by the invocation-start assessment:

* Markov's inequality on a probability space for a nonnegative
  measurable integrable variable and a positive threshold: MIT,
  *6.436J/15.085J Fundamentals of Probability*, Fall 2018,
  [Lecture 17, Section 1, p.1](https://ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/f44fa78f05ac31a4ba2bd82f599dcf60_MIT6_436JF18_lec17.pdf),
  including its indicator proof. No independence is required.
* Finite closed-subspace reproducing kernels, orthogonal projection
  and Cauchy--Schwarz: S. Lototsky,
  [*Reproducing Kernel Hilbert Space*, p.1, theorem, (1.2),
  Corollaries (3)--(4)](https://dornsife.usc.edu/sergey-lototsky/wp-content/uploads/sites/211/2023/06/RepKernHilbSp.pdf).
  Only finite-dimensional closed subspaces are used.

The count source remains Bellotti--Wong, arXiv:2412.15470v2,
[Theorem 1.1](https://arxiv.org/pdf/2412.15470v2), with L467's
closed-endpoint specialization. The density input remains Baluyot,
*On the Zeros of Riemann's Zeta-function* (2017),
[Theorem 1.2.1, p.16](https://urresearch.rochester.edu/fileDownloadForInstitutionalItem.action?itemFileId=183460&itemId=33320),
fixed theta=11/20<4/7, as used in L643. Their manuscripts remain
imported; no new source theorem or independent manuscript audit is
claimed. No RH, simplicity, spacing, positive paired measure, spectral
sign or effective onset is assumed.

## Conclusion

Define the fixed positive constants

    a_0=1/pi,
    q_0=(arctan(1/3)+pi/4)/pi,
    kappa=q_0-a_0>0,
    b_0=(q_0+a_0)/2,
    c_*=kappa/4, delta_*=kappa/(4b_0).

For every sufficiently large T there is a measurable set S_T inside
[T,2T], of Lebesgue measure at least (delta_*/2)T, such that every
X in S_T satisfies

    r_X>=c_* N,
    |tau_X|<=N^(2-1/160)+C_tail N^(3/2),                     (1)
    |tau_X|/(ell_X r_X)
       <=(2/c_*)[N^(-1/160)+C_tail N^(-1/2)] -> 0.           (2)

C_tail is independent of T, X and the constraint rank; the convergence
is uniform for X in S_T. The onset includes the existential onset and
constant in L643's density input. This is a local standard-tool
specialization (REPRODUCTION), not a claim of progress beyond the
checked literature. It supplies the simultaneous-height prerequisite
for the conditional Rayleigh diagnostic stated in L642. It proves no
eigenvalue sign, eigenvalue near zero in absolute value, assertion at
every large height, or RH conclusion. The assembly passed the scoped
critical audit below on 1 November 2026; the imported source manuscripts
are not independently certified.

## Proof

### Verification of the finite-space and count inputs being used

In L641's verified finite basis formula, the boundary diagonal is
sum_(j<N) 3/((x-u_j)^2+9/4). Its integral over [-1,1], divided by
2pi, is >=q_0 N. The boundary kernel is bounded by
min(2N/a,2/|x-y|). The exact projection identity for tr(A_N-A_N^2)
then gives the two endpoint integrals of this squared envelope.
For eta=a/N, either endpoint integral before division by (2pi)^2
is 6+4 log(2/eta): integrate 4b-b^2 v for 0<=v<eta and 4/v
for eta<=v<=2, where b=2N/a. Thus L641 (10)--(11) give

    d_N=dim E_N>=q_0 N-sqrt(N)V_N,
    V_N=[3+2 log(2N/a)]/pi^2=O(log N).                     (3)

For clarity, the spectral step uses lambda<=sqrt(N)lambda(1-lambda)
only below the threshold 1-N^(-1/2); each eigenvalue at or above
that threshold contributes at most one to tr A_N. Equality belongs
to E_N. The basis and integration in L641 justify the norm constants;
no asymptotic spectral distribution is imported. Finally
arctan(1/3)>26/81 and pi/4>3/4 imply q_0>1/pi, so all displayed
selection constants are strictly positive.

The local window in zeta coordinates is [X-1/2,X+3/2]. Each zero
occurrence belongs to it for a set of X of length at most two.
With L467's cumulative count input and its left-limit endpoint
convention, L641 (12) therefore gives

    integral_T^(2T) M_T(X) dX
      <=2 #{rho: T-1/2<=Im(rho)<=2T+3/2}
      <=2[V(2T+3/2)-V(T-1/2)+E(2T+3/2)+E(T-1/2)],

where V(H)=H log(H/(2pi e))/(2pi) and
E(H)=0.10076 log H+0.24460 log log H+8.08344. Both endpoints
are above e for large T. Passing the lower endpoint to its left
limit includes any zero at that endpoint; the source's continuous
envelopes justify this passage without a generic-height assumption.
Since V'(H)=log(H/(2pi))/(2pi), its difference is
(T/(2pi))log T+O(T). The E terms are O(log T). Consequently

    (1/T) integral_T^(2T) M_T(X) dX<=a_0 N+C_count           (4)

for one fixed C_count>=0 and every sufficiently large T, using
0<=log T-N<1. This verifies the average itself, not just the
existence of L641's one count-favorable height.

### The count-admissible set has fixed positive measure

Use normalized Lebesgue measure mu_T on [T,2T]. M_T is a finite
sum of indicators of closed intervals, restricted to this interval:
only zeros in the compact ordinate range [T-1/2,2T+3/2] occur.
The strip bound and entire-function compact finiteness from L018
give finitely many occurrences. Hence M_T is nonnegative, measurable
and integrable, as required by Markov.

Let A_T={X: M_T(X)<=b_0 N}. Markov and (4) show

    mu_T(A_T)>=1-(a_0+C_count/N)/b_0
             >=kappa/(4b_0)=delta_*                       (5)

once C_count/N<=kappa/4; here b_0-a_0=kappa/2. Strict and
nonstrict versions cause no loss: apply Markov to the complement
{M_T>b_0 N}, which is contained in {M_T>=b_0 N}.

There are at most M_T(X) scalar evaluation constraints. Rank-nullity
gives r_X>=d_N-M_T(X), with no independence requirement on those
rows. Thus, for X in A_T, (3) implies

    r_X>=(kappa/2)N-sqrt(N)V_N>=c_*N                       (6)

once V_N/sqrt(N)<=kappa/4. Boundary zero occurrences remain in
the local set, and conjugate zeta values have the same real part.
All their mixed local terms therefore vanish on U_X. Multiple zeros
can only make this upper bound on codimension more conservative.

### A small fixed-space annulus at the same heights

Use exactly L643's fixed kernel and nonnegative majorant

    F_N(x,y)=sqrt(k_E(x+iy,x+iy) k_E(x-iy,x-iy)),
    Z_T(X)=sum_(zeta: 1<|Re(zeta)-c_X|<sqrt(N))
                      F_N(Re(zeta)-c_X,Im(zeta)).

For fixed T the union of these annuli meets only finitely many zero
occurrences, since their real parts lie in
[T+1/2-sqrt(N),2T+1/2+sqrt(N)] and |Im zeta|<1/2. Kernel
evaluations are finite and continuous in this closed strip, away from
the poles at height -3/2. Thus Z_T is a finite sum of nonnegative
bounded continuous functions times interval indicators. It is
measurable and integrable. This justification requires no regularity
of the changing projection onto U_X.

The audited L643 estimate is, for a fixed constant C_ann,

    integral Z_T dmu_T=W_T<=C_ann N^(2-1/80).

Set B_T={X: Z_T(X)<=N^(2-1/160)}. Markov gives

    mu_T([T,2T]\B_T)<=C_ann N^(-1/160).                    (7)

For all sufficiently large T this is at most delta_*/2. Therefore
S_T=A_T intersect B_T is measurable and

    mu_T(S_T)>=mu_T(A_T)-mu_T([T,2T]\B_T)>=delta_*/2.       (8)

No independence or unique selected height has been asserted. All
finitely many interval endpoints may be retained; (5)--(8) and the
pointwise estimates use their stated strict/closed conventions.

### Projection domination and the complete tail

For any fixed X, U_X is a closed subspace of the finite-dimensional
E_N. Extend an orthonormal basis of U_X to one of E_N. The basis
formula for the kernel and Cauchy--Schwarz imply, for every permitted
z and v,

    |k_U(z,v)|<=sqrt(k_U(z,z)k_U(v,v))
               <=sqrt(k_E(z,z)k_E(v,v)).                    (9)

This is a mixed-kernel bound, with no extra factor r_X. Taking
z=x+iy, v=x-iy makes the right side F_N(x,y), including y=0
and both signs of y. There is no need to assume conjugation
invariance of U_X or a bound on an inverse constraint matrix.

We checked L642's full proof for the imported trace and tail.
Its Pi=I-D^dagger D is the orthogonal projection onto ker D by
the Penrose identities, even with repeated or dependent rows.
The basis identity f(z)Pi f(v)^* yields exactly k_U; the local
zero terms vanish, and conjugate occurrences make the total real.
The uniform envelope in its (3) bounds the trace kernel itself.
For s=|Re(zeta)-c_X|>=R>=max(2,sqrt(N)) it is at most
12 e^6 N/s^2. L467 with even symmetry gives the closed-shell
bound A_0 log(|v|+3), where A_0=36+M_0/log 2 and M_0 is the
finite number of zero occurrences with Re(zeta)=0. The two
ordinate directions are included. For m=floor R>=R/2 the tail
is at most

    24 e^6 A_0 N sum_(k>=m) log(c_X+k+4)/k^2
      <=144 e^6 A_0 N [log(c_X+R+4)+1]/R.                  (10)

The summation uses log(c_X+k+4)<=log(c_X+m+4)+log(k/m),
sum k^(-2)<=2/m and sum log(k/m)/k^2<=3/m, as proved in
L642. If the first shell includes extra points with s<R, only
its count is enlarged; the pointwise bound is applied to retained
points s>=R. Thus there is no uncovered noninteger shell or hidden
dependence on X, rank, basis or a fixed N. The bound also applies
to each unit-vector paired sum, justifying the finite trace exchange
with the infinite zero sum. These are verification of L642's needed
premises, not a new full-manuscript audit of its cited sources.

Take R=sqrt(N), which is >=2 here. Uniformly for T<=X<=2T,
log(c_X+sqrt(N)+4)+1=O(N), since log T<N+1. Equation (10)
therefore gives a fixed C_tail with the entire distant absolute
sum <=C_tail N^(3/2). The equality boundary s=sqrt(N) belongs
to this tail; s=1 belongs to the annihilated local part. From
absolute convergence, (9), and X in B_T,

    |tau_X|<=Z_T(X)+C_tail N^(3/2)
            <=N^(2-1/160)+C_tail N^(3/2).

Finally ell_X>=N-log(2pi)>=N/2 for sufficiently large N,
uniformly on [T,2T]. Combine this with (6) to obtain (1)--(2).
This proves the simultaneous conclusion with the entire mixed sum,
without discarding any zero order, displacement or distant tail.

The surviving limitations are mathematical: the selected set need not
include every height, the trace has no asserted sign, and a small
signed trace alone gives no small absolute eigenvalue. L641's
boundary-only countermodel and L642's failed deterministic annulus
envelope remain valid for their stated tests. The extra input used
here is L643's actual-zero density mean and its fixed-space majorant.

### Critical audit — 1 November 2026

Verdict: the stated simultaneous conclusion survives the exact approved
audit, with constants and exponent unchanged. This verifies a local
standard-tool specialization, not a new estimate beyond the checked
sources or a source-manuscript audit. The assessment saved before this
invocation is `drafts/literature/2026-11-01-l644-simultaneous-selection-audit.md`.
The relevant L641 proofs and the entire L642 proof were checked;
L643's previously audited mean is reused, not independently reproved.

For the finite-space normalization, the displayed e_j have norm one
under dx/(2pi): their boundary products have modulus one and
integral 2a/((x-u_j)^2+a^2) dx=2pi. If j>k, cancellation in
e_j conjugate(e_k) leaves only lower-half-plane poles and O(x^(-2))
decay, proving orthogonality by an upper contour. They form a basis
of the N-dimensional rational space. Telescoping gives precisely the
kernel in L641 (7), including the 2N/a boundary envelope. The diagonal
integral is minimized at |u|=1/2, giving q_0 N. For either endpoint,
integrating 4b-b^2 v over [0,eta], with b eta=2, gives 6;
integrating 4/v over [eta,2] adds 4 log(2/eta). Both endpoints,
divided by (2pi)^2, give exactly V_N. Since A_N is a positive
contraction, its eigenvalues below 1-N^(-1/2) contribute at most
sqrt(N) tr(A_N-A_N^2); all others contribute at most d_N.
This proves (3), including the equality convention at the threshold.
The rational inequalities 26/81+3/4=347/324>1 prove kappa>0.

For the count mean, L018's map sends beta+i gamma to
gamma+i(1/2-beta) injectively and preserves each order. The local
closed window is exactly [X-1/2,X+3/2]. Each occurrence is counted
for at most two units of X, so Tonelli for the finite counting sum
gives the factor two in (4)'s preceding display. Subtracting the
lower continuous count envelope at the left limit includes lower
endpoint zeros. Expanding V at H=alpha T+O(1), for alpha=1,2,
gives V(H)=alpha T log T/(2pi)+O(T); the errors E are O(log T).
The resulting mean is log T/pi+O(1)=N/pi+O(1), with a constant
independent of T. The local positive-ordinate window contains every
possible zero in that window; negative ordinates are not silently
removed from the exterior sum.

In particular Markov applies to an actual nonnegative finite measurable
count, rather than a choice of favorable height. Its bound on A_T is
(b_0-a_0-C_count/N)/b_0. Since b_0-a_0=kappa/2, the stated onset
C_count/N<=kappa/4 leaves exactly delta_*. Rank-nullity then gives
r_X>=(kappa/2)N-sqrt(N)V_N>=c_*N under the stated second onset.
Repeated rows can reduce rank; no Hermite interpolation, simplicity
or independent-row hypothesis is hidden in this codimension bound.

For the other selection event, only finitely many zeros meet the
union of moving annuli. Its evaluations stay away from every pole,
so the nonnegative bounded summands times interval indicators are
measurable. The exact exponent difference in Markov's inequality is

    159/80-(2-1/160)=318/160-319/160=-1/160.

Thus the bad-annulus measure tends to zero while the good-count
measure is at least delta_*. Once C_ann N^(-1/160)<=delta_*/2,
the intersection has measure at least delta_* T/2. There is no
independence assumption and no measurable selection of an eigenbasis,
evaluation inverse or variable-rank projection. The set S_T is defined
by the count and fixed-E_N majorant alone.

For each fixed X, orthonormal-basis extension inside E_N proves
k_U(z,z)<=k_E(z,z), and Cauchy--Schwarz proves (9) for arbitrary
two complex evaluations. Setting v=conjugate(z) gives exactly F_N;
there is no replacement by H_N in the annulus bound and no dimension
factor. In L642 the Penrose identities give D Pi=0, Pi*=Pi and
Pi^2=Pi, while Pi alpha=alpha whenever D alpha=0. Thus (6) there
is the correct kernel even with dependent or empty rows. Conjugating
a mixed summand exchanges the two conjugate zero occurrences.
The all-order exterior sum is therefore real after absolute convergence,
without asserting positivity or invariance of U_X under conjugation.

The zero-pair identification also retains the sign and normalization:
subtract the compensated logarithmic-derivative expansions at s_j and
r=1-conjugate(s_k), and divide by s_j-r. Reflection turns F(r)
into -conjugate(F(s_k)); the subtraction contributes a minus sign
which is canceled by r-rho=-(conjugate(s_k)-(1-rho)). This is
exactly L641 (6), with no separated divergent compensator. Its
second denominator is conjugate(s_k-(1-conjugate(rho))), so the
reflected zero becomes conjugate(zeta), as used in the mixed form.
The boundary integral of its rational functions gives C_jk with
denominator 2a+i(j-k)/N. Thus the full Gram, not its diagonal,
is the inherited norm. The grid's distinct poles give a bijective
(antilinear in v) correspondence with H_N. This check does not use
L640's arithmetic reduction or its unaudited norm estimates.

The tail check must be uniform in the growing N. In L642 (8),
upper evaluations have product factors of modulus <=1, while the
lower evaluations have squared factors <=q(b,|y|). Their geometric
mean gives (3) with coefficient 3N, not 3N r_X. Since
log q<=6|y|/(b^2+(a-|y|)^2), its exponential is at most
exp(3N/(2(b^2+1))). For s>=R>=max(2,sqrt(N)), b=s-1/2>=s/2,
so this is bounded by e^6 and the denominator gives 12 e^6 N/s^2.
The closed-shell count (9) of L642 follows from L467 on positive
ordinates, reflection on negative ordinates, and at most M_0
occurrences at zero. A shell crossing zero uses two subsets of
the positive [0,1] shell. The constant A_0 stated there covers
all three cases; M_0 is finite by compact finiteness and L018.

For k>=m=floor R, both intervals at distance k from c_X have
total count <=2 A_0 log(c_X+k+4). Apply the s>=R pointwise bound
only to retained zeros; enlarging their counts in the first shell
does not apply that bound to an inadmissible point. Equations
(11)--(12) of L642 then give

    48 e^6 A_0 N [2 log(c_X+R+4)+3]/R
       <=144 e^6 A_0 N [log(c_X+R+4)+1]/R.

Here sum k^(-2)<=2/m and sum log(k/m)/k^2<=3/m follow from
the stated first-term/integral bounds and log t<=sqrt(t).
All summands are nonnegative absolute values. This covers the full
infinite tail in both directions, proves absolute convergence for
the kernel and each unit-vector form, and permits finite trace/zero-sum
interchange. It contains no rank, X-dependent basis or fixed-N constant.
With R=sqrt(N), c_X<=2T+1/2 and log T<N+1 make the bound O(N^(3/2))
uniformly. Equality at s=sqrt(N) belongs to this tail; s=1 belongs
to the annihilated local set. No endpoints or multiplicities are lost.

Finally ell_X>=N-log(2pi)>=N/2 beyond a fixed onset. Together with
r_X>=c_*N, division of the annulus threshold and complete-tail bound
by ell_X r_X yields exactly (2). All finitely many onset requirements
can be satisfied simultaneously, including the existential density
onset; none is asserted effective. No error requiring repair was found.

The audit establishes only this prerequisite. In particular cancellation
in a small signed trace does not control absolute eigenvalues or their
signs. Applying the conditional average-Rayleigh diagnostic to a norm
reserve requires its precise separate finite-Hermitian specialization;
no such new conclusion is included here. L641's boundary-transfer
countervectors and L642's failed deterministic annulus envelope remain
valid in their original scopes. The direct mathematical inputs are
still L018, L467, L641, L642 and L643; the DAG needs no new edge.

## Mathlib

Full matching coverage is not checked; unknown availability is not
absence. Markov's inequality, finite-dimensional orthogonal projection,
rank-nullity, Cauchy--Schwarz and finite spectral theory are supporting
results, not a claimed formalization of the assembled actual-Xi
statement. No Mathlib search was needed for this application of the
already assessed tools. [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
