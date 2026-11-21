# Fixed shared-variable attempt, step213

Target: the exact panel0 target in the prior SPECIALIZE assessment
`literature/2026-11-09-h2-shared-taylor-panel-review.md`; no changed scope.
Main gap: L030-L032/C032a all-degree actual-Xi mixed positivity.
Local discriminator: full det H2 lower endpoint >0 on [0,1/5120],
combined with L917's two audited leading minors; a zero-containing
enclosure ends this implementation without refinement.

Essential inputs: L019/L036/L037/L058/L874/L917 and the assessed
Makino-Berz (2003) Definitions1-3, Theorems2/3, Section6. No browsing,
new theorem comparison or cross-notebook use is necessary. Existing
step195/204 failures and their preserved stopping conditions were read.

Implementation plan saved before lengthy work: x=(lambda-c)/r in [-1,1],
c=r=1/10240. Enclose all even moments through18 at c and the right
endpoint with exactly64 spatial panels, four theta terms, u<=2,
spatial order8 and100 digits. Center coefficient j=0,1,2 is
r^j M_(k+2j)(c)/j!; uniform remainder is bounded by
r^3 M_(k+6)(1/5120)/6 using L058 and positive moments.
Extend L917's complete tail method through18 before using those values.
Keep degree-two shared polynomials through normalization, the finite
logarithm recurrence through S6, and cofactor determinant evaluation.
Bound every discarded polynomial and polynomial/remainder interaction;
the mass range must exclude zero for the reciprocal. Save all evidence
and independently replay inclusion arithmetic and integration.

Completed: canonical L922 now records the complete conditional enclosure
and fixed-budget stop. Producer and full exact-rational/finite-integration
replay evidence are in `scripts/heat/h2-shared-taylor-213.json` and
`scripts/heat/h2-shared-taylor-check-213.json`. Every inclusion passes,
but the determinant and its constant coefficient interval contain zero.
No refinement was run. A preliminary ambient-context Decimal negation
defect was repaired using exact copy_negate; first-pass code and data
are preserved and excluded from the proof. The checker's initial exact
fraction serialization-limit failure was repaired before its full pass.
The source for an independent conceptual audit is nominated separately
with REVIEW_REQUIRED; this calculation does not audit itself.
Decimal library correctness remains assumed; global degrees/parameters,
flux, initialization and RH remain open.
