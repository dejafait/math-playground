# Actual theta signed compensation — completed source comparison

TARGET: Assess theta-specific integration-by-parts and signed-compensation results for the factorial-exact D_(r,r-1) integral after L766, and nominate one bounded actual-K inequality that could control its integrated sign without assuming coefficient positivity.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step391 searched exact theta/Toeplitz integration-by-parts, moment and cumulant terminology; inspected Nuttall's primary author preprint Lemma2.1 and Sections4.2–4.6; reused step389's representation assessment and recorded weighted-moment/finite-order scope comparisons. Queries, read limits and the new source-range mismatch appear below; no novelty claim.
SOURCE_EVIDENCE: Nuttall, Wronskians, Cumulants, and the Riemann Hypothesis, author copy det3CAEXP_2.pdf, Lemma2.1 p.4 and Sections4.2–4.6/(4.1)–(4.7), pp.12–15; 20 October 2011 NYNTS slides (29)–(44), slides21–31, and exceptional-case discussion, slides35–36. Reused Csordas–Varga Theorem2.4 and Katkova/Forrester assessments at their unchanged scopes; no new proof audit.
COMPARISON: Nuttall's cumulant integration-by-parts formula has coefficient range k>=r-1+ceil(m/2), conditional on the required reverse regularity; positive smoothing does not reach k=r-1 through that formula. Higher-order cumulant reverse regularity is Conjecture1, and Section4.6 retains exceptional cases even if it holds. No inspected result supplies signed compensation for L766's integral.
GAP: No bounded actual-K remainder inequality with independent support was found. Actual all-order cumulant signs, effective smoothing thresholds and the exceptional-index transfer are unresolved; the different-kernel induction in cumanal_a.pdf is only a lead with essential unread proof cases.
REASON: Park direct compensation of the product-K integrand; do not rename its desired sign as a remainder bound. Select iterated-tail cumulant induction as a different mechanism for one narrow source review before any mathematical attempt.
LITERATURE_REASON: The hypothesis and observable change from pointwise integrand nonnegativity to actual-theta integrated compensation, outside step389's assessed scope; essential source coverage for a sign-controlling derivative or compensation estimate is missing.
SCOPE: Completed literature-only discovery for the exact TARGET: derivative transfer, weighted-moment inequalities and cumulant reverse regularity. No mathematical continuation is approved by this assessment. The next different-kernel source target is REVIEW_REQUIRED; no new lemma, mathematical script or parameter scan.

## Original nomination, retained as history

At nomination this was not an approval. The next turn had to assess
coverage separately; no new mathematics for this target was performed
or approved in step390. The existing representation toolkit may be
reused but cannot be relabeled a sign theorem.

Read only the needed ranges of L019/L021/L766 and the prior signed
integral assessment. The source search should address the actual
identity K=2A''-A/2 and whether a known integration-by-parts or signed
compensation argument supplies a genuinely sufficient remainder
estimate for the factorial-exact coefficient integral. Retrieve exact
primary hypotheses and essential proof cases before importing results.
Account for boundary terms, factorials and convergence. Ordinary Gram
positivity, fixed-order eventual positivity, a rewritten determinant
sign or an RH-equivalent assumption does not supply the missing input.

The purpose is to nominate one bounded estimate only if its mechanism
has independent support. State its essential input IDs, exact required
sign/threshold, plausible use toward actual all-degree positivity and
a continuation/abandonment test. Preserve L766's pointwise obstruction
and L765's norm stop. Treat L766 as a written result awaiting independent
audit, not as audited infrastructure. If the search supplies no
independently testable compensation mechanism, record that finding and
choose a different central mechanism instead of renaming this route.
No cross-notebook input is proposed. Mathlib coverage remains unchecked.

## Completed comparison — step391

Main gap: actual-Xi all-degree positivity at growing orders. The
intermediate target reviewed was a sufficient signed estimate for the
full factorial-exact D_(r,r-1) integral. It could address this edge
family while leaving other indices and all-degree signs open. Continue
only upon identifying an actual-K inequality with independently
supported remainder control; abandon this direct mechanism otherwise.
None was found. This is a source-scope limit, not an impossibility
theorem or a negative actual minor.

### Three candidates and precise source limits

1. **Derivative transfer.** L019 supplies K=2A''-A/2, the nonzero
   boundary value A'(0)=-1/4 and its stated decay; L021 supplies finite
   moments. No inspected theorem signs the resulting cofactor terms,
   permits dropping origin boundaries or removes the A subtraction.
   No new integration-by-parts formula was derived here. Reuse
   step389's assessment of Katkova's fixed-order angular core/tail
   estimates and Forrester's identity; neither supplies this remainder.

