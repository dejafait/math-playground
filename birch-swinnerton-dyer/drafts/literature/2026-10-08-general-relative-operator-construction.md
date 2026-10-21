# General relative presentation and operator construction — source comparison

TARGET: Assess source coverage for constructing L037's complete torsion-free relative presentation and certified geometric-reflection/good-prime operators at arbitrary exact conductor N.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L029/L037 premises, fixed L030 coverage and ATTEMPTS/022--024; searched integral relative Manin terminology and general integer normal-form algorithms, then read exact author/book theorem statements and relevant proof cases listed in drafts/2026-10-08-general-relative-construction-source-notes.md.
SOURCE_EVIDENCE: Stein 2007 Sections 3.2--3.4, equation (3.2.1), Propositions 3.10--3.11 and Theorem 3.13; Stein online v0.1 star equations (11)--(12), Remark 1.43; Cremona corrected second edition 1997 Propositions 2.2.1--2.2.2; Sergeraert arXiv:2411.02422v1 Sections 2, 3.1, 4, 6--7 and Theorem 1 with proof; Sage 10.8 integer-matrix smith_form specification and singular/nonsquare/empty examples, retrieved 2026-10-08.
COMPARISON: The inspected presentation and integral relative-homology statements cover every positive N, without prime-level or absence-of-elliptic-points assumptions; endpoint algorithms cover each finite good prime. General rectangular/arbitrary-rank normal-form coverage is available, whereas rational absolute homology or the original square nonsingular Kannan--Bachem algorithm alone would not suffice.
GAP: Write the finite certified-construction specialization with full relation saturation, all integral-generator coordinates, orientation and every operator column; no such general assembly, implementation or runtime bound is produced in this review.
REASON: All essential theorem domains for this bounded construction argument are covered; remaining work is a cited known-algorithm specialization and evidence contract, not a new Manin or Smith theorem, a twist certificate or a BSD solution.
LITERATURE_REASON: Changed scope: arbitrary N and all requested good-prime operators, including integral relative-lattice certification, rather than the assessed conductor-389 T_2 instance.

SCOPE: Weight two, trivial character, full torsion-free relative symbols for Gamma_0(N) at positive exact conductor N; geometric reflection and any requested finite set of primes ell not dividing N. Exact conductor and independent a_ell(E) are supplied, and finite certified rational linear algebra is allowed; no arithmetic conductor production, prime cutoff or resource guarantee.

This completed review is literature-only. Essential canonical inputs are
L029 and audited L037. L030 and its fixed-equation assessment were read
only as comparisons. The detailed source record distinguishes inspected
theorems from inaccessible original-paper passages. No new mathematical
claim has been derived, no lemma or mathematical script has been changed,
and PROOF.md and DAG.md are unchanged by this step.

The main gap remains arbitrary-analytic-rank BSD. The intermediate
test is whether known algorithms discharge L037's finite construction
premises given the exact conductor and independent a_ell(E). Positive
coverage could support producing the relative line independently of q.
Independent twist scale, coefficient nonvanishing, rational membership,
divisible Sha and complex-order comparison remain unresolved.

The comparison passes the source-domain test. Continue by writing the
cited finite construction argument only; retain saturation and complete
operator witnesses as explicit requirements. Abandon or narrow any
claimed application that omits a generator, substitutes rational rank
for an integral lattice, silently uses prime-level lifts at composite N,
or loses the geometric sign. Passing this review is not certification of
an arbitrary implementation. Do not repeat the passed termination audit
or parked twist retrievals. The separately saved ready continuation is
subject to the supervisor's next-turn approval. Mathlib: not checked.
