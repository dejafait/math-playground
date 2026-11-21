# Lemma 992: zero fixed-cutoff logarithmic volume rate of the exact filter

## Hypotheses

Use exactly L990's oriented coefficients, including both polynomial
constant subtractions:

    K_m(u)=[L_(m-1)^(2)(u)-1]/(m-1),
    a_n=(K_n(n),K_(n+1)(n),K_(n+2)(n)),
    b_n=(K_n(2n),K_(n+1)(2n),K_(n+2)(2n)),
    c_n=(a_n cross b_n)/||a_n cross b_n||_1.

Fix N beyond C990a's cofinite-definition onset. In particular
||c_n||_1=1 for every n>=N. Use L990's audited additive normalized
row estimate away from leading collisions and its integer phase-orbit
equidistribution. No individual coefficient is assumed nonzero. No
rate of equidistribution, bound on shrinking-target visits, uniform
integrability of logarithms, solution growth, or arithmetic identity
is assumed.

For 0<delta<1 define the bounded function

    f_delta(z)=log(max(delta,|z_0|))-log(max(delta,|z_2|)).

Here and throughout, logarithms are natural. Define the exact operator
(Tx)_n=c_(n,0)*x_n+c_(n,1)*x_(n+1)+c_(n,2)*x_(n+2).

## Conclusion

For every fixed delta in (0,1), the exact, all-index average satisfies

    lim_(M->infinity) (1/(M-N+1))*sum_(n=N)^M f_delta(c_n)=0.       (1)

This includes indices with a zero individual coefficient. It does
not assert convergence of the uncut logarithmic ratio or a limit
uniform as delta tends to zero. The uncut leading-phase logarithmic
ratio has torus integral zero, but this integral is not asserted to
equal the uncut exact-index average.

If x,y are any two exact homogeneous solutions on a common finite or
infinite interval, their discrete determinant

    W_n=x_n*y_(n+1)-x_(n+1)*y_n

satisfies the division-free identity

    c_(n,2)*W_(n+1)=c_(n,0)*W_n.                                (2)

Thus a proposed positive lower-volume certificate obtained solely
from the fixed-cutoff phase average has rate zero, below its required
strictly positive rate. This stops that certificate. It does not
stop solution-specific matrix-product methods, construct a null
sequence of finite positive exponential growth, or decide whether
x in E and Tx in S implies x in S. It supplies no bound for actual
B_n, L984(H), or RH.

Step272, 10 November 2026: NEGATIVE for this bounded volume test,
under the prior EXPLORE assessment review267. POTENTIALLY_NEW only
records that the checked sources did not cover the exact statement;
it is not certified originality. Step274 independently audited the
stated bounded limit, uncut qualifications and singular-row algebra
under the separately approved SPECIALIZE review272; these claims pass.
The audit below clarifies the tail onset and logarithms of a solution
pair's determinant. No stronger result or numerical calculation is used.

## Proof

### Reused source contracts

The audited L990 input gives, with

    phi_n=n*(sqrt(3)/2+pi/3)-13*pi/12,
    psi_n=n*(1+pi/2)-pi,
    C=cos(phi), D=cos(phi+pi/3), E=cos(psi), T=sin(psi),
    h(phi,psi)=(-D*E+(D-C)*T, D*E, -C*T-D*E),
    g(phi,psi)=h(phi,psi)/||h(phi,psi)||_1 when h!=0,

the estimate

    ||c_n-g(phi_n,psi_n)||_1<=C_eta/n                           (3)

for every fixed eta>0, all sufficiently large n with ||h||_1>=eta,
and some finite C_eta. The phases are equidistributed on the
two-dimensional torus modulo 2*pi; L990 proves the stronger statement
on each residue class modulo12. Every fixed rectangle therefore has
its normalized area as limiting visit frequency. C990a ensures that
the exact c_n used also exist at all the remaining sufficiently large
indices, including those near collisions. No normalization estimate
at such collisions is imported.

