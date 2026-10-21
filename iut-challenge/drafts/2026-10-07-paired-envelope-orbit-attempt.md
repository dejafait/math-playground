# Paired-envelope orbit calculation — working reasoning

Approved target and coverage: `drafts/literature/2026-10-07-paired-envelope-orbit.md` (SPECIALIZE, unchanged). Main gap remains original finite B>=A. This attempt concerns only N=(pi J/6) intersect V and L025's exact finite-word subgroup Gamma.

Use the algebraic Z_3-span S of h(N), h in Gamma. N is full in V: pi H/6 is a full lattice in K, and its intersection with V is full. Boundedness follows from Gamma preserving M, commensurability, and N contained in a rational scaling of M. Noetherian finite generation makes S a lattice. L025's audited residual criterion then gives S=3^t M.

Scale candidate: 81N subset M because 81(pi J/6)=(27/2)pi J subset pi^28 O subset H subset J. The actual x=pi q_1/6 belongs to N since q_1 has zero pi^26 coefficient. L016's separator phi gives phi(27x)=phi((9/2)pi q_1)=-248/3, so 27x is not in J. Hence S cannot lie in 3^(-3)M; its scale must be 3^(-4)M. Check the arithmetic and every lattice obligation before promotion.

For the comparison, m=3q_1-16q_2 has constant coefficient zero, hence belongs to M. Its pi^18 coefficient is -13/9, giving valuation -4/3; other coordinates must be checked to exclude a lower minimum. Then 3^(-4)m has valuation -16/3<-4. If all individual h(N) lay in C, their ordinary finite Z_3-sums would too; this contradicts that point of S. Thus an actual finite-word orbit escape exists, without identifying h or field coordinates of presentation generators. A complete-table bound may also establish sharp orbit valuation -16/3; do not claim it until checked.

Independent gaps: actual-ind3 membership, native permitted-action identification, original initial data, higher powers, pilot transport, essentiality and original finite B>=A. Preserve L020 and ATTEMPTS/015–020. Continuation test: finish the exact scale/valuation proof and actual-orbit implication; abandon the span mechanism if any of these obligations fails rather than converting a loose upper bound into a violation.

Completed in L026: all obligations above were proved, the complete trace-zero minimum is -4/3, and a finite-word orbit image attains -16/3. The finite checker and full certificate are `scripts/coarse-ideal/check_paired_envelope_orbit.py` and `scripts/coarse-ideal/paired-envelope-orbit.json`; zero failures. The full argument lives only in the canonical lemma. Next routing and status live in PROGRESS.md; the new audit assessment is pending separate coverage approval.
