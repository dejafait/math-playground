# Simultaneous five/six-shell test — step 202 working note

Approved target: Test whether L060's minimizing columns admit a simultaneous PSD extension to the complete distance-six shell while preserving every represented unordered triple and forbidden-distance zero.

Reuse the unchanged SPECIALIZE gate in
`drafts/literature/2026-10-14-simultaneous-five-six-shell-extension.md`.
Inputs are audited L053,L054,L056,L059,L060, including the complete step-200
energy certificate, and foundations/04,09,10,12. No source refresh or new
general theorem is needed. The main gap remains arbitrary-center safety
at 67/68 agreements. This fixed prescription is only a necessary diagnostic.

First check all eligible anchor presentations of the prescribed moments.
Then use the imported full mixed-layer beta blocks on layers 0,5,6 under
the stabilizer of D. With normalized six-shell coefficients a_(r,q), the
diagonal is one, distances 1 through 4 are zero, and at r+q=5 the prescribed
coefficient is (p5/p6)*t_(q,r), where t is L060's minimizing column. This
dictionary is a provisional calculation to be verified against full sets.
The remaining 28 coefficients are nonnegative variables.

Verify beta diagonal normalization against the complete known five-shell
eigenvalues, all cross-block zero modes, constant/anchor transport, and
every six-shell mode. Seek a full exact primal witness or exact dual
contradiction. A numerical basis proposal will not count as evidence.
An obstruction parks this prescription; a complete pass parks the larger
exclusion diagnostic. Global moments, omitted scalar and label constraints,
representing measures, RS realization and the boundary remain unresolved.

Completed: the exact finite prescription is feasible. Canonical proof and
full witness definition are in L061. All 1668 constructor checks and 1928
independent substitution checks pass; both complete certificates are under
`scripts/finite-support/simultaneous-five-six-shell-*.json`. Full unordered
consistency holds, all old singular cross modes vanish, and the entire
remainder has 20 positive and 29 zero modes. The minimizing columns remain
unchanged. This parks the fixed exclusion diagnostic subject to separate
critical review, with no global feasibility or boundary conclusion.
