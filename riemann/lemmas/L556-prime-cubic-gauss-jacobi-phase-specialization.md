# L556 — Prime cubic Gauss–Jacobi phase specialization

## Hypotheses

Let O=Z[omega], omega=exp(2pi i/3), lambda=1+2omega=i sqrt(3),
and F=Q(omega). Fix a finite set S of prime ideals containing those
above 6. Let p be the generator equal to 1 modulo 3 of a prime ideal
outside S, and put P=N(p)=|p|^2 and alpha(p)=p/|p|. Both residue
degrees are allowed. On k=O/(p), define chi_p on units as the unique
sixth root of unity reducing to x^((P-1)/6), and extend all its powers
by zero at zero. Put rho=chi_p^2. Define

\[
 e(z)=\exp(2\pi i\operatorname{Tr}_{F/\mathbb Q}(z/\lambda)),
 \quad\check e(z)=\exp(2\pi i(z+\bar z)),\quad
 \psi(x)=e(x/p),
\]
\[
 \tau_\psi(A)=\sum_{x\in k}A(x)\psi(x),\qquad
 \gamma_2(p)=P^{-1/2}\tau_\psi(\rho),\qquad
 J(\rho,\rho)=\sum_{x\in k}\rho(x)\rho(1-x).
\]

Import the unconditional finite identity of Dunn–Radziwill v3,
(1.7)–(1.8), equivalently (2.1)–(2.2), with its Euler cubic-symbol
orientation. No prime-average theorem from that paper is assumed.

## Conclusion

For every such p,

\[
 J(\rho,\rho)=-p,\qquad
 \gamma_2(p)^3=-\alpha(p),\qquad |\gamma_2(p)|=1.       \tag{1}
\]

In particular an inert rational prime ell>3 has primary generator
p=-ell, P=ell^2, J=ell and gamma_2(p)^3=1. For split primes the
Jacobi sum is -p, not an unspecified associate or its conjugate.
This checks exactly the prime cubic phase used among L548's retained
finite Gauss inputs. It does not select an individual cube root or
prove the other prime Gauss identities, composite propagation,
coefficient estimates, uniform arithmetic closure or Xi positivity.
The result is a specialization of known mathematics, not a new identity.

## Proof

### Precise imports and reason for the application audit

