# Corollary C032f: a bounded-operator reduction of the normalized branch diagnostic

## Hypotheses

Use exactly the full theta kernel, omega=1/4, z=i, scalar c, and
complex compact smooth class of C032e (1)-(2). In particular
Psi(t)=K(t/2)/2, c=Xi(3i/4)/Xi(5i/4), and the same input is used
in both sigma components. Set

\[
 H=L^2((0,\infty),ds;\mathbb C),\qquad
 Y=L^2((0,\infty),du;\mathbb C^2),\qquad
 D=C_c^\infty((0,\infty);\mathbb C).
\]

Both measures are unweighted Lebesgue measure. For sigma=-1,+1 and
t>=0 define

\[
 a_\sigma(t)=(1+t)e^{\sigma t/8}\Psi(t),\qquad
 b_\sigma(t)=\big((1-c)-(1+c)t\big)e^{\sigma t/8}\Psi(t).
 \tag{1}
\]

The nominated diagnostic is

\[
 \delta=\inf_{f\in D,\ \|\mathbf G_+f\|_Y=1}
 \|\mathbf G_-f-c\mathbf G_+f\|_Y.
 \tag{2}
\]

## Conclusion

The integral formulas

\[
 (Ah)_\sigma(u)=\int_0^\infty a_\sigma(s+u)h(s)\,ds,
 \qquad
 (Bh)_\sigma(u)=\int_0^\infty b_\sigma(s+u)h(s)\,ds
 \tag{3}
\]

define bounded operators H->Y. Multiplication f=Psi h is a bijection
of D onto D, and on that class Ah=G_+f and Bh=G_-f-cG_+f. Moreover

\[
 \delta=\inf_{h\in H,\ \|Ah\|_Y=1}\|Bh\|_Y,
 \tag{4}
\]

and

\[
 \delta>0
 \quad\Longleftrightarrow\quad
 \operatorname{ran}A^*\subseteq\operatorname{ran}B^*
 \quad\Longleftrightarrow\quad
 \exists d>0:\ B^*B\geq d^2A^*A.
 \tag{5}
\]

The ranges in (5) are actual ranges in H, without closure. This is
a specialization of the cited Douglas theorem, not an assertion
that the inclusion holds. Neither delta=0 nor delta>0 is established
here. The full source norm, a completed transport, and actual-Xi
positivity remain unidentified. The independent conceptual audit1282
below accepts (1)-(5) only. The separate conceptual audit1291 accepts
the exact transform equivalence (12)-(20); neither audit decides delta,
and (21)-(25) remain outside their scope. This is not an RH candidate.

## Proof

