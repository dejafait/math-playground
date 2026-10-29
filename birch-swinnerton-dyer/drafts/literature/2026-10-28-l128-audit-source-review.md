# Source gate for the separate L128 conceptual audit

TARGET: Assess source coverage for a separate conceptual audit of L128's completed-branch scalar identity, including the opposite-algebra transfer, faithful-flat coefficient comparison and normalized local signs.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 532 read L128, relevant L123/L126/L127 passages, ATTEMPTS/061 and step 531; reused step 527's local-sign coverage and searched primary sources for Tate-module faithfulness, finite-algebra completion, Hensel/Nakayama and global multiplicity one. Queries, inspected passages and unsuccessful leads are in drafts/source-notes/2026-10-28-l128-audit-source-coverage.md.
SOURCE_EVIDENCE: Reused Schmidt Theorems 1.2.1/3.2.2 and Jacquet--Langlands Theorems 4.2/4.3(i)/15.1 through step 527; Fornea v2 Remark 2.12 and Section 2.4 https://arxiv.org/html/2603.28327v2; Milne, Abelian Varieties v2.0 (2008), Chapter I Theorem 10.15/Lemma 10.16, pp.49--50 https://www.jmilne.org/math/CourseNotes/AV.pdf; Stacks Lemmas 10.97.2--3 https://stacks.math.columbia.edu/tag/0BNH and 10.97.8 https://stacks.math.columbia.edu/tag/07N9, 10.153.3/7/9 https://stacks.math.columbia.edu/tag/04GE https://stacks.math.columbia.edu/tag/04GK https://stacks.math.columbia.edu/tag/04GM and 10.20.1 https://stacks.math.columbia.edu/tag/07RC; Badulescu, ESI 1970 (2007), Section 4 and Theorem 5.1(a)--(c), pp.21--25, n=1 proof case p.28 https://www.esi.ac.at/preprints/esi1970.pdf. Step 533 restores direct URLs here; prior inspected theorem/proof coverage is reused.
COMPARISON: Precise primary inputs now cover faithful finite-level endomorphism detection, completed finite-algebra factors, flat descent and global separation; existing sources cover local signs and tower control. None states L128's enlarged opposite-algebra coefficient action or its complete-moment scalar identity. Their applicability remains for the separate audit.
GAP: Critically check L128 Steps 1--5, especially the dual-action labels and ordinary summands, transfer of relations, original R_0/T/I identification and (5), good-Hecke separation at exact conductor, W involution and split/division sign conventions; no scalar conclusion is imported.
REASON: Separate essential source coverage is complete; a bounded conceptual audit is justified without more browsing or a reproof of the imported theorems. Approval covers the test, including a first precise failed comparison, and does not certify step 531's result.
SCOPE: Unchanged L123/L124/L126/L127/L128 hypotheses and original complete CM list, n, W, coefficient module, I, invariant domains and maps; no rationality, finite-local-condition, nonvanishing or general BSD assertion.
COVERED_TARGET: Critically audit L128's completed-branch scalar identity in the original I localization, checking the opposite-algebra coefficient action, faithful-flat comparison and split/division signs.
LITERATURE_REASON: The new separate audit needs essential coefficient-faithfulness, completed-ring comparison and global-multiplicity references not precisely recorded in the ready step-527 local-sign assessment; that unchanged local-sign coverage is reused.

The full argument is canonical in
[the lemma](../../lemmas/L128-completed-a-branch-normalizer-scalar.md).
Reuse `2026-10-27-degree-one-normalizer-scalar.md` and the matching
step-527 source note for unchanged construction and local-newvector
inputs. No additional literature is requested merely to repeat them.

Step 532 completes this review. The newly precise supporting imports and
their hypotheses, direct links, versions and read/access qualifications
are in [the source record](../source-notes/2026-10-28-l128-audit-source-coverage.md).
The COVERED_TARGET is the exact separately approved follow-on audit;
TARGET above preserves the source-review action completed this turn.
Retain L123/step-515, L124/step-520, L126/step-526 and L127/step-530.
Do not replace the original I-localized invariant domain by an arbitrary
classical quotient. The proof deliberately does not need an isomorphism
between I and the uncompleted weight-ring localization.

The later audit's bounded test is to validate or exhibit the first failed
comparison in L128 (2), including (5) and the opposite-algebra transfer;
then check (1)'s normalized signs and the unchanged descent yielding (3).
No rationality, finite local membership, nonvanishing or BSD claim is
part of this audit. Mathlib coverage remains not checked. Source approval
is not mathematical acceptance. Retain ATTEMPTS/061 and stop at the first
unsupported comparison; no automatic full-Hecke-linearity, arbitrary
oldspace scalar, or interchange of infinite limits is approved.
