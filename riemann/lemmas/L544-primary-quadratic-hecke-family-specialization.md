# L544 — Primary quadratic Hecke-family specialization

## Hypotheses

Let F=Q(sqrt(-3)), O=Z[omega], omega=exp(2 pi i/3), and
lambda=1+2 omega. Write q_a for the absolute norm of a nonzero integral
ideal a. Fix a finite set S of prime ideals containing the primes above
6 and the supports of the fixed presentation/ray datum. An ideal is
good if it avoids S. S is independent of every length and index.

Use the source arithmetic conventions: O is a PID, its units are
{+/-1,+/-omega,+/-omega^2}, and each ideal prime to lambda has a unique
generator a^# congruent to 1 modulo 3. These generators multiply.
For a good prime p let l_p(x) be its quadratic residue character,
zero at p|x. For squarefree good a define

\[
 l_a(x)=\prod_{p\mid a}l_p(x),\qquad l_1(x)=1,
 \qquad Q_a(b)=l_a(b^\#).
\]

The finite-field definition of the source sextic symbol gives
l_p(x)=chi_p(x)^3, so this is exactly L543's Q_a(b).

Use the following quadratic reciprocity identity, proved below from
L554 (7) and L555's finite correction table. Set
G=(O/4O)^*/((O/4O)^*)^2 and let [a] be the class of a^# modulo 4.
The group has representatives 1,-1,lambda,-lambda and, for coprime
squarefree good ideals a,b,

\[
 Q_a(b)=Q_b(a)R([a],[b]),\qquad
 R((-1)^i\lambda^j,(-1)^k\lambda^l)
       =(-1)^{il+jk+jl},\quad i,j,k,l\in\{0,1\}.       \tag{1}
\]

This is the quadratic content of the pinned manuscript's
`lem:quadratic-four-term`, `eq:reciprocity-four-class`, and the quadratic
CRT calculation in `lem:fixed-gauss-phase`. L555 audits the needed
prime/product Gaussian evaluation; L554 supplies its coprime
multiplicative extension. Their other imports retain their stated
qualifications. The general Goldmakher–Louvel theorem cited below is
imported, not reproved.

## Conclusion

For every epsilon>0, all U,V>=1, and arbitrary complex coefficients
z_b on squarefree good ideals of norm at most V,

\[
 \sum_{\substack{a\ {\rm sf,good}\\q_a\le U}}
 \left|\sum_{\substack{b\ {\rm sf,good}\\q_b\le V}}
                  z_b Q_a(b)\right|^2
 \ll_{\epsilon,S}(UV)^\epsilon(U+V)\sum_b|z_b|^2.     \tag{2}
\]

The bound includes unit ideals and noncoprime row/column pairs with
their stated zeros. Fixed row restrictions and fixed coefficient support
restrictions are allowed. It does not allow arbitrary masks depending
on both a and b. This proves L543 (1), using the established local
reciprocity inputs above, with no additional length loss. It reproduces a claimed
source application; no improvement or mathematical novelty is claimed.
Together with L543 it supplies the quadratic input for L542 at this
fixed S. The independent cubic primitive is supplied separately by
L545, not by this argument. Reflection, global closure and Xi positivity
remain open; no wider or varying-S conclusion is asserted.

## Proof

The source application is OpenAI, *The Quasi-Riemann Hypothesis:
A Zero-Free Half-Plane Re(s)>7/8*, 30 September 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[primary TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
`eq:quadratic-large-sieve` and its application paragraph, lines 2480–2517.
Arithmetic conventions are at 519–588; the quadratic identity
is at 772–799 and 900–920. Only its quadratic identity is needed here;
L554's cited cubic reciprocity import remains an upstream input.

The imported theorem is Leo Goldmakher and Benoit Louvel,
*A quadratic large sieve inequality over number fields*, Math. Proc.
Cambridge Philos. Soc. 154 (2013), 193–212,
[arXiv:1112.1642v2, 31 May 2012](https://arxiv.org/pdf/1112.1642v2),
Definition 1 and Theorem 1.1, PDF pp. 1–2. A quadratic Hecke family
consists of primitive finite-order Hecke characters of trivial infinite
type, of orders dividing two, indexed by all squarefree ideals avoiding
one fixed modulus. It must have reciprocity through a homomorphism on
all ideals avoiding that modulus to a finite group, and coprime
same-class products must induce primitive characters of conductor ab.
The theorem bounds the matrix with entries theta_b(a) and full norm
cutoffs by the factor (UV)^epsilon(U+V). Section 2, PDF pp. 4–5,
explicitly uses primitive inducing characters also for products.
Lemma 4.5 and its proof, PDF pp. 8–9, give the reciprocity/duality
orientation precedent. We justify the application below because merely
citing the abstract theorem leaves these arithmetic hypotheses open.

### Reciprocity application audit, 2026-10-31

We discharge exactly the formerly retained (1). Fix squarefree good
ideals a,b and write A=a^#, B=b^#. These are the primary elements used
in L554, with the same fixed S; they are odd because S contains all
primes above 2. At each good prime p, the cube of the Euler-defined
sextic character is the quadratic character: on units its residue is
x^((q_p-1)/2), and both characters are zero at p|x. Thus, including
the empty product at the unit ideal,

\[
 Q_a(b)=\chi_A(B)^3,\qquad Q_b(a)=\chi_B(A)^3.
                                                        \tag{6}
\]

Here the denominator/subscript of chi is the ideal of the displayed
primary element, not its numerator. If (a,b)=1, L554 (7) gives
chi_B(A)=R([A],[B])chi_A(B). Cubing and using R in {+1,-1} yields
Q_b(a)=R([A],[B])Q_a(b). Multiplying by R, whose square is one,
gives precisely Q_a(b)=Q_b(a)R([a],[b]), with the orientation in (1).
No conjugation or inversion of a sextic character was introduced.

For the correction, use L555 (3), whose full finite table is checked
under “All finite classes and the correction.” In its coordinates put
(a,b,d,f)=(i,j,k,l). Its exponent af+bd+bf is exactly il+jk+jl.
The classes and primary conventions are identical. L554's established
multiplicative extension already covers all coprime primary arguments,
so its squarefree specialization needs H(c) only at primes and distinct
prime products. No evaluation of H at general composite c is assumed.

If a=1, its primary generator is 1, Q_1(b)=1 by the empty product,
and Q_b(1)=1 by evaluation at 1. L555's formula gives R([1],[b])=1.
The case b=1, including a=b=1, is the same. In particular the ideal
(-1)=(1) has primary generator 1; the residue class [-1] in G is not
assigned to that ideal. No arbitrary unit associate is substituted.

If a,b share a prime p, the factor l_p(B) in Q_a(b) and the factor
l_p(A) in Q_b(a) are both zero. Hence both sides of (1) vanish.
The correction is still the nonzero finite class function of L555,
not a quotient of vanishing residue symbols. This proves the extension
of the identity to every squarefree good pair as well as its stated
coprime version. The four classes, all unit cases and every collision
are therefore included. Nothing here changes S or any analytic estimate.

This short applicability check removes the former retained reciprocity
premise in this file. It is a reproduction of the checked source claims,
not a new reciprocity theorem or an independent reproof of L554/L555
and their cited inputs. The Hecke-family application below is unchanged.

### Unit adjustment and construction on ideals

For squarefree good a put

\[
 e(a)=(q_a-1)/2\pmod2\ \in\{0,1\}.
\]

Every residue field at p|a has odd cardinality. The elementary
finite-field formula gives l_p(-1)=(-1)^((q_p-1)/2). Since products of
odd integers satisfy
(rs-1)/2=(r-1)/2+(s-1)/2 modulo 2, it follows that
l_a(-1)=(-1)^e(a). Also omega=(omega^2)^2, so l_a(omega)=1.

Let epsilon_lambda be the nontrivial character of
(O/(lambda))^*=F_3^*. For a unit u=(-1)^d omega^r,
epsilon_lambda(u)=(-1)^d and l_a(u)=(-1)^(d e(a)). Define a finite
character on units modulo f_a=a(lambda)^e(a) by

\[
 t_a(x)=
 \begin{cases}
 l_a(x),&e(a)=0,\\
 l_a(x)\epsilon_\lambda(x),&e(a)=1.
 \end{cases}                                                   \tag{3}
\]

When e(a)=0 the lambda factor is absent altogether: (3) is defined
also at x divisible by lambda, provided (x,a)=1. For e(a)=1 the
two factors are defined on the units modulo a(lambda) by CRT.
For every global unit u, t_a(u)=1. Because every ideal is principal,
theta_a((x))=t_a(x) therefore defines a character on the integral
ideals coprime to f_a, independent of the choice of generator. It is
multiplicative, extends to their fractional ideal group, and is trivial
on principal ray elements congruent to 1 modulo f_a. For a fractional
ray element one may clear a denominator coprime to f_a and apply the
same residue formula. Thus it is a ray character of modulus f_a with
trivial infinite type. Its order divides two.

This also checks the asserted primary adjustment directly. If x is a
lambda-unit, the unique unit u for which ux is primary satisfies
u x=1 modulo lambda, hence epsilon_lambda(u)=epsilon_lambda(x).
Consequently l_a(ux)=l_a(x)epsilon_lambda(x)^e(a)=t_a(x).
The omega-part of u contributes one. In particular theta_a(b)=Q_a(b)
for b prime to a and S, since epsilon_lambda(b^#)=1.

### Exact primitive conductor and zero values

The conductor divides f_a. To see that it contains every p|a,
choose a nonsquare y in (O/p)^*. CRT supplies x congruent to y
modulo p and to 1 modulo f_a/p. Then x is a unit modulo f_a,
t_a(x)=-1, and x=1 modulo f_a/p. Hence the ray character cannot
descend to any modulus dividing f_a/p. If e(a)=1, CRT similarly
supplies x=1 modulo a and x=-1 modulo lambda; this has t_a(x)=-1
and excludes descent to modulus a. These witnesses prove that the
conductor is exactly f_a; all its exponents are already at most one.
Here nontriviality of the quadratic character at each odd residue
field follows, for example, from cyclicity of its multiplicative group.

If a=1, e(a)=0 and theta_1 is the trivial character of conductor one;
the argument imposes no artificial lambda zero. If e(a)=0 for a!=1,
theta_a is likewise defined at lambda using (3). Extend theta_a by
zero exactly at ideals meeting its conductor. For every good b
colliding with a, that conductor contains their common prime, so
theta_a(b)=0=Q_a(b). For coprime good b the equality was proved above.
Thus equality of the matrix entries holds for every good pair, not
only for its coprime submatrix. In particular theta_a(1)=Q_a(1)=1.

### A global family and its same-class products

Choose once and for all c=(12) times the product of the primes in S.
Its support is exactly S. Let I(c) be all nonzero integral ideals
prime to c, including nonsquarefree ideals. For every a in I(c) the
primary generator a^# exists, is a unit modulo 4, and multiplies
exactly. Therefore a -> [a] is a homomorphism from this entire ideal
monoid to G. It also extends to the fractional ideal group if desired.
We have constructed theta_a for every squarefree a in I(c), rather
than only for the indices in an isolated class.

Equation (1) and the value identification give
theta_a(b)=theta_b(a)R([a],[b]) for coprime squarefree indices.
The group and factor are fixed independently of a,b. The reciprocity
factor also extends the equality through colliding pairs since both
matrix entries then vanish, although only coprime pairs are required.

We verify the same-class condition separately. For an odd element v,
N(v) is odd, and hence N(v^2)=N(v)^2=1 modulo 4. Norms of elements
congruent modulo 4 are congruent modulo 4. If [a]=[b], some unit
class v modulo 4 satisfies a^#=b^# v^2 modulo 4; thus q_a=q_b
modulo 4 and e(a)=e(b).

For coprime such a,b, on generators prime to ab(lambda) their
product character is

\[
 t_a(x)t_b(x)=l_a(x)l_b(x)
       \epsilon_\lambda(x)^{e(a)+e(b)}=l_{ab}(x).       \tag{4}
\]

The right side is invariant under all global units because
l_ab(-1)=(-1)^(e(a)+e(b))=1 and l_ab(omega)=1. It therefore defines
a ray character modulo ab on all ideals prime to ab, including lambda.
At each p|ab the nonsquare/CRT witness used above proves that this
character has exact conductor ab. It is precisely the primitive
character inducing theta_a theta_b: (4) identifies their restrictions
away from the original product modulus, and proves the cancellation
of its lambda factor. If e(a)=e(b)=1, the pointwise product of the
original zero-extended characters is still zero at lambda; it is not
being equated there with its primitive inducing character. This
distinction is exactly the product convention in GL Section 2, and
lambda never belongs to our matrix indices. The unit-ideal cases
are included: if a=1 is in the same class as b, then e(b)=0 and
theta_b already has conductor b.

This verifies all parts of Definition 1 with k=F and fixed c. Neither
a class restriction substituted for the full family nor Corollary 1.2
applied to an unverified sextic family is needed.

### Full-cutoff transpose and allowed restrictions

Let A_U and B_V be the finite sets of squarefree good ideals of norm
at most U and V. Form the matrix T, rows b in B_V and columns a in
A_U, with entries T_(b,a)=theta_a(b). Theorem 1.1, with outer
length V and coefficient length U, gives for every complex vector y

\[
 \|Ty\|_2^2\le C_{\epsilon,S}(UV)^\epsilon(U+V)\|y\|_2^2.
                                                               \tag{5}
\]

All entries are real, being 0 or +/-1. Hence the desired matrix is
T^*=T^t, including its collision entries. With the complex Hilbert
inner product, for any complex z and \|y\|_2=1,
|<T^*z,y>|=|<z,Ty>|<=\|z\|_2\|Ty\|_2. Taking the supremum over y
and using (5) gives
\|T^*z\|_2^2<=C_(epsilon,S)(UV)^epsilon(U+V)\|z\|_2^2.
Its a-coordinate is exactly sum_b z_b Q_a(b), proving (2).
Complex conjugation has not changed the coefficients or their norm;
reality is why transpose equals adjoint here. No dyadic cutoff from
GL Lemma 4.5 was substituted for Theorem 1.1's full cutoffs, and
there is no extra logarithmic or length factor.

Fixed coefficient restrictions are enforced by zeroing omitted z_b
before (5); fixed row restrictions decrease its final nonnegative
sum. The chosen modulus c is fixed, so the theorem's constant depends
only on epsilon and the fixed arithmetic datum, which may be denoted S
here. No estimate uniform in a growing S was used. This completes the
application at the stated fixed-S scope.

## Mathlib

Coverage of this complete Hecke-family specialization and the
Goldmakher–Louvel bound has not been checked. No matching formal result
is claimed. Finite-field characters, CRT, ray characters and
finite-dimensional Hilbert-space duality are supporting ingredients;
coverage of such ingredients would not by itself establish the full
arithmetic theorem or the full reciprocity application above. Full
matching Mathlib coverage of that application has not been checked.
