# Corollary C030a: finite heat–Laplace transfer to the mixed form

## Hypotheses

Use the actual Xi zeros and notation of L018/L024-L026/L030.
Choose one representative alpha_j from each pair {alpha,-alpha},
with its zero multiplicity, and put

\[
 \lambda_j=\alpha_j^2,\qquad
 S_m=\sum_j\lambda_j^{-m},\qquad
 \mathcal H(t)=\sum_j e^{-\lambda_jt}\quad(t>0).
\]

Fix an integer d>=0 and set k=d+1. For the positivity conclusion only,
assume the real symmetric matrix

\[
 B_k(t)=\bigl[(-1)^{r+s}\mathcal H^{(r+s)}(t)\bigr]_{0\le r,s<k}
 \quad\text{is positive definite for every }t>0.                 \tag{P}
\]

The trace and its derivatives exist unconditionally, as justified
below. Hypothesis (P) is not proved here. No real-zero assumption,
one-time substitute, or semidefinite substitute is made.

## Conclusion

For all nonnegative integers r,s, the following integral converges
absolutely and has the exact normalization

\[
 M_{rs}:=\int_0^\infty\!\int_0^\infty
      \frac{x^r}{r!}\mathcal H(x+y)\frac{y^s}{s!}\,dx\,dy
      =S_{r+s+2}.                                               \tag{1}
\]

Under (P), H_d=[S_{r+s+2}]_(0<=r,s<=d) is positive definite.
Consequently L030's Q(q)>0 for every nonzero real polynomial q of
degree at most d. This is a conditional fixed-degree implication,
not a new unconditional sign assertion or a proof of RH.

For q(X)=c_0+c_1 X the exact observable is

\[
 Q(q)=c_0^2S_2+2c_0c_1S_3+c_1^2S_4.                            \tag{2}
\]

Thus no coefficient factorial or mixed term has been lost. The
premise uses derivatives through order 2d; the conclusion uses
moments through S_(2d+2).

## Proof

### Squared nodes, multiplicities and convergence

By L026, write alpha_j=u_j+iv_j with |u_j|>4 and |v_j|<1/2.
For a_j=Re(lambda_j) and c=63/65 we have

\[
 a_j=u_j^2-v_j^2>63/4,\qquad
 a_j\ge c\,|\lambda_j|=c(u_j^2+v_j^2).                         \tag{3}
\]

Indeed 64v_j^2<u_j^2, which implies the second inequality.
L024 gives A=sum_j |lambda_j|^(-1)<infinity. For each integer m>=1,

\[
 \sum_j a_j^{-m}
 \le (4/63)^{m-1}(65/63)A<\infty.                              \tag{4}
\]

For epsilon>0 and any integer ell>=0,

\[
 |\lambda_j|^{\ell}e^{-a_jt}
 \le |\lambda_j|^{-1}
       \sup_{v>0}v^{\ell+1}e^{-c\epsilon v},\qquad t\ge\epsilon.
                                                                    \tag{5}
\]

The supremum is finite, so the derivative series converge uniformly
on every compact positive-time interval. Thus the trace is smooth
and H^(ell)(t)=sum_j(-lambda_j)^ell exp(-lambda_j t).
Here and below H in derivative prose denotes mathcal H.

L018 gives equal multiplicities under negation and conjugation of
Xi zeros. Squaring eliminates the representative's sign, and the
squared-node multiset is conjugation invariant, so mathcal H is real.
More explicitly we may select u_j>0. For rho=b+i gamma a zeta zero
with gamma>0, its Xi zero is alpha=gamma-i(b-1/2); hence
lambda=-(rho-1/2)^2. The pair {alpha,-alpha} corresponds to
{rho,1-rho}, with multiplicity. An off-line quartet contributes two
conjugate squared nodes; a critical-line pair contributes one real
squared node. Therefore

\[
 \mathcal H(t)=\sum_{\Im\rho>0}e^{(\rho-1/2)^2t}
             =\tfrac12\sum_\rho e^{(\rho-1/2)^2t}.              \tag{6}
\]

