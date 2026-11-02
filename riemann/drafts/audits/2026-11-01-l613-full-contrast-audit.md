# L613 independent full-contrast audit — 2026-11-01

Approved target: Audit L613's full weighted triangular-contrast O(T) bound, including all ordered multiplicities, the convolution representation and both tails.

Prior gate: `drafts/literature/2026-11-01-l613-triangular-contrast-audit.md`, SPECIALIZE before this invocation. This is a mathematical proof audit, not additional literature discovery. The primary-source checks below verify the imported interface; the finite bound is checked independently. Full proof and qualifications remain canonical in L613.

Main gap: actual-Xi all-degree signs at unbounded heights. Intermediate target: establish whether the finite full contrast has the claimed uniform little-o size. Downstream use: decide whether this fixed diagnostic merits charge-conversion work. Acceptance test: replay every ordered multiplicity, the strip/Fubini identity, central cancellation and both tails; accept only a uniform comparison with T sqrt(log T), otherwise identify a failed estimate. Charge conversion, complementary pairs, model normalization, Xi realization, exceptional centers and initial signs remain independent gaps.

## Source and duplicate checks

Reused the two scoped charged-pair/triangular literature assessments and the fixed-contrast and direct-source-transfer ATTEMPTS records. No stronger all-test nonimplication is inferred. Read corrected L612's finite parameter conventions and its preserved endpoint correction: L613 uses those parameters, not the formerly erroneous charge-length formula.

Directly rechecked BGST, arXiv:2306.04799v1, Section 3, (3.1)–(3.4), complete Lemma 5 proof and Section 4 (4.3), https://arxiv.org/html/2306.04799v1#S3 . The fixed triangle is real-even, integrable, supported in [-1,1], and Lipschitz at zero. Its squared-sinc Fourier transform uses the negative-exponent convention. Only compact support justifies the entire extension here; the source's broader sentence about arbitrary L1 functions is not imported.

Rechecked BGST, arXiv:2501.14545v3, Section 3 MT, correction footnote 2, and cumulative (3.3)–(3.5), https://arxiv.org/html/2501.14545v3#S3 . The footnote preserves the earlier Lemma 5 application; the cumulative result has an additive O(H sqrt(log H)) error. Neither theorem is applied to the artificial multisets. No dyadic subtraction, varying-test uniformity, improved error, or independent audit of the number-theoretic proof is claimed. These version URLs/equation numbers disambiguate differing displayed dates.

## Complete replay and verdict

The strip integral for the weight is correct only for |Re u|<2. With L>4 the actual pair real parts 0 and ±2/L are strictly inside. The triangular density has mass one, as does exp(-2|v|). The absolute double integral is bounded by exp(|Re u|A) times the convergent weight integral. Thus the convolution identity and each finite sum/integral interchange are justified. The exact two-sided tail evaluates the entire transform at 2, not the divergent weight integral there.

Each ordered horizontal-sign expansion gives 4 cosh²(x/L)|D_N(x)|². The collapsed family gives 4|D_N(x)|², including the multiplicity product four even when both indices coincide. The common phase exp(iTx) cancels. Subtraction gives exactly L613 (6), a nonnegative real integral; no individual complex pair is assigned a sign. The endpoints j=0,n and all N² ordinate pairs remain present, including gamma_n=2T when T/h is integral.

B=3L/2 exceeds A=L+log 2 because L>4. The interval 0<|x|<=B contains no nonzero zero of sin(2x/L), since 3<pi. Concavity of sin on [0,3] and convexity of sinh on [0,3/2] give exactly the stated ratio bound. At x=0 the integrand factor 4sinh²(x/L)|D_N(x)|² is zero with D_N(0)=N finite. Therefore the central integral is at most C0=4sinh²(3/2)/sin²(3); there is no lost N factor or limiting substitution at zero.

On both tails, |D_N|<=N and 4sinh²(x/L)<=exp(2|x|/L). The exact q_A tail yields 2N² sinh²(A) exp(-kappa B)/(A² kappa), with kappa=2-2/L>3/2. The factor two accounts for both tails. TL>=4 implies N=floor(TL/4)+1<=TL/2; A>=L implies N²/A²<=T²/4; sinh² A<=exp(2A)/4=T²; kappa B=3L-3. Substitution gives at most e³T/(2kappa)<=e³T/3. All inequalities are uniform for the full stipulated range of real T and retain floor/endpoints.

Verdict: accept the unchanged L613 bound 0<=Delta_T<=C0+(e³/3)T. The required ratio is bounded by C0/(T sqrt(log T))+e³/(3 sqrt(log T)), which tends to zero. H=2T gives a comparable source scale. This is an upper bound, not a sharp order, source-main-term match, all-test compatibility result or actual-Xi theorem. The proof has no failed estimate requiring repair. This establishes the reliability of an existing local negative diagnostic, without a new theorem beyond L613 or a novelty claim. Full/supporting Mathlib coverage remains unchecked.

The mathematical argument and its direct input convention are unchanged, so no DAG edge or PROOF.md assembly change is made. L613's canonical audit qualification is updated; the older overview's unaudited label is superseded by that dated audit and this checkpoint.
