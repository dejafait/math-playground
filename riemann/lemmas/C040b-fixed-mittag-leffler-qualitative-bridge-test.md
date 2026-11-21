# Corollary 40b: the fixed Mittag-Leffler qualitative bridge test has positive H_3

## Hypotheses

Let E_a(z)=sum_(n>=0) z^n/Gamma(an+1), and fix
F(t)=E_(3/2)(-t^2). Define e_n=1/Gamma(3n/2+1) and
gamma_n=n!e_n, so F(t)=sum_(n>=0)(-1)^n gamma_n t^(2n)/n!.
For real sequences use Delta f(n)=f(n+1)-f(n).
Put G(w)=E_(3/2)(-w), and define S_k=-k[w^k]log G(w) at w=0.
The logarithm is the analytic germ with log G(0)=0. Define the single
real symmetric matrix H_3=(S_(i+j+2))_(0<=i,j<=3).

## Conclusion

1. gamma_0=1 and gamma_n>0. For every integer n>=0 and r>=2,
   (-1)^(r-1) Delta^r log(gamma_n)>0.
2. For every real c>0, (gamma_n^(-c))_(n>=0) is a normalized
   Stieltjes moment sequence, including noninteger c.
3. There is a nonnegative integrable density m on [0,infinity), of
   mass1 and with all nonnegative moments finite, such that
   F(t)=integral_0^infinity m(u)cos(tu)du for every real t.
4. H_3 is positive definite. Its exact LDL^T pivots d_0,...,d_3 obey
   d_0>1/10, d_1>1/10000, d_2>1/10^7, d_3>1/10^10.

This one prescribed matrix supplies no negative direction and closes
the proposed fixed discriminator. Neither positivity at all degrees
nor a counterexample to the qualitative generic implication is proved.
F has entire order4/3 in t, rather than Xi's order1. No actual theta
realization, quantitative Kawano bound, full continuous Mellin-ratio
premise, or assertion about zeta zeros is included.

## Proof

### Normalization and the imported moment laws

Write b_n=gamma_n^(-1)=Gamma(3n/2+1)/Gamma(n+1), K=3^(3/2)/2,
and x=n/2. Gamma duplication and triplication give

b_n=K^n [Gamma(x+2/3)/Gamma(2/3)]
 [Gamma(x+1/3)Gamma(1/2)/(Gamma(1/3)Gamma(x+1/2))].              (1)

