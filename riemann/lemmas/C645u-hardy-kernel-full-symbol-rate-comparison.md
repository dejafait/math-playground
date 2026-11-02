# Corollary 645u: Hardy-kernel tests preserve the full-symbol exponential rate

## Hypotheses

Retain C645g's normalized Hardy spaces and C645n's rotated family:
n>=5, x=-5/4, R=11/8, eta=1/100, t_j=j/n, a common finite set Z
of distinct poles on Re(a)=x with |a|<=R-eta and x in Z, positive
integer original simple-pole residues r_a, and M=sum_a r_a<=n/3.
With |u|=1 put

    B_u(v)=product_(j=0)^(n-1) R*(v-t_j*u)/(R^2-t_j*conjugate(u)*v),
    alpha_a=a/R, d_a(u)=r_a*B_u(x)/(R*B_u(a)),
    q_u(zeta)=sum_a d_a(u)/(zeta-alpha_a),
    H_u f=P_-(q_u*f): H^2 -> H^2_-.

Here u=i exp(i theta), so this is exactly the conjugated-denominator
rotation of the assessed family. Both circle measures are normalized.
Set s=1-1/n and

    k_(s,psi)(zeta)=sqrt(1-s^2)/(1-s*exp(-i*psi)*zeta),
    Q_n=(mean_u ||q_u||_2^2)^(1/2),
    T_n=(mean_u sup_psi ||H_u k_(s,psi)||_2^2)^(1/2),
    A_n=(mean_u ||H_u||^2)^(1/2).

No separation, symmetry, Xi realization or sign hypothesis is added.

## Conclusion

The full response, including every spatial mode and signed cross term,
has the exact formulas (v=s exp(-i psi))

    H_u k_(s,psi)(zeta)
      =sqrt(1-s^2)*sum_a d_a(u)/[(1-v*alpha_a)*(zeta-alpha_a)],       (1)
    ||H_u k_(s,psi)||_2^2
      =(1-s^2)*sum_(a,b) d_a(u)*conjugate(d_b(u))
        /[(1-v*alpha_a)*(1-conjugate(v*alpha_b))
                                      *(1-alpha_a*conjugate(alpha_b))]. (2)

If q_u=sum_(k>=0)c_k(u) zeta^(-k-1), then

    mean_psi ||H_u k_(s,psi)||_2^2
      =sum_(k>=0) (1-s^(2*k+2))*|c_k(u)|^2.                        (3)

In particular

    sqrt(2*n-1)/n * Q_n <= T_n <= sqrt(2*n-1)*Q_n,
    T_n <= A_n.                                                   (4)

Thus optimized kernels at this radius and the complete constant-input
response Q_n have the same exponential rate, with a quantified
polynomial comparison. For every sequence of admissible families,

    log(sqrt(2*n-1)/n)/n
       <= log(T_n/Q_n)/n <= log(sqrt(2*n-1))/n -> 0.                (5)

The left endpoint tends to zero as well. No estimate on Q_n at rate
1/32 is established. Polynomial factors matter at that exact rate:
(4) alone neither proves nor refutes T_n>=c exp(-n/32), and an upper
bound for T_n would not be an upper bound for A_n. This is a
specialization of standard Hardy/Fourier identities, not a claimed
new mathematical mechanism, a solution of the angular detector, or
progress beyond the checked literature. A separate audit is outstanding.

## Proof

### Source scope and purpose

