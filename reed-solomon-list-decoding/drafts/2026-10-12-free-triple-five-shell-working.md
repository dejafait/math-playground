# Free-triple shell feasibility — step 177 working record

Gate: reuse the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-12-free-triple-five-shell-feasibility.md`.
Main gap: arbitrary-center safety at 68 agreements; independently 67
agreements, arbitrary pairs, RS realization and the uniform bound remain open.
Intermediate target: the exact saved free-triple feasibility slice.
Downstream use: decide whether changing triples can repair L054's failure
at L053's pairs. Continue on an exact global feasible witness or an exact
infeasibility certificate; otherwise preserve unresolved constraints.

Inputs: L053, L054 and foundations/04,09,12. No source refresh is needed.
ATTEMPTS/035 excludes the small-principal batch as a sufficient bound;
ATTEMPTS/036 excludes only the product assignment on the full shell.
Neither already decides this question.

## Before calculation

The slice is invariant under permutations of the 1024 coordinates:
singletons are constant; pairs depend only on intersection size; forbidden
distances and the full-incidence zero depend only on region sizes; every
anchor and every shell/principal test is included. Such a permutation
maps each union matrix to the corresponding anchor's matrix by simultaneous
row/column permutation. Averaging preserves nonnegativity, fixed values,
zeros and PSD. This uses Polak v1 Section 1.2, p. 3, as cited in the gate.
It applies to this full-incidence trial restriction, not arbitrary labeled
L020 rank restrictions. Unordered triples must still be identified under
all support permutations.

L054 identifies the shell with J(68,5) x J(956,5). After dividing by
rho*p5, the shell diagonal is one. Write d[r,q]=y[r,q]/p5 for distinct
triples, and a[r,q]=valency[r,q]*d[r,q]. Then each nonconstant spectral
condition is 1+sum H[a,b;r,q]*a[r,q]>=0, where H is the product
eigenvalue divided by relation valency. The constant Schur condition is
1+sum a[r,q]>=binomial(68,5)*binomial(956,5)*p5. Diagonal and zeros
remain fixed. These use L054's imported full spectrum, not new theory.

First bounded calculation: maximize the left constant row sum subject to
the 35 nonconstant inequalities and a>=0, with precisely the retained
zeros. An exact upper certificate below the required row sum would exclude
the entire slice without imposing any off-shell values. A sufficient row
sum permits a candidate only; check all three anchors and the global
unordered assignment before claiming feasibility. No extra PSD, scalar or
four-support constraints are added. Save full rational evidence to disk.

## Completed bounded test

The exact shell LP dual excludes even the relaxed independent shell
coefficients: row sum <=1143872642/5, while the fixed pairs require
4982733184/5. The strict gap is 3838860542/5. All 1318 independent
reconstruction checks pass, including every one of the 20 dual columns.
Thus there is no global triple assignment satisfying the approved slice;
no off-shell values or additional principal constraints need be fixed.
The full proof, qualifications, source imports and Mathlib status are
canonical in [L055](../lemmas/L055-free-triple-five-shell-fixed-pair-exclusion.md).
Certificate: `scripts/finite-support/free-triple-five-shell-results.json`;
independent report: `scripts/finite-support/free-triple-five-shell-audit-results.json`.

Decision: abandon only this exact free-triple repair at the fixed pairs
and full-incidence zeros. A separate critical proof audit remains pending.
No safety bound or progress beyond the checked source methods is claimed.
