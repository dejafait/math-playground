# L558 — Good-prime all-exponents finite Fourier formulas

## Hypotheses

Let O=Z[omega], omega=exp(2pi i/3), lambda=1+2omega, and
F=Q(omega). Let S contain the prime ideals above 6. Let p=1 modulo 3
generate a prime ideal outside S, and put k=O/(p) and P=N(p).
Both residue degrees are allowed. Write

\[
 e(z)=\exp(2\pi i\operatorname{Tr}_{F/\mathbb Q}(z/\lambda)),
 \qquad \psi(x)=e(x/p).
\]

Let H(x) on k^* be the unique sixth root of unity reducing to
x^((P-1)/6). For every integer j, define A_j(x)=H(x)^j on k^*
and A_j(0)=0. In particular A_0 is the unit indicator; no value of
0^0 is used. For j=0,...,5 and h in k define

\[
 C_{p,j}(h)=P^{-1}\sum_{x\in k}A_j(x)\psi(-hx),\qquad
 \tau_{p,j}^-=P^{-1/2}\sum_{x\in k}A_j(x)\psi(-x).
\]

Use L556 only for its proved field/additive normalization: psi is
well defined and nontrivial in both residue degrees. Its cubic Gauss
phase evaluation and its Dunn–Radziwill identity are not needed.

## Conclusion

For every j=0,...,5 and every h in k,

\[
 C_{p,j}(h)=
 \begin{cases}
 P^{-1/2}\tau_{p,j}^-H(h)^{-j},&j\ne0,\ h\ne0,\\
 0,&j\ne0,\ h=0,\\
 -P^{-1},&j=0,\ h\ne0,\\
 1-P^{-1},&j=0,\ h=0.
 \end{cases}                                                   \tag{1}
\]

The complete reconstruction, including zero frequency, is

\[
 A_j(x)=\sum_{h\in k}C_{p,j}(h)\psi(hx).                       \tag{2}
\]

These are exactly the good-prime formulas `eq:reflection-local-fourier`
retained in L546 Hypothesis 2. They also supply the one-prime values
retained in L547. This removes only that finite Fourier premise;
branch scalars, composite propagation, coefficient/support estimates,
arithmetic uniformity and signed-Xi transfer are separate. This is a
specialization of known finite Fourier mathematics, not a new identity.

## Proof

### Precise imports and applicability

