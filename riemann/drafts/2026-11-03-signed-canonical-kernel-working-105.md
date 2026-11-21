# Signed canonical-product correction: working record, step 105

Approved target: Test whether the signed canonical-product kernel correction for L666's full independent cube yields A_n(e)>=A_n(0)-n/100-C*log n along every straight displacement path, retaining finite endpoints and L657's complete charges.

Invocation-start coverage: `drafts/literature/2026-11-03-nonuniform-lattice-unit-residue-kernel.md`, EXPLORE, exact COVERED_TARGET. Reuse its primary logarithmic-ratio comparison and the ready Mahler-homotopy coverage. No new source theorem is assumed.

Main gap: actual-Xi all-degree mixed positivity. The intermediate loss would extend the audited baseline beyond sparse or two-half support; H/support, realization and signs remain independent gaps.

Read L666's exact family/path, L657 in full, L690's statement and Sections 3--5, L691's nonzero analytic-limit/logarithmic passage, L692's complete-mean proof and degree stop, and L665's two distinct recorded failures. Existing uncommitted notebook work is preserved.

Bounded attempt in progress: use the finite factor ratio P_e/P_0, rather than postulate a unit-residue reciprocal sine product. Its logarithmic derivative has exactly the new unit poles minus the old unit poles. Test whether an exact signed transport/regularized-log decomposition yields a uniform payment; keep the response correction itself, not just its absolute contour norm. The anchor is fixed and all M spatial moments stay inside the contour integral. Any passage to a singular logarithm must pay the known growing-term-count regularization cost.

Continuation/abandonment test: obtain the stated loss, a quantified useful partial signed-charge budget, or a proved failure of this specific closure. Returning only L665's small-anchor contradiction or absolute contour cost does not count as new evidence. No bound or lemma is claimed at this checkpoint.

## Completed attempt: EXPLORATION

Completed as a calculation, classified REPRODUCTION. No new lemma, uniform loss estimate, useful partial signed-charge payment, asymptotic countersequence or RH candidate was obtained. The finite identities reproduce existing residue/differentiation inputs. The new evidence is a bounded full-spatial logarithmic screen, not progress beyond the source theorems. PROOF.md and DAG.md are unchanged by this step.

### Signed object and unfinished closure

Write h=27/(10n), y_m=h(m+1/2), epsilon_m=h*e_m, and

    P_e(z)=product_m(z-y_m-epsilon_m),
    Delta k_e(z)=P_e'(z)/P_e(z)-P_0'(z)/P_0(z)
               =sum_m epsilon_m/[(z-y_m-epsilon_m)(z-y_m)].

This is the finite logarithmic derivative of the canonical-product ratio; its normalization constant is irrelevant. Its poles have the new unit residues minus the old unit residues, with cancellation when a shift vanishes. No reciprocal-product derivative weights, infinite extension, sine-type constants or small-correction assumption are substituted.

Use L690's positively oriented rectangle Gamma_n=[-2qh,2qh]+i[-2/25,1/8] and

    f(y;u,zeta)=W_(x+i*y)(u)*T_M((x+i*y)*zeta/R).

L666's cell separation puts every old/new node inside, at least 3h/8 from each corresponding vertical side. L690 Section 3 supplies holomorphy on this whole rectangle. The finite-product residue calculation in L665 Section 3 therefore gives the applicable replay

    G_e-G_0 = (2*pi*i*R)^(-1) integral_Gamma_n f(y)*Delta k_e(y)dy
            = R^(-1) sum_m integral_0^epsilon_m f'(y_m+s)ds.

The last expression is the fundamental theorem of calculus on the oriented displacement intervals. Both equal the direct finite signed node difference. The fixed anchor cancels only in this difference; it remains in each response and logarithm. All four sides, M moments, j=0 and angle 1/u remain. This is a specialization of the existing finite identity, not a new registered result or an unsigned contour bound. Its residue/simple-pole citations are canonical in L665 Section 1 and L690 Section 1.

The differentiated factor used in the computation is precisely L666 Section 6's

    partial_a log W_a(u)
       =-sum_(0<=j<n)[1/(a-t_j*u)+t_j/(U*u-t_j*a)],

including -1/a at j=0 and, in f', the derivative of the full T_M.

The singular-log closure is unfinished. At fixed n,e and delta>0, compact differentiation of the smoothed mean log(|G_(t*e)|^2+delta^2)/2 gives the integrand

    Re[(partial_t G_(t*e))*conjugate(G_(t*e))]
                   /(|G_(t*e)|^2+delta^2).

