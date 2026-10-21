# Reducible-fibre finiteness — bounded mathematical attempt

2026-10-12, step 246. RESEARCH / REPRODUCTION, actual proof_attempt.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-12-equality-reducible-fibre-locus-finiteness.md`;
its target and hypotheses are unchanged. No fresh source review is needed.

Main gap: universal primitive rational Hodge realization. Intermediate
target: finite set of reducible S_1 fibres of the hypothetical (14,21)
kernel. Plausible use: isolate exceptional parameters before attempting
stable-moduli arguments on their complement. This does not construct F,
an integrated germ, its mixed action, a cycle or transverse transport.

Inputs checked: L071's full exact-metric factor classification, L094's
complete slice/actual-family proof and audit, and L095's harmonicity,
positive norm and actual-derivative audit. The saved assessment's
duplicate comparison and ATTEMPTS/061 were reused. The compatible-line
and index-curvature stops are preserved.

Attempt to finish: Picard injectivity makes the unordered split factors
exactly {L,L^{-1}} at charge fourteen. HE uniqueness identifies all
such restrictions with one determinant-fixed unitary orbit. In a smooth
Coulomb slice at a chosen split parameter, SL2 forces every nearby
split representative to equal the central connection. The actual
slice derivative is r_u by L094/L095. Projecting the smooth slice
representative onto harmonic forms, then onto its four-dimensional
derivative image, gives a square real map with invertible derivative.
The inverse function theorem should isolate its zero and hence the
split parameter. Separately, stable fibres have h^0(End)=1; the split
fibre has h^0(End)=2 because neither L^2 nor L^{-2} has a section.
Proper perfect base change and semicontinuity should therefore make
the split parameter set closed. Compactness then gives finiteness.

Checks still to write rigorously: determinant-preserving unitary
identifications and the harmless unordered factors; the coordinate's
derivative before any quotient; the exact base-change coefficient and
fibre-dimension threshold; empty locus and compactness. Continue if
all four passages hold. Abandon this inference if a coordinate bridge
fails or an accumulating split locus remains compatible with the inputs.
No smooth quotient or exact quadratic normal form is being assumed.

Completed: all four passages are written in
`lemmas/L096-equality-kernel-reducible-fibre-finiteness.md`.
The achieved threshold is finite, possibly empty, not absence of split
fibres or a cardinality bound. Direct inputs are L071, L094 and L095;
L093 supplies context only. This conditional known-tool specialization
is ADVANCE / REPRODUCTION, pending a separate critical audit. No
kernel, cycle, integrated germ or transport has been produced.