Keith Conrad, *Characters of finite abelian groups (short version)*,
[author-hosted PDF](https://kconrad.math.uconn.edu/blurbs/grouptheory/charthyshort.pdf),
Theorem 4.1 and Corollary 4.2, p. 10, and (4.2)–(4.4), p. 11,
give character orthogonality and finite Fourier inversion: the sum
of a nonprincipal character is zero, the sum of the principal
character is the group cardinality, and the full dual has that
cardinality. These statements apply to any finite abelian group,
including (k,+) and k^*. No prime-size restriction is present.

Conrad, *Gauss and Jacobi sums on finite fields and Z/mZ*,
[author-hosted PDF](https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf),
Definition 2.1/Theorem 2.2, pp. 1–2, specify the zero extension even
for the principal character. Lemma 4.16, pp. 14–15, with the unit
substitution proof referred to Lemma 3.10, p. 6, gives Gauss scaling.
Its primitive-character version must not be applied to A_0. We use
only unit substitution for nonzero h and group orthogonality for
the zero and principal cases. Theorem 2.2's canonical additive
character is not assumed identical to psi.

The claim being audited is OpenAI, *The Quasi-Riemann Hypothesis*,
30 September 2026,
[pinned TeX, commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
definitions at lines 557–591 and 1688–1692, and the complete local
Fourier passage at 1881–1909. That assertion is not used as proof.
The independent standard statements above already cover the mechanism;
the following specialization checks its retained sign, inverse, zero
extension and P normalization. Reproving general Gauss theory or its
phase evaluations would add no needed input.

### Exact order and the full additive pairing

The characteristic ell of k is greater than three. The six roots of
unity in O remain distinct in k: reducing the factorization of X^6-1
gives six roots, and its derivative 6X^5 has no common root with it.
Thus reduction identifies the complex sixth roots bijectively with
the sixth roots in k. The standard cyclicity theorem for the
multiplicative group of a finite field gives a generator g of k^*.
Its power g^((P-1)/6) has order six. The Euler definition therefore
makes H a multiplicative character of exact order six. Each A_j
restricted to k^*, for j=1,...,5, is nonprincipal, including j=2,3,4.

By L556, psi is nontrivial for P=ell and P=ell^2. For nonzero h,
x -> hx permutes k, so x -> psi(hx) is nontrivial as well.
If psi(hx)=psi(h'x) for every x, nontriviality applied to h-h'
forces h=h'. We have P distinct additive characters. The cited
dual-cardinality theorem shows that these exhaust the additive dual.
This proves that the source pairing is complete also in residue
degree two, rather than presuming that the additive group is cyclic.

### Nonprincipal exponents

For h nonzero set y=hx in the defining sum. The substitution is
bijective, and A_j(h^(-1)y)=H(h)^(-j)A_j(y), also at y=0 since
both sides then vanish. Hence, for j=1,...,5,

\[
 C_{p,j}(h)
 =P^{-1}H(h)^{-j}\sum_y A_j(y)\psi(-y)
 =P^{-1/2}\tau_{p,j}^-H(h)^{-j}.
\]

The minus sign stays inside the base additive character psi(-y).
There is no additional H(-1) factor. The inverse arises from
x=h^(-1)y, not from a modulus calculation. For h=0 the additive
factor is one and multiplicative orthogonality gives
sum_(k^*) H(x)^j=0. The zero extension contributes nothing, proving
the first two cases of (1).

### Principal exponent and reconstruction

For j=0 and h nonzero, additive orthogonality gives
sum_(x in k) psi(-hx)=0. Its x=0 term is one, so summing only
over k^* gives -1. Dividing by P gives -P^(-1). For h=0 there
are P-1 unit terms, giving 1-P^(-1). In particular the principal
zero-frequency coefficient is not one. No nonprincipal or primitive
multiplicative-character theorem was applied in these two cases.

Finally all sums below are finite. For x in k,

\[
 \sum_h C_{p,j}(h)\psi(hx)
 =P^{-1}\sum_y A_j(y)\sum_h\psi(h(x-y))=A_j(x).
\]

The inner sum is P if x=y and zero otherwise by additive
orthogonality and the complete pairing just checked. This proves
(2), including x=0 and every frequency. The positive reconstruction
sign cancels the coefficient's negative sign. In the inert case
P=ell^2 and sqrt(P)=ell; the two factors in the nonzero case are
still P^(-1) and sqrt(P), not factors based on ell in place of P.
All six exponents and all four cases therefore pass the equality test.

## Mathlib

The ready assessment inspected official
[GaussSum.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/GaussSum.lean),
lines 63–76 and 102–133, master accessed 2026-10-31.
`gaussSum_mulShift_eq` gives inverse-character scaling for a unit
without a nonprincipal hypothesis; `gaussSum_one_right` gives zero
for nonprincipal multiplicative character and trivial additive
character; `gaussSum_one_left` gives -1 for principal multiplicative
character and nontrivial additive character over a finite field;
`gaussSum_one_one` gives the unit-group cardinality when both are
principal. The stated domain/codomain hypotheses hold for k and C.
[MulChar/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/MulChar/Basic.lean),
lines 64–68 and 94–107, uses zero on nonunits and the unit indicator
as its trivial character, matching A_0. These support all four cases.
A full matching Eisenstein-normalized assembly was not found in the
files checked; availability elsewhere was not checked. No Lean run
or new source inspection is claimed in this application audit.
