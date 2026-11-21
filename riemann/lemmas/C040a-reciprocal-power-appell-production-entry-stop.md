# Corollary 40a: a negative reciprocal-power Appell production entry

## Hypotheses

Use the actual Xi moments of L021, reciprocal-zero power sums S_k of
L025, S_2>0 from L027, and Newton recurrence of L040. Use the ordinary
coefficients a_j of G(w)=xi(1/2+sqrt(w)/2)/8 in L776. For the numerical
conclusion retain L778's audited polynomial evaluator, uniform complex
analytic error, and trusted Decimal/transcendental software contracts.
The new finite arithmetic uses exact integer/Fraction operations with
outward rounding; it does not independently attest that evaluator or its
backend. No RH, real-zero, zero-list, positive-measure or mixed-form
positivity hypothesis is made.

Define m_n=S_(n+2)/S_2 for n>=0, the formal series
M(t)=sum_(n>=0) m_n t^n/n!, and the lower triangular array
R_(n,k)=binom(n,k)m_(n-k) for 0<=k<=n, zero otherwise.
Let Delta delete the first row, and P=R^(-1) Delta R.
All these products are formal: R has diagonal one, its inverse is lower
triangular, and each entry in this product uses a finite sum.

## Conclusion

The single production entry satisfies

\[
 P_{2,0}=\frac{S_5}{S_2}
          -3\frac{S_3S_4}{S_2^2}
          +2\frac{S_3^3}{S_2^3},
\]
\[
 -0.000000004398201602576945
 \le P_{2,0}\le
 -0.000000004398201602576944<0.                 \tag{1}
\]

Thus P is not totally positive in the convention that every minor is
nonnegative. This rejects this particular Appell production-TP sufficient
construction. It does not reject Hankel positivity, other production
arrays, or RH. The computation passed its finite consistency checks
and the separate finite arithmetic/proof audit in step777 below. This is a
known-method specialization and informative route obstruction, not a
claim of mathematical novelty beyond the checked sources.

## Proof