Dunn and Radziwill, *Bias in cubic Gauss sums: Patterson's conjecture*,
Annals of Mathematics 200 (2024), no. 3, 967–1057,
[arXiv:2109.07463v3, 14 May 2024, Section 1.2 and Section 2](https://arxiv.org/html/2109.07463v3#S2),
defines the Euler-oriented cubic character and the normalized sum

\[
 \widetilde g(c)=|c|^{-1}\sum_{x\bmod c}(x/c)_3\check e(x/c),
 \quad \widetilde g(c)^3=\mu(c)c/|c|.                    \tag{2}
\]

We use (2) only for the primary prime c=p, with mu(p)=-1.
Its domain includes inert primes; the splitting discussion immediately
before (2.1) distinguishes their norm ell^2 from split norm ell.
These finite identities have no GRH premise. Hasse 1950, pp. 443–445,
is their cited upstream reference, not a separately inspected input.

Keith Conrad, *Gauss and Jacobi sums on finite fields and Z/mZ*,
[author's PDF, Definition 2.1, Theorems 2.2(2), 2.4, equation (2.2),
and Corollary 2.5, pp. 1–4](https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf),
provides, for the canonical finite-field trace additive character,

\[
 |G(A)|=\sqrt P,\quad G(A)G(\bar A)=A(-1)P,
 \quad G(A)G(B)=J(A,B)G(AB).                            \tag{3}
\]

The first two require A nonprincipal; the last requires AB
nonprincipal. All characters are zero at zero. The extension to our
psi is checked below rather than assumed from matching notation.

The claim under audit is OpenAI, *The Quasi-Riemann Hypothesis*,
30 September 2026,
[pinned commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
`lem:prime-gauss-identities`, first identity; conventions are lines
557–591 and the complete proof is 713–769. That claimed identity
is not a premise. The published stronger formula (2) avoids redoing
standard cubic theory. Checking the changed additive character and
exact unit is necessary for the locally retained input.

### Field, character and additive normalization

Since the residue characteristic is neither 2 nor 3, the six roots
of unity remain distinct modulo p. Thus 6 divides P-1. The cyclicity
of k^* and the Euler definition show rho has exact order three,
and rho^2=bar(rho) is also nonprincipal. The Euler exponent for rho
is (P-1)/3, agreeing with DR, with no conjugation. Although DR first
introduces the symbol on primary numerators, its Euler rule extends
to all nonzero residue classes: for any x not divisible by p, CRT
chooses a representative x'=x modulo p and x'=1 modulo 3, since
(p,3)=1. Thus its sum and ours use the same character on k.
Also rho(-1)=1, because -1=(-1)^3.

For y=a+b omega with real a,b, direct evaluation gives

\[
 \operatorname{Tr}(y/\lambda)=b,\qquad
 \operatorname{Tr}(\omega y/\lambda)=a-b.              \tag{4}
\]

Consequently e is one on O and the annihilator of O under
(x,y) -> e(xy) is precisely O. Thus psi is well defined modulo p.
If psi were identically one, e(x/p)=1 for all x in O would imply
1/p in O by (4), contradicting that p is a nonunit. This proves
nontriviality in both residue degrees.

To apply (3) explicitly, write P=ell^f with f=1 or 2. An additive
character of k has values among the ell-th roots of unity and hence
corresponds to an F_ell-linear functional. The trace pairing is
nondegenerate here: for b!=0, taking x=b^(-1) gives
Tr_(k/F_ell)(bx)=f!=0 in F_ell. Its map from b to linear functionals
is injective between vector spaces of equal dimension, hence onto.
There is therefore b!=0 such that psi(x)=exp(2pi i Tr_(k/F_ell)(bx)/ell).
Substitution y=bx yields tau_psi(A)=A(b)^(-1)G(A).
The factors cancel in the product and Gauss–Jacobi identities in
(3), and have modulus one. Hence (3) holds for psi, with every
nonprincipal hypothesis verified for rho and rho^2. In particular

\[
 \tau_\psi(\rho)^2=J(\rho,\rho)\tau_\psi(\rho^2),
 \quad\tau_\psi(\rho)\tau_\psi(\rho^2)=P,
 \quad\tau_\psi(\rho)^3=PJ(\rho,\rho).                 \tag{5}
\]

### Conversion of the published sum and the exact unit

The identity check-e(z)=e(lambda z) is literal, not a convention
about finite-field traces. Since lambda is invertible modulo p,
substitution y=lambda x in the finite sum gives

\[
 \widetilde g(p)
  =P^{-1/2}\sum_x\rho(x)e(\lambda x/p)
  =\rho(\lambda)^{-1}\gamma_2(p).                       \tag{6}
\]

Here rho(lambda)^3=1. Cubing (6) and applying (2) proves the second
identity of (1). Equation (5), with |p|=sqrt(P), now gives

\[
 J(\rho,\rho)=\frac{P^{3/2}}P\gamma_2(p)^3
            =-\sqrt P\,\frac p{|p|}=-p.                \tag{7}
\]

The modulus assertion follows from (3). No estimate or limiting
argument enters (6)–(7).

For a separate check of the primary-sign convention at split primes,
Jeremy Booher, *The 2011 T-shirt: Cubic Reciprocity*, 20 August 2011,
[Definition 2, Theorem 13 and Proposition 14, pp. 1, 4–5](https://www.math.canterbury.ac.nz/~j.booher/expos/cubic_rec_promys.pdf),
uses pi=2 modulo 3 and states J(chi_pi,chi_pi)=pi. Set pi=-p.
The ideal, residue field and Euler character are unchanged, so it gives
exactly (7). This split-prime theorem is not applied to inert primes.
For inert ell=2 modulo 3, the unique primary generator is -ell:
-ell=1 modulo 3, and no other unit preserves that residue. Formula
(7) gives J=ell and -alpha(-ell)=1, as asserted. Thus neither case
loses a sign, unit or conjugation.

This also resolves the unit issue in the pinned proof: its candidate
associate up is exactly -p, agreeing with its congruence J=-1 modulo
3 and p=1 modulo 3. The verification rests on the precise published
finite input (2); it is not an independent audit of Hasse's proof or
of the external zero-free-half-plane argument. The other retained
inputs of L546/L548 remain retained. No local lemma input is used.

## Mathlib

No Lean verification was run. The saved assessment inspected
[JacobiSum/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/JacobiSum/Basic.lean):
`jacobiSum_mul_nontrivial` supports the Gauss–Jacobi identity for an
arbitrary additive character over a finite field into an integral
domain, requiring the product character nontrivial.
[GaussSum.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/GaussSum.lean)
contains `gaussSum_mulShift_eq` and
`gaussSum_mul_gaussSum_eq_card`, supporting the character shift and
product formula, the latter requiring a nonprincipal multiplicative
character and primitive additive character. Nontrivial additive
characters over a field are primitive. These are supporting results;
no full matching Eisenstein-unit evaluation was identified in those
inspected sources. Coverage elsewhere is not checked.
