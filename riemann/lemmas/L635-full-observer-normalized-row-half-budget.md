# Lemma 635: a full-observer relative half-budget from normalized rows

## Hypotheses

Use exactly L629's Hermitian K_c(T,X), fixed nonnegative
w in C_c^infinity((0,1)) with integral 1, T<=X<=2T,
L=log T, N=floor(T^(1/100)), arbitrary a in C^N, and a common
real unit observer c=(c0,c1). Put

    M=log N, Gamma=a^*G_N a,
    B(c)=(28c0^2+c1^2)/(840pi^2).

Retain L623's full Gram identity, L624's complete shifted arithmetic
form B_N(q;a) with its analytic C_N(q), and the divisor-triangular
real change of basis V of L627/L634, with V^*G_N V=I. In particular,
every coordinate r in S_N, including r>N, is retained. Coefficients
and V stay fixed during shift differentiation. Use the three exact
weights in L629 (5)–(7), its qualified uniform transfer (1), and
L634 (20), whose normalized-row argument has the conceptual audit
in that lemma's Section 7. Section 5 below records the subsequent
audit of this contraction and its transfer through L629, including
the used L628 norm bound and L622 absolute-error conversion. No
blanket audit of other inputs or external manuscripts is assumed.

The already assessed external inputs remain C. P. Hughes and
M. P. Young, *The twisted fourth moment of the Riemann zeta
function*, J. reine angew. Math. 641 (2010), 203–236,
[arXiv:0709.2345v2, Theorem 1.1, (12)–(17), printed pp. 4–5
and the complete-sum holomorphy remark](https://arxiv.org/pdf/0709.2345v2#page=4),
and the finite-prime isometry of H. Hedenmalm, P. Lindqvist and
K. Seip, *A Hilbert space of Dirichlet series and systems of dilated
functions in L2(0,1)*, Duke Math. J. 86 (1997), 1–37,
[arXiv:math/9512211v1, Section 2.2, (2-7), Lemma 2.3,
pp. 7–9](https://arxiv.org/pdf/math/9512211v1#page=7).
Their arithmetic and torus specializations and local convergence
are those checked in L623/L624/L627/L634. No such source theorem
is reproved or claimed to supply the observer budget below.
There is no RH, zero-free, simplicity, spacing or pointwise sign
hypothesis.

## Conclusion

Let P_c(N,L;a) denote precisely the finite leading arithmetic form
on the right of L629 (1), without its O_w(Gamma/L) error. Uniformly
over all complex vectors a and all common real unit observers c,

    |P_c(N,L;a)-B(c)Gamma|
      <= B(c)Gamma [7794564687024429/20000000000000000+o(1)],
                                                             (1)

where o(1) is independent of a,c. The exact rational cost is
0.38972823435122145<2/5. Consequently one existential onset,
depending on fixed w but independent of X,c,a, gives

    |a^*(K_c(T,X)-B(c)G_N)a|
      <= (9/20) B(c)Gamma < (1/2)B(c)Gamma                 (2)

for a!=0; the non-strict half-budget holds also for a=0.
In particular K_c>=(11/20)B(c)G_N at this onset.

At a possibly larger common onset, the same relative bound holds
for L622's normalized actual signed integral

    I_c(T,X;a)=1/(T L^6) integral w_XT(t) W(t)
             |sum_(n<=N) a_n n^(-it)|^2
                         (c0 Z(t)+c1 Z'(t)/L)^2 dt:
    |I_c(T,X;a)-B(c)Gamma| <= (9/20)B(c)Gamma.           (2a)

Here Z=-Xi/A and W=D_1(Xi)/A^2 are exactly L622's zero-safe
normalizations. This application retains its named moment and
complete-sum holomorphy imports. Section 5 audits the previously
qualified passage and charges both transfer errors together.

This extends the existing c=(0,1) local row estimate to every
common real observer by a finite coefficient contraction. It is
a local advance under the prior EXPLORE assessment, with no
certified originality claim. The used-scope audit in Section 5
validates the contraction and relative transfer; external-source
qualifications persist. No numerical onset, pointwise Xi sign or
RH candidate is supplied. The common observer and fixed w are
essential scope restrictions.

## Proof

### 1. Full analytic entries and the coefficient norm used

Write a=Vy, and let T_nm(q) be the normalized arithmetic entry
with L634's convention

    B_N(q;Vy)=sum_(n,m<=N) y_n conjugate(y_m) T_nm(q).

L624 (1)/(5) and its proof give this identity by expansion of the
full absolutely convergent convolution, in both twist orientations.
On compact |Re q_j|<1/4 the finite-prime geometric sums and all
fixed derivatives converge locally uniformly: each derivative only
inserts polynomial factors in prime exponents into convergent
geometric sums. C_N(q) is analytic and nonzero there. Thus for fixed
N the following Taylor coefficients and pair symmetries are valid.
This convergence statement alone is not a uniform-in-N estimate.

Put t_nm,nu=[q^nu]T_nm(q) and v_n=n^(-1/2). The coefficients
t_nm,nu are real. Each entry is symmetric within each of the two
shift pairs, and exchanging those pairs transposes the entry:

    t_mn,nu=t_nm,(nu3,nu4,nu1,nu2),
    t_nm,0=delta_nm.

These follow either from L634's full torus integral by z->z^-1
at every prime (the fixed rational basis has real coefficients),
or from the convolution identity with exchanged coefficients.
No shift is conjugated. L634's boundary analysis and complete
weighted rows establish, for every k<=8,

    sup_(n<=N) M^(-k) sum_(m<=N)(v_m/v_n)
                          sum_(|nu|=k)|t_nm,nu| <= A_k+o(1),
    A_k=[u^k]exp(2u+4(exp(u)-1)).                         (3)

The uniformity in (3), rather than fixed-N convergence, is the
analytic input used below. It was obtained by majorizing the full
output row m in S_N, including m>N, before restricting the row.
Thus neither the convolution tail nor derivatives of C_N are lost.

### 2. Normalize the joint observer functional before estimating

For any multi-index nu let nu^down be obtained by sorting each
pair in decreasing order, and let o_nu be the number of distinct
pair swaps of nu, namely

    o_nu=(1 if nu1=nu2 else 2)(1 if nu3=nu4 else 2).

Let (w0,w1,w2) be L629's weights at nu^down. Since t_nm,nu is
constant on that orbit, its weight can be distributed equally
among the o_nu indices, before taking absolute values. Set

    D(c)=28c0^2+c1^2,
    alpha_nu(c)=5040(w0 c0^2+i w1 c0 c1+w2 c1^2)/(o_nu D(c)).
                                                             (4)

Indeed (6/pi^2)/B(c)=5040/D(c). Thus L629's exact finite
functional, divided by B(c), is represented in this basis by
the entry array

    C_nm(c)=sum_(|nu|<=8) alpha_nu(c)t_nm,nu/L^|nu|.     (5)

All degrees above eight vanish exactly in that functional. No
analytic remainder is discarded. At degree zero the weights
(1/180,0,1/5040) give alpha_0=1, the exact reference identity.

To bound (4), put x=sqrt(28)c0 and z=c1. For each orbit set

    A=180|w0|/o_nu,  D=5040|w2|/o_nu,
    J=1008|w1|/o_nu,  b_nu=max(A,D)+J/2.

Since sqrt(28)>5, the modulus of the imaginary cross coefficient
in (4), in these variables, is at most J. Triangle inequality and
2|xz|<=x^2+z^2 give for every real nonzero (x,z)

    |alpha_nu(c)|
      <= (A x^2+J|xz|+D z^2)/(x^2+z^2)
      <= b_nu.                                           (6)

This bounds the joint observer functional, including its imaginary
mixed term. Endpoint observers alone are not used as a substitute.
The bound remains valid for all signs of c0,c1 and arbitrary
complex arithmetic coefficients.

Exact maximization over the finite orbit table gives

    k       0   1     2     3    4    5     6     7     8
    b_k     1  27/5 301/10 105  420  840  2520  2520  5040,
    A_k     1   6    20  146/3 577/6 979/6 44261/180
                                             47127/140 4287229/10080,

where b_k=max_(|nu|=k)b_nu. The last three A_k entries occupy
k=6,7,8 respectively; the displayed line wraps only for width.
They are the coefficients in (3). All values are rational.

### 3. Hermitian extraction and the full weighted row bound

The exact weights obey pair-exchange symmetry

    w(nu3,nu4,nu1,nu2)=(w0(nu),-w1(nu),w2(nu)).

This is L629's finite signed prescription (and is checked for
every row in the certificate below). Equations (4) and the real
entry symmetry in Section 1 therefore give C_mn=conjugate(C_nm).
The array C is Hermitian. With the stated y_n conjugate(y_m)
convention the ordinary matrix of the quadratic form is C^transpose;
it too is Hermitian and has the same entrywise absolute values.
Consequently taking the real part in P_c does not enlarge any
entry or discard an uncontrolled imaginary quadratic term.

By (3), (5), (6), and M/L<=1/100, the weighted absolute rows of
the normalized defect E=C^transpose-I satisfy

    max_(n<=N)sum_(m<=N)|E_nm|v_m/v_n
      <= sum_(k=1)^8 b_k(M/L)^k(A_k+o(1))
      <= sum_(k=1)^8 b_k A_k/100^k+o(1)
       =7794564687024429/20000000000000000+o(1).           (7)

There are only eight degrees; the little-o is uniform in n,c.
In particular it is uniform in all coefficient vectors.
For completeness the Hermitian weighted row inequality follows
directly from

    |y_n y_m| <= [(v_m/v_n)|y_n|^2
                             +(v_n/v_m)|y_m|^2]/2.

Multiply by |E_nm| and sum; Hermitian symmetry makes the two
sums equal. Thus |y^*E y| is at most the row bound in (7) times
||y||^2. Since ||y||^2=Gamma, this proves (1) for arbitrary complex
a. This argument uses complete normalized entries, not products
of compressed shift operators or positivity of a complex measure.

### 4. Finite verification, transfer reserve and qualifications

Run from the active notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/full_gram/full_observer_row_budget.py

The full certificate is
`scripts/full_gram/full_observer_row_budget_certificate.json`.
It records all 175 orbit weights, all 495 underlying multi-indices,
their rational observer bounds, every degree maximizer and cost,
and 525 full-polynomial divisions/replays, one for each orbit and
output degree 2,3,4. Each quotient is multiplied back by the
Vandermonde by the exact-division routine. Its extracted weight
agrees with L629's separate alternant-coefficient prescription in
every case. This is a finite algebra replay, not an independent
conceptual audit. Pair-exchange symmetry, the reference coefficient,
and the coefficient exponential (computed two ways) also pass.
All 12 aggregate checks pass, with no failures.

The strict slack in (7) is

    2/5-7794564687024429/20000000000000000
      =205435312975571/20000000000000000>0.

Hence the uniform little-o is eventually smaller than this slack,
giving arithmetic defect at most (2/5)B(c)Gamma. L629 (1) adds
an error bounded by C_w Gamma/L uniformly over X,c,a. Because
B(c)>=1/(840pi^2) for every real unit observer, its relative cost
is at most 840pi^2 C_w/L. At a further common existential onset
this is <=1/20. Adding the two costs proves (2). For a=0 every
term is zero; for a!=0, Gamma>0 follows from the orthonormal basis
identity, and 9/20<1/2 gives the strict displayed comparison.

The argument changes no window, length exponent, observer family,
phase, signed derivative, gcd multiplicity or arithmetic normalization.
It replaces previously excessive sufficient constants using the
checked full-row majorant and the exact joint weights. Earlier
failed majorizations were not counterexamples, and are preserved.
The onset is not effective. The later audit in Section 5 supersedes
the original pending-audit status of this contraction and L629's
analytic transfer. An audited averaged margin does not establish
pointwise signs or RH.

### 5. Independent joint-observer and transfer audit, 1 November 2026

The claimed arithmetic contraction and exact-matrix bound (1)–(2)
pass this audit. The separately qualified actual-Xi application is
completed as (2a) below. This reproduces and validates the local
argument; it does not establish originality or audit the imported
moment manuscripts. L628 (1)–(2) and L629 (1)/(5)–(7) have their
used-scope audits in those canonical files. Unrelated input claims
are not prerequisites silently declared audited here.

**Uniform analytic input and matrix convention.** L624's full
convolution, its nonzero analytic normalization, and the real
divisor-triangular basis give exactly the entries T_nm in Section 1.
The fixed coefficients of every basis vector are real. Thus Taylor
coefficients are real and swapping the two shift pairs transposes
T, while swapping inside either pair fixes it. This remains true
with every output coordinate r>N retained. L634 (20) and Section 7
bound their complete weighted rows through degree eight: the incoming
bulk loses one degree, the two incoming boundary entries have the
separate O_k(x(d+1)^(k-1)) estimate, the outgoing remainders sum
with x^d, and the vacuum diagonal is identically one. Its uniform
remainder is justified by, for each fixed R,

    sup_(n<=N) M^(-k) sum_(p|n)
       (log p)^k(e_p+1)^(k-1)/p
       <= 2^(k-1)[(sum_(p<=R)log p/p)/M+1/R].

First M tends to infinity and then R does. The p^(-2) remainder
is summable. This is a common o(1) for all rows, not an onset
chosen for each vector. The finite-prime coefficient products and
full row sums are justified before this limit. These observations
check the precise analytic scope passed from L634 into (3).

Each pair orbit contributes a single common Taylor coefficient.
Dividing its weight by its orbit size therefore leaves the exact
functional unchanged; taking absolute values before that division
would lose the required budget. Coefficients t_nm,nu are Taylor
coefficients, so the factorial in L629's h_nu has already been
included. The scalar identity (6/pi^2)/B(c)=5040/(28c0^2+c1^2)
gives (4) without a further multiplicity.

In variables x=sqrt(28)c0 and z=c1, the normalized diagonal
coefficients have bounds A and D, and the absolute mixed coefficient
is 5040|w1|/(sqrt(28)o_nu)<1008|w1|/o_nu=J. Thus
|alpha_nu|<=max(A,D)+J/2 follows from 2|xz|<=x^2+z^2.
It holds for both signs and all sizes of the real common observer,
including either zero endpoint. No sign or vanishing of the imaginary
channel is assumed. Under exchange of the shift pairs, w1 reverses
sign and the other weights stay fixed. Hence C_mn=conjugate(C_nm).
The actual quadratic matrix is C^transpose because the entry
convention uses y_n conjugate(y_m). Both matrices are Hermitian
and |C_mn|=|C_nm|, so transposition preserves the weighted absolute
row bounds. This verifies the step for arbitrary complex a.

**Independent finite evidence.** Run

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/full_gram/full_observer_row_budget_audit.py

This script imports no notebook calculation module. As described
in L629's audit, it reconstructs the full polynomial quotients and
uses the original differential operators, without presuming their
symmetric simplifications. It checks every coefficient of all 525
quotients, all three observer weights, all 175 orbit bounds covering
495 multi-indices, and all pair-exchange signs against the original
certificate. Truncated exponentiation independently reproduces A_k.
The exact degree costs for k=1,...,8 are

    81/250, 301/5000, 511/100000, 4039/10000000,
    6853/500000000, 309827/500000000000,
    424143/50000000000000, 4287229/20000000000000000.

Their sum is precisely the rational number in (7), with the stated
positive slack to 2/5. All 16 checks pass, without failures. Full
quotients, comparisons, costs and the original certificate's SHA-256
are saved in
`scripts/full_gram/full_observer_row_budget_audit_certificate.json`.
This finite evidence supports the algebra only; the uniform analytic
argument is the one above and in L634, not a finite numerical test.

**One common reserve, including actual Xi.** L629's audited error
has size at most C_w Gamma/L. L622's distinct actual-Xi error has
size at most epsilon_T||a||^2. L629's audit of the L623 lower bound
converts the latter to at most eta_w(T)Gamma, where

    eta_w(T)=4 C'_w(1+L/100)^2
        [T^(-13/80)/L^4+T^(-97/50)/L^2]=o(1/L).

The constants C_w,C'_w may differ; both are independent of X,a,c.
For real unit c, B(c)>=1/(840pi^2). Therefore the combined relative
cost is at most 840pi^2(C_w/L+eta_w(T)), tending to zero uniformly.
Choose one onset so the arithmetic o(1) in (7) is at most its
positive slack to 2/5, and a further common onset so this entire
combined cost is <=1/20. Then (2) and (2a) hold simultaneously,
with 2/5+1/20=9/20<1/2. The reserve is not spent twice. At a=0
all terms vanish; otherwise Gamma>0 by the reference lower bound.

This settles the relative averaged margin for exactly the fixed
smooth window, length exponent 1/100, and one common real observer.
In particular this family cannot produce a negative averaged witness
at sufficiently large T under the named imports. No inference is
made about a height-dependent narrowing window, varying observer,
effective finite height, pointwise W, all-degree mixed positivity
or RH. These are different problems, not missing terms in this audit.

## Mathlib

Full matching Mathlib coverage of this observer-uniform full-Gram
estimate and its transfer has not been checked and remains unknown.
The primary isometry and moment inputs are cited above and used
through their local specializations. The rational polynomial
algebra, observer inequality and weighted Hermitian row argument
are proved at the needed scope here. The script certifies the
finite algebra only; it is not a Lean proof, a verification of the
analytic imports, an effective-height certificate or an RH proof.
