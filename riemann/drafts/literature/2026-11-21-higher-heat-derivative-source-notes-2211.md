# Higher heat-derivative source review2211

Completed 21 November2026. Literature-only; no new mathematical claim
is established. Exact target remains the step2210 nomination.

The previously unnamed computing_rh lead is Nicholas G. Polson and
Vadim Sokolov, *Computing the Riemann Hypothesis*, edition2, volumeI,
version3.0.0. The author summary identifies Section8.1 derivative and
Hankel results. Summaries are discovery aids, not proof coverage.
The primary PDF could not be retrieved by the web tool (octet-stream
or restricted URL); shell retrieval failed DNS. Tagged primary LaTeX
was accessible instead. The tagged main_vol1.tex and vol/v1_ch08.tex
identify ch/ch12.tex as Section8.1. No PDF/source identity is assumed;
the theorem numbers/pages below are the authors' catalog locators,
and the tagged labels and ranges identify the text actually inspected.

## Main gap, target and decision test

The gap is L030-L032/C032a actual-Xi all-degree algebraic mixed
positivity. The reviewed threshold was an actual-family finite
higher-heat-derivative inequality constraining Q(X^r P_3), r>=4.
Its use would be signed control after three real classes are cancelled.
Continue a direct signing route only if the source supplies a
noncircular inequality with that connection. A scalar restatement,
finite verification without uniform shift control, or an all-order
positivity premise fails that test. The source does supply stronger
scalar information, but no such mixed estimate was identified.

## Local comparisons and qualifications

Reused source comparison2207, finite transfer assessment1108,
mechanism comparison1117 and its finite-block stop. Read C030a/b's
statements and normalization, and L030 in full. C030b already imports
mixed positivity through degree29999999 relative to Polson v24's
preprint theorem and external verification; no fresh unconditional
certification of that theorem is claimed. This finite input does not
cover all shifts r>=4 of a fixed cubic. C919i/j's finite model and
L247's scalar logarithmic-derivative counterexample are different
observables and must not be conflated with heat-trace complete
monotonicity.

Read C919i's statement/normalization, C919j's statement and opening
phase estimates, L029/L030/L032/L034/L247 in full, and the relevant
complete-monotonicity stop. Their accepted audits are reused.
L032 already supplies detection of a nonreal summable reciprocal
node; no new detector or negative witness was constructed here.
The local all-order heat question is distinct from L247's all-order
derivatives in the resolvent variable. C919i/j do not settle it.

## Primary passages actually inspected

Nicholas G. Polson and Vadim Sokolov, *Computing the Riemann Hypothesis*,
edition2, volumeI, version3.0.0, November2026, independently published;
author landing page https://vsokolov.org/books/computing_rh/ and DOI
10.5281/zenodo.24377750. Primary tagged text:
https://raw.githubusercontent.com/VadimSokolov/computing_rh/v3.0.0/ch/ch12.tex
and the finite-information comparison in
https://raw.githubusercontent.com/VadimSokolov/computing_rh/v3.0.0/ch/ch13.tex .
The repository licenses the text CC BY4.0. The unversioned summary
had both an older1.29 description and a later1.70 entry; only the
tagged theorem text determines the comparison here.

The normalization uses a_j=-(rho_j-1/2)^2, one occurrence per
{rho,1-rho} pair, with multiplicity, and c_k(t)=(-1)^k W^(k)(t).
An off-line quartet contributes two conjugate exponents, not positive
real nodes. Read ch12 lines0-11,80-87,117-149,200-257,364-398,
432-445. These include the three candidate statements below, the
complete Hermite-envelope lemma and both its proof cases, the full
small-time and window proofs, and the entire improved-range proof.
The source's differentiation/interchange uses Gaussian decay;
C030a's local convergence justification is reused for the actual
notation. Source count, low-zero and ball-arithmetic inputs are
reported, not independently verified in this review.

1. Theorem8.1.6, catalog p105, label thm:ch12:blocks, asserts both
   leading heat Hankel blocks of size N are positive definite at
   every t>0 under line verification through
   T_N=20000N sqrt(1+log N); it records N<=30000000 from verification
   through3e12. This explicitly cites Polson v24 Theorem7.4. It is
   the existing C030b input, not a new extension.
