# Step576 working checkpoint — 12 November2026

Approved unchanged assessment562/approval563; RESEARCH/REPRODUCTION.
Main gap: L030-L032/C032a actual-Xi positivity. Intermediate target:
C999m(71) eta_action<=.002645 with K=65536, original predictor,
reference and allocation. Downstream use: finish the finite exact-map
connection for the fixed mixed quarter comparison; complementary
coercivity and all global obligations remain independent.

Plan: enclose the full finite T matrix using Section16(67) and its exact
diagonal cases, reusing pinned complete prime aggregates575. Compute
both T Vhat_c and T* Vhat_c by complete dense block products, retaining
all raw rows and1020 columns. Bound the entire entry uncertainty by its
Frobenius radius, all dense-product and block-addition rounding by the
inherited IEEE754 dot-product contract. Compare to the exact dyadic
Dhat575-W_hat565 with subtraction rounding paid. Apply exact weighted
neutral coordinates using the complete572 ratio and weight enclosures.
No FFT accuracy theorem is used. Save full ledgers, source/input hashes
and arrays. Stop after this one test: unpaid errors or overlap are
inconclusive, a proved complete upper bound pays the component. No
parameter/reference/allocation tuning. Sections12-16 remain unaudited.

Full proofs/certificates remain canonical in C999m and scripts/separation-seven;
this is unfinished reasoning, not a proved bound. All prior work is preserved.

## Prospective proof ledger (unfinished until full execution is checked)

Let C be the exact dyadic finite matrix assembled blockwise as centers
of the full prime-part T intervals, on raw0:65535. Let e_i and F_i be
upward Frobenius bounds for interval radii and centers in each128-row
block. Then e_T=(sum e_i^2)^(1/2) bounds the entire matrix error and
F_C=(sum F_i^2)^(1/2) bounds ||C||_F. Distinct output rows are orthogonal;
no within-row translation contribution is squared separately. For
V=Vhat_c exactly as saved in565, F_V>=||V||_F, the prime-part action
error in either orientation is <=e_T F_V. The transpose uses the same
finite matrix, not a separate approximate adjoint.

Compute TV by128-row full65536-term products. Compute T*V by the
sum of C_i^t V_i over all raw row blocks. V_i=0 on0:511 exactly.
The inherited dot-product contract bounds rounding in either final
product by gamma_(2K+32)(F_C F_V+1): the direct path has lengthK,
and the transpose path has128-term products and at most512 additions.
All paths including the later seven continuous additions have length
less than2K+32. This deliberately overcounts multiplication/addition
rounding and retains the inherited negligible-underflow qualification.

The continuous part uses ALL seven terms of Section16 in factored
form a_j b_j^t, with the exact prefactor absorbed into a_j. If centers
are ac,bc, Frobenius radii ea,eb and center norms Fa,Fb, the entire
operator discrepancy is <=ea(Fb+eb)+Fa eb. This follows by expanding
(a-ac)b^t+ac(b-bc)^t. Every finite K-term product bc^t V and ac^t V,
outer multiplication and output addition is charged by
q_j=[ea(Fb+eb)+Fa eb]F_V+gamma_(2K+32)(Fa Fb F_V+1).
The complete remaining continuous operator is bounded by Section16's
geometric tail 3^(-49.5)/(16.5(1-3^-6)). No entrywise tail truncation
is mistaken for an infinite operator bound. Include an additional
positive gamma_32((F_C+sum Fa Fb)F_V+1) for addition slack.
The sum of prime entry error, prime product allowance, sum q_j,
addition slack and the complete continuous tail times F_V is a valid
single-orientation error E. The pair error is <=sqrt(2)E; the matrices
are real, so these same operator bounds apply to complex head inputs.

Let Ahat=(fl(T*V),fl(TV)) be the resulting complete saved dyadic pair.
The target difference Dhat575-W_hat565 is the EXACT difference of
its saved dyadic arrays. Evaluate delta=fl(Ahat-fl(Dhat-What)). For
each128-row rectangle in each orientation, its subtraction error is
bounded by gamma_8(F_Ahat+F_Dhat+F_What+1). Aggregate tail rectangle
errors in quadrature, multiply by1/2 since1/sqrt(d_n)<1/2, and add
alpha times the combined two-low-row subtraction error, with alpha
from(70). This pays both floating subtractions, including cancellation.

Using the pinned572 tables, let rhat have |rhat-r|<1e-20 and let t be
the exact upward dyadic weight1/sqrt(d_n)<=t<1/2. Evaluate every
weighted dyadic difference row fl(t_n fl(delta_n-rhat_n delta_p)).
For a rectangle its discrepancy from the exact t-weighted row is
<=.5[1e-20 F_repeated_low+gamma_16(F_delta+1e-5 F_repeated_low+1)].
Aggregate these bounds in quadrature over disjoint tail rows and
orientations. Use upward Frobenius norms throughout, not previews.
If W is the Frobenius norm of all weighted evaluated rows, E_sub
and E_coord these two complete error ledgers, then C999m(7),(65) and
M_cert>=mu I give

 eta_action <= [W+E_sub+E_coord+zeta sqrt(2) E]/sqrt(mu), mu=.000999.

The zeta term uses the exact weighted neutral map and pays the whole
finite action error, including low outputs. Upward t only dominates
the true weighted Frobenius norm of the evaluated dyadic differences;
there is no assumed neutral raw projection or boundary evaluation.
A complete bound <=.002645 would pay(71); before that full check no
numerical conclusion follows. Sections12-17 require separate audit.

## Completed outcome

Production1567 and complete-evidence3596 checks pass. Full eta_action
<.000002142174<.002645; combined finite covariance<.083901959 M_cert
and mixed norm<.497655<1/2 under inherited contracts. Canonical proof
and all qualifications are in C999m Section17; full artifacts have
basename scripts/separation-seven/signed-mixed-inverse-action-576.
The separate evidence inspector has basename signed-mixed-inverse-action-check-576.
Sections12-17 remain unaudited; independent complement coercivity and
all global gaps remain. Next is the separately approved conceptual
audit nominated in assessment577. Earlier prospective notes are preserved.
