# 2026-10-04 — The extra-prime arithmetic transfer is a known input

Completed one literature-only assessment of the saved target in
[the existing review](../drafts/literature/2026-10-03-rank-zero-extra-relaxed-prime.md).
The target was preserved. Rechecked Sakamoto's abstract prerequisites,
then located and read the published arithmetic transfer and basis
statements. Compared the previously unread Angurel lead, including its
2026-06-08 v2; switching to the PDF resolved the v2 HTML access failure.
Reused adequate coverage of Kim, determinant descent and official scope.

Sakamoto's 2022 Section 2.5, Theorem 3.17 and Corollary 4.10 supply
the previously missing construction by citation, including a classical
mod-p Selmer basis at a minimal Kurihara index. The extra condition
p not dividing #E(F_p) is explicit; extending this application to the
broader local-torsion-only setting is parked. General rank-zero
components retain their actual auxiliary conditions.

The next direction is a mathematical application at E[p^2]: check
same-prime eligibility and every auxiliary local condition before
promoting the cited basis. The SPECIALIZE assessment preapproves its
exact target. No calculation or new result was derived during review.
Even a successful finite-depth lift would leave rational Kummer
membership, rational determinant membership and production from
m(E) = 2 unresolved. The rational lower bound remains missing.

Step BSD-2026-10-04-021-rank-zero-arithmetic-transfer-literature has
outcome ADVANCE, kind LITERATURE and classification KNOWN_IMPORTED.
This is local progress by importing a precise known input, not a
mathematical discovery or a rational-rank advance. Mathematical
exploration stays 0 of 3; STATUS remains IN_PROGRESS and no candidate
appears. Existing unfinished work and all stopped-route evidence
are preserved. DAG.md, lemmas/, scripts/ and foundations/ are unchanged.

Validation: `python3 ../scripts/docs/check_structure.py --problem birch-swinnerton-dyer`
passed with 14 nodes, 11 unique edges, an acyclic graph and valid local
links. The literature validator accepts the original TARGET, the exact
covered follow-up and the LITERATURE/KNOWN_IMPORTED report. All 93 entry
files are retained; the mathematical-artifact digest is unchanged.
Only the existing assessment, PROGRESS.md and PROOF.md changed, with
this history added. The local diff whitespace check passed. No
mathematical or computational test was run during this source review;
shared infrastructure and other notebooks were not edited.
