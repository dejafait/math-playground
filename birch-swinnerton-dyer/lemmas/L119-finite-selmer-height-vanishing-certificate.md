# L119 — Finite Selmer and height certificate for vanishing higher layers

## Hypotheses

Let E/Q be an elliptic curve, presented on a global minimal integral
Weierstrass equation, and let p>=5 be a prime of good ordinary reduction.
Use the classical cyclotomic conventions of
[foundations/03](../foundations/03-cyclotomic-control.md) and the ordinary
height conventions of [foundations/04](../foundations/04-cyclotomic-height-criterion.md).
In particular X is the classical infinite-level Selmer dual,
A=Z_p[[T]]_(T), M=X tensor A, h=ord_T f_X and delta=length_A(TM).
Let V_j be the full compact Selmer filtration of L118, with V_1 the full
rationalized compact Selmer space. Do not replace it by a marked rational
subspace. Neither finite Sha nor height nondegeneracy is assumed.

Supply these finite, rigorously justified arithmetic inputs:

1. Exact rational points P_1,...,P_k on E, with k>=0, and a certified value
   t=dim_Fp E(Q)[p]. No independence or saturation is initially required.
2. A certified integer upper bound b for the dimension of the **full**
   p-Selmer group over Q, satisfying b<=k+t. A lower bound, isogeny-Selmer
   dimension without comparison, or conjectural rank is insufficient.
3. If k>0, certified absolute point-height approximations sufficient to
   form the matrix described below, and the strict determinant test below.
   These are mathematical certificates, not unverified software output.

Here is an explicit precision contract for input 3. Let q_H denote Harvey's
quadratic ordinary cyclotomic height in arXiv:0708.3404v1, Section 2.2,
equation (3). Put q=-q_H and define the matrix below. The step-497
replacement below identifies its polarization directly with the canonical
Mazur--Stein--Tate cyclotomic pairing, without identifying the printed
Stein--Wuthrich sigma formula. The separate step-499 critical audit passes
this replacement at the stated hypotheses.
Put

\[
 B(P,Q)=\tfrac12\bigl(q(P+Q)-q(P)-q(Q)\bigr),\qquad
 H_{ij}=B(P_i,P_j).
\tag{1}
\]

For each P_i and each P_i+P_j with i<j, supply a rational representative
z_R and an absolute precision m_R>=2 such that

\[
 q_H(R)-z_R\in p^{m_R}\mathbf Z_p.
\tag{2}
\]

A certified zero/torsion point has height zero exactly; it may be recorded
as z_R=0 with any finite m_R>=2. No nonzero-point sigma formula is evaluated
at the identity or at a point whose required multiple is the identity.
All sums and this exception must be checked using the exact group law.

Form a symmetric rational matrix \widehat H by

\[
 \widehat H_{ii}=-z_{P_i},\qquad
 \widehat H_{ij}=-\tfrac12
   (z_{P_i+P_j}-z_{P_i}-z_{P_j})\quad(i<j).
\tag{3}
\]

Set N_ii=m_(P_i), and for i<j set
N_ij=N_ji=min(m_(P_i+P_j),m_(P_i),m_(P_j)).
Write v=v_p with v(p)=1 and v(0)=+infinity.
Choose an integer a>=0 satisfying, for every i,j,

\[
 a+v(\widehat H_{ij})\ge0,\qquad a+N_{ij}\ge0.
\tag{4}
\]

This is a check on the rational representatives and integer precisions,
not an assumption that the true heights are integral. Such an a exists.
Put

\[
 \widehat U=p^a\widehat H,\quad
 N=\min_{i,j}(N_{ij}+a),\quad
 D_0=\det\widehat H,\quad B_0=N-ak.
\tag{5}
\]

The required acceptance test is the strict inequality

\[
 \boxed{\quad v(\det\widehat U)<N\quad}
 \quad\text{equivalently}\quad v(D_0)<B_0.
\tag{6}
\]

For k=0 omit all height and precision inputs and tests (2)--(6), and use
the empty height determinant 1. The bound b<=t is still required.

