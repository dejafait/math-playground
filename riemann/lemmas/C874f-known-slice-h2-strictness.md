# Corollary 874f: strict H2 positivity at the known slice

## Hypotheses

Use the exact kernel K of L019, the entire family F of L058, and
L874's normalization. Fix lambda0=1/16 and write

    f(z)=F(lambda0,z),       g(z)=f(z)/f(0),
    log g(z)=-sum_(k>=1) S_k z^(2k)/k,
    H2=(S_(i+j+2))_(0<=i,j<=2).

The logarithm is the germ with value zero at zero. No RH, contact,
H3 positivity, simple-zero or auxiliary atomic-law premise is assumed.

## Conclusion

H2 is strictly positive definite. In particular there is no nonzero
real c with H2 c=0 at this slice, including vectors with c2=0.
The d=2 contact domain at lambda=1/16 used in the recent BPY/Poisson
proposals is therefore empty. This supplies no contact-flux sign on a
nonempty domain and no result below the known real-zero cutoff.

This is a checked specialization of known mathematics, not a new
real-rootedness or positivity mechanism. No explicit eigenvalue margin,
uniform parameter margin, continuation to zero or RH claim is made.

## Proof

### Published input and exact normalization

Import D. Platt and T. Trudgian, *The Riemann hypothesis is true up to
3 times 10^12*, Bull. London Math. Soc. **53** (2021), 792–797,
Section 3.4, Corollary 2: the de Bruijn–Newman constant satisfies
Lambda<=0.2=1/5. The primary version inspected is
[arXiv:2004.09765v1, 21 April 2020](https://arxiv.org/html/2004.09765v1).
Its supporting paragraph applies the finite-height theorem to the
Polymath conditional table. This published theorem, including its
rigorous computation, is imported; that computation is not replayed.

The transition statement and normalization are those in D. H. J.
Polymath, *Effective approximation of heat flow evolution of the
Riemann xi function, and a new upper bound for the de Bruijn–Newman
constant*, Res. Math. Sci. **6** (2019), article 31,
[arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2), (3)–(4)
and the following transition paragraph: all zeros of H_t are real
when t>=Lambda. L488(11) gives, with precisely that H_t,

    F(lambda,z)=8 H_(4lambda)(2z).

The identity follows from K(2u)=4 Phi(u) and an absolutely convergent
change of variables; it is not limited by the separate tail theorem
in L488. At lambda0, 4lambda0=1/4>1/5>=Lambda. The factor 8 and
the invertible real spatial scaling preserve reality and multiplicity
of zeros. Thus every zero of f is real. L058 gives f(0)>0.

### Deformed factorization; no hidden exponential factor

Apply the existing deformed product L063 at L=lambda0. Its full proof
has been checked for this use. In its growth bound, u^2<=2e^u and
completion of the square absorb L u^2 into half of pi e^(2u).
Substitution x=e^(2u) leaves the gamma-integral bound with
a=R/2+9/4 and m=ceil(a)<=R/2+13/4. Consequently the stated factorial
majorant gives log max_(|z|<=R)|f(z)|=O(R log R), which is order at
most one, not an assumption of finite exponential type.

The imported analytic theorem is the named Hadamard factorization
theorem in the order-at-most-one form; a precise source is I. Petrow,
*Introduction to Analytic Number Theory*, Theorems 7.5 and 7.7,
printed pp.57–58,
[2018 notes](https://www.homepages.ucl.ac.uk/~ucahpet/IANTnotes2018.pdf).
For an entire f of order at most one with f(0)!=0 it gives reciprocal-
square summability and f(z)=f(0)exp(bz) product_rho E1(z/rho),
where b=f'(0)/f(0) and E1(w)=(1-w)exp(w). This is a citation of
the theorem, not a reproof. L024 is its undeformed reference only;
the deformed growth hypothesis is supplied by L063.

Evenness from L058 gives b=0 and pairs opposite zeros with equal
multiplicity. The normally convergent genus-one logarithmic tails
permit their pairing, as checked in L063. Thus choose each positive
zero r_j once for its pair, repeated with its finite multiplicity, to get

    g(z)=product_j(1-z^2/r_j^2),       sum_j r_j^(-2)<infinity.   (1)

Order at most one excludes a quadratic exponential; evenness alone
would not do so. No sum of 1/rho is rearranged. Every zero is nonzero
and every positive representative belongs to (1); no finite census
or unbounded omitted-zero term is being substituted for this product.

### Infinitely many distinct support points

Define the probability density on the whole real line by

    q(u)=exp(u^2/16)K(|u|)/(2f(0)).

L019 and L058 show that q is nonnegative, integrable with integral one,
and its Fourier transform is g on the real axis. The named
Riemann–Lebesgue lemma for L1(R) gives g(x)->0 as |x|->infinity.
If f had only finitely many distinct zeros, each would have finite
multiplicity since f is a nonzero entire function. Formula (1), with
no exponential factor remaining, would make g a polynomial. No
nonzero polynomial tends to zero along the real axis, whereas g(0)=1.
This contradiction proves infinitely many distinct positive r_j.
The numbers t_j=r_j^(-2) therefore have infinitely many distinct
positive values. Repeated zeros simply repeat their values in sums.

### Coefficient matching and strict Taylor-Hankel positivity

Put B=sum_j t_j, so 0<B<infinity and 0<t_j<=B. Choose delta>0
with delta^2 B<=1/2. Uniformly on |z|<=delta,

    sum_j sum_(k>=1) |z|^(2k)t_j^k/k
        <=2 delta^2 sum_j t_j<infinity.                    (2)

The local logarithms of the factors in (1) consequently sum normally.
Their sum vanishes at zero and exponentiates to g, so it is exactly
L874's normalized logarithm. Absolute convergence permits exchanging
the two sums and Cauchy's coefficient formula gives

    S_k=sum_j t_j^k,            in particular k=2,...,6.    (3)

These sums are finite since sum_j t_j^k<=B^(k-1) sum_j t_j.
There is no factor 2 from the negative zeros: (1) already pairs them.
There is no factorial in S_k; the coefficient is -S_k/k by definition.

For a real c=(c0,c1,c2), set p(t)=c0+c1 t+c2 t^2. Finite expansion
using (3) gives the exact identity

    c^T H2 c=sum_j t_j^2 p(t_j)^2.                         (4)

The series is absolutely convergent: p is bounded on [0,B] and
sum_j t_j^2<=B^2. Each term is nonnegative. If c!=0, p is a nonzero
polynomial of degree at most two, hence has at most two distinct
real roots. The infinite distinct support proved above contains a
t_j with p(t_j)!=0, whose term in (4) is strictly positive. Thus
c^T H2 c>0 for every nonzero c, including the linear and constant
cases. This proves the claimed strictness and excludes H2 c=0.

No passage from strict distinct-node Loewner matrices to a confluent
limit is used. No zero simplicity, positive lower bound on the support,
identification with C874b's auxiliary atoms, or H3 hypothesis is needed.

### Scope of this audit and overlap

The ready assessment is
`drafts/literature/2026-11-21-known-regime-h2-strictness-audit-2144.md`.
C874a already uses the degree-one version of this Gram argument on
its different, higher-time band; it is a duplicate-method warning,
not an input asserting the present H2 conclusion. The new local work
checks the selected slice and exact Taylor indexing and strictness.

U. J. Choi, *RH-Conditional Positivity in a Theta-Kernel Langevin Model*,
[arXiv:2611.04359v1](https://arxiv.org/html/2611.04359v1),
Lemma 3.4, Theorem 4.1's final unconditional branch, (19) and the two
subsequent Hankel formulas cover the same product/moment method. Its
kernel is K/4, canceled by normalization, with a=lambda. Those passages
and their relevant proofs were inspected. This unreviewed preprint is
supporting coverage; the proof above rests on the published cutoff,
the classical theorems and the checked local applicability arguments.
Reproduction is justified by the exact H2 shift and the strictness
issue at confluent nodes. No advance beyond the known method is claimed.

The conceptual audit passes the stated fixed-slice claim. It supplies
no estimate for 0<=lambda<1/20, no boundary flux, no degree-uniform
continuation and no resolution of L030-L032/C032a. The previous score,
node-mass and Poisson stops remain intact. No numerical certificate
or mathematical script is required for this analytic specialization.

## Mathlib

Full matching coverage and formal coverage of this exact specialization
are unchecked; availability is unknown, not asserted absent. The
supporting inputs are Hadamard factorization, Riemann–Lebesgue, normal
convergence and finite polynomial root counting. No formal theorem is
claimed to verify their assembly here. Reference:
https://leanprover-community.github.io/mathlib4_docs/.