Reuse the unchanged invocation-start
[angular EXPLORE assessment](../drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md),
which covers analytic inputs and Fourier/coefficient analysis of this
family. C645g supplies the normalization and C645n the finite analytic
input projection identity. The standard operator convention is
L. Baratchart, S. Chevillard and T. Qian, *Minimax principle and lower
bounds in H2-rational approximation*, J. Approx. Theory 206 (2016),
17--47, preprint v2, 24 March 2015,
[Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
Use scalar Fourier Parseval from A. Levitt, *Analyse de Fourier et
applications*, [author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
version retrieved 2 November 2026, Theorem 1.3/Exercise 1.2 and
Theorem 1.11/Corollary 1.12, printed pp.6,8 (PDF pp.12,14).
These primary statements were inspected in the reused assessment.
The normalized circle exponentials have norm one. No Parseval identity
for an operator norm, Nehari reproof, or general reproducing-kernel
thesis is used. The calculation below is necessary to determine what
this nominated kernel test could improve over the complete symbol.

### Well-defined response and complete finite sum

Put rho=(R-eta)/R=273/275<1. All |alpha_a|<=rho. The grid zeros
have modulus <1<|a|, and the factor denominators do not vanish in
|v|<=R because R^2-t_j*R>0. For each fixed family d_a(u) is continuous
and bounded on |u|=1. Consequently, for some finite C depending on the
family,

    c_k(u)=sum_a d_a(u)*alpha_a^k,  |c_k(u)|<=C*rho^k.             (6)

This supplies an absolute uniform majorant in both angular variables
for all series below. No constant uniform in n or Z is claimed here.

The geometric series for k_(s,psi) has squared norm
(1-s^2)*sum_(j>=0)s^(2j)=1. For fixed n its only pole is outside the
closed unit disk. C645n's projection identity therefore applies:

    P_-[f(zeta)/(zeta-alpha)]=f(alpha)/(zeta-alpha).

It gives (1). Expanding its exterior kernels and applying scalar
Parseval gives (2), since

    sum_(l>=0) alpha_a^l*conjugate(alpha_b)^l
       =1/(1-alpha_a*conjugate(alpha_b)).

All denominators in (1)--(2) are nonzero; in particular
|1-v*alpha_a|>=1-s*rho>0 and
|1-alpha_a*conjugate(alpha_b)|>=1-rho^2>0. The finite double sum
may have complex summands, although its total is real and nonnegative.
No cross term is removed.

### Shift identity and the polynomial upper bound

Identify H^2_- with square-summable coefficient sequences
(c_0,c_1,...). The backward shift L(c_0,c_1,...)=(c_1,c_2,...)
is a contraction. Multiplication by a nonnegative spatial monomial
followed by P_- shifts the coefficient sequence backwards. Hence the
sequence h of H_u k_(s,psi) is

    h=sqrt(1-s^2)*sum_(j>=0) v^j L^j c,
    (I-v L)h=sqrt(1-s^2)*c.                                  (7)

The first series converges in the sequence norm, since s<1 and L
is a contraction. It agrees termwise with (1), either by (6) or by
boundedness of multiplication by q_u and of P_-. The triangle
inequality in (7) proves, for every psi,

    sqrt((1-s)/(1+s))*||q_u||_2
       <= ||H_u k_(s,psi)||_2
       <= sqrt((1+s)/(1-s))*||q_u||_2.                       (8)

The left inequality follows from
sqrt(1-s^2)||c||<=||h||+s||Lh||<=(1+s)||h||;
the right follows by summing the norm-convergent geometric series.
In particular the right constant is sqrt(2n-1).

### Kernel-angle average and the improved lower bound

For output coordinate l, (7) gives

    h_l=sqrt(1-s^2)*sum_(j>=0) s^j exp(-i*j*psi)c_(l+j).

Apply scalar Parseval in psi at each l and sum the nonnegative
terms. Convergence follows also from (6); thus either absolute
convergence or monotone convergence of the nonnegative sums justifies
every interchange. With k=l+j the result is

    mean_psi sum_l |h_l|^2
      =(1-s^2)*sum_(l,j>=0)s^(2j)|c_(l+j)|^2
      =sum_(k>=0)(1-s^(2k+2))*|c_k|^2,

which is (3). Its weights lie between 1-s^2 and 1. A supremum is at
least the mean, so

    sup_psi ||H_u k_(s,psi)||_2 >=sqrt(1-s^2)*||q_u||_2.

Together with (8) and 1-s^2=(2n-1)/n^2 this proves the first part
of (4) after angular integration. Every kernel has norm one, proving
T_n<=A_n. Formula (2) shows joint continuity in u,psi on the compact
two-torus. The supremum in psi is attained and continuous in u, so
no measurability or optimizing-input assumption is hidden in T_n.

Finally q_u is not zero: its distinct simple poles have nonzero
residues. Thus Q_n>0 and (4) gives T_n>0. Taking logarithms proves
(5). Its upper and lower bounds are O(log(n)/n), uniformly over
all the stated families. An exponential margin would survive these
factors, whereas an exact-threshold constant need not.

## Mathlib

Full matching coverage has not been checked; no absence claim is made.
The argument specializes scalar Fourier Parseval, geometric series,
contractive shifts and finite rational projection. It does not rely
on a Mathlib theorem about the largest Hankel norm or assert an
unevaluated reproducing-kernel equivalence for that norm.