### Scope, sources, and why the reduction is necessary

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-17-normalized-approximate-branch-compatibility-review-1270.md`,
completed1271. Its covered target includes output domains, an auxiliary
bounded-operator reduction, compact-core transfer, and the fixed
zero-versus-positive threshold. C032e supplies the full-theta bounds
and the separately audited exact compact obstruction. The latter
does not imply (5).

Import R. G. Douglas, *On majorization, factorization, and range
inclusion of operators on Hilbert space*, Proc. Amer. Math. Soc.
**17** (1966), 413-415, Theorem 1 and proof pp.413-414,
[primary scan](https://home.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf),
[DOI](https://doi.org/10.1090/S0002-9939-1966-0203464-1), as inspected
in the prior assessment. For bounded operators S,T on a Hilbert
space it equates ran S contained in ran T with SS*<=lambda^2 TT*
for some finite lambda>=0, and with a bounded factorization S=TC.
No closed-range hypothesis is imposed. The theorem is not reproved.
The work below verifies the particular bounded realizations and core;
it is necessary because division by Psi is not an asserted bounded
change of norm on any completed source space.

### Output domains and the common compact core

C032e (8) gives, for t>=0,

\[
 0<\Psi(t)\leq C\exp(9t/4-\pi e^t).
 \tag{6}
\]

The same corollary gives smoothness and a finite c. Thus for a finite
C_1, both kernels in (1), uniformly in sigma, have absolute value at
most C_1(1+t)exp(19t/8-pi e^t). Consequently

\[
 \sum_\sigma\int_0^\infty\!\int_0^\infty
 \big(|a_\sigma(s+u)|^2+|b_\sigma(s+u)|^2\big)\,ds\,du
 =\sum_\sigma\int_0^\infty t
 \big(|a_\sigma(t)|^2+|b_\sigma(t)|^2\big)\,dt<\infty.
 \tag{7}
\]

Tonelli and t=s+u give the equality, since the slice 0<s<t has
length t. For finiteness it suffices to integrate a constant times
t(1+t)^2 exp(19t/4-2pi e^t). It is bounded near zero; with x=e^t
its tail is an integral of
(log x)(1+log x)^2 x^(15/4) exp(-2pi x), which is finite.

For every u>=0 the kernels in (3) are square integrable in s by
the same bound without the factor t. Cauchy-Schwarz defines the
integrals for h in H and, after integration in u, proves

\[
 \|Ah\|_Y^2\leq
 \left(\sum_\sigma\int_0^\infty t|a_\sigma(t)|^2dt\right)\|h\|_H^2,
 \quad
 \|Bh\|_Y^2\leq
 \left(\sum_\sigma\int_0^\infty t|b_\sigma(t)|^2dt\right)\|h\|_H^2.
 \tag{8}
\]

These are bounded-operator statements, sufficient for the argument;
no conclusion about relative output norms follows from them alone.

On each compact subinterval of (0,infinity), Psi and 1/Psi are
smooth and bounded. Hence h=f/Psi and f=Psi h preserve D, its
support, and complex values, and are inverse maps on D. Substitution
in C032e (2) proves the two identities following (3), without changing
the output measure or treating the two components independently.
In particular every original compact input has the required Y outputs.

Use the standard density theorem for smooth compactly supported
functions in L2 of an open subset of R, applied to (0,infinity)
and to real and imaginary parts. Thus D is dense in H. By (8),
h_n->h in H implies both Ah_n->Ah and Bh_n->Bh in Y. This is
simultaneous approximation by a single input sequence.

A is nonzero: for a nonzero nonnegative smooth compact h,
a_sigma(t)>0 and (Ah)_sigma(u)>0 for every u>=0. Therefore the
normalization sets in (2) and (4) are nonempty and the infima are
finite nonnegative real numbers. For any h in H with ||Ah||=1,
choose h_n in D converging to h. For all sufficiently large n,
q_n=||Ah_n|| is nonzero and tends to 1. Then

\[
 f_n=\Psi h_n/q_n\in D,\qquad
 \|\mathbf G_+f_n\|_Y=1,\qquad
 \|\mathbf G_-f_n-c\mathbf G_+f_n\|_Y
 =\|Bh_n\|_Y/q_n\longrightarrow\|Bh\|_Y.
 \tag{9}
\]

The infimum on D is at least the one on H; (9) gives the reverse
inequality. This proves (4). It would also transfer any subsequently
proved auxiliary zero-defect sequence to the original compact class
by choosing sufficiently accurate approximants separately at each
index. No such auxiliary sequence is supplied here. The input norms
may diverge; none is part of the original normalization.

### Exact specialization of the operator-range theorem

For d>0, homogeneity and (4) show that delta>=d is equivalent to
||Bh||>=d||Ah|| for all h in H. If Ah=0 this inequality is
automatic; otherwise divide h by ||Ah||. Squaring gives exactly
B*B>=d^2 A*A as a quadratic-form inequality on H.

To apply the quoted same-space version of Douglas without an
unmentioned rectangular extension, work on Z=H direct-sum Y and
define bounded maps

\[
 S(h,y)=(A^*y,0),\qquad T(h,y)=(B^*y,0).
\]

Their ranges are ran A* direct-sum {0} and ran B* direct-sum {0},
and SS* and TT* have respective upper-left blocks A*A and B*B,
all other blocks zero. Douglas therefore says that the inclusion in
(5) is equivalent to A*A<=lambda^2 B*B for finite lambda>=0.
Since A is nonzero, any such lambda is positive, and d=1/lambda
gives the last condition in (5). Conversely that condition permits
lambda=1/d. This proves (5) with every operator on a stated domain.
In particular, showing only closure inclusion or absence of a compact
null vector cannot replace the missing exact inclusion.

### Independent conceptual audit — 17 November 2026, step1282

Under the unchanged, separately approved SPECIALIZE assessment
`drafts/literature/2026-11-17-bounded-branch-reduction-audit-review-1280.md`,
this audit accepts (1)-(5). It verifies the existing specialization,
not a new operator theorem or a determination of delta. Douglas
Theorem 1 and proof pp.413-414 are imported with the precise citation
above; the primary comparison recorded in review1270 is reused.
No closed-range hypothesis or theta-specific estimate is imported.

**Full-kernel domain check.** C032e supplies positivity, smoothness,
the finite scalar c and (6). Its positive-axis bound is precisely the
L019 bound with the substitution t/2, supported by L016's uniformly
convergent differentiated series. Even continuation to negative t is
not needed for (1)-(5). The finite coefficient estimate

\[
 |(1-c)-(1+c)t|\leq (|1-c|+|1+c|)(1+t)
 \quad(t\geq0)
\]

works for complex c as well. Thus the same absolute majorant covers
both signs and both kernels. Tonelli applies to their nonnegative
squared absolute values before any finiteness assertion. The change
(s,u) to (s,t=s+u) has Jacobian one and range 0<s<t, so its slice
weight is t, exactly as in (7). Near t=0 the majorant is integrable;
on the tail x=e^t gives x^(19/4)/x=x^(15/4) and an exponentially
decaying factor exp(-2pi x), with only the stated logarithmic factors.
This proves (7), not merely an unweighted one-variable kernel bound.

For each u>=0 the corresponding one-variable squared kernel tail
is also integrable. Cauchy-Schwarz therefore gives an absolutely
convergent defining integral for each h in H; integration of the
pointwise estimate in u gives (8). Measurability follows from the
measurable kernels and these absolutely convergent integrals. The
operators are complex linear and bounded H->Y; the squared Y norm
is the sum of the squared component norms. No inequality between
A and B is obtained here.

**Common core and normalization check.** For nonzero f in D, Psi
has a positive minimum on supp(f), and both Psi and its reciprocal
are smooth there. The zero input maps to itself.
Multiplication and division consequently preserve the single compact
input, so the identities following (3) hold for the same h in both
components. These statements do not assert a bounded inverse on H.
The standard density of C_c^infinity in L2 of an open set applies
to this complex D by approximating real and imaginary parts.
Boundedness gives simultaneous convergence in the two Y outputs.

For a nonzero nonnegative h in D, the strictly positive kernels
a_sigma make every (Ah)_sigma(u)>0. Hence ||Ah||>0 and the
normalized sets are nonempty. Boundedness makes the defect of such
a normalized bump finite, so delta is finite and nonnegative.
Let delta_H be the right side of (4). The bijection on D gives
delta>=delta_H. Conversely fix any h in H with ||Ah||=1, choose
h_n in D tending to h, and put q_n=||Ah_n||. For large n, q_n>0
and q_n->1. In addition to (9), the full vector estimate is

\[
 \left\|\frac{Bh_n}{q_n}-Bh\right\|_Y
 \leq \frac{\|Bh_n-Bh\|_Y}{q_n}
       +|q_n^{-1}-1|\,\|Bh\|_Y\longrightarrow0.
\]

The identical estimate with A proves normalized plus-output
convergence. Thus delta<=||Bh|| for every normalized h, and taking
the infimum gives delta<=delta_H. No minimizer, uniform support,
uniform reciprocal bound or bounded input norms are required.
This proves (4) with arbitrary complex cancellation retained.

**Form and actual-range check.** For d>0, (4) implies
delta>=d exactly when ||Bh||>=d||Ah|| for every h in H.
If Ah!=0 this follows by normalizing h; if Ah=0 the inequality
is simply ||Bh||>=0 and imposes no extra condition. Conversely
the global inequality applies to every normalized h. Squaring,
using the complex Hilbert adjoints, yields B*B>=d^2 A*A.
Since delta is finite, delta>0 is equivalent to existence of such d.

On Z=H direct-sum Y the adjoints of the displayed S and T are
S*(h,y)=(0,Ah) and T*(h,y)=(0,Bh). Hence SS* and TT* are
diag(A*A,0) and diag(B*B,0). The ranges of S and T themselves,
not their closures, are ran(A*) direct-sum {0} and ran(B*) direct-sum {0}.
All maps are bounded on this same complex Hilbert space. Douglas
therefore applies exactly as stated and produces a finite lambda
in A*A<=lambda^2 B*B. Lambda=0 would force ||Ah||^2=0 for
every h, contradicting the positive bump; thus d=1/lambda>0.
The converse uses lambda=1/d. The direction and positivity of the
constant in (5) are correct; no surjectivity or closed range is used.

**Verdict and limits.** No defective implication or required repair
was found in (1)-(5). This establishes the correctness of the existing
auxiliary reduction with its stated hypotheses. It does not infer a
relative bound from positive kernels, compactness, compact exact
injectivity or closure inclusion. Equations (10)-(25), the value of
delta, actual-range membership, the completed source metric and any
transfer to actual-Xi signs remain outside this audit. The existing
direct mathematical inputs are unchanged; no new lemma is introduced.

### The remaining comparison and the failed pointwise shortcut

L020, positivity of K(v)=2Psi(2v), and the integrable tails give

\[
 0<\Xi(3i/4)=\int_0^\infty K(v)\cosh(3v/4)\,dv
 <\int_0^\infty K(v)\cosh(5v/4)\,dv=\Xi(5i/4).
 \tag{10}
\]

Strictness holds on every interval of positive v. Hence 0<c<1 and
t_0=(1-c)/(1+c) lies in (0,1). At t=t_0 both b_sigma vanish,
while both a_sigma are strictly positive. Thus even the pointwise
kernel ratio has no positive lower bound. This is only the failure
of that shortcut: integration with arbitrary complex h can cancel,
and the pointwise fact neither proves nor refutes (5).

For clarity the exact unpaid form is explicit. Set
p(t)=1+t and q(t)=(1-c)-(1+c)t. For any proposed d>0,
B*B-d^2A*A has real symmetric integral kernel

\[
 R_d(s,t)=2\int_0^\infty
 \cosh\!\left(\frac{2u+s+t}{8}\right)
 \Psi(u+s)\Psi(u+t)
 \big[q(u+s)q(u+t)-d^2p(u+s)p(u+t)\big]du.
 \tag{11}
\]

This follows by composing the kernels in (3) and summing sigma;
the cross-integrals converge by (7) and Cauchy-Schwarz. For compact
h, all compositions and the associated triple integrals are
absolutely integrable, since its s,t support is compact and (6)
controls the u tail. Thus its quadratic form is
integral integral conjugate(h(s))R_d(s,t)h(t) ds dt. Boundedness
then extends the form to H. Establishing nonnegativity of that form
for every complex h, or proving the exact range inclusion fails,
is still required. No entrywise sign check, finite fit, compactness
argument, or invocation of Douglas alone supplies it.

The bounded attempt1272 stops with this comparison unpaid. It has
resolved the auxiliary domain/core issue, but has not met the
zero-versus-positive discriminator. It uses known Hilbert-space
machinery with explicit theta applicability; no progress beyond the
checked literature or independent mathematical originality is claimed.

### Adjoint witness test — 17 November 2026, step1273

This is a second bounded attempt under the unchanged ready review1270,
not an audit of the preceding reduction. Test

\[
 g=A^*(0,e^{-u})\in H
 \quad\hbox{for membership in }\operatorname{ran}B^*.
 \tag{12}
\]

The following calculation gives an exact transform criterion for this
one membership and shows that its positive-real pointwise norm test
does not exclude membership. Neither membership nor nonmembership is
proved. In particular no conclusion about delta follows. This section
uses C032e's full-theta continuation and the Fourier uniqueness theorem
already inspected there; it imports no new transform-class theorem.

Write alpha=1-c, beta=1+c, a=1/8 and t0=alpha/beta. By (10),
beta>0 and 0<t0<1. Extend the kernels a_sigma,b_sigma in (1)
to the strip T={z: |Im z|<pi/2} using Psi_ext from C032e.
For y=(y_-,y_+) in Y define on that strip

\[
 J_y(z)=\sum_{\sigma=-1,+1}\int_0^\infty
 b_\sigma(z+u)y_\sigma(u)\,du,
 \qquad
 j(z)=\int_0^\infty a_+(z+u)e^{-u}\,du.
 \tag{13}
\]

These are holomorphic even when y has no compact support. Here are
the required noncompact-input bounds. C032e (6), after rescaling, is

\[
 \Psi_{\rm ext}(z)=\sum_{n\geq1}
 (4\pi^2n^4e^{9z/4}-6\pi n^2e^{5z/4})e^{-\pi n^2e^z}.
 \tag{14}
\]

For a compact Q in T, Re(e^z) has a positive minimum d on Q.
At z+u with z in Q and u>=0 the exponential in the nth term
has modulus at most exp(-pi*d*n^2*e^u). Splitting this exponential
into two equal factors bounds one by exp(-pi*d*e^u/2) and makes
the sum of the other times any fixed power of n uniformly finite.
The remaining exponentials in (14) and its first derivative are
bounded by C_Q exp(M_Q*u). Including the affine and exponential
factors in a_sigma,b_sigma gives, for each kernel k and k',

\[
 \sup_{z\in Q}|k(z+u)|+\sup_{z\in Q}|k'(z+u)|
 \leq C_Q(1+u)e^{M_Q u-\kappa_Qe^u},\qquad \kappa_Q>0.
 \tag{15}
\]

The right side belongs to L2(0,infinity). Apply this bound on a
slightly larger compact neighborhood when taking difference quotients.
Cauchy-Schwarz against each y_sigma gives an integrable majorant
and justifies differentiation in (13). On positive real s, the
real-valued kernels in (1) identify J_y(s)=B*y(s) and j(s)=g(s).
Indeed the absolute double integral for the adjoint pairing against
any h in H is at most
||b_sigma(s+u)||_L2(ds du) ||h||_H ||y_sigma||_2, by
Cauchy-Schwarz on the product space; (7) makes it finite. Fubini
therefore proves the adjoint formula. The same argument applies to
a_+ and e^{-u}. The pointwise integrals in (13) supply their continuous
representatives.
If these agree as H elements, their continuous representatives agree
on (0,infinity). The identity theorem on T then gives equality on
the entire real axis. This step is essential: the original adjoint
equation alone is initially only a half-line equality.

Define the entire function and the half-plane transforms

\[
 F(z)=\int_{\mathbb R}e^{zt}\Psi_{\rm ext}(t)\,dt
       =2\Xi(2iz),\qquad
 Y_\sigma(z)=\int_0^\infty e^{-zu}y_\sigma(u)\,du
       \quad(\Re z>0).
 \tag{16}
\]

C032e (8)-(9) pay all fixed exponential weights for F and its
derivatives; t=2v gives its factor 2 and Xi's evenness gives the
displayed argument. For Y_sigma, Cauchy-Schwarz and the exponentially
weighted powers of u give holomorphy and

\[
 |Y_\sigma(z)|\leq\frac{\|y_\sigma\|_2}{\sqrt{2\Re z}}.
 \tag{17}
\]

For every real r>0 the required absolute interchange is

\[
 \int_{\mathbb R}\!e^{rs}\int_0^\infty
 |b_\sigma(s+u)y_\sigma(u)|\,du\,ds
 =\left(\int_{\mathbb R}e^{rt}|b_\sigma(t)|\,dt\right)
   \left(\int_0^\infty e^{-ru}|y_\sigma(u)|\,du\right)<\infty.
 \tag{18}
\]

Tonelli and t=s+u prove the equality; C032e's real tails and (17)'s
Cauchy-Schwarz estimate prove finiteness. The same estimate applies
to a_+ and e^{-u}. Consequently set

\[
 d_\sigma(r)=\alpha F(r+\sigma a)-\beta F'(r+\sigma a),
 \qquad R(r)=\frac{F(r+a)+F'(r+a)}{r+1}.
 \tag{19}
\]

The actual membership equation for this y is equivalent to

\[
 d_-(r)Y_-(r)+d_+(r)Y_+(r)=R(r)
 \quad\hbox{for every real }r>0.
 \tag{20}
\]

Necessity follows from (13), (18) and the transform of e^{-u},
which is 1/(r+1). For sufficiency, retain the hypothesis that the
Y_sigma are transforms of actual y_sigma in L2, not arbitrary
pointwise solutions. Put D(s)=J_y(s)-j(s). Equation (18) gives
e^{rs}D(s) in L1(R) for every r>0. Its bilateral transform
E(z)=integral exp(zs)D(s)ds is holomorphic on Re z>0: on any compact
substrip two surrounding positive real weights dominate both tails,
and slightly wider such weights also dominate |s| for differentiation.
Equation (20) makes E(r)=0 on (0,infinity), so the identity theorem
gives E=0 on that half-plane. For fixed r0>0, the continuous L1
function exp(r0*s)D(s) has Fourier transform E(r0-i*xi)=0 for all
real xi. The Fourier uniqueness theorem used in C032e, [NIST DLMF
1.14(i), Uniqueness](https://dlmf.nist.gov/1.14.i), therefore gives
D=0 everywhere. Restriction to positive s proves B*y=g. This proves
the stated equivalence without an unproved Hardy-space identification.

### Independent adjoint-transform audit — 17 November 2026, step1291

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-17-adjoint-transform-equivalence-audit-nomination-1290.md`.
This audit accepts exactly (12)-(20), retaining the accepted bounded
operators (1)-(5). It verifies the noncompact application of classical
uniqueness; it does not reprove a transform theorem, decide membership,
or audit the subsequent positive-axis test (21)-(25). The primary
Fourier uniqueness citation is NIST DLMF, Section 1.14(i), **Uniqueness**,
[direct source](https://dlmf.nist.gov/1.14.i), with the inspected
hypotheses and convention comparison retained in review1266. The
standard identity theorem is used on connected open domains. The
additional work is necessary because neither a half-line almost
everywhere identity nor a formal bilateral transform is sufficient.

**Fixed data and strip majorant.** The scalar c is real: L020 and the
strictly positive K give the two positive, finite cosh integrals in
(10), and their strict ordering gives 0<c<1. Only reality and finiteness
are needed for the adjoint formula here. C032e (5)-(9), based on L016's
modular identity and L019's full series, supply one holomorphic even
Psi_ext on T, not a separately joined negative-half-line function.
Substitution v=z/2 and division by 2 in C032e (6) give exactly (14).
The strip is |Im z|<pi/2; no boundary point is used.

Here is a complete check of (15). Enlarge any compact subset of T to
a compact neighborhood Q still contained in T, and set
d=min_{z in Q} Re(e^z)>0. For u>=0 and n>=1,

\[
 e^{-\pi d n^2 e^u}
 \leq e^{-\pi d e^u/2}e^{-\pi d n^2/2}.
 \tag{A1291.1}
\]

The series (14) has powers at most n^4 and real exponential factors
at most exp(9u/4), up to constants depending on Q. Its derivative
has powers at most n^6 and factors at most exp(13u/4). This follows
by differentiating each summand, including the factor e^{-pi n^2 e^z};
the resulting additional factor is -pi n^2 e^z. The sums of
(1+n^6)exp(-pi d n^2/2) are finite. On every compact subset the same
estimates give uniform convergence of the differentiated series, so
this differentiation is legitimate. Multiplication by the affine
factors and e^{sigma(z+u)/8}, and their first derivatives, therefore
gives (15) with, for example,

\[
 M_Q=27/8,\qquad \kappa_Q=\pi d/2,
 \qquad m_Q(u)=C_Q(1+u)e^{27u/8-\kappa_Q e^u}.
 \tag{A1291.2}
\]

Both signs and both kernels are covered. The constant C_Q absorbs
the fixed coefficients and bounded z factors. The squared envelope
is integrable: x=e^u gives a constant times
integral_1^infinity (1+log x)^2 x^{23/4}e^{-2kappa_Q x}dx.
It is finite at x=1 and at infinity. Thus m_Q is in L2(0,infinity).
For each arbitrary y_sigma in L2, m_Q|y_sigma| is in L1 by
Cauchy-Schwarz. The enlarged neighborhood controls the derivative
along all sufficiently short difference-quotient segments. Dominated
differentiation in (13) is consequently valid, including for complex
inputs with no support or pointwise-growth restriction. The same
argument applies to j because e^{-u} belongs to L2. It proves
holomorphy of J_y and j on the whole connected strip T.

**Adjoint representatives and extension of equality.** For s,u>0
all four kernels are real. Use the convention that the inner product
is linear in its first variable. For each component and h in H,

\[
 \int_0^\infty\!\int_0^\infty
 |b_\sigma(s+u)h(s)\overline{y_\sigma(u)}|\,ds\,du
 \leq \|b_\sigma(s+u)\|_{L^2(ds\,du)}
       \|h\|_H\|y_\sigma\|_2<\infty.
 \tag{A1291.3}
\]

Indeed the squared product-space norm of h(s)y_sigma(u) factors
as ||h||^2||y_sigma||^2 by Tonelli; the other norm is paid by (7).
Fubini now gives <Bh,y>=<h,J_y>. In particular the adjoint contains
y_sigma, not its conjugate, in (13): conjugating the real kernel in
the adjoint formula leaves the kernel unchanged. The pointwise
representative lies in H, since a second Cauchy-Schwarz estimate gives

\[
 \int_0^\infty |J_y(s)|^2ds
 \leq \|y\|_Y^2
       \sum_\sigma\int_0^\infty\!\int_0^\infty
                    |b_\sigma(s+u)|^2du\,ds<\infty.
 \tag{A1291.4}
\]

Replacing b_sigma by a_+ and y by e^{-u} proves the same assertions
for j and g. Thus (13) represents precisely B*y and A*(0,e^{-u})
on (0,infinity). If those H elements agree, their continuous
representatives agree at every s>0: otherwise continuity would give
a nonzero difference on an interval of positive measure. The identity
theorem then applies to J_y-j on T, with positive real zeros
accumulating at any positive interior point. Equality follows on T,
in particular on the entire real axis. No equality at the endpoint
s=0, no boundary uniqueness theorem and no density assumption on y
are needed.

**Actual transforms, factors and absolute interchanges.** C032e (8)
implies, for every real R>=0 and integer m>=0,
\(\int_{\mathbb R}|t|^m e^{R|t|}|\Psi_{\rm ext}(t)|dt<\infty\).
These bounds prove that F
in (16) is entire with derivatives obtained under its integral.
Changing t=2v and using the evenness of K_ext gives

\[
 F(z)=\int_{\mathbb R}K_{\rm ext}(v)e^{2zv}dv
     =2\int_0^\infty K(v)\cosh(2zv)dv
     =2\Xi(2iz).
 \tag{A1291.5}
\]

All integrals are absolute by those same bounds, and the last equality
is L020, since cos(2izv)=cosh(2zv). This checks the factor 2, the
argument 2iz and the use of the complete density.

For an actual y_sigma in L2 and x=Re z>0,
integral_0^infinity e^{-xu}|y_sigma(u)|du<=||y_sigma||/sqrt(2x).
On a compact subset of Re z>0, the functions u^m e^{-xu} have a
common L2 majorant for m=0,1 (and every fixed m). This proves both
(17) and holomorphy of Y_sigma there, without a Hardy-space theorem
or any assumption of L1 integrability of unweighted y_sigma.

For real r>0, apply Tonelli to the nonnegative integrand in (18).
The change t=s+u has unit Jacobian and s ranges over all of R for
each fixed u. It produces exactly e^{rt}e^{-ru}, so the integral
factors as stated. Its first factor is finite by C032e (8), including
the affine and exponential factors in b_sigma. Its second is finite
by the preceding L2 estimate. The same argument for j has second
factor integral_0^infinity e^{-(r+1)u}du=1/(r+1). Thus ordinary
complex-valued Fubini is justified after absolute integrability has
been proved. Integrating the affine kernels gives

\[
 \int_{\mathbb R}e^{rt}b_\sigma(t)dt
   =\alpha F(r+\sigma a)-\beta F'(r+\sigma a),\qquad
 \int_{\mathbb R}e^{rt}a_+(t)dt=F(r+a)+F'(r+a).
 \tag{A1291.6}
\]

Hence the minus sign, both shifts and r+1 in (19) are correct.
The global equality already obtained from B*y=g proves (20).

**Converse, including all uniqueness hypotheses.** Now start with
an arbitrary actual y in Y whose transforms satisfy (20) for every
real r>0. Set D(s)=J_y(s)-j(s), a continuous function on R. Applying
(18) separately to its three terms proves e^{rs}D(s) in L1(R) for
every r>0. The same Fubini calculation shows that its bilateral
transform E(r) equals the left side of (20) minus R(r), hence is zero.

To check analyticity rather than assume it, fix a compact subset of
Re z>0, with 0<ell<=Re z<=L. Set p=ell/2 and q=L+1. On s<0,
(1+|s|)e^{ell s}<=C_ell e^{ps}; on s>=0,
(1+s)e^{Ls}<=C e^{qs}. The weighted L1 conclusions at p and q thus
give one integrable majorant for both e^{zs}D(s) and its z derivative
on that compact subset and, after a slight enlargement, for difference
quotients. Therefore \(E(z)=\int_{\mathbb R}e^{zs}D(s)ds\) is holomorphic
on the connected half-plane Re z>0. Its zeros E(r)=0 for all positive
real r have an interior accumulation point, so E vanishes throughout
that half-plane.

Fix r0>0. The function v(s)=e^{r0s}D(s) is complex, continuous and
absolutely integrable on R. For every real xi its unnormalized Fourier
transform with negative exponential is E(r0-i*xi)=0. DLMF 1.14(i)
Uniqueness applies: frequency reversal converts its positive-exponential
convention, and its nonzero normalization has no effect on a zero
transform. Thus v=0 everywhere, and D=0 everywhere. Restricting to
(0,infinity), the established adjoint representatives give B*y=g.
Both directions of (20) are now checked for the stated actual L2 pair.

**Verdict and limits.** No defective implication or required repair
was found in (12)-(20). The audit validates the existing specialized
criterion; it gives neither a preimage nor nonmembership and no sign
for delta. It does not replace actual Laplace transforms by arbitrary
holomorphic scalar solutions, discard a component, impose a norm cap,
or use positivity of scalar kernels to infer positivity of the signed
form. The positive-axis test (21)-(25), the source metric, signed
realization, initialization and all-degree actual-Xi positivity remain
outside this audit. C032e and L020 remain the direct mathematical
inputs; L016 and L019 enter through C032e's cited continuation/bounds.
No new node or dependency is introduced.

### Positive-real-axis obstruction test — original step1273, unaudited here

The positive-real-axis obstruction test in (20) can now be completed.
For real x write m(x)=F'(x)/F(x). The strictly positive full density
Psi_ext makes F(x)>0. Evenness gives m(0)=0 and m(-x)=-m(x).
Differentiating under the integral gives

\[
 m'(x)=\frac{\int t^2e^{xt}\Psi_{\rm ext}(t)\,dt}{F(x)}-m(x)^2>0.
 \tag{21}
\]

This is the variance of the probability density
exp(xt)Psi_ext(t)/F(x). Strictness holds because that density is
positive on every real interval and is not concentrated at one point.
Also m(x) tends to infinity as x tends to positive infinity. Indeed,
for any fixed M>0 and x>0,
F(x)>=exp(M*x) integral_[M,M+1] Psi_ext(t)dt. If the increasing m
had a finite upper bound L, integration of (log F)'=m would give
log F(x)<=log F(0)+L*x, contradicting this lower bound with M>L.
Thus there is a unique rho>0 with m(rho)=t0.

Equation (19) becomes

\[
 d_\sigma(r)=\beta F(r+\sigma a)
                   (t_0-m(r+\sigma a)).
 \tag{22}
\]

The two coefficients never vanish together for r>=0: their vanishing
would require both r-a=rho and r+a=rho, impossible since a>0.
In particular d_-(0)>0. The zero of d_- at r=rho+a only fixes
one transform value:

\[
 Y_+(\rho+a)=
 \frac{1+m(\rho+2a)}
 {(\rho+a+1)\beta(t_0-m(\rho+2a))}<0.
 \tag{23}
\]

Negative transform values are allowed for the stated complex class;
they do not contradict any hypothesis. Dropping a component or imposing
nonnegative y would incorrectly strengthen the membership problem.

Let S(r)=(|d_-(r)|^2+|d_+(r)|^2)^(1/2)>0. Cauchy-Schwarz in the
two components and (17) give the necessary condition

\[
 \|y\|_Y\ \geq\ M_*:=\sup_{r>0}
       \frac{\sqrt{2r}\,|R(r)|}{S(r)}.
 \tag{24}
\]

Crucially, 0<M_*<infinity. The quotient is continuous for r>0
and tends to zero at r=0 because S(0)>0 and R is finite there.
For sufficiently large r, m(r+a)>=t0+1. Since S(r)>=|d_+(r)|,

\[
 \frac{\sqrt{2r}|R(r)|}{S(r)}
 \leq \frac{\sqrt{2r}}{r+1}
       \frac{1+m(r+a)}{\beta(m(r+a)-t_0)}
 \leq \frac{\sqrt{2r}}{r+1}\frac{2+t_0}{\beta}
 \longrightarrow0.
 \tag{25}
\]

Continuity on the remaining compact interval proves finiteness;
positivity of F(r+a)+F'(r+a) proves strict positivity. No numerical
constant or computed maximum is asserted. Infinite M_* would have
excluded all L2 preimages; the actual test gives a finite necessary
lower bound on a preimage norm, for which no upper budget is imposed.
It therefore does not exclude a preimage. Nor does it construct one:
analyticity, one-sided support and joint L2 realizability of both
Y_sigma in (20) remain essential. The simple positive-real test is
stopped here. The normalized delta threshold remains undecided after
two attempts; this is an exploratory reduction, not a positivity
advance or a claim of originality beyond the sources checked.

## Mathlib

The full normalized pair, the particular domain/core reduction, and
Douglas's theorem in Mathlib were not checked; availability is unknown.
The supporting theta references recorded in C032e do not constitute
a formalization of (4)-(5). No Lean or numerical verification is claimed.
The particular adjoint transform criterion (20) and finite necessary
bound (24)-(25) also have unchecked Mathlib coverage; no absence claim
is made. The informal conceptual audit1291 above verifies (12)-(20)
only and is not a formal verification or an audit of (21)-(25).
