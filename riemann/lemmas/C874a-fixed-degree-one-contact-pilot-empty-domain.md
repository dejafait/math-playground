# Corollary 874a: the fixed degree-one density-dual pilot has an empty contact domain

## Hypotheses

Use the exact theta kernel and heat family of L019/L058,

    F(lambda,z) = integral_0^infinity exp(lambda u^2) K(u) cos(zu) du,
    g_lambda(z) = F(lambda,z)/F(lambda,0),

and L874's normalized local logarithm and matrix

    log g_lambda(z) = -sum_(k>=1) S_k(lambda) z^(2k)/k,
    H1(lambda) = [[S2,S3],[S3,S4]].

Assume 1/4<=lambda<=1/2. The fixed pilot seeks a single tuple
(a0,...,a4,alpha,beta) in [-16,16]^7 for

    P(u) = sum_(j=0)^4 a_j u^(2j+1),
    Q(u) = u^2 R(u)+P'(u)+(2lambda u+K'(u)/K(u))P(u)
                         +alpha R(u)+beta uR'(u),

where R is exactly L874's d=1 response. Its contact domain additionally
requires c0^2+c1^2=1, c1!=0, H1 positive semidefinite and H1 c=0,
with both null rows retained and no exclusion of S2=0 in advance.

## Conclusion

H1(lambda) is strictly positive definite throughout the specified band.
Consequently the pilot's actual contact domain is empty. Its statement
Q(u)<=0 for every u>=0 at every such contact is vacuously true for every
tuple in the coefficient box, and cannot distinguish the tuples.

This is a rigorous obstruction to using this fixed pilot as a
nonvacuous boundary-sign test, not infeasibility of its coefficient
class. No pointwise residual inequality at a noncontact, contact flux
sign, contact below the band, new real-zero theorem or RH result is
claimed. The proof is a specialization of known inputs, not a new
positivity mechanism. Its independent audit remains pending.

## Proof

### The density correction is valid, but supplies no sign

The known input is C. Ley and Y. Swan, *Stein's density approach and
information inequalities*, Electron. Commun. Probab. **18** (2013),
paper 7, Definition 2.1 and Theorem 2.2, pp.2–3,
[final journal paper](https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/2578/2199.pdf),
DOI 10.1214/ECP.v18-2578. Only its forward density identity is used:
the expectation of (Pp)'/p vanishes when the endpoint products vanish
and the derivative is integrable. Its primary hypotheses and both
proof directions were already inspected in
`drafts/literature/2026-11-09-contact-polynomial-dual-discovery.md`.
The following checks specialize that known rule, rather than reprove
a general Stein theorem.

Here p(u)=exp(lambda u^2)K(u)/F(lambda,0) is positive, differentiable
and normalized on (0,infinity). The score is exactly

    p'(u)/p(u) = 2lambda u+K'(u)/K(u).

The positive-tilt term is retained. L058 and L874 give finite constants
C0,C1 with

    K(u) <= C0 exp(9u/2-pi exp(2u)),
    |K'(u)| <= C1 exp(13u/2-pi exp(2u))       (u>=0).

After multiplication by exp(lambda u^2), every polynomial multiple
of either bound is integrable. Indeed lambda<=1/2, and the negative
exp(2u) term eventually dominates any quadratic and linear exponent
and every power of u. At zero all products are continuous and finite.
It follows that (Pp)' is absolutely integrable, since its absolute
value is bounded by the sum of the three integrable terms obtained
from |P'|K, 2|lambda|u|P|K and |P||K'|. Also P(0)=0, and Pp tends
to zero at infinity by the same bounds. Both endpoint products vanish.
Thus the cited rule gives

    E[P'+(2lambda u+K'/K)P] = 0.

