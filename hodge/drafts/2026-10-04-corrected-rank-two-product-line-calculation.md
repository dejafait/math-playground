# 2026-10-04 — Corrected rank-two product-line index calculation

The turn-start SPECIALIZE
[assessment](literature/2026-10-04-corrected-point-rank-two-integrality.md)
explicitly preapproves the exact saved product-line HRR target.
No new literature work is needed. The gap is an actual compatible
representative reaching the fourth NS-fixed RM direction. The
intermediate test asks whether all integral product-line indices
eliminate any of L048's surviving corrected rank-two characters.
An empty region would stop these data; surviving data still require
finite-rank realization, local freeness, stability and transport.

L045's fixed K-class exclusion, L046's unchanged-data exclusion and
the presentation stops do not answer this changed-character test.
L048 supplies the forced character, including the full transcendental
square contribution to its fourth component. Its untwisted test is
not repeated as a new result.

For corrected pure coefficients p=4+a,t=4+b and an actual product
line bundle with factor Chern classes x,y, put m=q(x,x)/2,
n=q(y,y)/2 and k=integral_X tau_D (x tensor y). Surface HRR makes
m,n integers; integrality of the full mixed class makes k an integer.
The product-line HRR expansion is

\[
I_{a,b}(x,y)=2(m+2)(n+2)+p(n+2)+t(m+2)+k+(pt+78)/6.
\]

Its difference from the untwisted value is
(t+4)m+(p+4)n+2mn+k, always an integer. Thus every product-line
index has the same fractional part, and all of them are integral
exactly when 6 divides pt. No correction pair passing L048 can be
removed by this filter. The full proof is stored in
[L049](../lemmas/L049-corrected-rank-two-product-line-indices.md).

Decision: an informative NEGATIVE for further filtering by these
indices, classified as REPRODUCTION of the assessed HRR and character
tools. It supplies no additional algebraic class or RM direction.
The span remains 21 and the attained directions three against four
required. No complete Hodge candidate is present.

Verification: independently multiplied the truncated
K3-product cohomology classes using
`scripts/cubic-kahler/check_corrected_rank_two_product_line.py`,
and compared with the formula on all 36 pure-coefficient residue
pairs and 64 divisor-twist pairs from the full fixed rank-four
lattice. All 2304 checks passed, including twists outside W; the
same 15 residue pairs survive. Three actual-region fibre/section
twists give 9, 4 and 17/2, in agreement with the proof. The general
assertion uses the integral difference, not a finite sample.

The required checker
`python3 ../scripts/docs/check_structure.py --problem hodge` passed
with 50 nodes and 110 unique edges. Checkpoint fields are unique;
the completed target has exact prior ready coverage and the new
target exactly matches its REVIEW_REQUIRED assessment. The original
assessment and all 287 existing local artifacts other than the three
current overview/checkpoint/DAG files are unchanged; six new step
artifacts were added and none deleted. These checks certify structure
and arithmetic, not bundle realization or the Hodge conjecture.