## Conclusion

For certified inputs and (when k>0) test (6), the full conditional
conclusion, with the step-497 canonical-height replacement, is:

\[
 \begin{gathered}
 \operatorname{rank}E(\mathbf Q)=k,\qquad
 \Sha(E/\mathbf Q)[p^\infty]=0,\qquad R_p(E)\ne0,\\
 h=k,\qquad \delta=0,\qquad TM=0,\qquad
 M\simeq(A/(T))^k,\qquad V_j=0\ (j\ge2).
 \end{gathered}
\tag{7}
\]

The P_i form a basis of E(Q) tensor_Z Q_p. They need not form a saturated
integral Mordell--Weil basis. For k>0 the certified determinant enclosure is

\[
 \det H\in D_0+p^{B_0}\mathbf Z_p.
\tag{8}
\]

Both the determinant and B_0 may have negative valuation/exponent.
Failure of (6) or of the sharp Selmer threshold is inconclusive; it is
neither evidence that the height is degenerate nor a counterexample to BSD.
This is a conditional finite-input specialization of known arithmetic
theorems. No successful curve, uniform producer, comparison with complex
analytic order, full Sha finiteness, or refined BSD formula is established.
**Review qualification:** step 494 passed the finite algebra, rank/Sha,
spanning and k=0 branch, and held the positive-rank normalization.
Step 497 supplies the replacement proof below; the separate step-499
critical audit passes its positive-rank canonical-regulator handoff. The original printed
Stein--Wuthrich comparison remains unresolved. No full BSD candidate is
asserted.

## Proof