2. Theorem8.1.14, catalog p118, label thm:ch12:window, gives c_k(t)>0
   for t>=1.29 and integer 0<=k<=t(H-23)^2, H=3e12; combining its
   small-time theorem gives every t>0 through order1.29(H-23)^2.
   Its full proof retains the complex tail, a verified real zero
   within15 of sqrt(k/t), and N(r)<=r^2. The displayed comparison is
   e^(-450t) versus e^(t/2-tD^2)(H^2+1/t+H/(tD)), D>=23.
3. Theorem8.1.17, catalog p121, label ps:thm:free, states c_k(t)>0
   for every k>=0 on0<t<=1.70, and for every t>0 through integer
   order1.70(H-23)^2>1.52e25. The all-order short-time ingredient is
   Theorem8.1.10, catalog p111, label thm:ch12:cmint: k>=1 on
   (0,0.019] without zero information, and all k on(0,1.29] using
   verification to1e12. The improved proof combines that result,
   the window theorem and a prime-power envelope at cutoff1e9.
   Its stated endpoint margin is>0.4564. Neither its certificate
   nor its50,851,223-term prime-power computation was replayed.

For the small-time cases, read the exact F_k hypergeometric
normalization and B/C_epsilon bounds, both contour/Hermite cases,
the k/t monotonicity argument and the explicit prime tail with q>1.
This checks what is claimed and what premises the proof uses; it is
not an independent mathematical audit of those inequalities.
Read ch13 lines0-18 for the precise source perturbation statement;
its full proof remains the already assessed Polson v24 input in1117.
No extension of its finite-order obstruction to local all-order heat
signs is asserted. The ch12 compound-Poisson statement/proof was
also inspected for scope; its small defect is not imported as a
polynomially weighted remainder estimate. The ch11 weak-limit
opening was inspected only to exclude an automatic closure shortcut.

## Comparison with the requested form

C030a/b already identify the source's finite mixed conclusion.
For a fixed r, X^r P_3 has degree r+3; a fixed degree cap does not
cover all integers r>=4. Selecting three actual distinct real classes
with their multiplicities is still necessary; this review supplies
no ordered-class census. Algebraic squares and both complex
occurrences remain essential. A scalar c_k sign is not the sign of
an arbitrary signed coefficient combination, and the source states
no such implication for Q(X^r P_3). No new integral representation
or derivative-to-Q implication was derived here.

All derivative orders on a bounded time interval are genuinely
stronger source information than the two C919j signs. They are not
global complete monotonicity, and the all-order Hankel premise in
Theorem8.1.4 is explicitly an RH equivalence. Neither the finite
C919i/j counterexample nor the source's finite-test perturbation
has been shown here to preserve the newly inspected local all-order
property. Thus no combined insufficiency theorem is claimed.

Decision: NEGATIVE source-scope/overlap evidence closes this lead as
a direct uniform cubic-sign mechanism. It is not a disproof of the
cubic inequality, the source's assertions, or RH. The completed
assessment is EXPLORE: the bounded review found no matching signed
estimate; it does not certify novelty. No known theorem was newly
inserted into the canonical proof, so no lemma, DAG or PROOF edit
is needed. Full matching/supporting Mathlib coverage is unchecked.

## Search record and one continuation

External queries included computing_rh heat/derivatives, Riemann
heat trace higher derivatives positivity, and heat trace completely
monotone interval nonreal zeros. Notebook searches used computing_rh,
Polson/Williamson, higher-derivative, local complete monotonicity,
all-order heat and annihilator terms, then selected the exact
1108/1117/1340/2207 comparisons and September23 scalar stop.
Search snippets, catalog entries and unrelated claimed proofs are
not theorem evidence. No novelty inference follows from no match.

The only nominated continuation tests the distinct local all-order
premise on L029's unchanged infinite-zero F, rather than tuning the
frozen five-node model or raising a finite sign cap. Its exact
literature-first action and missing coverage are in
2026-11-21-local-all-order-heat-model-gate-2211.md. It would delimit
that premise alone, not the conjunction of all source properties.
No heat derivative of that model was calculated in this turn.
An actual-Xi signed estimate remains unidentified, so a protected
creative central attempt is not justified yet. No cross-notebook
input, token accounting, scheduler change or source-access campaign.