L657's endpoint integrability permits convergence of the endpoint means as delta decreases to zero: for delta<=1 their nonnegative differences from log|G| are bounded by an integrable constant minus log|G|. This does not interchange the limit with the path derivative or bound its signed negative part. The ready growing-term-count regularization results supply no such estimate by themselves. No uniform small-value assertion was assumed. This is saved unfinished reasoning, not an additional lemma or impossibility theorem.

### Bounded numerical test

Reproduce with

    python3 scripts/one-sided-hankel/signed-canonical-correction-105.py
    python3 scripts/one-sided-hankel/signed-canonical-correction-105.py --extend-once

The full floating diagnostic is `scripts/one-sided-hankel/signed-canonical-correction-105.json`. It stores all selected rational shifts (denominator 10^10), optimization traces, every sampled spatial logarithmic mean, four-side contour values, transport values and diagnostic checks. NumPy was available; SciPy was unavailable and was neither installed nor needed.

At n=51,99 use zero and one seeded dense random start, at most 40 projected-gradient iterations each. Optimization uses 96 angular and 256 spatial samples and |G|^2+10^(-16). Round selected shifts inside [-1/8,1/8]. Validation removes this smoothing: at each of 128,256,512 angular points and a separately shifted 512-point grid, compute every spatial root at the actual degree and use L657's complete root formula. No spatial root is omitted according to its modulus. Roots and angular integration remain floating.

The early losses motivated exactly one larger zero-start optimization at n=195, then size escalation stopped. Two n=195 dense patterns provide comparisons within the same test. Estimated losses A_n(0)-A_n(e) on the shifted fine angular grid are:

| n | start/pattern | estimated loss | n/100 | difference of two fine angular grids |
| --- | --- | --- | --- | --- |
| 51 | zero, optimized | 0.712619 | 0.51 | 0.0002353 |
| 51 | random, optimized | 0.678282 | 0.51 | 0.0012142 |
| 99 | zero, optimized | 1.318348 | 0.99 | 0.0000757 |
| 99 | random, optimized | 1.300314 | 0.99 | 0.0001721 |
| 195 | alternating extrema | -0.176828 | 1.95 | 0.0020177 |
| 195 | random extrema | -0.517986 | 1.95 | 0.0014022 |
| 195 | zero, optimized | 1.587890 | 1.95 | 0.0001309 |

Grid differences are diagnostics, not error bars. The n/100 column omits the unknown C*log n and onset, so early values above it are not counterexamples. At n=195 the tested optimized loss is below n/100. There is no global optimization or justified n-to-infinity conclusion.

Across every baseline/validation grid the maximum relative spatial-root residual is 1.474e-13 (threshold 1e-7); the largest discrepancy between leading- and constant-coefficient root formulas is 6.928e-14. The directional-gradient discrepancy is 8.851e-11 (threshold 1e-6). At the selected n=51 vector and both tested angular/spatial pairs, direct versus four-side signed-contour error is at most 1.207e-14 and versus signed transport at most 2.749e-15 (relative errors, thresholds 1e-7 and 1e-9). Diagnostic failure lists are empty. These checks are not analytic enclosures or a critical proof audit.

### Complete charges and limits of verification

Keep L657's exact A_n(e)=m_0(e)+Z_n(e)-P_n; P_n is unchanged. The script also evaluates its exact denominator-mean formula and the complete spatial root mean at u=0. Numerical Z changes are explicitly inferred from this identity, not an independent angular numerator-root census. For the zero-start cases they are about -0.712882,-1.318369,-1.587891; m_0 changes are 0.0002630,0.00002014,0.000000754. These locate the observed numerical loss in the unresolved charge without bounding it. No numerator zero or denominator factor is deleted to produce a lower estimate.

Inspected the complete selected gradient, contour/transport, summary and failure fields using `../scripts/loop/inspect_json.py`, and the full n=99 zero-start rational shift vector. Summary maxima aggregate all root validations. Individual roots were not independently certified, and full angular numerator roots were not computed. No diagnostic is promoted to rigorous target evidence.

The signed decomposition avoids the stopped small-anchor premise but supplies no bound on the singular logarithmic negative part. Park this unclosed contour/finite-screen argument; do not repeat descent or extrapolate its first two sizes to a linear failure. This is one mathematical EXPLORATION attempt, with inherited counters untouched, not a nonexistence result.

A different independently testable model asks about Fourier gaps of the infinite unit-weight half-lattice counting measure with the same fixed extra atom and displacement cap. No implication from a gap or its absence to finite rational A_n is established: finite truncation, complex angular dependence, all moments and complete charges would need separate work. That new target is REVIEW_REQUIRED, not approved in this turn.

Mathlib: no new search or matching-coverage claim. Reuse only the univariate root-formula support recorded in L657. No formal script validation or complete signed-log theorem is asserted.