**Imported sources and the purpose of the specialization.** The finite
Kummer exact sequence is Milne, *Elliptic Curves*, second edition (2021),
IV, equation (29), printed p.113, with finiteness in Theorem 3.1, p.114:
[primary text](https://www.jmilne.org/math/Books/EC2.pdf#page=118).
L001 already supplies its torsion-corrected dimension/rank use. L003
supplies the conditional characteristic-order theorem, and audited L118
supplies the higher-layer accounting. Those arithmetic inputs are imported,
not reproved. The point-height source is Harvey, *Efficient computation of
p-adic heights*, [arXiv:0708.3404v1](https://arxiv.org/pdf/0708.3404v1),
Theorems 1--3, pp.1--2, Section 2.2, p.4, and Section 5, pp.11--12.
The source assessment predating this attempt is
[the finite-certificate comparison](../drafts/literature/2026-10-25-selmer-height-finite-certificate.md).
The specialization adds the finite matrix error contract and checks that
these inputs establish the existing arithmetic premises. It is not a
reproof of a height, descent, control or cotorsion theorem.

**Point-height precision and conventions.** In Harvey's notation let
n_1=#E(F_p), let n_2 be the lcm of the Tamagawa numbers, and put
n=lcm(n_1,n_2). For desired m>=2, Theorem 3 uses sigma_p modulo I_(m'+1),
where m'=m+2v(n) and I_d=(p^d,p^(d-1)t,...,t^d). Theorems 1--2 supply this
sigma precision: for d>=4 require E_2 modulo p^(d-3); d<=3 is treated
directly there. Thus (2) means absolute precision after all multiplication,
division and logarithm operations. Proposition 9's bad-prime condition
is handled by Section 5's multiplication by n_2. To avoid applying a
nonzero-point formula at zero, first test [n]R exactly. If it is zero,
quadraticity gives n^2 q_H(R)=0, hence q_H(R)=0. Otherwise use the stated
point computation with its hypotheses and precision verified. No
implementation has been verified in this step.

**Canonical-height replacement (step 497).** Import Barry Mazur,
William Stein and John Tate, *Computation of p-Adic Heights and Log
Convergence*, Documenta Mathematica, Extra Volume Coates (2006), 577--614,
[publisher PDF](https://ems.press/content/book-chapter-files/27479),
equation (1.1), p.579; Theorem 1.3, p.580; equations (1.7)--(1.9), p.581;
and Sections 2.1 and 2.6--2.8, pp.582--587. Write h_MST for its quadratic
height and C for its canonical cyclotomic bilinear pairing. With the
Iwasawa logarithm and ordinary unit-root choice, its cyclotomic functional
is p^(-1) log_p composed with the cyclotomic character, and

\[
 h_{MST}(R)=p^{-1}\log_p(\sigma(R)/d(R)),\qquad
 C(P,Q)=h_{MST}(P)+h_{MST}(Q)-h_{MST}(P+Q),\qquad
 C(R,R)=-2h_{MST}(R).
\tag{15}
\]

The displayed sigma formula is initially for non-torsion R reducing to
the identity at p and to the identity component at every bad prime.
The source extends the height quadratically and the pairing bilinearly.
Theorem 1.3 uses c=(b_2-E_2)/12 on the given model; b_2 need not vanish.
Use the same global minimal equation and invariant differential as Harvey.
His explicit normalization statement, arXiv:0708.3404v1, printed p.2,
gives q_H=2p h_MST; his Section 2.1 equation (2) uses that same sigma
constant. This imports the canonical construction, not its conjectural
nondegeneracy. In particular MST Conjecture 1.1 is not an input.

Here is the extension check relevant to all points in (1)--(3). For
non-torsion R, take n=lcm(n_1,n_2) as above. Reduction at p is killed by
n_1; the bad-prime component groups are killed by their orders and hence
by n_2. Thus [n]R is admissible and is nonzero. The imported identity at
[n]R and quadraticity give
n^2 q_H(R)=2p n^2 h_MST(R); division by the nonzero integer n^2 in Q_p
proves the same identity at R, even when p divides n. For torsion R,
choose a nonzero integer u killing it. Both quadratic heights vanish at
zero, so u^2 q_H(R)=u^2 h_MST(R)=0 and both heights are zero. The same
argument includes the identity. Bilinearity kills pairing with a torsion
argument. Therefore a torsion sum P+Q also causes no exception: use its
exact zero height in polarization, never a nonzero-point sigma formula.

Substituting q=-q_H=-2p h_MST into the actual half-polarization (1) gives

\[
 B(P,Q)=-p\bigl(h_{MST}(P+Q)-h_{MST}(P)-h_{MST}(Q)\bigr)
       =p C(P,Q),\qquad q(R)=p C(R,R).
\tag{16}
\]

The minus sign and the factor 1/2 cancel the opposite polarization and
the factor 2 in Harvey's normalization; the remaining scalar is +p,
not a unit but a nonzero element of Q_p. These identities extend to
E(Q) tensor Q_p. They use neither finite Sha nor a nondegeneracy premise.
The canonical pairing is linear in its cyclotomic functional (MST,
Sections 2.1/2.6--2.8). Replacing p^(-1)log_p(kappa) by log_p(kappa)
therefore gives exactly B=p C. Both are representatives of the canonical
ordinary cyclotomic height in foundations/04. No equality with the literal
Stein--Wuthrich sigma in (14), nor any de Rham basis correction to it,
is asserted or needed.

**Absolute precision under this replacement.** Keep the entire numerical
contract in q_H units. Negation has no precision loss, and 2 is a unit,
so (2)--(8) are unchanged. The extension by n above is an exact identity;
it does not license keeping predivision precision. Harvey's Theorem 3
already targets the final absolute exponent m after its division by n^2,
using m'=m+2v(n). Torsion/zero is treated exactly as specified in (2).
For an optional conversion, h_MST(R) is enclosed by
z_R/(2p)+p^(m_R-1) Z_p. If G_C=(C(P_i,P_j)), (16) gives

\[
 G_C=H/p,\qquad
 (G_C)_{ij}\in\widehat H_{ij}/p+p^{N_{ij}-1}\mathbf Z_p,\qquad
 \det G_C\in p^{-k}D_0+p^{B_0-k}\mathbf Z_p.
\tag{17}
\]

Thus v(p^(-k)D_0)<B_0-k is exactly test (6). There is no extra assumption
that C is integral. We do not actually rescale the stored balls.
For ell=log_p(kappa(gamma))!=0 from foundations/04, B/ell has entry
exponent N_ij-v(ell), determinant exponent B_0-k v(ell), and center
ell^(-k)D_0 for its determinant if ell is exact. C/ell instead has entry
exponent N_ij-1-v(ell) and determinant exponent B_0-k-k v(ell), centered
at (p ell)^(-k)D_0. All such strict tests are equivalent by subtracting
the same scalar valuation from both sides. The proof only needs exact
nonvanishing, so no finite approximation of ell is used. If an
approximation is used, its error must be propagated as in (9).

If a producer uses a different scalar normalization, it must first
certify conversion to this contract. For example, multiplication by an
exact scalar c changes an entry error exponent N_ij to N_ij+v(c).
For a certified ball c in c_0+p^C Z_p with c_0!=0 and C>v(c_0), conversion
of an entry H_ij in x+p^J Z_p gives representative c_0 x and error exponent
at least

\[
 \min\{v(c_0)+J,\ C+v(x),\ C+J\}.
\tag{9}
\]

Indeed expand (c_0+epsilon)(x+e)-c_0 x=c_0 e+epsilon x+epsilon e.
The strict scalar test fixes v(c)=v(c_0) and excludes c=0. Formula (9),
or a sharper proved bound, is required before the subsequent integral
scaling if such a finite conversion is actually performed. It is not
enough to retain the preconversion number of digits.

**Entry and determinant errors.** Because 2 is a p-adic unit, subtracting
the three point-height balls in (1) gives
H_ij-\widehat H_ij in p^(N_ij) Z_p; the diagonal follows directly.
This also covers exact zero/torsion sums. The ultrametric inequality
requires no independence of the errors or strict inequality between
their valuations. All entries of U=p^a H and \widehat U are integral by
(4), and U-\widehat U has entries in p^N Z_p.

Replace the columns of \widehat U successively by those of U. The
difference of consecutive determinants has one column from
U-\widehat U and all other columns integral. In the permutation formula
for each such determinant, every product is in p^N Z_p. The same is
true of their finite sum and of the sum over column replacements.
Consequently

\[
 \det U-\det\widehat U\in p^N\mathbf Z_p.
\tag{10}
\]

There is no factor k! or loss of p-adic digits from adding terms. Since
det U=p^(ak) det H and det\widehat U=p^(ak)D_0, division of (10) by
p^(ak) proves (8) with B_0=N-ak, including negative B_0. Under (6),
every element of the ball (8) has valuation v(D_0), by the strict form
of the ultrametric law, and therefore det H!=0. An enclosure with
v(D_0)>=B_0 contains zero and yields no conclusion. If N=0 the scaled
determinant is integral, so the strict test cannot pass. Increasing
certified precision may help, but termination is not asserted.

Two algebraic boundary checks help locate the precision loss. For k=1,
B_0=min N_ij, so scaling loses no digits after scaling back. For k=2,
take \widehat H=diag(p^(-d),1) and H=diag(p^(-d),1+p^J), with d>=1,
J>=2 and all entry precisions declared J. With a=d, formula (5) gives
B_0=J-d; indeed det H-det\widehat H=p^(J-d). Thus retaining exponent J
for this nonintegral determinant would be false. These are exact matrix
checks, not computed elliptic-curve inputs.

**Independence, the sharp Kummer threshold and Sha.** By finite generation,
W=E(Q) tensor_Z Q_p has dimension r=rank E(Q). The bilinear pairing (1)
extends to W. If sum_i c_i P_i=0 in W, pairing with every P_j gives
H^t c=0. The determinant test therefore implies c=0, and k<=r. This
argument also rules out torsion or repeated dependent points among the
accepted P_i. For k=0 it simply gives 0<=r, without using height inputs.

Let d_p=dim_Fp Sel_p(E/Q) and a_p=dim_Fp Sha(E/Q)[p]. The finite Kummer
sequence and the torsion correction of L001 at n=1 give

\[
 d_p=r+t+a_p.
\tag{11}
\]

Here |E(Q)/pE(Q)|=p^(r+t), since for its finite torsion group the kernel
and cokernel of multiplication by p have the same order. No Sha
finiteness is needed for (11); Sha[p] is a finite quotient of Sel_p.
The supplied full upper bound now gives

\[
 k+t\le r+t\le d_p\le b\le k+t.
\tag{12}
\]

Every term is equal. Thus r=k, a_p=0, and in particular b=d_p=k+t.
A nonzero element of the p-primary torsion group
D=Sha(E/Q)[p^infinity] would have some order p^e with e>=1; multiplying
it by p^(e-1) would give a nonzero element of Sha[p]. Hence D=0.
This proves a stronger p-primary conclusion than finiteness and assumes
nothing about the prime-to-p part of Sha.

**Full rational regulator and the imported height criterion.** The
independent k points now form a basis of the k-dimensional space W.
The q-pairing is therefore nondegenerate on all of W. To check the
regulator's lattice qualification, choose an integral free
Mordell--Weil basis Q_1,...,Q_k. Express the P_i modulo torsion by an
integer matrix C_lat on that basis. Independence gives det C_lat!=0. If G is
the height matrix on the Q_i, then H=C_lat^t G C_lat and
det H=(det C_lat)^2 det G. Thus det G!=0, regardless of any p-power index
in this point lattice. By (16), the canonical MST regulator on that
integral basis is p^(-k)det G, which is nonzero. The other canonical
cyclotomic functional normalizations in foundations/04 multiply this
by a nonzero scalar to the k-th power. Hence R_p(E)!=0 for k>0.
No regulator value on a saturated basis has been computed.
For k=0 the ordinary determinant is 1 on W=0, so its nonvanishing follows
with no height calculation or normalization comparison.

With the canonical replacement (16), apply L003(2):
its odd ordinary prime hypothesis holds; the control and
cotorsion conventions match; D=0 is finite; and the full rational
regulator is nonzero. The sufficient Schneider--Perrin-Riou theorem is
used through Ray, *Remarks on Hilbert's tenth problem and the Iwasawa
theory of elliptic curves*, Theorem 3.4, printed p.445 (the precise source
is *Bull. Aust. Math. Soc.* 107 (2023), 440--450,
[primary statement](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/32000D6BB2B3EC97CAD0B6F932B84935/S000497272200082Xa.pdf/remarks-on-hilberts-tenth-problem-and-the-iwasawa-theory-of-elliptic-curves.pdf#page=6);
the scope is recorded in foundations/04). Its sufficient implication allows CM;
no non-CM converse, residual-surjectivity hypothesis, fine-Selmer claim,
or Iwasawa main conjecture is used. L003 gives h=k, TM=0,
M=(A/(T))^k and delta=0. In L118's finite nonnegative sum
delta=sum_(j>=2) dim_Qp V_j, every summand must therefore vanish.
In particular V_2=0 and all higher layers vanish. This also covers
k=0, when M=0 and V_1=0.

**Threshold, duplicates and remaining gaps.** L001 alone already gives
the rank bound, and L003 already gives the conditional height criterion.
This proof only closes their finite-input interface and the determinant
precision calculation; it is not a new arithmetic vanishing theorem.
The marked-subspace obstruction in L019 is respected: the sharp Selmer
bound proves full rational spanning and D=0 before the full-space
criterion is applied. No map from a height radical onto a Sha quotient
is assumed. ATTEMPTS/002's characteristic-order obstruction and
ATTEMPTS/031's localization gap remain intact and are not proof inputs.
Neither a proper height minor without (12) nor a Selmer upper bound
without the determinant certificate has the asserted consequence here.

The achieved threshold is V_2=0, h=r=k for eligible finite inputs; the
main goal still requires r=m(E) for arbitrary E/Q. No comparison of h
with m(E), guaranteed production of sharp bounds/nonzero heights, or
new arithmetic example has been provided. p=3 is outside the approved
Harvey precision contract. Inconclusive inputs do not imply failure of
any conjecture. The historical audit below held the earlier sign-only
handoff; the step-497 replacement passes the separate step-499 review.

**Historical critical audit (2026-10-25, step 494): partial PASS,
normalization hold on the original route.** The following records the
failure that motivated (15)--(17); its printed-formula discrepancy is
not resolved by the replacement.
The full proofs of the entry balls, integral scaling, column telescoping,
strict test and optional scalar-ball multiplication survive independent
review. In particular both true and approximate scaled matrices are
integral, the determinant error is p^(N-ak), and the nonintegral diagonal
example attains that exponent. A ball touching zero cannot pass. No
independence of entry errors or factorial valuation estimate is needed.
The sharp chain (12) retains the full Selmer and torsion corrections;
Sha[p]=0 kills every p-primary torsion element, with no finiteness premise.
Independence precedes this chain and spanning follows it. The lattice
change multiplies the determinant by a nonzero square, even when the
index is divisible by p. For k=0, r=0 and D=0 follow without any point
height, the full regulator is the empty determinant 1, and L003/L118
give all remaining conclusions. These cases do not require new sources.

The positive-rank normalization comparison has a specific unresolved
source discrepancy. Write b_2=a_1^2+4a_2 and let D_omega denote
differentiation with respect to the fixed invariant differential.
Harvey, arXiv:0708.3404v1, Section 2.1, equation (2), printed p.3, states

\[
 D_omega^2\log\sigma_H=-x-(b_2-E_2)/12.
\tag{13}
\]

Stein--Wuthrich, Section 4, printed p.1770, first defines Bernardi's
sigma by D_omega^2 log sigma_B=-x. Its equation (4.1) then writes
sigma_SW=exp(e_2 log_E^2/24) sigma_B, with e_2 labeled E_2(E,omega).
Since D_omega log_E=1, these displayed formulas give

\[
 D_omega^2\log\sigma_{SW}=-x+e_2/12.
\tag{14}
\]

If the two displayed E_2 quantities are literally identified as the
previous proof did, equality of the sigma functions in (13)--(14)
requires b_2=0. L119's minimal-model hypotheses impose no such
restriction. This is a comparison of the printed formulas, not a claim
that the intended canonical heights differ or that (7) has an arithmetic
counterexample. The necessary reconciliation may involve the de Rham
basis or a source correction: Stein--Wuthrich Section 3.5, printed
p.1767, explicitly uses eta=x omega. The different constants cannot be
silently removed by asserting that both functions are called canonical.
Any correction involving a square of log_E is also not automatically a
common scalar on the height matrix.

Thus the original sign-only conversion is not certified by the passages
checked. Harvey's own canonical-height description is retained, but the
exact match to foundations/04's regulator conventions is not repaired by
name matching. Reconciliation with the primary constructions is reserved
for a separate source review. No change to the arithmetic hypotheses of
L003 or to audited L118 is claimed. At step 494 this obligation held the positive-rank final application;
the finite algebra and k=0 conclusions remained established. Step 497
now supplies a different canonical input in (15)--(17), without proving
the discarded literal identification; its separate critical review passes
in step 499 below. No implementation,
successful curve, full Sha finiteness or BSD candidate was produced.

**Separate replacement critical audit (2026-10-26, step 499): PASS.**
This verdict concerns (15)--(17) and the full-regulator handoff under the
stated finite-input hypotheses. It does not certify the disputed printed
SW formula or any implementation. The arithmetic theorems remain imported
from the precise sources above. The prior finite-algebra audit is reused.

The functional is fixed before comparing formulas: MST Sections 2.1
and 2.8 compose the universal ordinary height with p^(-1)log_p(kappa).
Linearity in that functional identifies pC with the height for
log_p(kappa). On the same model and differential the constants in MST
(1.7)--(1.9) and Harvey (2) agree, including b_2. With Harvey's explicit
q_H=2p h_MST, direct substitution in (1) yields
B=-p(h_MST(P+Q)-h_MST(P)-h_MST(Q))=pC. On the diagonal,
B(R,R)=q(R)=-2p h_MST(R)=pC(R,R), independently checking both the
sign and the factor 2. The surviving scalar p is nonzero, not a unit.
No conjectural nondegeneracy or arbitrary choice of bilinear form enters.

For each non-torsion point separately, the integer n kills its reduction
in E(F_p) and its classes in E(Q_l)/E_0(Q_l) at bad primes l. These local
quotients have the Tamagawa orders used in n_2 on a minimal model.
Its multiple is nonzero and meets the admissible formula's hypotheses.
Cancellation of n^2 takes place in Q_p, so p dividing n causes no failure
of the exact identity. For a torsion point a killing multiple proves its
height zero; bilinearity also kills torsion arguments. These cases include
zero and torsion sums of non-torsion points. Thus (3)'s diagonal and
all off-diagonal entries represent the same pairing on the rationalized
Mordell--Weil space. No affine formula is evaluated at zero.

This exact extension is distinct from precision transport: Harvey
Theorem 3 uses m'=m+2v(n) before division by n^2 to guarantee the final
absolute exponent m. Section 5 uses units for the logarithm and its
Lemma 8 preserves their absolute precision. Proposition 9 applies only
to its bad-prime-admissible Q, odd modulus and multiplier at least 2.
If that multiplier n/n_2 equals 1, its coordinates are already the input
coordinates and no use of Proposition 9 is needed. The paired signs
cancel in t and disappear under the Iwasawa logarithm. None of this
replaces (2)'s demand for certified final balls.

Since 2 is a unit, negation and half-polarization incur no loss before
(4)--(8). Multiplication of a ball by an exact nonzero scalar c sends
x+p^J Z_p to cx+p^(J+v(c)) Z_p. Applying this identity to entries and
to the already enclosed determinant proves (17), with respective losses
1 and k. Applying it to ell^(-1) and (p ell)^(-1) gives exactly the two
entry and determinant exponents stated after (17). Centers and error
exponents shift together, so every strict nonzero test is equivalent.
This remains true for negative exponents and nonintegral heights.
For a numerical scalar conversion (9) requires a certified ball for the
actual multiplier, including its inverse if division is intended; a ball
for ell alone cannot be substituted as a ball for ell^(-1). The proof
uses exact scalars and makes no such numerical substitution.

Finally, the audited sharp chain (12) proves full spanning and zero
p-primary Sha before the regulator theorem is applied. On an integral
basis, the point-lattice change multiplies the determinant by a nonzero
square and the conversion from B to C multiplies it by p^(-k). Hence the
canonical regulator is nonzero even with p-power lattice index. Ray
Theorem 3.4 uses that nonvanishing, finite p-primary Sha, odd ordinary p
and classical cotorsion; each hypothesis is supplied here or in
foundations/03. Its separately normalized regulator does not change the
order conclusion. There is no non-CM hypothesis in that implication.
L003 and the audited L118 then give (7); k=0 retains the earlier pass.
The DAG inputs remain unchanged. The original SW discrepancy and the
absence of concrete arithmetic inputs or a complex-order comparison
remain unresolved. This is verification of a known-method conditional
specialization, not a new general arithmetic theorem.

## Mathlib

Full matching finite Selmer/height/higher-layer certificate: **not
checked**. Supporting arithmetic Kummer sequence, ordinary height,
characteristic-order theorem and derived-height filtration: **not
checked** for matching library coverage. The full MST canonical pairing,
Harvey normalization and their comparison to the arithmetic regulator:
**not checked** for Mathlib coverage. Determinant multilinearity,
finite-dimensional independence and ultrametric valuation facts:
**not checked** for exact theorem names. No absence claim is made.
The elementary error analysis is proved above; the arithmetic inputs
are the precise named sources and existing canonical results cited here.
