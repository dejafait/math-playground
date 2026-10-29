# L466 critical application audit — approved source scope

TARGET: Critically audit L466 against Sra v1 Theorem 1.3 and Platt–Trudgian Theorem 1 for normalization, closed endpoints and central multiplicities, retaining the finite-height limitation.
CHECKED: 2026-10-25
DECISION: IMPORT
SEARCH_EVIDENCE: Reused the finite-height coverage/import assessments and initial-sign duplicate/failure comparison; retrieved the author landing page and followed its PDF link; no new mechanism search was needed.
SOURCE_EVIDENCE: Sra v1 (20 October 2026), https://suvrit.github.io/papers/riem-xi/riem-xi-v1.pdf, (1.1), (1.5), Theorem 1.3, printed pp. 1–3, complete Lemmas 4.1–4.2 and Theorem 1.3 proof, pp. 9–11; Platt–Trudgian https://arxiv.org/pdf/2004.09765v1, Theorem 1 and Section 2, p. 2, freshly retrieved.
COMPARISON: These primary statements and essential proof cases cover the exact application audit; L466 has an inconsistent decimal T in its specialization paragraph that the audit must repair before accepting that application as written.
GAP: No essential source case is missing for the nominated audit; L466's decimal T discrepancy remains unrepaired under this literature-only gate. Full manuscript verification, computation rerun and Mathlib coverage are outside scope.
REASON: Approve a critical citation-application audit, including correction of the identified specialization discrepancy, without a new proof or broader sign claim.
SCOPE: Exact TARGET only; compare L018 and L466 with the cited primary results, correct any application discrepancy, and retain finite-height nonnegativity only.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED requires separate approval of this newly nominated audit; existing coverage is reused and exact primary cases reconfirmed, rather than repeating discovery.

## Primary scope and retrieval

Suvrit Sra, *On some positivity properties of the Riemann Xi function*,
v1, (1.1), (1.5), Theorem 1.3, pp. 1–3, uses the actual Xi normalization
and the factorial convention recorded in L466. Its theorem assumes T>1/2
and critical-line zeros for 0<gamma<=T; its conclusion includes all orders
and the closed interval. Lemmas 4.1–4.2, pp. 9–11, cover real factors,
conjugate pairs, the exponential and locally uniform coefficient limits,
without division by the center value. The final theorem proof explicitly
handles central multiplicities. These complete cases were read, rather
than inferred from the abstract.

Dave Platt and Tim Trudgian, *The Riemann hypothesis is true up to
3 times 10^12*, arXiv:2004.09765v1, Theorem 1, p. 2, gives height
3,000,175,332,800. Section 2 describes interval arithmetic and the Turing
count. No computation rerun is claimed. The Sra author landing page
https://suvrit.github.io/papers/riem-xi/ identifies the version and its PDF;
following that link retrieved all 25 pages. There is no source blocker.

## Local comparison and continuation test

The saved finite-height assessments remain adequate; this approval adds
no independent mathematical result. L018's statement and L255's complete
proof were inspected for the local conventions and duplicate mechanism.
L255 uses a nonzero-center normalization in its general argument; it is
not the source for central multiplicities. The initial-sign assessment's
recorded finite-sign masking and count/gap failures concern global
inferences and do not obstruct this finite-height citation audit. No
cross-notebook input or October fixed-half-plane premise is involved.

A concrete local discrepancy was found: L466's proof paragraph following
the Platt–Trudgian citation writes `T=3,000,000,000`, whereas its conclusion
and the approved import use `3*10^12`. The former numeral is smaller by a
factor of 1000 and does not give the stated interval by substitution.
This is an application-text defect to repair during the approved audit,
not evidence against either source theorem. No lemma is modified here.

Continue with the exact saved audit, using L018 and L466 and the primary
locations above; repair the decimal specialization and check all three
named cases before accepting the application. Narrow or suspend the import
if another source/application mismatch survives. Do not reproduce L255 or
claim an independent full-source audit. The downstream use is a reliable
bounded-height sign input. Unbounded-height initial signs, effective tail
overlap and global mixed positivity remain unresolved; Mathlib coverage
remains unchecked.