The apparent division by K is harmless here: in the absolute score
integral it cancels against the density, leaving |K'|. All the other
terms of Q are polynomial and absolutely integrable. At a hypothetical
contact L874 would additionally give E R=E[uR']=0 and

    E Q = E[u^2 R] = c^T H1'(lambda)c.

This verifies the interface of the proposed test. It supplies no
pointwise sign. The contact hypothesis itself fails in the fixed band,
as shown next; no coefficients or compact-interior/tail sign for Q
need to be manufactured after that failure is established.

### The unchanged band lies in a known all-real-zero regime

Import the following already assessed primary statements. C. M. Newman,
*Fourier Transforms with Only Real Zeros*, Proc. AMS **61** (1976),
245–251, Theorem 3, p.247,
[DOI](https://doi.org/10.1090/S0002-9939-1976-0434982-5), gives the
transition theorem. We use its exact modern primary restatement in
D. H. J. Polymath, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de Bruijn–Newman
constant*, Research in the Mathematical Sciences **6** (2019), article
31, [arXiv:1904.12438v2, 4 August 2019](https://arxiv.org/html/1904.12438v2):
the introduction, paragraph after (4), states a finite real Lambda with
all zeros of H_t real if and only if t>=Lambda; Theorem 1.1 states
unconditionally Lambda<=0.22=11/50. These are the unchanged statements
already inspected in
`drafts/literature/2026-10-30-global-transition-activation-coverage.md`.
Their original proofs and numerical verifications are accepted by
citation, not independently replayed here. No conditional improvement,
RH premise or assertion of simplicity is used.

L488 equation (11) supplies the exact normalization

    F(lambda,z) = 8 H_(4lambda)(2z).

Its proof uses K(2u)=4 Phi(u) and substitution in absolutely convergent
integrals, so the identity holds for every real lambda. L488's separate
tail theorem has a restricted time range; that range is not a
restriction on this identity, and that tail conclusion is not used.
The nonzero factor 8 and invertible real spatial scaling preserve the
reality of every zero. On the fixed pilot band,

    1 <= 4lambda <= 2,       1 > 11/50 >= Lambda.

Hence every zero of every slice in the band is real. This is an
unconditional known real-zero input at positive time; it says nothing
here about the undeformed slice lambda=0. No part of C489a's
conditional finite-collision conclusion is needed.

### Strictness of the actual degree-one matrix

Fix one lambda in the band. L058 gives F(lambda,0)>0, and L063 supplies
order at most one and the paired product

    g_lambda(z) = product_j (1-z^2/rho_j^2),
    sum_j |rho_j|^(-2) < infinity.

All zeros are now real and nonzero, so choose rho_j>0, with
multiplicity, from each pair. There are infinitely many distinct
positive zeros. To check this rather than assume it, L058's derivative
formula and K>0 give, for every integer n>=0,

    [z^(2n)] F(lambda,z)
      = (-1)^n/(2n)! integral_0^infinity
                         u^(2n) exp(lambda u^2) K(u) du != 0.

Thus F(lambda,.) is not a polynomial. A finite zero set would make
L063's paired product a polynomial, a contradiction. A nonzero entire
function has finite multiplicity at each zero, so the infinite zero
set also has infinitely many distinct positive representatives.
This is the same elementary positive-atomic Gram argument used for
L056's different comparison kernel; its application is written out
because L056's kernel-specific hypotheses cannot be assumed here.

Put x_j=rho_j^(-2)>0 and B=sum_j x_j<infinity. Choose a positive r
with r^2 B<1/2. For |z|<=r, every |z|^2 x_j<1/2 and

    sum_j sum_(k>=1) |z|^(2k) x_j^k/k
       <= 2|z|^2 sum_j x_j < infinity.

The logarithms of the product therefore sum absolutely and uniformly
on this disk. They vanish at zero, so their sum is the same normalized
logarithm as in L874. Coefficient extraction is justified by the
displayed normal convergence, and gives, in particular,

    S_k(lambda) = sum_j x_j^k,                 k=2,3,4.

For any nonzero real c=(c0,c1), finite expansion now yields

    c^T H1(lambda)c = sum_j x_j^2(c0+c1 x_j)^2 > 0.

The series converges: 0<x_j<=B, the linear polynomial is bounded on
[0,B], and sum_j x_j^2<=B sum_j x_j<infinity. Every summand is
nonnegative. A nonzero linear polynomial has at most one distinct
root, whereas the x_j have infinitely many distinct positive values,
so at least one summand is strictly positive. Repeated zeros cause
only repeated positive terms and do not affect this argument.

Consequently H1 is positive definite at each lambda in the entire
closed band, with no uniform eigenvalue lower bound claimed or needed.
In particular S2>0 there; the S2=0 case was not removed by dividing
by S2 but ruled out by the actual-law proof. A nonzero null vector
would give c^T H1 c=0, contradicting strict positivity. This proves
emptiness for both null rows together, and in fact for every nonzero
c whether or not c1 vanishes.

### Consequence for the bounded attempt

The approved pilot has no actual pair (lambda,c) on which its proposed
pointwise sign would be tested. Its universal contact-only predicate
is therefore true for every coefficient tuple, without establishing
any signed function Q on a nonempty domain. This is not a failed
sample, a generic-moment countermodel or infeasibility of polynomial
density corrections. The fixed pilot is retired as nondiscriminating;
neither its band nor its class is enlarged in this result. Lower
parameters, higher degrees, initialization, tangency and RH remain
separate questions. No complete solution or candidate is proposed.

## Mathlib

Full matching coverage and supporting formal coverage of this exact
specialization are unchecked; absence is not asserted. The imported
analytic ingredients are the named density identity, the precise
real-zero threshold and bound above, and L063's Hadamard product.
The remaining local argument is absolutely convergent coefficient
extraction and strict positivity of a positive-atomic Gram form.
Reference: https://leanprover-community.github.io/mathlib4_docs/.
