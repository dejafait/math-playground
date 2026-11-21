# Approved quartic differential test1463

The assessment1461 EXPLORE target is unchanged. Main gap:
actual-Xi all-degree positivity and the unshifted Jensen exceptional-root
deficit. This attempt tests only the generic finite-degree implication
from hyperbolicity preservation to nonreal-count contraction.

Candidate saved before source-normalization verification:
q(z)=1-z^2+(3/2)z^4, p(x)=x^4+15x^2-1.
Direct algebra suggests q(D)x^4=(x^2-6)^2 and
q(D)p=x^4+3x^2+5. The first polynomial is real rooted (double
roots); p has two nonreal roots and the output has four if the
suggested identities and counts check. Universal preservation still
requires the exact Walsh normalization and coverage of repeated roots.
These are candidate calculations, not yet the completed certificate.

The bounded acceptance test is an exact witness with universal
quartic preservation and multiplicity-aware counts. No degree sweep,
actual-Xi assertion or sector-specific contraction conclusion is allowed.
Use Walsh as imported in Craven--Csordas1983 Theorem3.3 and remarks,
pp.257--258, rather than Theorem3.4 with a dropped coefficient sign.

## Completed bounded test

The candidate passes. Full proof, hypotheses, exact normalization,
root counts and source citations are canonical in
[C020m](../../lemmas/C020m-quartic-differential-preservation-does-not-contract-nonreal-count.md).
The rational arithmetic certificate is
`scripts/quartic-differential/certificate-1463.json`; all checks pass,
and the complete relevant Sturm data were inspected using the shared
JSON inspector. Universal preservation uses the cited Walsh theorem;
the script verifies its map normalization rather than proving it.
The primary theorem statement/remarks were read on pp.257--258 of the
matching scan after author-hosted range and page-image requests failed.

This is an informative negative for the generic finite-degree upgrade,
not an actual-Xi advance or a certified-original example. No degree
sweep occurred. The same approved test can next receive an independent
proof audit of this supplied answer; no changed target/source gate is
needed. No new central creative mechanism has been prepared by the
quartic obstruction: actual signed data and a restricted count mechanism
remain missing.
