# Initial curvature interface — conditional audit nomination

TARGET: Audit the conditional implication in Liu–Mao 2610.04972v1 Lemma3.3 from the stated Lemma3.1–3.2 sector inputs to |g_0(z)-2W(2z/pi)/(z(1+W(2z/pi)))|<=20/n^2 on |z-n|<=n/2 for real n>=12000, including branches and all four error terms.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed Proposition3.5 scope review and its narrow duplicate/failure comparison; no claim of novelty. This is an exact printed source claim, with the unaudited saddle input retained as a hypothesis.
SOURCE_EVIDENCE: https://arxiv.org/html/2610.04972v1 (versioned primary HTML; PDF https://arxiv.org/pdf/2610.04972v1), Liu–Mao arXiv:2610.04972v1 Lemma3.3 and its branch/four-error proof pp.31–37, Lemma2.3 definitions, Lemma3.1 sector bounds and Lemma3.2 statement/final assembly; full source and read limits are recorded in 2026-11-05-liu-mao-quantitative-curvature-scope.md.
COMPARISON: The source states the exact estimate. The proposed work checks only its conditional finite-difference interface; it neither reproves the long saddle estimate nor imports the full all-iterate theorem. L790 concerns a different derivative bound and range; L772 has no matching analytic-curvature premise.
GAP: Check all shifted domains, compatible logarithms, Lambert-W derivatives, Cauchy remainder disks, Gamma branch identity and four error terms conditional on the explicit sector inputs; actual saddle validity and minor signs remain independent gaps.
REASON: A bounded reproduction audit could validate the exact interface of a newly identified actual-coefficient premise before any attempt to transfer it to exceptional signs. This newly written ready nomination receives separate next-turn approval.
SCOPE: Conditional Lemma3.3 only, real n>=12000 and the complete closed disk. No Proposition4.5, full theorem audit, unconditional Xi sign, new saddle estimate or growing-order minor mechanism is approved.

Reuse [the completed scope review](2026-11-05-liu-mao-quantitative-curvature-scope.md)
for exact definitions of H, Lambda, W_0, H_*, T, p, h_0, epsilon
and all numerical bounds. The paper's numbered result, not an
unverified source conclusion promoted to a local premise, fixes the
target. State Lemma3.1's sector bound and Lemma3.2's complete relative
error/nonvanishing/logarithm conclusion explicitly as assumptions.
Retain the actual integral definition and the positive real branch.
No claim that these assumptions were fully audited is permitted.

Import the standard analytic-logarithm theorem on a simply connected
zero-free domain, the identity theorem, Cauchy's derivative estimate,
Taylor's integral remainder and Gamma's functional equation. The
primary proof spells out their use in (3.55)–(3.68); do not reprove
these general theorems. A reproduction is justified to check branch
compatibility, complete complex disks and the source's effective
constants, rather than to rename a known result as new mathematics.
Full matching Mathlib coverage is not checked.

The independent audit must check both disk margins (shift by 1 and
Cauchy radius n/7), differentiations using W_0 exp(W_0)=2z/pi,
the four bounds 1,8,5,4 divided by n^2, and their full sum against
20/n^2. State any restriction that is stronger than the printed
hypotheses. A failed inequality or branch mismatch is decisive
negative evidence; preserve it without silently changing constants.
A pass establishes only this conditional interface. No transfer to
the all-degree k=r-1 signs is claimed, and no unrelated lemma count
or script is required.

Essential local context is L018/L021/L776 for notation, L772/step410
for the generic obstruction and L790 for the distinct existing
high-index derivative estimate. None supplies the unpaid saddle
premise or a mixed-minor positivity premise. No cross-notebook input.

## Direct-source recovery — 5 November 2026, step654

The versioned [primary HTML](https://arxiv.org/html/2610.04972v1)
was retrieved successfully. Source identity, Lemma3.1–3.2 statements,
Lemma3.3 statement and the branch/decomposition passages (3.55)–(3.63)
were rechecked solely to repair the missing direct citation. The complete
prior source review is reused; its duplicate and failure comparison is
unchanged. No new search for the same theorem or independent proof audit
was performed. The source URL now appears directly in SOURCE_EVIDENCE.

The conditional target and SPECIALIZE decision are unchanged. This is a
process repair, not new mathematical evidence or endorsement of the source
proof. Continue with the saved audit and its existing pass/fail test;
retain the sector estimates as assumptions and the minor-sign implication
as an independent gap. No new continuation or creative mechanism is nominated.
