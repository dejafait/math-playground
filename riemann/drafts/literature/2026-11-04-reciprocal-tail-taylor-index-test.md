# Reciprocal-tail Taylor index — nominated finite obstruction test

TARGET: Test whether L779's fixed-pair 3-by-3 Taylor Hankel matrix for g_3=-h_3 has at least two negative eigenvalues, obstructing the proposed N_1 membership.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step443's completed projection-weighted-reciprocal-inertia-review.md, including exact reciprocal/Taylor/Hankel/negative-square queries and local duplicate/failure comparison; no exact actual-tail result was found among the inspected sources, with no novelty inference.
SOURCE_EVIDENCE: Song–Hao–Hu–Chen, Advances in Mathematical Physics 2014, Article605492, expansion(66) p.9, Theorem14 and complete proof p.10 https://onlinelibrary.wiley.com/doi/pdf/10.1155/2014/605492; source statement and qualifications are in the parent assessment. L777 and the audited L779 supply the local analytic and coefficient interfaces.
COMPARISON: The cited necessary Taylor-index condition is known; the difference is a rigorous finite sign calculation using actual certified reciprocal Laurent coefficients. Neither N_1 membership nor a theorem transferring its index to J-Q is known. Only the proposed premise is tested.
GAP: Identify the exact five signed coefficients with the cited Taylor convention and certify the complete 3-by-3 inertia, including coefficient errors; no coefficient or matrix value has been inspected for this target yet.
REASON: Test a concrete potential obstruction to the optional low-index premise before attempting a growing-order kernel argument; this is separate from the stopped positive-block normalization and does not assume global real zeros or a minor sign.
SCOPE: One fixed (r,R)=(3,2048) test, retaining L779's software/analytic contracts. New ready continuation written in step443; separate supervisor approval is required before research. This file specifies a test, not a mathematical conclusion.

The main gap is actual-Xi all-degree mixed positivity. A paid structural
kernel premise might help the exceptional-minor inertia route, whose
exact projection weighting and coupled comparison remain unresolved.
This test could instead eliminate the particular proposed N_1 premise.
It cannot prove or refute the desired J-Q threshold, even if the proposed
similarity is later established. A finite necessary test passing is no
evidence of half-plane membership. Do not treat k=2 or n_-(J)=1 as a
theorem about the index of g_3.

Use L776/L777's actual b=p/F and the fixed certified real/simple
grouping of L779. Preserve L017/L018/L021 normalizations and L780's
adverse-block evidence. Define beta_n to be b's real coefficient at
positive Laurent index n; no positivity of its value is assumed. Use
the proposed analytic function and test matrix

    h_3(z)=sum_(n>=0) beta_(4+n) z^(n+1), g_3=-h_3,
    H=(-beta_(4+i+j))_(i,j=0)^2.

These specify the future test. Check the indexing against the cited
source before its use; identify the required Taylor expansion at the
real point 0 from L777's convergence. The membership hypothesis is
examined by a necessary obstruction, never assumed as a proved input.

Use only the five complete coefficient rectangles/errors for indices
4 through8 from `scripts/actual-fredholm/independent-phase-certificate-437.json`
or its audited copy in `scripts/actual-fredholm/audit-439/`. Resolve the
exact selected fields using the JSON inspector, read the five complete
load-bearing values and their error conventions, and retain aliasing,
phase, factor and arithmetic qualifications of L779's repaired data.
A preview or the earlier failed recursive-phase certificate is not a
valid input. Do not replay the full certificate or change r,R,N.

The required threshold is a rigorous lower bound n_-(H)>=2. A complete
exact rational LDL/congruence or interval spectral certificate must pay
every entry error and any pivot denominator; floating eigenvalues do
not decide the test. Cite the standard law of inertia rather than
reproving it. Save full evidence to an active-notebook certificate and
print only inertia, actual/required margins, failures and paths.
This is a known-method specialization, classification REPRODUCTION,
with no claim of new general mathematics.

If the excess negative index is certified, park this particular N_1
ansatz; no RH, negative minor, or failure of all finite indices follows.
If n_-(H)<=1 is certified, record that the test is nondiscriminating;
it does not justify asserting membership or repeating with larger size.
If the saved input precision cannot settle inertia, record the exact
unresolved margin and stop this fixed-data diagnostic. Repetition needs
a materially different discriminating input or target, not an automatic
precision/order sweep. No global zero hypothesis is allowed.

No source-access blocker or cross-notebook input is needed. General
grouping, complex/multiple poles, global class, exact weighting, coupled
inertia, growing orders/radii and other mixed minors remain independent.
Full matching Mathlib coverage is unchecked. No mathematical calculation,
lemma or script was made in preparing this assessment.