Indeed triplication applied with z=x+1/3 cancels the Gamma(x+1)
factor from duplication with z=x+1/2. The remaining constant is
sqrt(3)/(2sqrt(pi)); evaluating at x=0 normalizes the two displayed
factors to1. The power is 3^(3n/2)/2^n=K^n. All gamma arguments
are positive, including at n=0. The identities are NIST DLMF
[5.5.5](https://dlmf.nist.gov/5.5#E5) and
[5.5.6](https://dlmf.nist.gov/5.5#E6); no pole is encountered.

Import Berg, *On powers of Stieltjes moment sequences, II*,
[arXiv:math/0412340v1](https://arxiv.org/pdf/math/0412340v1),
Theorems5.1 and5.2, printed14-15. These supply probability laws
whose Mellin transforms, for any c>0, are
[Gamma(a+z)/Gamma(a)]^c, a>0, and
[Gamma(a+z)Gamma(b)/(Gamma(a)Gamma(b+z))]^c, 0<a<b,
respectively, on Re(z)>-a. The positive-real branch is understood
for real z>-a. We use only this real domain, so there is no choice
of a complex power in the specialization.

Choose independent positive variables U_c,V_c from these laws with
a=2/3 in the gamma case and a=1/3,b=1/2 in the beta case.
Then X_c=K^c sqrt(U_c V_c) has
E(X_c^n)=b_n^c for every n>=0 by (1), because n/2>=0 lies in
both Mellin domains. Independence and finite positive moments justify
factorization, or equivalently Tonelli on the product law. Its
zeroth moment is1. At c=1 this is K sqrt(G B), with
G~Gamma(2/3,1) and B~Beta(1/3,1/6). This proves the second claim
and the coefficient normalization. It uses the imported gamma and
beta power laws, not closure under arbitrary moment-sequence quotients.

### All finite-difference orders, including n=0

Extend f(x)=log b_x to x>=0 using (1), with n replaced by x.
Differentiating twice gives

f''(x)=1/4 integral_0^infinity
 t exp(-xt/2) A(t)/(1-exp(-t)) dt,
A(t)=exp(-2t/3)+exp(-t/3)-exp(-t/2)>0.                       (2)

Here the trigamma integral follows by differentiating the digamma
integral [DLMF5.9.16](https://dlmf.nist.gov/5.9#E16) for positive
arguments. In the three terms their arguments are x/2+2/3,
x/2+1/3 and x/2+1/2. On any compact x interval in [0,infinity),
differentiation is dominated: near t=0 the second-derivative integrand
is bounded, and at infinity every derivative is bounded by a constant
times a polynomial in t times exp(-t/3). Higher derivatives obey
the same domination. Positivity in (2) is strict since
exp(-t/3)>exp(-t/2) and exp(-2t/3)>0 for every t>0.

For r>=2 apply the repeated fundamental theorem of calculus to
Delta^r f(n)=integral_[0,1]^r f^(r)(n+u_1+...+u_r) du.
Differentiation in (2) and Tonelli for the sign-adjusted positive
integrand give

(-1)^r Delta^r f(n)=integral_0^infinity
 exp(-nt/2)(1-exp(-t/2))^r A(t)/[t(1-exp(-t))] dt >0.        (3)

The integrand is O(t^(r-2)) near0 and O(exp(-t/3)/t) at
infinity for n>=0. Thus (3) is finite even at n=0 and is strictly
positive on t>0. Since log gamma_n=-f(n), (3) is exactly the first
claim. The geometric factor K^n contributes only an affine function
to f, annihilated by differences of order at least2.

### Positive cosine density with justified integration

Import Mainardi-Mura-Pagnini, *The M-Wright function in time-fractional
diffusion processes: a tutorial survey*,
[arXiv:1004.2950v1](https://arxiv.org/html/1004.2950v1),
Section4, (4.1)-(4.5) and (4.10)-(4.12). For 0<nu<1 its
M-Wright function M_nu(u) is nonnegative on [0,infinity) and has
moments integral u^q M_nu(u)du=Gamma(q+1)/Gamma(nu q+1)
for real q>-1. Take nu=3/4 and m=M_(3/4). The moment at q=0
is1 and all nonnegative moments are finite.

For any fixed real t, Tonelli applied to the nonnegative absolute
cosine-series terms gives

integral m(u) sum_(n>=0) |tu|^(2n)/(2n)! du
=sum_(n>=0) |t|^(2n)/Gamma(3n/2+1)<infinity.                 (4)

The final series converges for every t by Stirling's formula.
Consequently the cosine series can be integrated absolutely, giving
integral m(u)cos(tu)du=sum (-1)^n t^(2n)/Gamma(3n/2+1)=F(t).
This also justifies the source's cosine transform in the precise
specialization, without inferring an interchange from analyticity.
Stirling gives the entire order4/3 in t by the coefficient formula:
lim_(n->infinity) 2n log(2n)/log Gamma(3n/2+1)=4/3.
The zero odd coefficients do not affect that limsup.

### The single logarithmic matrix and its rational certificate

G is entire by the same Stirling estimate, G(0)=1, and hence it is
nonzero on a neighborhood of0 where its logarithmic germ exists.
Differentiate that germ: G'(w)=-G(w)sum_(k>=1)S_k w^(k-1).
Coefficient comparison gives, for k=1,...,8,

S_k=sum_(j=1)^(k-1)(-1)^(j-1)e_j S_(k-j)+(-1)^(k-1)k e_k.   (5)

This is the finite coefficient calculation used in L040, repeated
here for this independent germ rather than importing any actual-Xi
product or zero hypothesis. No interpretation as zero sums is needed.

The full reproducible certificate is `scripts/mittag-leffler/fixed-h3-779.json`;
run `python3 scripts/mittag-leffler/fixed-h3-779.py` from this notebook.
All inputs and arithmetic are rational intervals. Start from Machin's
identity pi=16 arctan(1/5)-4 arctan(1/239), enclosing the arctangents
by alternating partial sums with 60 and20 terms and their next terms.
Machin's identity itself follows from tan(2 arctan(1/5))=5/12,
tan(4 arctan(1/5))=120/119 and the tangent subtraction formula:
tan(4 arctan(1/5)-arctan(1/239))=1. This angle lies in(0,pi/2),
so it equals pi/4. The branch follows from arctan(1/5)<1/5 and
the strictly smaller arctan(1/239), using the same alternating bounds.

Integer square roots give enclosing rationals for sqrt(pi), whose
squares are checked against the entire pi interval. For even n,
e_n=1/(3n/2)!; for odd n put k=(3n+1)/2 and use
e_n=4^k k!/((2k)!sqrt(pi)). These enclose every e_0,...,e_8.
Apply (5) and assemble H_3. Every operation rounds its two endpoints
outward to the fixed rational grid10^(-60); floor and ceiling ensure
inclusion. No floating-point approximation is a proof input.

For completeness the elimination recurrence certified in the file is
l_jj=1,
d_j=h_jj-sum_(k<j) l_jk^2 d_k,
l_ij=(h_ij-sum_(k<j)l_ik l_jk d_k)/d_j, i>j.
Interval arithmetic contains the exact values inductively, retaining
repeated-variable dependence by inclusion rather than independence.
Every pivot interval is strictly positive, allowing the next division.
Their full rational lower endpoints exceed respectively
1/10,1/10000,1/10^7,1/10^10, by exact integer comparisons.
Therefore H_3=L diag(d_j)L^T is positive definite by invertibility
of the unit lower triangular L. Rounded displays of the pivots are
0.23255090877118,0.00133718538930,7.16515916489e-7,1.96381643834e-10;
the complete rational endpoints, not these displays, certify the signs.

The prescribed negative-direction goal failed: solving the leading
3-by-3 block and using one fixed rounding supplied the trial vector
(-674511/10^9,22193377/(5*10^8),-564535943/10^9,1), whose form is
strictly positive, approximately1.96381643835e-10. The certificate
retains that failure as well as the stronger positive-definiteness
test of this same matrix. An initial unrounded serialization exceeded
Python's digit-conversion limit; the rigorous fixed outward rounding
repaired storage without changing the mathematical test or precision
in a campaign. No other model, degree or adjacent matrix was tested.

### Scope of the imported coefficient comparison

Kawano, *Logarithmic Inequalities of Arbitrary Order for the Riemann
Xi Coefficients*, [Preprints.org202611.0383v1](https://www.preprints.org/manuscript/202611.0383),
Theorem1.1 and Corollary2.1, identifies the qualitative properties
being compared. Its proof and numerical certificates are not premises
here and have not been independently audited. The model satisfies
only the specified qualitative conclusions; no quantitative lower
bound or full continuous hypothesis from that paper is claimed.
The family already appears in Konstantopoulos-Patie-Sarkar,
Ann.Inst.Fourier74(2024),377-421,
[Section4.2.4, printed399](https://www.numdam.org/item/10.5802/aif.3600.pdf#page=24).
That source's nonreal-zero assertion is not used in this finite test.
This is a known-method specialization and a failed fixed discriminator,
not a claim of a new family, an all-degree result or a theorem about Xi.

## Mathlib

Full matching coverage has not been checked; availability is unknown.
The imported gamma/beta product-convolution laws, M-Wright theorem,
strict all-order specialization and exact matrix certificate are
justified above rather than attributed to Mathlib. Supporting matrix
notion: [Matrix.PosDef](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/PosDef.html#Matrix.PosDef).
No formal Lean verification or absence claim is made.
