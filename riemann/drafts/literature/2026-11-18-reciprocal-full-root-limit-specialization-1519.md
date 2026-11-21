# Full reciprocal-root limit specialization1519

TARGET: Establish lim_(d->infinity) H_d/d = sum_(F(w)=0) |Im(1/w)| with an absolutely convergent multiplicity-counted full zero sum for C028b's actual F=Theta/gamma_0, using C028f and the reviewed classical inputs, without RH.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed literature-only review1519 of the exact infinite-sum target in assessment1518; bounded exact/stronger-result searches and scoped duplicate/failure checks are recorded in 2026-11-18-reciprocal-full-root-limit-source-notes-1519.md. No exact matching weighted identity was established by search and no novelty is inferred.
SOURCE_EVIDENCE: Reused O'Sullivan arXiv:2007.13582v2 Section3.1 Theorem3.1 proof sketch/Corollary3.2; Tao246A Notes4 Theorem37, https://terrytao.wordpress.com/2016/10/11/math-246a-notes-4-singularities-of-holomorphic-functions/ ; Tao246B Notes1 Proposition8/Theorem22 proof equation(20), https://terrytao.wordpress.com/2020/12/23/246b-notes-1-zeroes-poles-and-factorisation-of-meromorphic-functions/ . Complete read qualifications and comparison with Campbell--Jalowy2605.31356v1 are in source-notes1519.
COMPARISON: Known tools cover compact Jensen convergence, multiplicity-preserving Rouche counts and reciprocal-zero summability for nonzero entire functions of order below1; C028b supplies the finite inversion identity and C028f the uniform strict polynomial tail. The empirical Cauchy law concerns different normalized measures and input scaling, so it does not replace the weighted-limit specialization.
GAP: Prove only the local assembly: common origin exclusion, compact weighted multiset convergence including zero-free complement and cutoff cases, imported entire-tail applicability, and an explicit two-tail limit passage. No general Jensen/Rouche/Hadamard theorem reproof is needed.
REASON: Essential source coverage is complete for a bounded classical specialization. It identifies the exact unpaid nonreal-zero functional; it supplies no estimate forcing that functional to vanish and no progress beyond the checked sources is claimed.
SCOPE: C028b/C028f actual positive b_j, U_d=J_d(u/d)/gamma_0, F(0)=1 and order1/2, d>=3 tending through integers; all algebraic/analytic multiplicities. No RH, LP membership, simple zeros, effective onset or K, vanishing compact mass or actual off-line zero. Full matching Mathlib coverage remains unchecked.

Use the complete source qualifications and four bounded proof obligations
in [source-notes1519](2026-11-18-reciprocal-full-root-limit-source-notes-1519.md).
The general reciprocal summability input is the floor(rho)=0 case of
Tao's explicitly proved equation(20), whose origin/finite-zero/infinite-zero
cases were read. Import it with the actual order and nonvanishing-at-zero
hypotheses checked; do not silently invoke a full matching limit theorem.
Canonical full proof and citations belong in one lemma file if the
specialization succeeds.

Continue if every proof obligation passes with fixed zero-free cutoffs
and both tails separately controlled. Otherwise preserve the first failed
claim and its hypotheses. The known conditional one-zero obstruction
remains intact, and summability cannot be read as compact-mass vanishing.

This is a newly written ready continuation, awaiting the supervisor's
separate next-turn approval. No research attempt or full identity has
been completed in the literature-only turn that prepared it. It is an
established-route specialization, not a creative central sign mechanism.
