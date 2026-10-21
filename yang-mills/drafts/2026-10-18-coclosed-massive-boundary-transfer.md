# Co-closed massive boundary transfer — completed attempt and continuation

Approved target: Assess whether L090's complete co-closed/co-closed rough-sector trace T_hh is O(N^(5/2) log(eN)^2) for both actual probes.

Reuse the unchanged EXPLORE assessment
`literature/2026-10-17-coclosed-sector-quantitative-remainder.md`.
The main gap is interacting cutoff removal with reflected error
<=c_box/2, continuum axioms and finite positive mass. The intermediate
test is L228(23), both localized finite-to-bulk factor comparisons at
epsilon=N^-1 and delta=N^(-4/3). Success would combine L226 and L228
into the proposed complete-sector rate, leaving all other component
rates and interacting estimates independent.

Saved before proof work: use L205's already proved mass-uniform
Chebyshev inverse residual on the common spectral interval [0,16].
Approximate both massive inverses, including the vertex inverse inside
each Q_delta, by degree O(N^(2/3)log(eN)) polynomials with sufficiently
small absolute error. Keep Q H R Q^2 in its original order. Its entire
polynomial product has range o(N). On either side of the compact
generator selector every path should stay inside the box, where finite
relative and whole-grid stencils, and L228's coefficient samples,
agree. Local rank O(N^4) converts operator error to Hilbert--Schmidt
error. No covariance input row is removed. This is a prospective
argument, not yet an established comparison.

Continue if both adjoint-side errors are <=C p(k)sqrt(N)log(eN)^2;
abandon this absolute transfer if its actual polynomial error or
total range misses that budget without a justified repair. Check the
vertex/edge rectangular spaces, normal end rows, all three Q factors,
both trace orientations and whole-grid source rows. L205's old
covariance-leg theorem is not directly a theorem about this product;
only its uniform scalar polynomial residual and finite-path method
are reused. L109/ATTEMPTS/032 and ATTEMPTS/030 remain retained stops,
not bans on squared moments or uniform varying-mass comparisons.

Essential inputs: L003 L009 L088 L089 L090 L205 L225 L226 L227 L228;
inherited L018 L026 L028 L085 L086. Upstream L225--L228 critical
audits remain pending. No new source review, numerical script or
supervisor-state change is made. Mathlib coverage is not checked.

## Completed result

[L229](../lemmas/L229-coclosed-two-sided-massive-boundary-transfer.md)
proves both comparisons, by approximating all four inverse-bearing
factors of Q H R Q^2 in their original order. The common degree is
ceil(60 N^(2/3)log(eN)), the inverse residual is at most 2(eN)^(-20),
and the complete range is at most 4m+2+r_H=o(N). Polynomial paths
starting from either chi endpoint cannot reach a physical end.
The original resolvent/projection errors still retain every source
row and every genuine relative end condition. Local rank converts
their operator error into O(p(k)N^-10) on both sides. Full analytic
details, hypotheses, qualifications and Mathlib status are canonical
in L229; no numerical certificate is needed.

Consequently the regularized finite trace differs from the bulk trace
by O(N^-8), and L226 plus L228 gives
|T_hh|<=C_i N^(5/2)sqrt(log(eN)), within the requested threshold.
This is local standard-method progress, conditional on the imported
analytic inputs, with no claim of originality or upstream audit.
L225--L229 await separate critical audits. The degree/range test
succeeds asymptotically; no numerical value of the sufficiently-fine
mesh threshold or of the final C_i is claimed.

Continue the unchanged approved target by separately critically
auditing L229's scalar approximation specialization, both endpoint
path identities, localized rank conversion and original two-orientation
trace assembly, relative to imported L225--L228. Essential IDs for
this audit are L003 L009 L088 L089 L090 L205 L225 L226 L227 L228
L229, with inherited L018 L026 L028 L085 L086. In particular check
the rectangular vertex/edge spaces, all three Q factors, the actual
coefficient extension agreement and preservation of every covariance
input row. Treat L225--L228 as stated analytic premises rather than
silently certifying them. Stop or repair if an identity fails on the
actual relative spaces or if a hidden mass-dependent loss breaks the
budget. Independent complete-response rates, interacting reflected
control, continuum axioms and finite positive mass remain unresolved.