This matches Sra's H (p1) and Polson's W, Definition 5.1, (4),
printed p8, in [arXiv:1708.02653v24](https://arxiv.org/pdf/1708.02653v24).
Polson's Section 6.4, printed p15 (PDF index14), uses sigma_n=S_(n+1).
Its sharper endpoint estimates are unnecessary here. Bounds (3)-(5)
are an applicability argument from the existing local inputs, rather
than a reproof of the source's stronger heat asymptotics.

Set G(t)=sum_j exp(-a_j t). This is finite and continuous for t>0,
and |mathcal H(t)|<=G(t). With u_r(x)=x^r/r!, Tonelli's theorem and
the gamma integral give

\[
 A_{rs}:=\int_0^\infty\!\int_0^\infty
       u_r(x)G(x+y)u_s(y)\,dx\,dy
       =\sum_j a_j^{-r-s-2}<\infty.                            \tag{7}
\]

This controls both endpoints jointly, including the corner x=y=0.
It justifies exchanging the node sum and both integrals in (1).
For each node, set t=x+y and z=x/(x+y), with Jacobian t. Euler's
beta integral and the gamma Laplace integral yield

\[
 \begin{aligned}
 \int\!\int u_r(x)u_s(y)e^{-\lambda_j(x+y)}\,dx\,dy
 &=\frac{1}{r!s!}\int_0^1 z^r(1-z)^s\,dz
                   \int_0^\infty t^{r+s+1}e^{-\lambda_jt}\,dt\\
 &=\frac{1}{(r+s+1)!}(r+s+1)!\lambda_j^{-r-s-2}.
 \end{aligned}                                                \tag{8}
\]

The cited formulas are [DLMF 5.12.1](https://dlmf.nist.gov/5.12.E1)
and [DLMF 5.9.1](https://dlmf.nist.gov/5.9.E1): use beta parameters
r+1,s+1 and gamma parameters mu=1, nu=r+s+2, z=lambda_j.
Their real-part conditions hold by (3); the integer powers introduce
no branch choice. Absolute convergence was established before this
complex evaluation. Summing (8) proves (1), consistently with L025.

### Strict kernel signs and both determinant compositions

Import Suvrit Sra, *On some positivity properties of the Riemann Xi
function*, [Hexagon 2610.00584v1](https://hexagonmath.org/pdf/2610.00584v1),
Proposition C.2, printed p19, based on Lemma C.1, pp18-19.
For a smooth real f, its strict differential Hankel premise at every
positive time implies strict total positivity of f(x+y) through that
finite order. Apply it to f=mathcal H using (5) and (P). Hence for
every 1<=n<=k and strictly increasing positive x_1,...,x_n and
y_1,...,y_n,

\[
 \det[\mathcal H(x_a+y_b)]_{a,b=1}^n>0.                       \tag{9}
\]

The signs in (P) cause no reversal: for each n<=k its leading
block is congruent to [mathcal H^(r+s)(t)]_(r,s<n) by the diagonal
matrix diag(1,-1,...,(-1)^(n-1)). Thus every initial differential
determinant required in Proposition C.2 is positive. No shifted
block is needed for this theorem. No infinite-order theorem or new
Wronskian argument is needed.

Fix such n, and first restrict each variable to I=[epsilon,R],
where 0<epsilon<R. Let K(x,y)=mathcal H(x+y) and
F_r^I(y)=integral_I u_r(x)K(x,y) dx. All these functions are
continuous on the relevant compact sets. Apply Andreief first in y
to the pair of lists (F_r^I) and (u_s), then in x to the lists (u_r)
and (K(.,y_b)). Its exact version is Giulio Ruzza,
[*Introduction to Random Matrix Theory, Riemann-Hilbert problems,
and Universality*, 4 May 2022](https://webpages.ciencias.ulisboa.pt/~gruzza/introRMT.pdf),
Lemma 3.1.1, (3.1.1), printed pp27-28. The hypotheses allow complex
measurable functions with every cross product in L1; there is no
conjugation. Compact continuity verifies those hypotheses at both
applications. Writing M^I for the corresponding double-integral
matrix, transposing an evaluation matrix when necessary gives

\[
 \det[M^I_{rs}]_{r,s=0}^{n-1}
 =\frac{1}{(n!)^2}\int_{I^n}\!\int_{I^n}
       V_n(x)\det[K(x_a,y_b)]_{a,b=1}^n V_n(y)\,dx\,dy,        \tag{10}
\]

where

\[
 V_n(x)=\det[u_r(x_a)]_{\substack{0\le r<n\\1\le a\le n}}
       =\frac{\prod_{a<b}(x_b-x_a)}{\prod_{r=0}^{n-1}r!}.
                                                                    \tag{11}
\]

Transposition changes no sign. Each composition contributes exactly
one factor 1/n! in (10).

For completeness, the pairwise L1 conditions also hold before
truncation. For fixed y>0,

\[
 \int_0^\infty u_r(x)|K(x,y)|\,dx
 \le\sum_j e^{-a_jy}a_j^{-r-1}<\infty
\]

by (4). Thus F_r(y)=integral_0^infinity u_r(x)K(x,y)dx exists, and
integral_0^infinity |F_r(y)u_s(y)|dy<=A_rs by (7). Domination on
compact y-intervals gives measurability (indeed continuity).

The complete 2n-variable integrand in (10) is absolutely integrable,
not just its entries. Expand its three determinants and take absolute
values. Each of the at most (n!)^3 terms is bounded by an expression
of the form

\[
 \prod_{a=1}^n u_{r_a}(x_a)G(x_a+y_{\tau(a)})
                      u_{s_{\tau(a)}}(y_{\tau(a)}),            \tag{12}
\]

where (r_a) and (s_b) permute 0,...,n-1 and tau permutes 1,...,n.
Pairing x_a with y_tau(a), its integral is
product_a A_(r_a,s_tau(a)), finite by (7). In particular, if
A_*=max_(r,s<n) A_rs, the integral of the absolute value of the
complete determinant product is at most (n!)^3 A_*^n.
This proves the needed domination for both compositions and their
joint improper limit, without appealing to signs of complex terms.
It also permits independent cutoffs I_x and I_y: the product of their
indicators is bounded by one against the same integrable majorant.
Consequently either iterated cutoff removal gives the joint limit.

### Improper limits retain strictness

Take I_m=[1/m,m], m>=2. Equation (7) gives M^(I_m)_rs -> M_rs.
Continuity of a finite determinant and the preceding absolute
integrability pass (10) to the entire positive quadrant in every
variable. The determinant product is invariant under a permutation
of the x variables: V_n and the rows of K acquire the same sign.
The same holds in y. Collision sets have Lebesgue measure zero.
There are (n!)^2 chambers, so their count cancels the prefactor:

\[
 \det[S_{r+s+2}]_{r,s=0}^{n-1}
 =\int_{0<x_1<\cdots<x_n}\int_{0<y_1<\cdots<y_n}
          V_n(x)\det[K(x_a,y_b)]V_n(y)\,dy\,dx.                \tag{13}
\]

The integrand is positive at every point of this ordered open set
by (9) and (11). To retain an explicit compact contribution, choose
x_a=y_a=a for a=1,...,n. At this point the integrand has some value
eta>0. By continuity, a sufficiently small closed product box around
it stays strictly ordered, positive and inside [1/2,n+1]^(2n), with
integrand at least eta/2. Its positive volume gives a strictly
positive lower contribution in (13). The rest of the ordered domain
is nonnegative. This proves strict positivity of the improper
integral; entrywise convergence alone would not have done so.

For n=1 the empty Vandermonde products equal one, so the same
argument covers S_2. Since n was arbitrary up to k, all leading
principal minors of H_d are strictly positive. By (1) and the reality
of the trace, H_d is real symmetric. Sylvester's criterion for real
symmetric matrices now proves H_d>0.

Strictness has not assumed an unproved rank bound for the spectrum.
If there were only r<k distinct squared nodes, derivative expansion
would express B_k as a sum of r rank-one matrices over C (with their
multiplicity weights), so its rank would be <=r, contradicting (P).
In particular repetitions cannot manufacture strictness when the
premise is false.

Finally put p(x)=sum_(r=0)^d c_r x^r/r!. The finite expansion of the
absolutely convergent integral gives

\[
 \int_0^\infty\!\int_0^\infty p(x)\mathcal H(x+y)p(y)\,dx\,dy
 =\sum_{r,s=0}^d c_rc_sS_{r+s+2}=Q(q)
\]

by L030, where q(X)=sum c_r X^r. For d=1 this is exactly (2).
It is a bilinear kernel representation of the algebraic-square
observable, not a replacement by absolute-value squares. For a
nonzero coefficient vector, positive definiteness proves the stated
strict sign.

The degree-one and degree-two signs were already known locally;
they are normalization checks here. The local contribution is the
conditional two-stage specialization with its improper-integral
justification, not a result claimed beyond the checked sources.
No source finite-sign theorem is applied, no all-degree premise is
established, and no common-graph realization follows.

### Critical audit — 16 November 2026, step1112

The fixed-degree implication passes the separate conceptual audit
approved in nomination1110/review1111. This verifies the conditional
specialization of the cited tools; it establishes no new unconditional
heat-block or mixed-form sign beyond the sources checked.

- L018/L024/L026 justify (3)-(6) with multiplicity and nonreal nodes:
  conjugation pairs survive squaring, while negation contributes no
  extra copy. No real-spectrum premise enters the estimates.
- The joint absolute integral (7) is finite even at the origin corner.
  Formula (8) cancels r!, s! and (r+s+1)! and gives precisely the
  shift r+s+2. It never substitutes a modulus square for L030's form.
- The exact strict premise of Sra Proposition C.2, including all
  positive times, was matched to (P). Ruzza Lemma 3.1.1 was matched
  separately to both pairs of function lists. The proof above checks
  every cross product in L1, orientations and both factors 1/n!.
- The (n!)^3 A_*^n estimate bounds the complete integrand. Separate
  endpoint removals and the joint limit therefore agree. The two
  chamber counts cancel (n!)^(-2); positivity on a closed box of
  positive volume prevents loss of strictness in that limit.
- Reality and all leading minors give Sylvester's criterion through
  size d+1. The n=1 case, insufficient distinct-node rank, the mixed
  term 2c_0c_1 S_3 and maximum moment S_(2d+2) are all covered.

The original p15 locator for Polson Section 6.4 is correct: p14 in
the earlier coverage notes confuses PDF index14 with printed page15.
Only its trace and moment conventions are used. The independent
all-degree signs and common-graph realization remain open. This is
an audit of C030a relative to its stated local inputs, not a fresh
audit of all their ancestors or of a source finite-sign theorem.

## Mathlib

Not checked for a full matching theorem, the strict differential-to-
kernel transfer, or the two-stage determinant identity. No absence
claim is made. The analytic proof above is informal and has not been
formalized. Reference: [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
