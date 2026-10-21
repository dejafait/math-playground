# L101 — Fourth-order-pole dictionary and one insufficient upper certificate

## Hypotheses

Use C012a's finite instance: Q=65537, E=F_Q embedded in
F=F_(Q^28), H<=E* of order n=1024, k=64 and m>=1. Message rows
are in F[X] of degree less than 64. The model is the closed simultaneous
column-Hamming model in [foundations/02](../foundations/02-pinned-list-model.md),
with threshold T=Q^28/2^128. Its comparison with the unavailable ABF
statement retains [foundations/01](../foundations/01-target-and-source-audit.md)'s
qualification.

Fix A=a0+a1 X+a2 X²+a3 X³ in E[X], with a0!=0, and put P=X^68+A.
The received word is Y_A(x)=(P(x)/x^4,0,...,0) on H. For a subset
S of H write g_S=product_(x in S)(X-x). Define the finite counts

\[
 M_{67}(A)=\#\{(S,r): S\subset H,\ |S|=67,\ r\in E^*,\quad
                  g_S(X)(X-r)\equiv A\pmod {X^4}\},
\]
\[
 N_{68}(A)=\#\{J\subset H:|J|=68,\quad g_J\equiv A\pmod {X^4}\}.
\]

No squarefreeness is required of g_S(X)(X-r): r may belong to S.

## Conclusion

Let D_A be the set of distinct monic polynomials g_S(X)(X-r) in
the defining pairs for M_67(A). The entire list with at least 67
simultaneous agreements is in bijection with D_A by

\[
 G\longmapsto(f_G,0,\ldots,0),\qquad f_G=(P-G)/X^4\in E[X],
 \qquad\deg f_G\le63.                                      \tag{1}
\]

Its cardinality L_A, independently of m, is exactly

\[
 L_A=M_{67}(A)-67N_{68}(A).                                 \tag{2}
\]

Put B=769, C=binomial(1024,67), V=binomial(835,67). One uniform
character-sieve upper certificate is

\[
 L_A\le M_{67}(A)\le U:=C/Q^3+(1-Q^{-3})BV.                 \tag{3}
\]

Exact arithmetic gives

\[
 3676307<U/T<3676308.                                      \tag{4}
\]

Thus this particular upper allowance fails the sufficient test U<=T.
It is parked without retuning. This is not a lower bound on an actual
list, a uniform-cap impossibility, an unsafe center, a family exclusion
or arbitrary-center safety. The 955–957 boundary is unchanged. The
dictionary and specialization reproduce the assessed known tools;
no progress beyond the inspected sources' methods or novelty is claimed.
The separate critical proof audit on 2026-10-20 retains exactly these
restricted conclusions; its evidence and scope are recorded below.

## Proof

