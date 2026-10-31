# L557 — Prime sextic Gauss product specialization

## Hypotheses

Let O=Z[omega], omega=exp(2pi i/3), lambda=1+2omega=i sqrt(3).
Fix a finite set S of prime ideals containing those above 6. Let p=1
modulo 3 generate a prime ideal outside S, and put P=N(p)=|p|^2.
Both split and inert primes are included. On k=O/(p), define H=chi_p
by the sextic Euler rule: H(x) is the unique sixth root of unity
reducing to x^((P-1)/6) for x nonzero. Every power of H is zero at zero.
Use L556's field and additive-character normalization:

\[
 e(z)=\exp(2\pi i\operatorname{Tr}_{\mathbb Q(\omega)/\mathbb Q}(z/\lambda)),
 \quad\psi(x)=e(x/p),\quad
 \tau_j=\sum_{x\in k}H(x)^j\psi(x),\quad
 \gamma_j(p)=P^{-1/2}\tau_j\quad(1\le j\le5),
\]

where sqrt(P)>0. Import the finite-field mixed Jacobi identity of
Cohen Lemma 4.9 and the Gauss identities of Conrad stated below.
These are unconditional finite-field inputs. No theta or Xi positivity
hypothesis is made.

## Conclusion

For every such p,

\[
 \boxed{\gamma_1(p)\gamma_2(p)
   =\overline{\chi_p(4)}\,\gamma_3(p)\gamma_2(p)^3.}       \tag{1}
\]

The equality includes the exact complex phase and normalization in
both residue degrees. It reproduces the prime sextic input retained
in the L546/L548 setting; it does not discharge all of L546 Hypothesis 2.
Other finite Fourier formulas, composite propagation, coefficients,
arithmetic uniformity and Xi signs remain outside this conclusion.

## Proof

### Precise imported identities

