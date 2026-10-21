# Affine-plane coefficient-obstruction attempt

Started 2026-10-12, under the unchanged ready EXPLORE assessment
`drafts/literature/2026-10-12-affine-plane-equality-realization.md`.
Exact target: determine realization of L072's sixteen supports under any
bijection to fixed H over F_(97^20). Main local gap: a sixteen-count
family is still possible, whereas safety needs at most fifteen.

Intermediate test: seek a uniform forced zero among L075's 64 support
coefficients, using the four parallel classes and the actual RS moment
columns. A full survivor would instead require all L010 gates. Essential
inputs: L010, L026, L072 and unaudited L073/L074/L075. These inputs do not
certify any labeling. No positive-only label sampling is authorized.

Possible mechanism: compare full error lifts on two disjoint blocks in
each class. Their span meets the two-dimensional syndrome plane, and
relations among the four block syndromes yield codewords with constrained
support. Test whether the resulting polynomial root constraints across
classes contradict fullness, rather than merely restate the common
alternating equations. Continue only on a new uniform restriction with
a concrete closure test; otherwise retain the failed inference and
reassess. Independent arbitrary-family, triangle and challenge-definition
gaps remain.

Completed: [L076](../lemmas/L076-affine-plane-automatic-fullness.md)
proves automatic fullness and simplifies L075's criterion to rank 27.
The two-class lift idea sharpened into a sparse-column comparison: two
disjoint deficient supports admit a selected cross-line meeting their
active coordinates, and the resulting at-most-eight-column union makes
a transversal impossible. The moment-column branch instead forces
twelve full supports plus one weight-one event, violating L010's 64
budget with cost at least 96. Without a moment column, each parallel
class has at least three full blocks. These verify all polynomial gates;
sixteen distinct intersection lines with one deficiency would cost at
least 76 against 64. This proof retains extension weights and uses a
new chart only for the auxiliary L010 application.

The original forced-zero closure therefore fails for a mathematical
reason, recorded in ATTEMPTS/028. A surviving rank-27 kernel must yield
an equality realization by L075. The concrete remaining test is rank
28 for every labeling, or one exact rank-27 labeling with its complete
kernel and construction. No labeling test, mathematical script, new
source assessment or global count improvement was made. The proof and
its earlier kernel inputs still await separate critical audit.