2. **Weighted moments.** Reuse the complete universal-factor comparison
   in `ATTEMPTS/2026-09-21-theta-moment-literature-screen.md`:
   Csordas–Varga, *Moment Inequalities and the Riemann Hypothesis*,
   Constructive Approximation 4 (1988), 175–198, Theorem2.4 p.181,
   factors on p.179 (2.11)–(2.16),
   [author PDF](https://www.math.kent.edu/~varga/pub/paper_161.pdf).
   Its paired-real-zero factors, summable reciprocal squares and
   restricted imaginary-axis weights yield adjacent-moment inequalities,
   not an arbitrary signed cofactor bound. That assessment already
   checks actual-K scaling and factorials. Also reuse the unchanged
   finite-order scope warning in
   `2026-10-31-actual-theta-quartic-residual-scope.md`; no additional
   localization mechanism or calculation was pursued.

3. **Iterated-tail cumulants.** John Nuttall,
   [*Wronskians, Cumulants, and the Riemann Hypothesis*, author copy](https://publish.uwo.ca/~jnuttall/det3CAEXP_2.pdf),
   Lemma2.1 p.4 and Sections4.2–4.6, pp.12–15, (4.1)–(4.7).
   Numbering here is that 16-page copy, not the journal pagination
   (Constr. Approx. 38 (2013), 193–212;
   DOI 10.1007/s00365-013-9200-8). Its Phi uses the existing
   K(u)=4Phi(u/2) normalization. It defines Psi_0=Phi and Psi_m by
   repeated upper-tail integration, with kernel
   (t-u)^(m-1)/Gamma(m). Formula (4.4) uses positive Mellin
   parameters s,t, integer m>=0 and ordered nonnegative chambers.
   Section4.4 states k>=r-1+ceil(m/2): positive smoothing leaves
   the requested edge outside this formula. At m=0 arbitrary-order
   reverse regularity has not been supplied. Section4.5 labels the
   needed eventual cumulant premise Conjecture1. Section4.6 explicitly
   retains infinitely many exceptional cases under that conjecture.

Nuttall Lemma2.1 assumes analyticity near (0,infinity) and strict signed
derivative determinants at every t>=0 and p<=r; it invokes Karlin,
*Total Positivity* (1968), Theorem2.6 p.55. Positivity of Phi is not
that determinant hypothesis. Read the full lemma/application proof
and the complete definition, repeated integration-by-parts/composition,
coefficient-range, conjecture and exceptional-case discussion in
Sections4.2–4.6. The
[20 October 2011 lecture](https://publish.uwo.ca/~jnuttall/Nuttall_NYNTS_2011c.pdf),
slides21–31 and35–36, supplies the same conditional framework.
Karlin's original theorem and the full finite-order analytic/numerical
proofs were not audited or independently imported. A future use must
check all endpoints and absolute convergence with the actual kernel;
no new cancellation or interchange justification was performed here.

### Decision and independently identifiable next source

The new evidence is the stated smoothing/index cost and the remaining
exceptional cases. It changes the route: park direct product-K
compensation, preserving L765's norm stop and L766's written,
unaudited pointwise obstruction. No actual integrated sign is decided.

A different mechanism has a specific source lead: Nuttall,
[*Cumulants, the Riemann Hypothesis, and Similar Problems*](https://publish.uwo.ca/~jnuttall/cumanal_a.pdf),
20-page author manuscript. Sections1–2/3.3 specify the different kernel
Theta_1(u)=exp(u/4-pi exp(u)/12) product_(j>=1)(1-exp(-2pi j exp(u)))
and claim eventual all-order cumulant reverse regularity for it.
The essential Sections4–5 induction, its order cost and transfer
hypotheses remain unread. No claimed analogous-kernel theorem is
imported as actual theta. Review that proof separately before
nominating any actual-K inequality. This lead changes representation
and kernel-transfer question; it does not approve mathematics.

A creative attempt is not justified yet: a transferable induction
estimate and exceptional-index control are missing. A finite-order
sign or a restatement of all-order Wronskian positivity would not
remove that blocker. The separate next assessment is REVIEW_REQUIRED.

### Search, duplicates and access

Queries included `Riemann xi theta kernel Toeplitz determinant
integration by parts total positivity`, `Riemann theta kernel moment
inequalities integration by parts Csordas Varga Turan determinants`,
`Nuttall Riemann xi function kernel total positivity derivative
determinants`, `John Nuttall Wronskians cumulants Riemann Hypothesis
2013 pdf`, and exact Riemann queries for `cumulant` `sign-regularity`,
`integration by parts` `Toeplitz`, `signed compensation` `kernel
factorial`, and Nuttall `Wronskians` `2013` `correction`.
No absence, novelty or correction claim follows from these searches.
Unrelated Riemann–Hilbert/Toeplitz hits were not mathematical evidence.

Local searches covered relevant actual-theta/Toeplitz assessments,
theta ATTEMPTS, and exact Nuttall/cumulant/source-filename terms in
literature, foundations and history. No prior matching cumulant-source
assessment was located in those bounded searches. Read L019/L021/L766;
reused supplied PROOF/DAG and adequate prior literature. No sibling
notebook read; no claim of exhaustive duplicate exclusion.

Browser Nuttall PDFs supplied the needed text. Shell retrieval failed
DNS. The Csordas–Varga PDF had no extracted text and screenshot
attempts yielded no readable pages; existing adequate coverage was
reused without claiming a fresh primary reading. No persistent essential
access blocker is reported. Full matching Mathlib coverage remains
unchecked. No lemma, mathematical script, DAG or PROOF argument changed.