**Known production criterion and its scope.** Alan D. Sokal, *Total
positivity of some polynomial matrices that enumerate labeled trees and
forests I: forests of rooted labeled trees*, Monatshefte fuer Mathematik
(2022), [DOI 10.1007/s00605-022-01687-0](https://doi.org/10.1007/s00605-022-01687-0),
[published primary PDF](https://discovery.ucl.ac.uk/id/eprint/10144793/1/Sokal2022_Article_TotalPositivityOfSomePolynomia.pdf),
Theorem 2.19, equations (2.33)-(2.35), PDF pp.22-23, gives the
production entries of an exponential Riordan array [F,G] over a
commutative ring containing the rationals:

\[
 p_{n,k}=\frac{n!}{k!}(z_{n-k}+k A_{n-k+1}),\quad
 Z(s)=\frac{F'(\overline G(s))}{F(\overline G(s))},\quad
 A(s)=G'(\overline G(s)).                           \tag{2}
\]

The coefficients of A and Z here are **ordinary** coefficients, and
negative indices vanish. The hypotheses F(0)=1, G(0)=0, invertible
G'(0), and invertible array diagonal hold for F=M,G=t over R because
m_0=1. Its columns n! [t^n] {M(t)t^k/k!} equal the defined R entries.
Thus A=1 and Z=M'/M, with no convergence or measure assumption.
The lower-Hessenberg P is row-finite. Under the additional, unpaid
hypothesis that all its minors are nonnegative, Sokal's Theorem 2.14,
PDF p.19, implies total positivity of the zeroth-column Hankel matrix
of its output R. That column is m_n, so multiplication by S_2>0 would
give the corresponding S_(i+j+2) Hankel minors. This known implication
motivates the diagnostic; it is not a positivity premise here. Neither
Theorem 2.20 (which assumes F=1) nor any converse is used. The general
theorems are imported, not reproved; the actual entry and coefficient
normalization are the necessary specialization.

**The complete finite entry identity.** Write
M=1+m_1 t+m_2 t^2/2+m_3 t^3/6+O(t^4). Formal division gives

\[
 M^{-1}=1-m_1t+(m_1^2-m_2/2)t^2+O(t^3),\qquad
 [t^2]\, (M'/M)=m_3/2-3m_1m_2/2+m_1^3.
\]

Equation (2) with n=2,k=0 multiplies this by 2!, proving
P_(2,0)=m_3-3m_1m_2+2m_1^3. There is a direct indexing check:
the leading three rows/columns of R and the needed inverse row are

\[
 \begin{pmatrix}1&0&0\\m_1&1&0\\m_2&2m_1&1\end{pmatrix},
 \qquad (R^{-1})_{2,0:2}=(2m_1^2-m_2,-2m_1,1).
\]

Column zero of Delta R in rows 0,1,2 is (m_1,m_2,m_3)^T.
Their product gives the same entry, including all three terms. No
other production entry or minor is evaluated. Substituting the m's
gives the conclusion's identity.

**Actual theta coefficients and every error.** L776 gives
a_j=M_(2j)/(8*4^j*(2j)!), while L040 uses
e_j=M_(2j)/((2j)!M_0). Therefore

\[
 e_0=1,\qquad e_j=4^j a_j/a_0\quad(1\le j\le5).       \tag{3}
\]

In particular these e_j are neither the raw a_j nor the factorial-scaled
gamma_j used for the different L791 model. The inherited complete record
is `scripts/actual-fredholm/fixed-pair-certificate-431.json`.
Its evaluation/coefficients enclose the exact polynomial P_0 defined by
L778's finite theta integrals, including its cell integration errors.
L778 proves for the analytic difference on the entire closed disk

\[
 |G-P_0|\le E_G<3.141\,10^{-48},\qquad |w|\le1600.
\]

Cauchy's coefficient estimate adds the symmetric error
E_G/1600^j to the saved coefficient interval at **each** j=0,...,5.
All six complete input intervals and the complete error interval were
inspected; index 5 is taken directly from this evaluator, rather than
extrapolated from L791's five gamma intervals. Before use, the current
source hash was matched against L791 and the step433/478 audit records,
and the entire evaluator record was compared with the step433 replay.
The saved audits report PASS and empty failures; their relevant full
checks and expected Inexact/Rounded flags were inspected. This reuses
their analytic/software conclusions and is not a new evaluator audit.

Starting from (3), apply the justified finite L040 recurrence exactly
through k=5:

\[
 S_k=\sum_{j=1}^{k-1}(-1)^{j-1}e_jS_{k-j}
                  +(-1)^{k-1}ke_k.                       \tag{4}
\]

The a_0 interval is strictly positive. The computed normalization obeys

\[
 0.000037172599285269686164\le S_2
              \le0.000037172599285269686165,
\]

so every division in (3) and the m normalization excludes zero.
This also agrees with the independent qualitative L027 input.

**Finite certificate and reproducibility.** Run
`python3 scripts/central-jacobi/appell_production_entry_775.py` from
the notebook. The full certificate is
`scripts/central-jacobi/appell-production-entry-775.json`.
It saves input/program hashes, all six raw coefficients, each exact
Cauchy-error upper bound, corrected a_j, all e_0,...,e_5 and S_1,...,S_5,
the normalized m's, inverse row, three entry enclosures, actual/required
thresholds, every check and any failure. The current run has 31 checks,
PASS, and no failures. No transcendental evaluator was run or changed.

The imported Q operations in `scripts/central-jacobi/audit_478.py` use
exact Fractions and outward rounding on the 10^(-100) grid: addition
adds endpoints, multiplication takes the extrema of four endpoint
products, and reciprocal reverses endpoints of a zero-excluding
interval. Integer floor/ceiling then enlarges each image. Negation
reverses endpoints exactly. These operations enclose correlated inputs
by enlargement; they never presume independence. The prescribed six
coefficient errors are retained before any normalization or recurrence.

Evaluating the entry formula gives (1). A finite triangular inverse
recurrence separately computes the needed inverse row and the same
matrix entry, with a strictly negative enclosure. Also the complete
numerator S_5 S_2^2-3S_3 S_4 S_2+2S_3^3 has a strictly negative upper
endpoint, and division by the positive S_2^3 gives another strictly
negative enclosure. Both overlap the first; these are finite arithmetic
consistency checks, not independent analytic verification. The complete
relevant output endpoints and checks were inspected, not just previews.
Since a 1-by-1 minor of P is negative, TP fails, proving the restricted
stop. Other minor signs, other arrays, actual-Xi mixed positivity in all
degrees, and RH remain unresolved. L057's finite-test obstruction and
L825's centered-factor lowering obstruction have different hypotheses
and are comparisons, not premises of this calculation.

**Independent finite audit, 13 November 2026 (step777).** The unchanged
SPECIALIZE assessment775 covers this audit. No general theorem or new
entry was investigated. The formal array has diagonal m_0=1 and its
column k is n! times the coefficient of t^n in M(t)t^k/k!. Hence it
is the exponential Riordan array [M,t] with the source's ordinary Z
coefficients. Row deletion in P=R^(-1) Delta R makes column zero of
Delta R equal to (m_1,m_2,m_3,...)^T. Solving the first three entries
of row2 of R^(-1) gives exactly (2m_1^2-m_2,-2m_1,1), so both the
source formula and direct multiplication give the stated P_(2,0).
The diagonal is invertible and each product entry has only finitely
many terms. No convergence of M, positive measure, converse production
criterion or extra Fredholm zero-count hypothesis is needed. Only
L776's unconditional coefficient normalization is used from that lemma.

L021/L776 give a_0=M_0/8 and a_j=M_(2j)/(8*4^j*(2j)!), proving
(3) with e_0=1 exactly. L025's locally convergent logarithm and L040
justify all five finite Newton steps, including the alternating signs
and final factor k in (4). No RH hypothesis enters that recurrence.
L778's P_0 is the polynomial of exact finite integrals; its saved
coefficient intervals already contain every cell integration error.
The analytic difference G-P_0 is bounded on the whole complex disk,
so Cauchy's formula on its radius1600 boundary adds precisely
[-E_G/1600^j,E_G/1600^j] at each j=0,...,5. In particular index5 is
present in the full L778 record and has its own nonzero error addition;
the L791 five-coefficient comparison is not used to supply it.

Run `python3 scripts/central-jacobi/appell_entry_audit_777.py`.
This separate implementation imports no local code, Q arithmetic or
step775 run function. It uses pairs of exact Fractions, endpoint
addition, sign reversal, the extrema of four products, and the extrema
of four direct quotients for a denominator interval excluding zero.
For fixed nonzero denominator, division is linear in the numerator;
for either fixed numerator endpoint it is monotone in the denominator
on a zero-excluding interval. Thus the four corners bound its image.
Each operation then replaces endpoints l,u by
floor(10^110*l)/10^110 and ceil(10^110*u)/10^110. The defining integer
inequalities prove outward enlargement, including negative endpoints.
Thus every operation encloses its image; repeated use remains valid
for correlated inputs. This is independent finite arithmetic with a
different grid and direct division, not a rerun of the original code.

The complete audit evidence is
`scripts/central-jacobi/appell-entry-audit-777.json`: PASS, 100 checks,
empty failures. All six raw coefficients and Cauchy-error fractions
match the original inputs. Independently reconstructed corrected
a_j, e_0,...,e_5, S_1,...,S_5 and m_0,...,m_3 are contained in their
original exact intervals. Both a_0 and S_2 have positive lower endpoints;
the computed S_2^3 denominator also has positive lower endpoint.
The explicit inverse-row product, the entry formula and the power-sum
numerator divided by S_2^3 each have negative upper endpoint and are
contained in their corresponding original exact enclosures. The
numerator itself has negative upper endpoint. The independent entry
and S_2 intervals are contained in the displayed bounds (1) and the
displayed S_2 bounds above; this checks containment, not mere overlap.
The complete relevant endpoints, e/S values and all checks were
inspected. Consequently the same strict negative 1-by-1 minor and the
restricted construction stop pass this audit without a changed bound.

The audit matches all step775 input hashes, the step433 evaluator and
saved-data checker program hashes, the L791/step478 source provenance,
and the entire evaluator record against the step433 replay. The saved
step433/478 checks and expected Decimal flags were inspected. All
original inputs and evidence remained byte-identical. This reuses the
audited L778 analytic proof and trusted evaluator/backend contracts;
it does not rebuild or independently attest the transcendental backend.
This is local validation of a known-method route obstruction, with no
claim beyond the checked sources and no added all-degree sign input.

## Mathlib

Full matching coverage is unchecked; no presence or absence claim is
made for this specialized production-entry obstruction. The cited Sokal
theorems and the named Cauchy coefficient estimate are informal inputs.
The inherited evaluator and backend have not been formally verified.
