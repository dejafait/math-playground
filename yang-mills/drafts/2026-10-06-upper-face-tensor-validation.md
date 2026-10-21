# Upper-face tensor implementation — working record

STEP_ID: YM-20261006-047-upper-face-tensor-validation

Reuse the unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md` for the exact saved
combined-response target. Main gap: the interacting continuum
construction and ultraviolet-uniform reflected comparison. Intermediate
target for this bounded implementation step: reproduce the complete
cutoff-12 pure-sector sums by L033's double-Laplace/tensor contraction,
without allocating a seven-index array. Downstream use: enable evaluation
at the same high cutoff as L033's full spectral-tail bound, before any
signed power-term or compensation test. Essential inputs: L008 and
L030–L033 and the existing continuum finite-sum implementation.

Continuation test: compare separated heat kernels with direct dense
contraction at fixed heat times, then compare each pure sector and its
axial-zero/positive parts with the saved finite-cutoff sums. Use explicit
relative/absolute tolerances; failure stops larger-cutoff use until
corrected. Even success gives only an implementation diagnostic: no
certified coefficient quadrature, double-integral enclosure or rounding
bound is assumed. Preserve all previous work and ATTEMPTS/011–015;
the failed lattice global-norm mechanism is not reopened.

Unfinished reasoning saved before implementation: expand the already
defined weak Q and N monomials and multiply corresponding component
entries. For each monomial pair, four one-dimensional matrix products
contract independently against exp(-s omega^2 k_j^2) and
exp(-r omega^2 ell_j^2). Sum all four second-index components, retaining
the even axial frequencies and the zero frequency when admitted.
Combine identical monomial products with exact rational coefficients.
Integrate s,r in a finite log-time window using composite Gauss–Legendre
rules, whose convergence is diagnostic only. Check the approximations
to both inverse weights over the actual finite eigenvalue range.

Independent unresolved gaps: certified finite coefficient integrals,
time integration and rounding, I_3/I_6 and their full compensation,
other plaquettes/pairings, action/measure/insertion/flow jets, L019,
finite matching, reflected error <= c_box/2 on a prescribed trajectory,
continuum fields, full reflection positivity, infrared control and finite
positive mass. None is a premise. Known flow/matching inputs are reused
by the saved assessment; no general source theorem is reproved here.

## Completed bounded implementation and evidence

Outcome: EXPLORATION / RESEARCH / REPRODUCTION; actual task implementation.
The new `scripts/combined-ward-response/check_continuum_tensor.py` applies
the already proved L033 identity. Canonical proofs and qualifications
remain L008 and L030–L033; this step adds no lemma, mathematical source
import or claim of originality. Mathlib coverage of the full computation
and supporting numerical integration is not checked; it is not formalized.

For each pure potential and second-index component, the program combines
monomial-product coefficients with exact fractions. Its numerical tables
reuse the existing one-dimensional coefficient integrals. If A_j,B_j
are the two weak-monomial matrices, it contracts their entrywise product
against the left/right heat vectors in coordinate j, then multiplies the
four scalar factors, exactly as L033 section 4 specifies. Restricting the
left component to 1 and its axial index to zero is the definition of Z,
not a new projection. Positive left axial derivatives vanish identically.
All second-index components are retained; its even axial frequencies
follow L032. The zero/positive axial parts are reported separately.
Triplet component 3 has no surviving weak products in either potential;
shear component 3 is retained. The code imposes no sign on the products.

The four-dimensional mode sum uses only one-dimensional frequency-pair
tables of at most (M+1)^2 entries and heat-time tables. For P time nodes
and the fixed finite monomial expansion, storage scales as O(M^2+P^2),
with at most 32 product terms in a temporary batch. This statement concerns
the new tensor evaluator; the small-cutoff validation function deliberately
calls the old dense assembler at M=4 only. No large-cutoff run was made.

The time integration uses s=tau exp(z), r=tau exp(v), including the
Jacobians s(s-tau) and r. Its finite upper endpoint is
tau+80/(3(pi/8)^2)=172.9839867495898, with 16 equal log-time panels.
Degrees 8 and 12 per panel give 128 and 192 nodes. Coefficient integrals
use the existing degree-96 rule on its four subintervals. All numerical
values are binary64 diagnostics, with no rigorous quadrature, finite-time
tail or rounding enclosure. Checking the inverse weights on every integer
squared-frequency sum between 3 and 4M^2 covers a superset of the finite
mode eigenvalues, but the computed discrepancies are not certified bounds.

Reproduce this bounded check with:

```sh
OPENBLAS_NUM_THREADS=1 python3 scripts/combined-ward-response/check_continuum_tensor.py --cutoffs 4 12 --time-degrees 8 12
```

Full evidence: `scripts/combined-ward-response/continuum-tensor-certificate.json`.
The complete relevant `/heat_checks`, `/rows/3`, `/rows/2/inverse_checks`
and `/failures` were inspected with the supervisor JSON inspector using
`--full`. The fixed-time check at M=4 tests all eight pure-sector/axial
parts on the 3-by-3 grid s=(tau,0.2,1), r=(tau,0.35,1.5), including
the smallest heat times. The largest |tensor-dense|/(1+|dense|) is
8.24674414620e-15, against required <1e-10. This compares independently
assembled contractions while sharing the weak expansion and coefficient
integrals; it cannot detect an error common to those inputs.

At M=12, degree 12 reproduces every saved sector part within
4.54747350886e-13, against its componentwise tolerance
1e-8+1e-9|reference|. The totals are
(290.672016725872,1854.720139834544). Refining time degree 8 to 12 changes
any sector part by at most 4.54747350886e-13. The corresponding maximum
relative inverse-weight discrepancies are (1.33e-15,1.33e-15), against
required <1e-11; degree 8 gives (1.09e-14,1.11e-15). There are no recorded
failed checks. These are reproductions of finite-cutoff numerical values,
not a new mathematical advance or evaluated infinite I_i.

The continuation test passes for implementation agreement only. A
materially larger retained sum can now be attempted without a seven-index
allocation; at M=112 the inherited coefficient/time rules must be checked
again, rather than treating small-cutoff accuracy as uniform. The next
bounded subtask within the unchanged approved response target is a
cutoff-112 tensor evaluation with coefficient/time refinement and the
inverse-weight diagnostics at that cutoff. The purpose is to determine
whether the high-cutoff calculation is numerically feasible before trying
to certify it. Any diagnostic discrepancy beyond its tolerance stops use
of that rule and must be preserved. A sign still requires a certified
retained value at 112 together with all numerical error bounds and L033's
tail at the SAME cutoff. L019 compensation, other vertices/pairings,
the complete logarithm and the reflected-error threshold remain open.
Mathematical exploration usage is 1 of 3 after L033; historical exhausted
branches retain their stop evidence. The approved target and review are
unchanged, so no new continuation assessment is written or self-approved.
