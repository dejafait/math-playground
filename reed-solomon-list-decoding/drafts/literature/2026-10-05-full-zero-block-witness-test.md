# Full zero-index blocks — approved witness diagnostic

TARGET: Test L022's explicit rational triple assignment against both full (0,0) Schrijver blocks for A(1024,10,68), with exact PSD or negative-quadratic certificates.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the prior Schrijver/exact-instance/implementation search in 2026-10-05-triple-distance-sdp-certificate.md; scoped searches of local SDP assessments, ATTEMPTS/012, history/042–043 and the selected-SDP working note found only the four-index zero-block test, with no full-zero-block certificate or duplicate diagnostic.
SOURCE_EVIDENCE: Reused foundations/04 and directly checked Schrijver's eight-page author manuscript III.A (58), p. 6, and III.B (64)–(65), p. 7; corroborated Kim–Toan arXiv:1212.3467v1 III.B (31)–(35), printed pp. 8–9, especially the complete index sets and affine second family.
COMPARISON: The imported theorem supplies both full zero-index constraints; L022 supplies only selected-block feasibility. Testing its prescribed extension needs exact finite arithmetic, not a new coding theorem or a reproof. No inspected source supplies the result of this particular diagnostic.
GAP: Determine whether the same piecewise rational assignment, explicitly extended to all admissible orbits used here, violates either full block or remains PSD; all other omitted constraints and full-SDP feasibility remain unknown.
REASON: Separate review now covers the changed full-index scope and its normalization. The known necessary constraints apply, while the value of this explicit point on them requires implementation; no novelty claim follows.
SCOPE: Only both (0,0) matrices on 0,...,68 for n=1024,w=68,v=956,d=10, evaluated at L022's unchanged piecewise assignment; no optimization, new ansatz, new SDP family or full scalar-constraint feasibility claim.

Approved scope: both source (0,0) matrices on indices
0,...,68, evaluated at the same repeated-word/forbidden-distance/product
assignment as L022. This is a test of one explicit point, not optimization
of a larger SDP or construction of its full variable closure. A negative
rational quadratic witness would identify a specific constraint capable
of eliminating this point; exact PSD would park this particular addition
as a means of excluding it. Neither finding alone decides the threshold.
No new formula, simplification or feasibility claim is established here.

Inputs: L001, C001a, L021, L022 and foundations/04. C001a's C012a/L019
inputs remain unchanged. L021's rational pair witness is specified by
its exact linear systems; L022 specifies p_i and lambda=p_68. No new
mathematical input is imported from another notebook.

## Source comparison and applicability

[Schrijver](https://homepages.cwi.nl/~lex/files/codes.pdf), IEEE Trans.
Inform. Theory 51 (2005), 2859–2866, III.A (58), III.B (64)–(65),
supplies the complete matrices and symmetry conditions. Use the same
integer coefficients as foundations/04. No reproof is justified.
The block order is |W_k intersection V_l|; at k=l=0 the ranges are
0,...,68 and 0,...,956, hence the retained indices are 0,...,68.
The parameters satisfy even d and 0<10<136<=1024. The prior support
dictionary applies to the whole tuple list and permits extra agreements.

[Kim–Toan](https://arxiv.org/pdf/1212.3467v1), v1, 14 December 2012,
III.B (31)–(35), independently gives the same full index range and
second-family entries with p_(i+j-t-s)-y. Their normalization uses actual
nonzero multinomial orbits. Preserve foundations/04's qualification:
do not reconstruct the unused printed complement prefactor in (61).
The matrix formulas themselves are the imported input.

The scope change is explicit extension of a prescribed formula, not an
inference of extendibility. On each admissible orbit put h=i+j-t-s;
use L022's forbidden-distance branch first, its repeated-word branch
second, and its product branch otherwise. Previously untouched variables
are assigned by that prescription, never set to zero merely because they
were omitted. Retain t-s in orbit identification and compare overlapping
values with the existing certificate. This review asserts no new scalar
inequality or PSD sign for the extension. Full scalar verification would
be necessary for any later claim of full feasible primal status.

## Bounded certificate requirements and decision test

Construct only the two rational 69-by-69 matrices. Stream admissible
orbits per entry rather than construct a full optimization-variable or
scalar-row closure. Keep original indices, coefficients and exact
rational values recoverable in the certificate. Check symmetry and
reconstruct the four-index principal matrices against L022 before
interpreting any sign. This is finite witness evaluation; the earlier
20000-variable optimization cap does not describe this different task.
If construction or arithmetic cannot finish in one bounded attempt,
save the completed entries and unfinished stage; resource failure is
neither PSD nor a negative certificate.

For a negative result save a rational vector x in original index order
and independently verify x^T A x<0 from the source-entry reconstruction.
For a PSD result save an invertible rational congruence E^T A E=D,
inspect every entry identity and require every diagonal entry nonnegative;
zero pivots require a zero residual row. Check both families. Numerical
eigenvalues or a preview of the certificate are insufficient. Preserve
full certificates under scripts/finite-support/ in the research turn.

A negative witness identifies an omitted constraint excluding this
specific extension, and can motivate a separately reviewed stronger
certificate target. It does not exclude other extensions of the selected
point. Exact PSD in both families parks these two blocks as a way to
exclude this extension; it proves no full-SDP feasibility. Keep the
above-threshold objective and the unresolved safety threshold distinct.
Do not add more blocks or tune the assignment within this test.

The earlier assessment's search and stronger-result comparison remain
adequate for this unchanged Schrijver framework: Polak's four-word bounds
and Kim–Toan's later enhancements are separate, unapproved leads. No
fresh broad search or novelty inference is needed. This turn's narrow
primary-source reread resolves the changed index/normalization case only.

Independent gaps: actual list safety at 67/68 agreements, full SDP value,
actual packing, RS determinant transfer, interleaving sharpness and ABF
comparison. The 955–957 bracket and all earlier stops remain in force.
Mathlib matching coverage remains not checked. This approval does not
reject or downgrade the completed L022 certificate. The future step is
RESEARCH / REPRODUCTION under SPECIALIZE, not a new mathematical discovery.
