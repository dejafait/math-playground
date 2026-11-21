# Known order-five nonnegativity: import gate

TARGET: Import the order-five consequence of Katkova's finite-order coefficient theorem for the actual normalization, recording D_(5,4)>=0 with explicit scaling, matrix indices and source-index qualifications, without a numerical determinant calculation.
CHECKED: 2026-11-05
DECISION: IMPORT
SEARCH_EVIDENCE: Reuse step569's exact-cell comparison in 2026-11-05-actual-theta-order-five-cell-coverage.md; no broader target or new search is proposed.
SOURCE_EVIDENCE: Katkova math/0505174v1 definitions/(3)–(8), Theorem B/Theorem1 and full short proof pp.2–6. The printed sector safely covers order five; retain the PF43/PF44 qualification documented in step569.
COMPARISON: The nonnegative sign is known. Only applicability to G and the selected minor remains to be written canonically; no strictness or all-degree theorem is covered.
GAP: Explicit positive constant/geometric scaling and ordered Toeplitz row/column identification must be checked. Strict positivity and a degree-uniform bridge are outside scope.
REASON: Close the finite-cell source question without redundant computation or claiming a known sign as discovery. This newly written ready continuation requires separate next-turn approval.
SCOPE: One KNOWN_IMPORTED applicability step using L018/L019/L021 and L776 definitions only; no source reproof, maximal-order correction, strictness lemma or mathematical script.

Primary citation: Olga M. Katkova, *Multiple positivity and the Riemann
zeta-function*, Comput. Methods Funct. Theory7 (2007),13–31,
DOI10.1007/BF03321628; numbering binds to
[math/0505174v1, pp.5–6](https://arxiv.org/pdf/math/0505174v1#page=5).
Use the safe order-five application, retaining step569's explicit sector
versus PF threshold qualification. The inaccessible revision/journal
version is not required or presumed inspected.

Check G(w)=xi_1(w/4)/8 coefficient by coefficient with every positive
constant/geometric factor. Identify increasing rows0,...,4 and
columns4,...,8 of the source Toeplitz matrix. Write only the necessary
sign-preserving scaling and theorem applicability. Do not upgrade
nonnegative to positive. If the match passes, store full hypotheses,
precise citation, qualifications and Mathlib status canonically. Stop
on a mismatch; do not rescue the import by a determinant experiment.

L772/L786/L792/C792a/b/L812 are comparisons, not sign premises. No
cross-notebook input is used. Matching Mathlib coverage is unchecked.
The downstream use is a bounded known actual input and exclusion of a
redundant negative-cell route. All-degree mixed positivity and RH remain
open; no new central sufficient-sign mechanism is asserted.
