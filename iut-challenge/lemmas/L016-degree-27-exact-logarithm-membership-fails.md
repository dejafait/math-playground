# L016 — Degree-27 exact logarithm multiplication membership fails

## Hypotheses

Let K = Q_3(pi), pi^27 = 3, v_3(3) = 1, O = O_K and J = log(O^times). The logarithm is the convergent principal-unit logarithm, extended by log(-1) = 0. Put H = pi^14 O. No O-module structure on J is assumed. This is the fixed one-factor, beta = 1, scalar a = pi packet of the [prior SPECIALIZE assessment](../drafts/literature/2026-10-04-degree-27-logarithm-membership.md), not an original IUT initial-data instance.

Import the principal-unit quotient description from **Hess–Pauli–Pohst, Computing the Multiplicative Group of Residue Class Rings**, author-hosted 18-page manuscript, **§3, pp. 3–5**, and inverse log/exp above e/(p-1) from **Proposition 5.1(iii–iv), pp. 9–10** ([primary manuscript](https://page.math.tu-berlin.de/~kant/publications/papers/hepapo.pdf)). Only these inspected inputs and the standard continuous logarithm homomorphism are used; no cyclotomic image formula or withdrawn theorem is imported. The manuscript's date/publication identity is unspecified. L015 supplies H subset J, J subset pi^(-54) O, and the conditional radius-81 consequence of the inclusion tested here, with its source/family qualifications intact.

## Conclusion

The exact inclusion 18pi(O union J) subset J is **false**. An actual input witnessing failure is

\[
x=18\pi\log(1+\pi).
\]

For y = sum_(r=0)^26 c_r pi^r define the Q_3-linear functional

\[
\phi(y)=3c_0-\frac{31}{3}c_1+9c_{15}-9c_{18}.
\]

Then phi(J) subset Z_3, whereas

\[
\phi(x)\in-\frac{992}{3}+9\mathbb Z_3,
\qquad v_3(\phi(x))=-1.
\]

The proof certifies the complete logarithm image modulo H, rather than a sampled subgroup. It stops this sufficient membership mechanism in this packet. It supplies **no** coarse-orbit counterexample, actual orbit radius, original initial-data realization, or essential IUT flaw.

## Proof

### Imported filtration and complete image coverage

X^27-3 is Eisenstein, giving the degree-27 field and uniformizer pi. In its power basis the summands c_r pi^r have distinct fractional valuation parts, so v_3(y) = min_r(v_3(c_r)+r/27). Integrality is equivalent to every c_r in Z_3. Thus O = Z_3[pi], its residue field is F_3, and

\[
H=\bigoplus_{r=0}^{26}3^{d_r}\mathbb Z_3\pi^r,
\qquad d_r=\begin{cases}1&r<14,\\0&r\ge14.\end{cases}
\]

The imported deep log/exp theorem applies because 14/27 > 1/2. In the manuscript's integer valuation normalization this is precisely 14 > e/(p-1) = 27/2. Thus log(1+H) = H; we use this existing input from L015 and do not reprove the analytic inverse theorem.

Let U_j = 1+pi^j O. The imported quotient description identifies U_j/U_(j+1) with F_3. For each 1 <= j <= 13 the class of 1+pi^j represents its generator, since its leading coefficient is 1 in the residue field. Removing these thirteen successive classes writes every unit as

\[
(-1)^\epsilon\prod_{j=1}^{13}(1+\pi^j)^{\epsilon_j}u_{14},
\qquad \epsilon_j\in\{0,1,2\},\quad u_{14}\in U_{14}.
\]

The residue-unit signs have logarithm zero. The continuous homomorphism log has compact, hence closed, image J. Integer stability and passage to limits give Z_3-stability. Conversely every listed logarithm and H belongs to J. Consequently

\[
J=H+\sum_{j=1}^{13}\mathbb Z_3\log(1+\pi^j).
\]

This is the required specialization of the known unit-filtration method, not a reproof of the general unit-group theorem. No claim that arbitrary units multiply J into itself is involved.

### Controlled infinite tails and exact representatives

For j=1,...,13 let S_j = sum_(k=1)^242 (-1)^(k+1) pi^(jk)/k. For k in [3^h,3^(h+1)), h >= 5, each term has integer uniformizer valuation

\[
jk-27v_3(k)\ge3^h-27h.
\]

At h=5 the latter is 108 >= 14. Its successive increment is 2*3^h-27 > 0, and the bound tends to infinity. Hence the omitted series converges inside the closed ideal H, for every one of the thirteen j, proving log(1+pi^j)-S_j in H.

Here are all representatives q_j modulo H. A pair r:c denotes the coefficient c of pi^r; every omitted coefficient is zero.

| j | Nonzero coefficients of q_j |
| --- | --- |
| 1 | 0:16/9, 1:1, 2:1, 3:7/3, 4:2, 5:2, 6:1/3, 7:1, 8:1, 9:16/9, 10:2, 11:2, 12:5/3, 13:1, 15:2/3, 18:1/9, 21:1/3, 24:1/3 |
| 2 | 0:1/3, 2:1, 3:2, 4:1, 6:1/3, 8:2, 9:4/3, 10:2, 12:4/3, 18:1/9, 24:2/3 |
| 3 | 0:7/3, 3:1, 6:1, 9:7/3, 12:2, 18:1/3 |
| 4 | 4:1, 8:1, 9:1/3, 12:1/3, 24:1/3 |
| 5 | 3:1, 5:1, 10:1, 15:1/3, 18:1/3 |
| 6 | 0:1, 6:1, 9:1, 12:1, 18:1/3 |
| 7 | 7:1, 9:1, 21:1/3 |
| 8 | 8:1, 24:1/3 |
| 9 | 0:1, 9:1 |
| 10 | 3:1, 10:1 |
| 11 | 6:1, 11:1 |
| 12 | 9:1, 12:1 |
| 13 | 12:1, 13:1 |

These are exact finite rational congruences. Specifically, coordinate r of S_j is

\[
s_{j,r}=\sum_{\substack{1\le k\le242\\jk\equiv r\ (27)}}
\frac{(-1)^{k+1}3^{(jk-r)/27}}{k},
\qquad v_3(s_{j,r}-q_{j,r})\ge d_r.
\]

All 351 inequalities are checked with exact fractions by `python3 scripts/coarse-ideal/check_degree_27_membership.py`; the full finite sums, representatives and coordinate congruences are saved in `scripts/coarse-ideal/degree-27-membership.json`. For a reproducible residue rule, 9s_(j,r) is integral at 3: this follows also from L015's outer bound and the H-valued tail just proved. Reduce this rational number modulo 3^(d_r+2), inverting its denominator prime to 3, and divide its canonical integer residue by 9. This gives exactly the displayed q_(j,r). The script checks the congruences against the unreduced rational sums, rather than treating a displayed preview or numerical precision as evidence.

It follows that log(1+pi^j)-q_j in H. Every q_j belongs to J: subtract this H-valued error from the logarithm, using H subset J. Equivalently q_j = log((1+pi^j)exp(q_j-log(1+pi^j))), an actual unit logarithm by the deep inverse theorem. The complete image is therefore exactly

\[
J=H+\sum_{j=1}^{13}\mathbb Z_3q_j.
\]

This equality certifies all logarithm-image classes modulo H without needing to list the finite quotient element by element.

### A separator on the complete image and an actual infinite input

Substitution of the full table gives

\[
(\phi(q_1),\ldots,\phi(q_{13}))
=(0,0,4,0,0,0,0,0,3,0,0,0,0).
\]

On H only coordinates 0,1,15,18 can contribute. Their generator values are 9, -31, 9, -9, respectively, all integral at 3. Thus phi(H) subset Z_3, and the complete-image equality proves phi(J) subset Z_3.

Multiplication by pi sends coordinates (c_0,...,c_26) to (3c_26,c_0,...,c_25). Hence

\[
\phi(18\pi y)=162c_{26}-186c_0+162c_{14}-162c_{17}.
\]

For q_1 the latter three high-index coordinates are zero and c_0=16/9. Thus phi(18pi q_1) = -186(16/9) = -992/3, of valuation -1. For h in H, c_0 in 3Z_3 and c_14,c_17,c_26 in Z_3. Every term in this formula is in 9Z_3, proving phi(18pi H) subset 9Z_3. Since log(1+pi)-q_1 in H, the actual x satisfies phi(x) in -992/3+9Z_3. The numerator 992 is prime to 3, so this error cannot cancel the valuation -1. Therefore x is outside J, as asserted. Also 18pi H subset H directly by ideal valuation, and 18pi O subset H; neither is the failing branch.

### Exact membership computation and qualifications

For completeness the certificate tests all 40 generating columns (thirteen q_j and twenty-seven generators of H), plus all twenty-seven O generators, after multiplication by 18pi. It finds exactly one failing generator input, q_1; all other 66 tests pass. These supplementary membership checks use exact diagonalization over Z_3, not sampled units. At each stage choose an entry of least 3-adic valuation in the remaining rectangular matrix, swap it to the diagonal, and clear its column by row subtractions and its row by column subtractions. Every subtraction coefficient is in Z_3 by the minimal-valuation choice. Such subtractions and swaps are invertible over Z_3. Track the full row transformation U and column transformation V. The script independently verifies U G V = [D 0], for the original generator matrix G and nonzero diagonal D; it also verifies that the first twenty-seven columns of G V are dual to the rows of D^(-1)U, and that all original generator coordinates are integral. Thus membership is exactly integrality of D^(-1)U x. All transformations, lattice basis, generator coordinates, 67 membership coordinate vectors and failed coordinates are stored in full in the certificate. The separator above is checked separately on the displayed generators and proves the negative conclusion without relying on this diagonalization.

There are zero failed finite verification checks; one input fails the mathematical inclusion. Infinite tails and all-unit coverage are proved here, not inferred from the computation. L015's conditional radius-81 argument remains valid as an implication, but its sufficient premise is false in this packet. No new saturation theorem is established. The earlier ideal-sandwich upper radius 243 versus required 81 is not converted into a lower bound by this failure.

Classification is **POTENTIALLY_NEW** only in the bounded-search sense of the prior assessment: the inspected sources support the analytic and filtration inputs but do not decide this exact multiplication inclusion. No certified originality or progress beyond all existing literature is claimed. Original initial data, pilot transport, complete permitted images, essentiality, normalization and finite B >= A remain unresolved.

## Mathlib

Full degree-27 multiplication-membership failure and exact field-specific logarithm image: **not checked**. Supporting Eisenstein/local-field, unit-filtration, log/exp, valuation and lattice coverage: **not checked**. The primary citations above are supporting inputs, not matching Mathlib theorems; unknown availability is not evidence of absence.