**Precise imports and why specialization is needed.** Gao,
*Asymptotic distributions of the number of zeros of random polynomials
in Hayes equivalence class over a finite field*,
[arXiv:2203.06729v5](https://arxiv.org/html/2203.06729v5),
2024-01-07, definitions (1)–(2), Proposition 2, (15)–(16), and
Theorem 3, (17)–(19), give arbitrary-domain chosen-root incidence
identities with monic residual factors. Take q_source=Q, modulus X^4,
ell=0, t=4, k_source=64 and D=H. This modulus is monic, every domain
point avoids its zero and a0!=0 is coprimality. For j=67 and 68 the
residual degrees are respectively one and zero. Proposition 1 supplies
exact-root inversion. These general identities are imported, not
reproved. The RS/ambient-field correspondence and explicit terminal
two-count correction below are the local applicability argument.
Gao's quantitative full-domain results are not applied to the proper H.

Li and Wan, *Distance Distribution in Reed-Solomon Codes*,
[arXiv:1806.00152v3, Section 4](https://arxiv.org/html/1806.00152v3#S4),
2019-07-30, Lemma 4.1, printed pp. 9–10, imply that for a nontrivial
character psi of (E[X]/f)*, extended by zero on nonunits, the complete
degree-one monic sum has absolute value at most (deg f-1)sqrt(Q).
The inspected statement/proof includes imprimitive characters and
requires no squarefreeness. We use f=X^4, so the bound is 3sqrt(Q).
We do not use the separate bound that requires triviality on E*.

Li and Wan, *Counting polynomial subset sums*,
[arXiv:1507.06329v1, Section 2](https://arxiv.org/html/1507.06329v1#S2),
2015-07-22, Theorem 2.1 and Corollary 2.2, printed p. 5, supply the
weighted distinct-coordinate sieve on an arbitrary finite domain.
The Lemma 2.6 proof supplies the cycle exponential identity used below.
These tools are imported without reproof. The prior
[SPECIALIZE assessment](../drafts/literature/2026-10-20-order-four-pole-dictionary-uniform-upper.md)
and its completed source review cover their hypotheses and proof cases.
The changed denominator, residual-factor sum, subgroup restriction,
powered characters and finite threshold test are the specialization.
L099–L100 are comparisons, not mathematical inputs; their constant-H
Fourier container cannot be copied to this family.

**The entire list, descent and multiplicities.** For every defining pair,
G=g_S(X)(X-r) is monic of degree 68 and P-G is divisible by X^4.
Its leading terms cancel, so deg(P-G)<=67 and (1) has degree at most
63. On H the denominator x^4 is nonzero and

\[
 P(x)/x^4-f_G(x)=G(x)/x^4.                                 \tag{5}
\]

Consequently the exact agreement set is S if r is outside H or belongs
to S, and is S union {r} if r belongs to H minus S. A repeated residual
root is allowed and supplies no extra agreement. Distinct G yield
distinct f_G. Their evaluations are distinct because their difference
has degree at most 63 and cannot vanish on all 1024 evaluation points.

Conversely let (f1,...,fm) be any ambient-field message tuple agreeing
on at least 67 columns. The polynomial G=P-X^4 f1 is monic of degree
68 since deg(X^4 f1)<=67. Choose any 67 agreement points S. The factor
theorem over F gives G=g_S(X)(X-r) for a unique r in F, since the monic
quotient has degree one. At zero,

\[
 a0=G(0)=-r g_S(0),\qquad r=-a0/g_S(0)\in E^*.             \tag{6}
\]

Here g_S(0) is a nonzero element of E. Thus G and f1 descend to E,
and their ending coefficients give the required congruence. Every
other row vanishes at those same 67 points and has degree at most 63,
so it is identically zero. This proves completeness for every m, with
no scalar projection, extra extension-field choices or exponent m.

A monic degree-68 polynomial has at most 68 distinct roots. If G has
exactly 67 roots in H, there is exactly one defining pair: S must be
its entire H-root set and the monic residual quotient is unique. This
includes the repeated-root case. If it has 68 roots, it is g_J for a
unique 68-subset J and has exactly 68 defining pairs, one for each
omitted element r of J. There are precisely N_68(A) such G. Hence
M_67=(L_A-N_68)+68N_68, proving (2). Empty fibers are included.
This is the explicit two-terminal-moment specialization, not an
identification of chosen-subset incidences with distinct messages.

**Full unit group and orthogonality.** Set R=E[X]/(X^4) and G4=R*.
Each unit is uniquely c(1+uX+vX²+wX³), with c in E* and u,v,w in E.
Since 2 and 3 are invertible, truncated logarithmic coordinates give
an isomorphism

\[
 c(1+uX+vX^2+wX^3)\longmapsto
 (c,\lambda_1,\lambda_2,\lambda_3)
 =(c,u,v-u^2/2,w-uv+u^3/3)                                \tag{7}
\]

from G4 to E* times (E,+)^3. Indeed multiplication gives normalized
coefficients u+u', v+v'+uu', w+w'+uv'+vu'. Substitution in (7) gives
the sum of the respective three lambda coordinates. Its inverse uses
u=lambda1, v=lambda2+lambda1²/2,
w=lambda3+lambda1 lambda2+lambda1³/6. All denominators divide 6,
which is nonzero in characteristic Q. Thus |G4|=(Q-1)Q³.

Writing e_Q(z)=exp(2 pi i rep(z)/Q), all its characters are

\[
 \chi(c,\lambda)=\theta(c)e_Q(\alpha\lambda_1+
                          \beta\lambda_2+\gamma\lambda_3),\quad
 \theta\in\widehat{E^*},\quad\alpha,\beta,\gamma\in E.     \tag{8}
\]

The multiplicative cyclic group has Q-1 characters and the three
additive prime-field factors each have Q. Their finite geometric-sum
orthogonality gives |G4|^(-1) sum_chi chi(z A^(-1))=1 if z=A and 0
otherwise. Here A is its unit residue, and every product being counted
is also a unit. Let r_x denote X-x modulo X^4, and put

\[
 W_\chi=\sum_{S\subset H,\ |S|=67}\prod_{x\in S}\chi(r_x),
 \qquad R_\chi=\sum_{r\in E^*}\chi(r_r).
\]

Then exactly

\[
 M_{67}(A)=\frac1{(Q-1)Q^3}\sum_{\chi\in\widehat{G4}}
                              \chi(A)^{-1}W_\chi R_\chi.  \tag{9}
\]

Although g_S(0) belongs to H (because -1 belongs to H), the residual
factor has arbitrary constant -r in E*. No constant-H restriction is
imposed on G. The full group in (9) is the actual four-ending-coefficient
class group. It imposes no surjectivity or uniformity assumption.
The zero/nonunit residual r=0 is excluded by a0!=0 in (6); extending
characters by zero will allow its harmless insertion in complete sums.

**Principal and constant-only characters.** The principal character
has W=C and R=Q-1, so its contribution to (9) is C/Q³. If
alpha=beta=gamma=0 and theta is nonprincipal on E*, then
R=sum_(r in E*)theta(-r)=0 by multiplicative orthogonality.
Every such character therefore contributes exactly zero, irrespective
of W or its powered exceptions. In particular theta can restrict
principally to H, or some powers theta^j can be principal; no
nontrivial bound is applied to those powers. This accounts for all
Q-2 nonprincipal constant-only characters. There remain exactly
(Q-1)(Q³-1) characters with a nonzero additive parameter vector.

**All powers and subgroup twists.** For one of the remaining characters
and 1<=j<=67, set C_j(chi)=sum_(x in H)chi(r_x)^j. The annihilator
of H in the character group of E* has size 64. Its usual indicator,
and -1 in H from C012a, give

\[
 C_j(\chi)=\frac1{64}\sum_{\eta:\eta|_H=1}\sum_{x\in E^*}
             (\chi^j\cdot(\eta\circ\mathrm{ct}))(X-x).    \tag{10}
\]

Here ct is constant term. Every inner character is nontrivial: its
additive parameter vector is (j alpha,j beta,j gamma), which is nonzero
because 1<=j<=67<Q; eta changes only the constant factor. Inserting
x=0 contributes zero since X is a nonunit. Each inner sum is therefore
the complete degree-one monic sum in Lemma 4.1 with modulus X^4.
Its hypotheses hold even when the character is imprimitive. Averaging
64 bounds with factor 1/64 leaves

\[
 |C_j(\chi)|\le3\sqrt Q<769=B\quad(1\le j\le67).         \tag{11}
\]

The same lemma, without any subgroup restriction, gives
|R_chi|<=3sqrt(Q)<B. Thus the residual factor's complete sum is
retained and bounded, rather than dropped or replaced by a restricted
sum. The strict rounding follows from 9Q=589833<769²=591361.
All initially even, powered and twisted nonconstant characters are
covered by the same nonzero additive-vector argument.

**One absolute sieve, including its factorial.** The imported weighted
sieve applies to the symmetric weight product chi(r_x) on H^67.
For a permutation sigma with c_j cycles of length j it gives

\[
 67!W_\chi=\sum_{\sigma\in S_{67}}(-1)^{67-\sum_jc_j}
                                      \prod_j C_j(\chi)^{c_j}.
\]

Each subset has 67! ordered presentations. Retaining all lengths
1 through 67, (11) and the imported cycle identity imply

\[
 |W_\chi|\le\frac1{67!}\sum_{\sigma\in S_{67}}B^{\#cycles(\sigma)}
 =[t^{67}]\exp\left(B\sum_{j\ge1}t^j/j\right)
 =[t^{67}]\,(1-t)^{-B}=\binom{835}{67}=V.                 \tag{12}
\]

These are formal coefficients; no convergence or limit is used.
The rising binomial in (12) is essential. Taking absolute values in
(9) only after the exact constant-only cancellation gives

\[
 |M_{67}(A)-C/Q^3|
 \le\frac{(Q-1)(Q^3-1)}{(Q-1)Q^3}BV=(1-Q^{-3})BV.
\]

Together with the nonnegative correction in (2), this proves (3).
No favorable cancellation in the remaining characters or between
M_67 and N_68 has been assumed or estimated.

**Exact finite verdict and verification.** In reduced form the cap is

\[
 U=\frac{2211340517199957589162144257334337756937202012137649382601040951578025005970261168784407494466928772074809150947486720}
          {281487861809153}.
\]

Writing U=A_U/d_U, exact integer cross multiplication verifies

\[
 3676307\,Q^{28}d_U<2^{128}A_U
                     <3676308\,Q^{28}d_U,
\]

so the required ratio <=1 fails. This is a failure of the specified
upper allowance, not evidence that L_A or M_67 exceeds T. The main
arbitrary-center gap and the finite bracket remain unresolved.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/order_four_pole.py`.
The complete certificate is
`scripts/coefficient-fibers/order-four-pole-results.json`.
All 4143 checks pass, with no failures: two independent binomial
reconstructions, every unsigned cycle coefficient through 67,
character-count normalization and exact threshold comparison. The full
cap, principal term, error, threshold and positive failure margin were
inspected, with no floating-point comparison.

The small case is E=F_17, H=<9> of order eight, k=2 and five agreements,
with P=X^6+A and pole X^4. All 896 pairs (S,r) are retained: 280
repeated-root, 448 outside-H and 168 extra-agreement pairs. Exact
polynomial multiplication, descent signs, logarithmic multiplication
and supports are checked. All 756 occupied centers and one empty
center receive a separate enumeration of all 17² scalar messages;
the entire lists match, including incidence multiplicities and
M_5-5N_6. These finite checks support the algebra, rather than replace
the symbolic ambient-field, character or arbitrary-width proofs.

The separate arithmetic reconstruction command is
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/verify_order_four_pole.py`.
All 2488 independent checks pass in
`scripts/coefficient-fibers/order-four-pole-verification.json`:
unsigned Stirling cycle counts reconstruct every coefficient, full
integer arithmetic reproduces the cap and failure interval, elementary
symmetric sums reconstruct all 896 residual products, and independent
Horner evaluation of every message reconstructs all 757 entire lists
and corrections. This is computational verification; the separate
symbolic review follows.

**Separate critical audit, 2026-10-20 (step 377).** The approved
[audit coverage](../drafts/literature/2026-10-20-order-four-pole-critical-audit.md)
and its completed primary-source review were reused without changing
the imports or deriving a new estimate. No load-bearing defect was found.
The following checks retain the proof, with the original limitations.

For the forward map, the degree-68 leading coefficients cancel before
division by X^4; divisibility is coefficientwise, and the resulting
degree is at most 63. Equation (5) holds at every domain point because
zero is excluded. For the converse, division by a chosen monic g_S
takes place over F, but the quotient is monic linear and its constant
is fixed by a0. Equation (6) therefore proves descent without assuming
that an arbitrary ambient message already has coefficients in E.
The same chosen 67 columns force each other row to be zero. Evaluation
injectivity follows from 1024>63, so no distinction between messages
and codewords changes the count.

The multiplicity split is exhaustive: a polynomial counted by M_67
has at least 67 and at most 68 distinct H-roots. In the 67-root case
the only possible subset is that entire root set, even when the residual
root repeats one of its elements. A residual outside H supplies no
extra root. In the 68-root case every root is simple, the polynomial
is uniquely g_J, and each of the 68 omissions gives one pair. No
polynomial is counted by two distinct J. This verifies exactly
M_67=L_A+67N_68, including empty fibers; it does not justify replacing
the correction by 68N_68 or treating the incidence count as a list size.

The normalized truncated-log product and both inverse identities in
(7) hold coefficientwise over the rationals with denominators dividing
powers of 6, hence in E. The additional checker verifies these
polynomial identities before specialization. Consequently (8) exhausts
the characters of the full group of size (Q-1)Q^3. The residual r
ranges over all E*, so the constant-H subgroup is not the orthogonality
group in (9). The principal residual sum is Q-1. Every other
constant-only residual sum is exactly zero, even if its restriction
to H or a cycle power is principal.

For the remaining (Q-1)(Q^3-1) characters, multiplication of their
nonzero additive parameter vector by each j=1,...,67 is invertible
in E. Twisting by a constant-term character does not alter this vector.
Each of the 64 inner characters in (10) is therefore nonprincipal,
including imprimitive cases. The indicator has the correct sign:
eta(-x)=eta(x) since -1 belongs to H, and its average is 1_H(x).
At x=0 the unit character extended by zero contributes zero. Thus
Li–Wan Lemma 4.1 applies to every complete sum with the nonsquarefree
monic modulus X^4, using only its nonprincipal degree-one bound.
It also applies to the complete residual sum. The cumulative
trivial-on-field-units estimate and any full-domain subgroup
substitution are unnecessary. The factor 1/64 cancels the number
of twists, not the Fourier denominator.

The sieve uses a symmetric product weight on H^67. Each permutation
cycle imposes exactly its corresponding power, and each distinct
subset has 67! presentations. The unsigned cycle coefficient is
binomial(B+66,67), not binomial(B,67). The resulting nonconstant
character count divided by the full group size is exactly 1-Q^(-3).
Taking absolute values only after the constant-only zeros gives (3);
discarding 67N_68 is permissible because it is nonnegative. Nothing
in this bound controls its actual cancellation or supplies a lower
bound for a fiber.

The independent reconstruction was rerun: all 2488 checks passed.
The additional command
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/coefficient-fibers/audit_order_four_pole.py`
passes all 4294 checks, with no failures, and saves full evidence in
`scripts/coefficient-fibers/order-four-pole-critical-audit.json`.
It checks the manuscript's entire rational cap, both strict integer
cross products, all cycle coefficients and parameter counts, all nine
formal log/inverse coordinate identities, and every saved small-case
branch, descent sign, support size and incidence total. It also checks
that no center or message is duplicated in the saved lists. The
independent reconstruction checks the complete 896-pair universe,
every polynomial through elementary symmetric sums, all 757 saved
entire lists through all 17² messages, and all terminal corrections.
All 4143 constructor check records and 2488 reconstruction check
records were inspected programmatically in full, not inferred from
their previews. The small case remains evidence for the implementation,
not a substitute for the symbolic proof above.

Both strict cross products are positive, retaining (4) against the
required U/T<=1. The failed allowance remains parked. This audit
adds verification of an existing reproduction, not a stronger estimate
or progress beyond the inspected methods. Actual fiber maxima,
arbitrary-center safety, the ABF comparison and the 955–957 boundary
remain unresolved. C012a is still the only direct local mathematical
input; L099 and L100 remain contrasts. No dependency edge changes.

## Mathlib

Full fourth-order-pole dictionary, terminal correction, character-sieve
certificate and finite threshold result: **not checked** in Mathlib.
Supporting root/division, finite-field character orthogonality, truncated
logarithm and binomial facts: **not checked**. Unknown coverage is not
evidence of absence. The precise primary citations supply the known
counting and character/sieve tools. Pinned ArkLib definitions are present
as recorded in foundations/02; they specify the list model, not this
specialization.
