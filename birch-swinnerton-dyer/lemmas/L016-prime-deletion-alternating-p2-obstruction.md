# L016 — The alternating residual obstruction to fixed-prime p^2 lifting

## Hypotheses

Retain all hypotheses, eligible primes ell_1,ell_2, coefficient-compatible
systems and normalizations of L015. In particular, p >= 5 is non-anomalous
and ordinary, the residual representation is surjective, and the two-prime
index N = ell_1 ell_2 is delta-minimal modulo p. Both primes belong to
P_(2,0). Neither finite Sha nor positive rational rank is assumed.

Use R = Z/p^2 Z, k = F_p, S_m = Sel(Q,E[p^m]), and the actual components
c_i = c_i^(2), e_i = c_i^(1), g_i = iota(h_i) of L015. Its residual basis,
coefficient exactness, Cartesian conditions and four error formulas are
inputs. Put G_2 = H^1_(F_cl^N)(Q,E[p^2]); this relaxes precisely the two
auxiliary primes and retains every other classical condition.

Import the self-dual classical and transverse local conditions in
Sakamoto, *p-Selmer group and modular symbols*, Documenta Math. 27 (2022),
[Definitions 2.3/2.4, printed p. 1898](https://ems.press/content/serial-article-files/29299?nt=1#page=8),
and its perfect Tate-duality framework in
[Theorem 2.1, printed p. 1897](https://ems.press/content/serial-article-files/29299?nt=1#page=7).
Use the standard Brauer reciprocity law: the local invariants of a global
Brauer class sum to zero. The local classes here are cup products with the
Weil pairing; this is also the reciprocity underlying that duality theorem.
These are applications of the already assessed framework, not reproofs of
the source's construction or residual-basis theorem.

At ell_i choose u_i in the unramified line and t_i in the transverse line
with phi_i^fs(u_i) = 1 and v_i(t_i) = 1 after the fixed tensor
trivializations. Write local Tate-pairing values in R using
a/p^2 mod Z <-> a mod p^2. Define the unit lambda_i by

\[
\langle a u_i+b t_i,a'u_i+b't_i\rangle_i
   =\lambda_i(ab'+ba'),\qquad \lambda_i\in R^\times.
\tag{1}
\]

Let A_i be the unramified coefficient of loc_(ell_i)(c_i). It is a unit
because e_i has nonzero localization there. A bar denotes reduction to k.

## Conclusion

The one-prime scalar errors always vanish at this depth:

\[
\delta_2(\ell_1)=\delta_2(\ell_2)=0.
\tag{2}
\]

There exist B,C in k such that

\[
\begin{array}{ll}
\operatorname{loc}_{\ell_1}(c_1)=A_1u_1,
 &\operatorname{loc}_{\ell_2}(c_1)=pB t_2,\\
\operatorname{loc}_{\ell_1}(c_2)=pC t_1,
 &\operatorname{loc}_{\ell_2}(c_2)=A_2u_2,
\end{array}
\tag{3}
\]

where pB and pC mean the canonical injections k -> pR. The remaining
errors obey precisely the following reciprocity constraint:

\[
\tau:=\bar\lambda_2\bar A_2 B
     =-\bar\lambda_1\bar A_1 C\in k.
\tag{4}
\]

In particular h_1 is on the e_2 line, h_2 is on the e_1 line, and their
vanishing is equivalent to tau = 0. The actual prescribed classes form an
R-basis of G_2 in either case. A residual alternating form on S_1 has matrix

\[
\Omega=\begin{pmatrix}0&\tau\\-\tau&0\end{pmatrix}
\tag{5}
\]

in the basis e_1,e_2, with radical exactly rho(S_2). Consequently:

- If tau = 0, both prescribed classes are classical, S_2 = G_2 is free of
  rank two over R, and rho(S_2) = S_1.
- If tau != 0, neither prescribed class is classical, S_2 = pG_2 is
  isomorphic to k^2, and rho(S_2) = 0. This forces rank E(Q) = 0 and
  Sha(E/Q)[p^infinity] = Sha(E/Q)[p] isomorphic to k^2.

The reciprocity and two-prime finite-singular constraints tested here
permit a nonzero tau in an explicit maximal-isotropic localization model.
That model is not a full Kato system or an elliptic-curve realization.
The value of tau for the actual arithmetic family is not evaluated. Even
tau = 0 supplies only a p^2 Selmer basis, with no rank-two lower bound.

## Proof

**The signs and local nondegeneracy.** The local Tate form on H^1 with
E[p^2] coefficients is symmetric. Swapping two degree-one cup factors
introduces a minus sign, and swapping the arguments of the alternating
Weil pairing introduces another minus sign. Their product is plus.
The unramified and transverse lines are each their own annihilator, by
the imported local conditions. They are complementary free rank-one
R-modules by Sakamoto's
[Section 2.3, printed p. 1902](https://ems.press/content/serial-article-files/29299?nt=1#page=12).
Perfectness therefore makes their cross-pairing a unit, proving (1).
One must not substitute an alternating form for this local symmetric form.

For any two global classes x,y in G_2, their local cup-pairings vanish
outside ell_1,ell_2: both localizations lie in the same self-orthogonal
classical condition. Odd-p cohomology at the real place is zero. Brauer
reciprocity thus gives

\[
\langle\operatorname{loc}_{\ell_1}x,
       \operatorname{loc}_{\ell_1}y\rangle_1
+\langle\operatorname{loc}_{\ell_2}x,
       \operatorname{loc}_{\ell_2}y\rangle_2=0\quad\text{in }R.
\tag{6}
\]

**Self-pairing kills the diagonal errors.** L015 and
[Definition 2.18, printed p. 1903](https://ems.press/content/serial-article-files/29299?nt=1#page=13)
give loc_(ell_i)(c_i) = A_i u_i + delta_2(ell_j)t_i for j != i;
at ell_j the class is transverse. Apply (6) with x = y = c_i. The
transverse self-pairing at ell_j is zero, leaving

\[
2\lambda_i A_i\delta_2(\ell_j)=0.
\tag{7}
\]

Since 2, lambda_i and A_i are units, (2) follows. L015 now gives
phi_1^fs(h_1) = 0 and phi_2^fs(h_2) = 0, using injectivity of the
local socle maps. Its residual localization isomorphism shows
h_1 is on the e_2 line and h_2 on the e_1 line. Set
B = phi_2^fs(h_1) and C = phi_1^fs(h_2) in k. The other two error
formulas of L015 yield (3). Apply (6) with x = c_1,y = c_2 to obtain

\[
p\bigl(\lambda_1 A_1 C+\lambda_2 A_2 B\bigr)=0.
\tag{8}
\]

Here representatives for B,C in R can be chosen arbitrarily. Dividing
an element of pR by p means its canonical identification with k, and
(8) gives (4). All four weights in (4) are nonzero. Thus B = 0 iff C = 0,
and both vanish iff h_1 = h_2 = 0. Their specific coordinates are
h_1 = (B/bar A_2)e_2 and h_2 = (C/bar A_1)e_1.

**The prescribed classes generate the entire relaxed group.** The
residual relaxed group is S_1 by L015. Reduction sends any z in G_2 to
this S_1. Subtract a linear combination of c_1,c_2 with the same residual
coordinates. The difference is iota(b) for a unique global residual class
b. Cartesian propagation places b in the residual relaxed group S_1.
The coefficient identity p c_i = iota(e_i) then places this difference
in the span of p c_1,p c_2. Hence G_2 = R c_1 + R c_2.

For independence, reduce any relation a_1 c_1 + a_2 c_2 = 0. The
residual basis forces a_i = p b_i. Injectivity of iota and
p c_i = iota(e_i) then force both b_i = 0 modulo p. Thus a_i = 0 in R,
and the asserted basis is proved without assuming classical lifting.

**Define the residual obstruction form and its radical.** A lift of
x in S_1 to G_2 has auxiliary singular coordinates in pR, since its
reduction is classical. For x,y in S_1 choose X,Y in G_2 lifting them.
At the two primes write f_i(Y) for the unramified coefficient and
s_i(X) for the transverse coefficient. Define

\[
\Omega(x,y)=\left[p^{-1}\sum_{i=1}^2
              \lambda_i s_i(X)f_i(Y)\right]\in k.
\tag{9}
\]

Changing X by a lift with the same reduction adds iota(S_1), whose
singular coordinates are zero. Changing Y changes its finite coordinates
by multiples of p, which multiply s_i(X) in pR to zero in R. Thus (9)
is independent of the chosen lifts. For x = x_1 e_1+x_2 e_2 and
y = y_1 e_1+y_2 e_2, equations (3)/(4) give

\[
\Omega(x,y)=\bar\lambda_1 C\bar A_1 x_2y_1
             +\bar\lambda_2 B\bar A_2 x_1y_2
            =\tau(x_1y_2-x_2y_1).
\tag{10}
\]

This proves (5) and alternation. Its radical consists of x with both
singular coordinates of X zero: the finite localization coordinates of
y range over k^2, and the weights are units. Such X is precisely
classical. Equivalently every other lift differs by a classical iota(S_1),
so rho(S_2) equals this radical.

If tau = 0, equations (3)/(4) make every class of G_2 classical.
If tau != 0, a combination a_1 c_1+a_2 c_2 has zero singular
coordinates exactly when p a_2 C = p a_1 B = 0, that is, both a_i
are divisible by p. Hence S_2 = pG_2 and rho(S_2) = 0.
This verifies the two alternatives, including the exclusion of a
one-dimensional classical reduction image in this setting.

**Interpret the nonzero alternative without assuming finite Sha.**
By the Kummer diagram used in L015, rho(S_2) contains the rational
Kummer image E(Q)/pE(Q): reduction on E(Q)/p^2E(Q) is onto. A zero
image forces that quotient to vanish. Surjective E[p] excludes rational
p-primary torsion, so rank E(Q) = 0. The same diagram now gives
p Sha[p^2] = 0 and S_1 isomorphic to Sha[p] isomorphic to k^2.
If a p-primary Sha element had order p^a with a >= 2, multiplying it
by p^(a-2) would give an element of exact order p^2 in Sha[p^2],
contrary to p Sha[p^2] = 0. Therefore the whole p-primary Sha is killed
by p and equals this finite k^2. This is a conditional conclusion,
not a determination of tau or of the complex analytic order.

**A surviving-error localization model.** Work over any odd p and
take L = R^4, with coordinates (f_1,s_1,f_2,s_2) and perfect symmetric
form

\[
\langle x,y\rangle=f_1s'_1+s_1f'_1+f_2s'_2+s_2f'_2.
\tag{11}
\]

At each prime the finite and transverse coordinate lines are complementary
self-annihilating lines. Set

\[
c_1=(1,0,0,p),\qquad c_2=(0,-p,1,0),\qquad
G=R c_1+R c_2.
\tag{12}
\]

The basis has zero Gram matrix, so G is isotropic. Directly, an element
y orthogonal to c_1,c_2 satisfies s_1 = -p f_2 and s_2 = p f_1;
these equations describe G itself. Thus G is maximal isotropic.
Its residual space is the finite k^2 with basis e_1,e_2. The coordinate
reduction has kernel pG, and the injection e_i -> p c_i identifies
this kernel with that residual space, respecting all four local lines.
The residual doubly relaxed space is also k^2. At depth two the
classical intersection is G intersect {s_1 = s_2 = 0} = pG, whose
reduction is zero. The modified groups relaxed at one prime and
transverse at the other are R c_1 and R c_2.

Take phi_i^fs to be the finite coordinate and v_i the singular
coordinate, and put g_1 = p c_2, g_2 = -p c_1. Then the residual
errors are h_1 = e_2,h_2 = -e_1, all three scalars
delta_2(1),delta_2(ell_1),delta_2(ell_2) are zero, and the full set
of two-prime relations in L015 holds:

\[
v_2(c_1)=p=\phi_2^{fs}(g_1),\qquad
v_1(c_2)=-p=\phi_1^{fs}(g_2),\qquad
\phi_1^{fs}(g_1)=\phi_2^{fs}(g_2)=0.
\tag{13}
\]

The own-prime singular coefficients and those of g_i are zero.
The residual own-prime finite values are both 1, consistent with the
source's residual relation phi_i^fs(e_i) = -delta_1(N) for the unit
delta_1(N) = -1. This model has lambda_i = A_i = 1, B = 1,C = -1
and tau = 1. It therefore refutes forced vanishing from exactly
the reciprocity, coefficient and two-prime relations tested above.
It supplies no components at a third prime realizing delta(N), no
full system, and no arithmetic realization; compatibility with further
global construction data remains a separate question.

`python3 scripts/prime-deletion/check_p2_reciprocity.py` checks this
finite localization package exactly at p = 5, including the full
orthogonal complement, coefficient kernels and both tau alternatives.
Its output is `scripts/prime-deletion/p2-reciprocity-result.json`.
The all-p proof is the calculation above, not those finite checks.

The continuation threshold is not met: tau for the actual family
remains unknown, and self-duality permits a surviving error. Stop the
deduction of automatic promotion from this tested package. The achieved
unconditional rank bound is still r <= 2. Even the zero alternative
does not identify two rational Kummer directions or connect N to m(E).
This is a reproduced specialization of the assessed finite-coefficient
duality framework, with no progress beyond checked literature claimed.

## Mathlib

Full coverage of the actual-family scalar obstruction and dichotomy:
**not checked**. Supporting local Tate pairings, Brauer reciprocity,
Cartesian Selmer structures, coefficient exact sequences and Kummer
diagrams: **not checked**. Sakamoto's named construction/basis results
are imported through L015; Theorem 2.1, Definitions 2.3/2.4/2.18 and
Section 2.3 support this specialization. They are not claimed as a
full-statement match or Mathlib theorem names. No library absence or
certified novelty inference is made.