Henri Cohen, *Computational Number Theory in Relation with L-Functions*,
[author-hosted course notes](https://www.math.u-bordeaux.fr/~cohen/rennes2.pdf),
Definitions 4.2, 4.3 and 4.5, printed pp. 22–24, and Lemma 4.9,
printed p. 26, state, for a finite field of odd cardinality, its
quadratic character eta, and a nonprincipal character A,

\[
 A(4)J(A,A)=J(A,\eta),\qquad
 J(A,B)=\sum_{x\in k}A(x)B(1-x).                        \tag{2}
\]

The inspected notes state this lemma as an exercise without a proof;
we import its theorem statement, not an independently verified proof.
Cohen's principal character is one at zero, while nonprincipal
characters are zero there. All characters used in (2) below are
nonprincipal, so that convention difference has no effect.

Keith Conrad, *Gauss and Jacobi sums on finite fields and Z/mZ*,
[author's PDF](https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf),
Theorem 2.2(2), Theorem 2.4 and equation (2.2), pp. 2–3, give

\[
 |G(A)|=\sqrt P,\qquad G(A)G(\overline A)=A(-1)P,
 \qquad G(A)G(B)=J(A,B)G(AB).                           \tag{3}
\]

The first two require A nonprincipal; the third requires AB
nonprincipal. Conrad uses the canonical finite-field trace additive
character and zero extensions. L556's normalization argument proves
that psi here is well defined and nontrivial, for both residue degrees,
and transports precisely these identities to tau_psi. In particular,
if psi(x)=exp(2pi i Tr_(k/F_ell)(b x)/ell), b nonzero, then

\[
 \tau_\psi(A)=A(b)^{-1}G(A).                            \tag{4}
\]

In the last identity of (3), the factors A(b)^(-1)B(b)^(-1)
and (AB)(b)^(-1) agree. In the inverse pair they multiply to one,
and in the modulus formula they have modulus one. Thus every use
of (3) below is valid for the actual psi. This uses only L556's
field/additive normalization argument, not its cubic-unit evaluation.

The claimed formula being audited is OpenAI, *The Quasi-Riemann
Hypothesis*, 30 September 2026,
[pinned TeX commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
`lem:prime-gauss-identities`, second identity, complete lemma/proof
lines 703–769. Its assertion is not a premise. Cohen (2), together
with Conrad (3), supplies the independent known identity; only its
application to the retained conventions is derived here. Reproving
mixed Jacobi or Hasse–Davenport theory is unnecessary.

### Character hypotheses and exact product

The residue characteristic is neither 2 nor 3, so the six roots of
unity remain distinct in k. Hence 6 divides P-1. Cyclicity of k^*
and the Euler definition imply that H has exact order six. Put
rho=H^2 and eta=H^3. Then rho has exact order three and eta is the
unique quadratic character. H, rho, eta and H^4 are all nonprincipal.
The products needed for Gauss–Jacobi are H*H=H^2 and H*eta=H^4,
which are nonprincipal as required. Moreover H^4=bar(rho) on units
and also at zero. The modulus identity in (3) proves all tau_j used
below are nonzero.

Apply (2) with A=H, and (3) to the two indicated pairs:

\[
 H(4)J(H,H)=J(H,\eta),\qquad
 \tau_1^2=J(H,H)\tau_2,\qquad
 \tau_1\tau_3=J(H,\eta)\tau_4.                         \tag{5}
\]

Eliminate the Jacobi sums, dividing only by nonzero tau_1, tau_2 and tau_4:

\[
 H(4)\frac{\tau_1^2}{\tau_2}
       =\frac{\tau_1\tau_3}{\tau_4},\qquad
 \tau_1\tau_4=H(4)^{-1}\tau_3\tau_2.                   \tag{6}
\]

Since rho(-1)=1 (its value has order dividing both two and three),
the inverse pair in (3) gives

\[
 \tau_2\tau_4=P.                                      \tag{7}
\]

Multiply (6) by tau_2 and use (7), then multiply by tau_2/P:

\[
 \tau_1 P=H(4)^{-1}\tau_3\tau_2^2,
 \qquad
 \tau_1\tau_2=H(4)^{-1}\frac{\tau_3\tau_2^3}{P}.         \tag{8}
\]

Divide (8) by P. Its left side is gamma_1 gamma_2. Its right side
is H(4)^(-1) gamma_3 gamma_2^3 because the four unnormalized Gauss
factors contribute P^2. Finally 4 is a unit in k and H(4) has modulus
one, so H(4)^(-1)=overline(H(4)), proving (1). No replacement of
algebraic products by absolute values enters the argument.

For split primes P=ell and every normalization above uses sqrt(ell).
For inert primes P=ell^2, the field is F_(ell^2), and every normalization
uses ell. Cohen (2) and Conrad (3) are stated over arbitrary finite
fields of odd cardinality; L556 verifies the actual nontrivial psi in
both cases. Thus no prime-field-only proof is extended to the inert
case. The additive transport in (6) can also be checked directly:
both tau_1 tau_4 and tau_3 tau_2 acquire the same factor H(b)^(-5)
under (4). There is no missing quadratic Gauss phase or choice of a
square root of a character value. The identity leaves gamma_2^3
unevaluated and does not choose any individual Gauss root.

This is a local application audit of known mathematics, not a result
beyond the cited sources or an audit of the entire external analytic
argument. The exact equality passes the stated phase/normalization
test; none of the independent coefficient, uniformity or Xi gaps is
resolved by it.

## Mathlib

No Lean verification was run. Reuse the saved assessment's inspection
of [JacobiSum/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/JacobiSum/Basic.lean):
`jacobiSum_mul_nontrivial` supports the Gauss–Jacobi identity when the
product character is nonprincipal; the division form
`jacobiSum_eq_gaussSum_mul_gaussSum_div_gaussSum` additionally requires
a target field, nonzero image of the finite-field cardinality and a
primitive additive character. L556 records supporting
`gaussSum_mulShift_eq` and `gaussSum_mul_gaussSum_eq_card` in
[GaussSum.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/GaussSum.lean),
with the nonprincipal and primitive hypotheses. A nontrivial additive
character of a field is primitive. These are supporting results.
The saved bounded search of JacobiSum/Basic.lean did not identify the
mixed identity (2); full matching coverage elsewhere remains unchecked.
