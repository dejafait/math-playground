# Lemma 956: generic strip hypotheses do not give Jensen-disk-free endpoints

## Hypotheses

Put c=cosh(2π)>1 and define the entire function

f(z)=(c+cos(8πz))/(c+1).

For a real entire function g, let J(g) be the union, over its nonreal
zeros ρ, of the closed disks {z: |z-Re ρ|≤|Im ρ|}. This is Kim's
Jensen-disk convention: Young-One Kim, *Critical points of real entire
functions and a conjecture of Pólya*, Proc. Amer. Math. Soc. **124**(3)
(1996), 819–830, definitions pp819–820 and Theorem1 p821,
[DOI](https://doi.org/10.1090/S0002-9939-96-03083-3),
[published PDF mirror](https://scispace.com/pdf/critical-points-of-real-entire-functions-and-a-conjecture-of-3sul01urof.pdf).

## Conclusion

The function f is nonconstant, even, real entire, has order1 and genus
at most1, and satisfies f(0)=1. Its complete zero set is

ρ_k^±=(2k+1)/8 ± i/4,  k∈ℤ,

with every zero simple. In particular every zero lies in |Im z|<1/2.
Nevertheless ℝ⊂J(f), with every real point strictly inside a disk.
Thus the listed symmetry, normalization, genus and strict-strip
hypotheses do not guarantee even one real point outside J(f), let alone
arbitrarily large such points in either direction.

## Proof

**Elementary inputs and scope.** Use the complex exponential definitions
of sine and cosine and the exponential formula for cosh; see
[NIST DLMF §4.14, formulas4.14.1–3](https://dlmf.nist.gov/4.14).
The zero calculation reuses L052's exponential-quadratic method, but
L052's particular parameter conclusion is not applied to these different
parameters. We write out the specialization because disk coverage,
rather than the existence of nonreal strip zeros, is the property being
tested. Kim's count theorem is not reproved or applied to this model.

The cosine formula makes f entire, f(-z)=f(z), and
f(conjugate z)=conjugate f(z). The denominator is positive and f(0)=1.
Moreover f''(0)=-(8π)²/(c+1)≠0, so f is nonconstant. On the real axis
f(x)≥(c-1)/(c+1)>0; hence no real zeros require a separate convention.

**Complete zeros and multiplicities.** Set w=exp(i8πz), which is never
zero. Then f(z)=0 if and only if

w²+2cw+1=0.

Since c=(exp(2π)+exp(-2π))/2, the two distinct roots of this quadratic
are -exp(2π) and -exp(-2π). Write z=x+iy. The modulus and argument of
w=exp(-8πy)exp(i8πx) show that these are attained exactly when

x=(2k+1)/8,  y=±1/4,  k∈ℤ.

Both signs occur, and these exhaust the preimages of the two quadratic
roots. Thus the displayed zero set is complete. At any such zero,
cos(8πz)=-c and the complex identity sin²u+cos²u=1 gives
sin²(8πz)=1-c²≠0. Therefore
f'(z)=-8πsin(8πz)/(c+1)≠0, proving simplicity.

**Order and genus.** For |z|≤r the exponential formula gives
|cos(8πz)|≤exp(8π|Im z|)≤exp(8πr). Consequently

M_f(r):=max_{|z|≤r}|f(z)|
 ≤(c+exp(8πr))/(c+1)≤exp(8πr).

Conversely f(ir)=(c+cosh(8πr))/(c+1) is positive and at least
exp(8πr)/(2(c+1)). Hence log M_f(r)=8πr+O(1) as r→∞, so the order
limsup log log M_f(r)/log r is exactly1. Invoke the standard named
**Hadamard factorization theorem, finite-order form**: a nonzero entire
function of order1 admits canonical factors of genus at most1 and an
exponential of a polynomial of degree at most1. A direct reference is
Yum-Tong Siu, *Weierstrass and Hadamard Factorization of Entire Functions*,
Harvard Math213a, Fall2024, named Hadamard theorem and the definition of
genus, pp4–5,
[author-hosted notes](https://people.math.harvard.edu/~siu/math213a/weierstrass_and_hadamard_factorization_of_entire_function.pdf).
The genus definition includes the degree of the exponential polynomial.
This theorem does not
assume real zeros. Its hypotheses hold by the just-proved growth and
f(0)=1; it proves genus≤1, including the exponential factor. This is
the same standard theorem used in L024, not an application of L024's
Xi-specific conclusion. No assertion about Xi or any real-zero
factorization is used. Since f is real entire, it also belongs to Kim's
genus1* class with Gaussian exponent α=0, should that class be required.

**Exact disk coverage.** The conjugate pair ρ_k^± gives the same disk

D_k={z: |z-(2k+1)/8|≤1/4}.

There are no other disks because the zero list is complete. Given any
x∈ℝ, choose k=floor(4x). Then k/4≤x<(k+1)/4, while the center of D_k
is k/4+1/8. It follows that

|x-(2k+1)/8|≤1/8<1/4.

Thus x is strictly inside D_k, with at least1/8 of radial clearance.
This proves ℝ⊂J(f), for both tails and all intervening points, without
a numerical plot, truncation or limiting disk argument. ∎

**Qualifications.** This is a generic-model obstruction and an elementary
specialization of known zero algebra and factorization, not a claim of
novelty or a result about actual Xi. No theta-kernel representation,
zeta-like zero density, actual-Xi endpoint failure, critical-zero
estimate, all-degree mixed sign, or RH conclusion follows. The
counterexample rejects only deduction of Kim's endpoint premise from
the hypotheses stated here. It leaves actual-Xi-specific endpoint
arguments and other boundary identities open.

**Critical replay, 9 November 2026, step118.** All load-bearing checks
pass. The substitution w is never zero, and the two distinct quadratic
roots have exactly the displayed logarithmic preimages; there is no
omitted real zero or zero at the origin. The nonzero derivative checks
the multiplicity of every preimage, independently of that enumeration.
The bounds on M_f hold for all r≥0 and imply, for large r,
8πr-log(2(c+1))≤log M_f(r)≤8πr. Thus the finite-order theorem applies
with order exactly1; it bounds both canonical-factor genus and the
exponential polynomial's degree. No real-zero assumption is used.
The floor choice works for negative as well as positive x, including
cell boundaries; the distance is at most1/8, strictly below the disk
radius1/4. The clearance is uniform on the entire real axis, so neither
closure of an infinite union nor an endpoint limit is being assumed.
L052's parameter-specific conclusion, L024's Xi product and L057's
finite-Hankel result are not premises. This replay confirms the generic
countercertificate without extending its hypotheses or its conclusion.

## Mathlib

Full matching coverage has not been checked and is unknown. No formal
verification is claimed. Elementary exponential/trigonometric identities
and Hadamard factorization are supporting inputs, not an identified
formal theorem for this complete disk certificate. Reference:
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