The bulk source behind (3) is A. Gil, J. Segura and N. M. Temme,
*Asymptotic approximations to the nodes and weights of Gauss-Hermite
and Gauss-Laguerre quadratures*, arXiv1709.09656v1, 27 September2017,
[section3.3, equations81-87](https://arxiv.org/html/1709.09656v1#S3.SS3),
with fixed alpha=2 and compact scaled arguments [1/9,1/2]. The
orbit input is the already checked specialization in L990 of the Weyl
criterion and linear-sequence result in T. Tao, *Higher Order Fourier
Analysis*, 5 June2012 manuscript, Proposition1.1.2, Exercise1.1.5 and
Proposition1.1.5,
[printed pp5-7](https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-142-tao7-higher-book-05june2012.pdf#page=13).
For open sets with boundary of measure zero, the precise visit-frequency
formulation is Exercise1.1.1, printed p4 of the same manuscript,
[PDF page12](https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-142-tao7-higher-book-05june2012.pdf#page=12),
already inspected in review272's separate coverage approval.
Their hypotheses and the exact nonresonance calculation are retained
in L990. These general source results are not reproved here. The
additional work is the reflection, bounded exact-index passage and
singular-row accounting for this operator.

### Reflection and the leading fixed-cutoff mean

Write the torus with normalized area measure mu, and let

    R(phi,psi)=(-phi-2*pi/3,-psi) modulo 2*pi.

This is a measure-preserving involution. The trigonometric identity
cos(phi+2*pi/3)=D-C gives, after applying R,

    C'=D-C, D'=D, E'=E, T'=-T.

Substitution in h proves exactly

    h(R(phi,psi))=(h_2(phi,psi),h_1(phi,psi),h_0(phi,psi)).       (4)

Its l1 norm is unchanged. The leading collision set Z={h=0} consists
of the four torus points D=T=0: if E!=0, h_1=0 implies D=0,
then C!=0 and h_2=0 implies T=0; if E=0, T is nonzero and
h_0=h_2=0 would force C=D=0, which is impossible. Conversely
D=T=0 makes all three entries vanish. Set g=0 at Z. Equation(4)
then holds for g everywhere, and

    f_delta(g(R(phi,psi)))=-f_delta(g(phi,psi)).                (5)

For fixed delta this function is bounded in absolute value by
L_delta=log(1/delta), and continuous outside the finite set Z.
It is Riemann integrable, and (5) gives

    integral f_delta(g) dmu=0.                               (6)

Rectangle equidistribution applies to this bounded Riemann-integrable
function: finite lower and upper rectangular sums bound its averages
and converge to the same integral. Thus the average of
f_delta(g(phi_n,psi_n)) tends to zero. Assigning values at Z causes
no problem; its finite set has measure zero, and its neighborhoods
can have arbitrarily small limiting visit frequency.

### Passage to the exact coefficients with every index retained

Fix delta. The function t -> log(max(delta,|t|)) is 1/delta
Lipschitz on [-1,1]. Choose a finite union U of small open torus
rectangles containing Z, with boundary of measure zero. Its area
may be arbitrarily small. On the compact complement of U,

    eta_U=min ||h||_1>0.

By (3), at all sufficiently large indices outside U,

    |f_delta(c_n)-f_delta(g(phi_n,psi_n))|
                      <= C_(eta_U)/(delta*n).                (7)

The sum of this bound divided by M-N+1 tends to zero. At every
index inside U both terms are bounded by L_delta, including when
an exact coefficient or the entire leading h vanishes. The difference
there is at most 2*L_delta. Equidistribution gives the visit frequency
mu(U). Finitely many indices before (7)'s onset also contribute zero
in the limit. Consequently

    limsup_M |average_(N<=n<=M)(f_delta(c_n)-f_delta(g_n))|
                                     <=2*L_delta*mu(U).       (8)

For this fixed delta, first take the limit in M for each fixed U,
then choose U of arbitrarily small area. The right side tends to
zero. Combining with (6) proves (1). No index was deleted from the
average, and delta was not allowed to depend on M or U's onset.

### What the uncut leading integral does and does not give

For fixed phi the functions h_0 and h_2 of psi are single sine/cosine
combinations, with amplitudes

    R_0(phi)=sqrt(D^2+(D-C)^2),
    R_2(phi)=sqrt(D^2+C^2).

Each lies between 1/sqrt(2) and sqrt(3/2), since its two cosines
have phase difference pi/3. Hence integral |log|h_j|| dmu is finite
for j=0,2: after a translation in psi, its integrand is bounded by
a uniform constant plus |log|cos(psi)||. The latter is integrable
at its zeros because |cos(psi)| is comparable to distance from the
zero, and integral_0^epsilon |log t| dt is finite. Fubini applies
to the nonnegative absolute-value integrand. Equation(4) therefore
also proves

    integral (log|h_0|-log|h_2|) dmu=0,                       (9)

with arbitrary values assigned on the zero sets, which have measure
zero. The normalization in g cancels in this ratio wherever defined.
Equation(9) is a torus integral only. Equidistribution for bounded
tests and (3) do not identify the exact-index average of this
unbounded function.

In particular, if both outer exact coefficients are nonzero on a
chosen tail, increase N to that tail's onset for (10)-(11), if needed;
the bounded limit (1) is unchanged by this finite deletion. Define

    r_delta(t)=max(0,log(delta/|t|)), t!=0.

There is the exact identity on that tail

    log|c_(n,0)/c_(n,2)|
       =f_delta(c_n)-r_delta(c_(n,0))+r_delta(c_(n,2)).        (10)

The sufficient missing tail estimate for passing from (1) to a zero
uncut mean is

    lim_(delta down to0) limsup_(M->infinity)
       average_(N<=n<=M)(r_delta(c_(n,0))+r_delta(c_(n,2)))=0. (11)

Neither (11) nor eventual nonvanishing of the individual outer
coefficients has been proved. If there is a zero coefficient, its
uncut logarithm cannot be used in (10); the polynomial identity (2)
below remains the applicable statement. Even (11), if established,
would give zero determinant rate, not the positive rate sought by
this volume certificate or a bound on growth in individual directions.

### Exact block volumes and singular rows

Multiply the homogeneous row for x by y_(n+1), the row for y by
x_(n+1), and subtract. The middle terms cancel, giving
c_(n,0)*W_n-c_(n,2)*W_(n+1)=0. This proves (2) without division.
At a row with c_(n,2)=0 and c_(n,0)!=0 it forces W_n=0. At a
row with c_(n,0)=0 and c_(n,2)!=0 it forces W_(n+1)=0. If both
outer coefficients vanish, normalization forces c_(n,1)!=0,
so both solutions have their middle coordinate zero and both W's
are zero. These constraints do not by themselves show that any
prescribed initial vector extends through that row.

On an interval on which every c_(n,2)!=0 the companion matrices
are exactly

    A_n=[[0,1],[-c_(n,0)/c_(n,2),-c_(n,1)/c_(n,2)]],
    det(A_n)=c_(n,0)/c_(n,2).

For a finite block n=N,...,M, write P=A_M*...*A_N. Then

    det(P)=product_(n=N)^M c_(n,0)/c_(n,2),
    W_(M+1)=W_N*product_(n=N)^M c_(n,0)/c_(n,2).

The second equality also holds for W_N=0 and needs no division by
W_N. The logarithm of |det(P)| additionally requires every
c_(n,0)!=0. Writing it as log|W_(M+1)|-log|W_N| also requires
W_N!=0; under these hypotheses every W in the block is nonzero.
The function
f_delta(c_n) is only a cutoff of this logarithm; it is not the
logarithm of an exact propagated volume. Therefore (1) stops the
proposed positive fixed-cutoff mean test, not the exact product.
A determinant of unit exponential rate can coexist with exponential
expansion in one direction and contraction in another. No stability
claim follows from a zero volume rate, even if the uncut limit were
subsequently proved to be zero.

The required infinite feasibility and upper growth bound for the
fixed anchor of working271 remain unproved, as does its positive
exponential limsup. Nothing here extends that finite certificate.
Nonzero subexponential forcing and arbitrary initial data would also
be required for a proof of the original positive stability implication.

### Independent conceptual audit — step274, 10 November 2026

Reused the prior SPECIALIZE assessment review272, L990's audited
formulas(5)-(7) and residue-class orbit argument, and C990a's audited
cofinite-definition contract. The latter is used only to retain every
exact normalized row, not as a conditioning or individual-pivot bound.
L991 and working271 supply motivation and stops, not premises.

The two outer entries after reflection are explicitly
-D*E-C*T and -D*E+(D-C)*T; the middle entry is D*E. Thus there
is no orientation sign omitted in (4). At D=0, C is nonzero,
so the E!=0 and E=0 cases in the collision proof exhaust all phases
and leave exactly two choices each for phi and psi. Defining g=0
on these four points preserves the reflection identity and boundedness.
R is an involution with area-preserving linear part -I.

For fixed delta, the two-coordinate Lipschitz bound is at most
(|c_0-g_0|+|c_2-g_2|)/delta, hence at most ||c-g||_1/delta;
no extra unbounded factor is lost in (7). Off a fixed U, its Cesaro
sum is O_delta,U(log(M)/M). Inside U it is at most 2*L_delta
times the visit fraction. The boundary-null visit theorem applies
to the finite rectangle union (overlaps can be partitioned); all
boundary indices are in the compact complement or have zero limiting
frequency. Continuous-away-from-Z bounded tests are Riemann integrable.
The finitely many residue classes in L990 together give the same
all-integer normalized torus measure. Thus the three operations are
legitimate in their stated order: fix delta and U, let M tend to
infinity, then shrink U. Neither delta nor U is chosen as a function
of the running index. The exact rows at leading collisions are covered
by boundedness, not by (3).

For the uncut qualification, R_2^2=1+cos(2*phi+pi/3)/2 and
R_0^2=1+cos(2*phi+pi)/2. These verify both uniform amplitude
bounds and the absolute-integrability argument. Reflection is therefore
valid for the uncut torus integral. In (10), log|t| equals
log(max(delta,|t|))-r_delta(t) for every nonzero t, which verifies
both tail signs. For each fixed delta, (1) bounds the limsup absolute
uncut average by the limsup average of the two nonnegative tails.
Condition (11) would make this bound zero; neither the condition nor
the necessary nonzero tail has been supplied. No assertion is made
about an uncut average containing an exact zero coefficient.

The subtraction proving (2) is valid for every row whose three
coordinates belong to the common solution interval. It yields exactly
c_0*W_n-c_2*W_(n+1). Each one-zero-outer case forces only the stated
Wronskian to vanish. With both outer entries zero, c_1!=0 forces
x_(n+1)=y_(n+1)=0, hence both W's vanish. None of these cases
licenses forward continuation of arbitrary data. The displayed block
formulas retain W_N=0; their logarithmic form has the additional
nonzero hypotheses now made explicit above.

The bounded-average claim and scoped stop pass. This is validation
of the existing specialization, not a new theorem beyond the sources
checked. Fixed-cutoff mean zero is not an exact propagated volume,
and even an independently justified zero determinant rate would not
bound an individual direction's growth. The original inverse question,
working271's infinite feasibility and all arithmetic obligations remain
unresolved. No new DAG input or RH argument is introduced.

## Mathlib

Full matching coverage for this exact operator and its fixed-cutoff
average has not been checked. The audited local asymptotic and orbit
inputs have the primary citations above. Finite determinant algebra,
Riemann integrability and measure-preserving changes of variables are
supporting mathematics, not an identified full matching Mathlib
theorem. No absence or formalization claim is made.
