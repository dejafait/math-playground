# Fixed-interval signed-measure smoothing audit — working record

Approved target: audit paper 67 v1 (3.7)–(3.8) for finite real even
signed convolution measures, including atoms, bounded G_I u, and the
application of L513–L514. Gate: the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-30-weil-eigenfunction-boundedness-coverage.md`.

Main gap: arithmetic control of boundary flux near a null Weil
eigenvalue, and ultimately actual-Xi all-degree positivity. This step
only seeks fixed-operator regularity to discharge the bounded-data
premise for eigenvectors; full-Weil identification and collars remain.

Continuation test: dominate each L2 Dyson term after zero extension by
the whole-line convolution P_t * |mu|^{*j}, with simplex coefficient
t^j/j!. Check the time-one L2 kernel norm and obtain a genuine
L2-to-L-infinity limit, rather than assuming L2 convergence implies it.
Then use G_I u=(lambda+c)u+K_mu u and apply L514 and L513. Failure of
domination or the limit retains L513's boundedness premise.

Local screen: L513 and L514 contain no full-operator eigenfunction
smoothing proof; prior support-propagation and rank-trace stops concern
independent arithmetic/near-null estimates. No sibling notebook input.
This is reproduction/specialization, not creative work or a new claim
beyond the assessed sources.

Completed: the application passes the stated test. The full proof is
canonical in `lemmas/L515-signed-measure-eigenfunction-smoothing-and-trace-application.md`.
It checks finite-measure actions on equivalence classes, complex data,
the total-variation lattice induction in L2, the summable time-one
L2-to-L-infinity operator bounds and identification of both series
limits on the finite interval. The eigen-equation then gives bounded
G_Iu before invoking boundary regularity. L514 and L513 are applied
with their existing qualifications; L514's full proof was not
independently critically audited here.

Primary reinspection within the existing gate: paper 67 v1 Section 3.1
(3.4)–(3.6), Section 3.2 (3.7)–(3.8) and Section 7 (7.1);
Engel–Nagel III.1.3 and III.1.9–1.10 including strong-integral versus
operator-norm convergence; GR v1 Section 2's killed density and
half-speed normalization. Existing literature assessments supply the
remaining imported boundary, part-process and core-closure coverage.
The small-time ultracontractivity warning is respected: no smoothing
for every small positive time is asserted or required.

Result: local known-result reproduction, not progress beyond the
checked sources. This discharges the bounded-data premise for the
defined model, conditional on the local trace/domain inputs; it does
not independently identify the full Weil operator or give the missing
arithmetic estimate. No numerical or mathematical script is needed.
Next nominate a separate critical audit of the two new canonical
proofs at their actual fixed-operator scope, with prior source coverage
reused and a separate continuation approval. No justified central
creative mechanism follows from this absolute smoothing estimate.
