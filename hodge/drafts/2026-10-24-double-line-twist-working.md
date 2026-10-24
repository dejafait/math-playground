# Double line-twist specialization — working checkpoint

2026-10-24, step 512. Invocation-start SPECIALIZE coverage:
`drafts/literature/2026-10-24-double-line-twist-summand-spectrum.md`.
Target unchanged: Assess whether double line twists and the opposite hyperkahler transform constrain every nontrivial slope-zero line summand of L147's M.

Main gap: universal primitive rational Hodge realization. Intermediate
threshold: an additional necessary multiplicity constraint on the actual
conditional M, usable in a future common-kernel/decomposition test.
Continue if finite, evaluable comparisons add a restriction; park if
all candidates merely produce uncontrolled images. No F or nonempty Z
is assumed. Preserve W in ordinary degree two.

Inputs read: L052 exact-h line lattice, L071 full character and actual
compatible connection, L093 both untwisted concentrations, L147 full
ordinary character, L154 stable-type bounds, L155 actual section vanishing,
L156 no trivial factors and h^1(M)=119-z. Supplied prior comparison
covers the general theorems; no new literature search is needed.
ATTEMPTS/087 and October 12's forward-IT failure remain in scope.

Preliminary calculation, not yet a finished result: every nontrivial
stable summand has H^0=H^2=0. A line L_B^t has h^1=7t^2-2.
Thus m_t(7t^2-2)<=119-z<=119, so a possible nonzero t must
satisfy |t|<=4. The opposite charge-21 restrictions are all stable;
line tensoring should preserve endpoints in each rotation. Need to
compute the signed character, cross-power duality and both total-degree
one comparisons and check multiplicities before making a conclusion.

Completed: the canonical proof is now L157. Opposite power images have
cohomology (0,70r^2,0), not acyclicity. The selected residual tests give
additional bounds m_{-1}<=12, m_1<=8 and their sum <=14, retaining
formal compatible branches. The bounded filter is complete; separate
critical audit is proposed and not performed in this step.

Arithmetic recovery: the initial script check failed its higher-power
line-index formula because its test instantiated every line with d=-7.
Corrected that test to the actual d=-7t^2, then reran the full checks
successfully. This was a test-data bug, not a source or existence
assertion; the written line-index formula is -121-168t^2-56t.
The final full certificate has no failures. See the canonical result
and its reproduction command rather than treating this preliminary
working note as proof.
