# Positive two-site update: source comparison1926

20 November 2026. Literature only; completes the saved review1925 target.
No kernel coefficient, determinant identity, derivative enclosure, lemma
or mathematical script is derived here. Approval concerns source coverage,
not correctness or success of an unimplemented calculation.

## Primary import and precise convention

A. M. Delgado, L. Fernandez, T. E. Perez and M. A. Pinar,
*Multivariate Orthogonal Polynomials and Modified Moment Functionals*,
SIGMA12(2016),090, DOI10.3842/SIGMA.2016.090,
[published primary PDF](https://www.emis.de/journals/SIGMA/2016/090/sigma16-090.pdf).
Read (2.3), (3.1)-(3.14), Theorem3.1 and its complete proof, pp8-10.
It assumes both original and modified functionals quasi-definite.
The proof covers lower-degree expansion, the finite-site system,
invertibility contradiction, norm formula and converse. Reuse1908/1920's
univariate interpretation. In row-vector convention its n=4, two-unit-mass
formula is

    v_4=(p_4(a),p_4(b)),
    q_4(x)=p_4(x)-v_4*(I_2+K_3)^(-1)*k_3(x),
    (K_3)_(i,j)=K_3(c_i,c_j), c=(a,b),
    k_3(x)=[K_3(a,x),K_3(b,x)]^t,
    K_3(s,t)=sum_(j=0)^3 p_j(s)p_j(t)/h_j.

The p_j are base monic polynomials; h_j are base squared norms.
This is the cited formula with N=2,Lambda=I_2, imported without reproof.
It gives exact invertibility, not interval widths or derivative bounds.

## Applicability and input scope

C028t already verifies the positive full-theta base and two positive unit
atoms, meeting the theorem's hypotheses. Sites remain distinct on B.
Dividing the modified measure by3 changes no monic polynomial. No
exterior-support or zero-monotonicity theorem is needed; the interior-site
warning1920 remains. No actual-root reality is assumed.

Reuse Gautschi2004 Section2.1.1 Theorem2.1, pp52-54, with full statement
and proof inspected1920. Base p_0,...,p_4 need moments through7;
h_0,...,h_3 need moments through6. Odd base moments are zero. Reference
input therefore remains I_0,I_2,I_4,I_6, with no h_4 or reference order8.
Actual quartic input still includes I_8 and its factorial conversion as in
C028u. These are formula index checks, not computed coefficients or bounds.
Every base Gram/norm division still needs a rigorous enclosure.

The kernel definition exposes positive Gram structure. A later calculation
may use the standard Cauchy--Binet formula for Gram determinants to retain
it. The finite algebra and resulting divisor certificate must be written
and verified during research. No positive determinant expansion or
numerical lower bound is established here. Direct interval subtraction
in a 2x2 determinant can still lose positivity; exact nonsingularity
alone is not a usable interval reciprocal.

The source is pointwise in the sites. C028t already justifies smooth
coefficient dependence by its nonsingular moment system. Ordinary finite
polynomial, product, quotient and inverse-matrix differentiation suffice
for this representation; retain both kernel evaluation arguments and
all normalization terms. No integral differentiation is required. Complete
formulas and full-collar enclosures remain work, not imported bounds.

## Quantitative coverage and bounded test

Reuse source-notes1924's full statement/proof assessment of Rump,
*Verification methods*, Acta Numerica19(2010), Theorem13.3,(13.1)-(13.9),
corrected author PDF pp87-89, and range inclusion (5.16)-(5.17).
Its hypotheses do not change with representation. A complete box-Jacobian
and all paid divisors must precede strict inclusion. Point rank or a
midpoint target cannot replace these obligations.

Keep B=[-1/4,1/4]x[3/4,5/4], x0=(0,1), both signs and the unchanged
f_e=(e*g-gamma,k-k_actual). Reuse1924's deterministic point-Jacobian
midpoint inverse choice and strict inclusion threshold. Certify base
norms, update divisor and V before reciprocals. At most one whole-box
range/Krawczyk attempt per sign; no solver, subdivision, sweep, radius/mass
change or source refinement. An unpaid bound or failed sufficient test
stops this representation inconclusively. Exclusion of both signs excludes
only B; inclusion gives conditional matching via C028u's affine equivalence.

## Reuse, duplicates and decision

Read source-notes1908/1920/1924, C028t's construction, C028u's complete
statement/proof, working1925 and its named ATTEMPTS/history records.
The exact-image searches1924 remain adequate: family, observables and
target are unchanged. The new primary check addresses the changed
evaluation; no new search quota or originality inference. No inspected
source supplies this theta collar image or uniform full-cost bound.
The failed Cramer enclosure does not exclude a different evaluation.
All scalar/width/H2/cost stops remain; no cross-notebook input is used.
Optional PDF screenshots failed, but complete primary theorem/proof text
was accessible; no essential hypothesis or proof case remains blocked.

Decision: SPECIALIZE for exactly review1925's saved target, ordinary
reproduction/development; full matching Mathlib coverage unchecked.
No mathematical certificate was run or enlarged. Complete1925 evidence
remains unchanged and must be inspected as needed before numerical reuse.
Essential inputs: C028a/d/q/t/u,L019/L021,L917/audit197,L037 and unchanged
panel0 moments. Analytic containment and Decimal correctness remain
conditional. A match could remove two degree-four residuals; lower
residuals, all-degree signs, full costs and H_d=o(d) remain open.
No justified central creative mechanism is supplied: a concrete signed
full-cost estimate uniform in degree remains missing.
