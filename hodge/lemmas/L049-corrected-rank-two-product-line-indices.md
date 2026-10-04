# L049 — Product-line indices add no corrected rank-two obstruction

## Hypotheses

Retain L048's smooth projective K3 self-product X=S x S, fixed
ample chamber and full integral mixed class tau_D. Its correspondence
operator is D|_N=2A_c+4pi_K and D|_T=2U. Write
e_1=eta tensor 1, e_2=1 tensor eta and P=eta tensor eta, with
integral_S eta=1. For integer a,b set p=4+a,t=4+b and

\[
\beta_{a,b}=p e_1+t e_2+\tau_D.
\]

The corrected data have a+b<=-13. A putative locally free bundle F
has rank two, c_1(F)=0 and ch_2(F)=beta_(a,b). Thus L048 forces
ch_3(F)=0 and ch_4(F)=(pt+78)P/6. No bundle or K-class realization
is assumed. Let L(x,y)=p_1^*L_x tensor p_2^*L_y be any actual
integral product line bundle, with x=c_1(L_x), y=c_1(L_y).
Put

\[
m=\tfrac12q(x,x),\quad n=\tfrac12q(y,y),\quad
k=\int_X\tau_D(x\otimes y)=q(Dx,y).
\]

Here q is the actual cup-product pairing on S. The equality defining
k uses the fixed self-adjoint correspondence convention. Integral
divisor classes in the entire NS(S), rather than just W, are allowed.

## Conclusion

For an actual F its product-line Euler characteristic must be

\[
\chi(X,F\otimes L(x,y))
 =2(m+2)(n+2)+p(n+2)+t(m+2)+k+\frac{pt+78}{6}.                 \tag{1}
\]

For the formal forced character, the same expression defines its
HRR index I_(a,b)(x,y). All m,n,k are integers, and

\[
I_{a,b}(x,y)-I_{a,b}(0,0)
 =(t+4)m+(p+4)n+2mn+k\ \in\mathbb Z.                         \tag{2}
\]

Consequently every integral product-line index has exactly the
same fractional part as the untwisted index. They are all integral
if and only if 6 divides pt. In particular the entire L048 region

\[
\{(a,b)\in\mathbb Z^2:a+b\leq-13,\quad6\mid(a+4)(b+4)\}        \tag{3}
\]

survives this test unchanged. Even one product-line twist cannot
repair an untwisted failure. Passing asserts neither a finite-rank
topological bundle, an integral K-class nor a locally free, stable
and transportable algebraic representative.

This is an informative NEGATIVE for using these indices as a
further filter, classified as REPRODUCTION of the assessed HRR and
character tools. No progress beyond the checked literature is
claimed. The known span stays 21 and the attained RM directions
three against four required; the universal Hodge gap stays open.

## Proof

**Import HRR and the line character.** Use the smooth proper
Hirzebruch--Riemann--Roch statement in
[Stacks Section 42.66, Tag 02UO](https://stacks.math.columbia.edu/tag/02UO)
and character multiplicativity and the line exponential in
[Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM).
The Todd expansion is supported by
[Section 42.65, Tag 02UN](https://stacks.math.columbia.edu/tag/02UN).
These inputs and their applicability to product-line twists were
already read in the ready SPECIALIZE assessment. Their general
proofs are imported. Only this substitution is derived here.

L048 supplies td(X)=(1+2eta) tensor (1+2eta) and the forced
full character

\[
\alpha_{a,b}=2+\beta_{a,b}+\frac{pt+78}{6}P.
\]

If F exists, alpha_(a,b)=ch(F), so smooth proper HRR computes
its genuine Euler characteristic. The formal integral can also
be evaluated without asserting existence.

**Integrality of the twist quantities.** Surface HRR for the actual
line bundle L_x on a K3 surface gives
chi(S,L_x)=2+q(x,x)/2. Its Euler characteristic is an integer,
so m is an integer. The same argument gives n in Z. This is an
application of the imported HRR formula, not an assertion that
arbitrary rational classes have even square.

L048's beta_(a,b) is integral, and p e_1+t e_2 is integral.
Their difference tau_D is therefore an integral cohomology class.
Since x tensor y is integral, its pairing with tau_D is integral,
giving k in Z. This uses the *full* mixed class. Its rational
projection to N tensor N need not itself have integral tensor
coefficients; no integral orthogonal splitting of H^2 is assumed.

**Expand the product without losing mixed terms.** On a surface
exp(x)=1+x+m eta and exp(y)=1+y+n eta. The rank-two contribution
to the top-degree integral of alpha exp(x+y) td(X) is
2(m+2)(n+2). The p e_1 term needs the top component on the
second factor and contributes p(n+2); the t e_2 term contributes
t(m+2). The fourth-character contribution is (pt+78)/6.

The mixed class has degree two in each factor. Its only nonzero
top-degree product with the line character and Todd class uses
x tensor y and contributes k. Terms using a point class on either
factor overshoot that factor's top degree. Since the Todd class
has no degree-two component, there is no other mixed contribution.
This proves (1) for all integral product lines.

The transcendental part of tau_D pairs trivially with x tensor y
by orthogonality to NS. It remains essential in alpha's already
forced fourth component: L048's full mixed square is 156, with
transcendental contribution 120. Nothing in (1) replaces that
square with its divisor part.

**The integer threshold is unchanged.** Setting x=y=0 gives
I_(a,b)(0,0)=8+2(p+t)+(pt+78)/6, as in L048. Subtracting this
value from (1) gives (2). Every coefficient and every m,n,k in
(2) is integral. Thus for every twist its index is integral
exactly when the untwisted one is. L048 proves that condition to
be 6|pt; adjoining its independent integer Bogomolov condition
a+b<=-13 gives precisely (3). The trivial product line also
shows necessity for the all-twists assertion.

For example, twist by the fibre class x=f_ell and the zero-section
class y=O in the fixed chamber. Here m=0,n=-1. L044 supplies
u_1=f_ell, u_2=f_ell+O-E_exc, u_3=-2f_ell+E_exc and its integral
tensor coefficient matrix B_0. Only q(u_2,f_ell)=1 is nonzero,
so B_c acts on f_ell by -2u_1+u_2+u_3=O-3f_ell. Its addition
to the original 4 id divisor action gives D f_ell=f_ell+O.
Thus k=q(f_ell+O,O)=1-2=-1. The indices for corrections
(-13,0), (-10,-10) and (-7,-7) are respectively
9, 4 and 17/2. The first two already pass L048 and remain
integral; the last retains its half-integral failure.

The exact verification command is
`python3 scripts/cubic-kahler/check_corrected_rank_two_product_line.py`.
It independently multiplies classes in the truncated surface-product
cohomology ring, using the fixed full rank-four divisor lattice.
It checks 2304 indices across all 36 pure-coefficient residue pairs
and 64 twist pairs, including divisors outside W, and the three
actual examples. The argument (2), rather than these finite checks,
proves the universal assertion. No numerical sample proves bundle
existence, stability or transverse transport.

## Mathlib

Coverage of the full all-product-lines statement: **not checked**.
No matching declaration or absence from checked Mathlib sources is
asserted. The directly linked Stacks HRR, character and Todd statements
are supporting inputs, not matches for this evaluated correction
family. Kunneth, integral cup-product pairing and degree truncation
are standard supporting tools. L048 supplies the full character and
mixed-square contribution. This is a reproduction with no certified
originality or Hodge resolution claim.
