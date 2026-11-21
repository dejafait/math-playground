# Fourth-order large-smoothing comparison — completed source review

TARGET: Assess a uniform large-m asymptotic for the r=4 full-B cumulant determinant and its complete theta perturbation on u>=0, seeking an effective M4 with relative error below 1/2.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step398 searched variable-m asymptotic, uniform, RR4 and iterated-integral terminology; followed the author's numerical-pattern and March2013 progress reports; reused step392/393 coverage. No inspected matching effective uniform relative theorem was located; no novelty inference follows.
SOURCE_EVIDENCE: Newly read Nuttall Progrepa.pdf Sections2.1–3.2, pp.2–4 (March2013); Treestory.pdf Section3.1, p.6; cumanal_a.pdf Theorem5.6/Section5.5.3, pp.17–19, with earlier essential proof coverage reused; Wang–Yang author PDF, definitions and Theorems1.1–1.3, pp.2–4. Exact links and read limits below.
COMPARISON: The full-B large-smoothing program is known precedent, still conjectural in the inspected progress report; the Theta1 theorem and coefficient Laguerre results do not supply a full-B signed lower bound, effective M4 or uniform relative error. L767/L768 settle only the audited fixed pair.
GAP: Positive S_(4,m)(B;u) and complete-theta relative error<1/2 uniformly for every u>=0 and integer m>=M4 remain unproved; moving height regimes and determinant cancellation require explicit control.
REASON: Coverage now supports one bounded development attempt on the identified quantitative difference; no known matching theorem is available for import from the sources inspected. This is established-route exploration, not a new mechanism or approved theorem.
LITERATURE_REASON: The invocation changed determinant order and made smoothing variable; essential exact-scope coverage was missing. This review completes that gate and does not justify another unchanged source turn.
SCOPE: Literature-only completed step; ready coverage for the exact source target and the single research continuation below, subject to separate next-turn supervisor approval. Full B, L019 K, the stated factorial convention, r=4, integer m>=7 and all u>=0 only; no general-r or exceptional-index transfer.
COVERED_TARGET: Test the r=4 full-B cumulant comparison uniformly for all integers m>=M4 and u>=0, seeking explicit M4>=7, a positive signed base and relative complete-theta error below 1/2.

The following paragraphs retain the original nomination and its limits;
the completed step398 decision and bounded continuation follow them.

Main gap remains actual-Xi all-degree positivity. This intermediate
target tests whether the successful fixed comparison has a controllable
smoothing-order mechanism, rather than merely certifying another
fixed integer pair. Even an effective M4 would leave general r and the
exceptional coefficient interface unresolved. No claim that it suffices
for RH is made.

Use L019's full first summand B and exact K, and the original convention
C_m(F;u)=1/(m-1)! integral_u^infinity (v-u)^(m-1)F(v) dv. For the
proposed target set S_(4,m)(F;u)=det[partial_u^(i+j) C_m(F;u)]
for i,j=0,...,3 and integer m>=7; the usual sign (-1)^6 is positive.
These definitions nominate a question, not a derived assertion.
The prospective threshold is an explicit M4>=7 such that the base is
strictly positive and the absolute actual/base error is below 1/2
for all m>=M4 and all u>=0, retaining u=0 and the moving transition
between m and x=pi exp(2u). A sign obstruction or a quantitatively
unpaid error in one specified regime is a useful alternative finding.

Reuse L767/L768 only within their audited fixed scope. They give a
normalization and finite-evidence method, not the required uniformity.
The prior source assessments already explain why pure-exponential
induction and the different Conrey–Ghosh kernel do not transfer by
citation. Preserve those stops; identify a specific full-B asymptotic
estimate or a genuinely different representation before authorizing
mathematical work. Do not repeat an unchanged inaccessible-source
search or label a parameter scan an all-order mechanism.

The next source review should first locate primary statements and
essential proof cases concerning the full polynomial factor and joint
smoothing/height regimes, then compare stronger known results and
recorded obstructions. An adequate exact theorem should be imported;
otherwise an EXPLORE/SPECIALIZE decision must identify the bounded
difference and its test. This nomination does not approve that decision.

No justified creative central-gap mechanism emerged from the fixed
audit: the retained signed-split method has a direct source precedent
and provides no general order cost or edge transfer. This new source
target is intended to determine whether a substantive mechanism is
available, not to assign a creative label or meet a lemma quota.
Mathlib coverage remains unchecked. No cross-notebook input is proposed.

## Completed comparison — step398

### Primary scope and stronger-result checks

Reuse the adequate step392/393 assessments rather than re-auditing their
sources. In particular the unsmoothed full-polynomial formula in
basicRH.pdf Theorem3.1, the RR3 result in det3CAEXP_2.pdf, and the
positive-level numerical splits in RHsplit.pdf have their recorded
qualifications. No theorem from these sources is newly imported.

Nuttall, [*Wronskians and the Riemann Hypothesis*](https://publish.uwo.ca/~jnuttall/wronskRH.pdf),
August2012, seven-page report, Section3.3/Conjecture1 and Section4.1,
pp.4–5, was checked specifically for the changed quantifiers. The
increasing-m full/first-term ratios there are numerical trends at
specified heights; they are not a bound on the supremum over height.
This is exact mechanism overlap, not proof of the proposed inequality.

Nuttall, [*Progress Report on the RH and the Eight CG Functions*](https://publish.uwo.ca/~jnuttall/Progrepa.pdf),
March2013, four-page author report, Sections2.1–2.2, p.2, still
separates proved low orders, numerical higher-order regularity and
the conjecture. Large smoothing with first-term dominance is proposed,
not proved. Sections3.1–3.2, pp.2–4, retain lower-index gaps and give
numerical minor patterns. They supply no quantitative full-B bound.

The linked [*Numerical Patterns Related to the Riemann and Conrey–Ghosh Phi Functions*](https://publish.uwo.ca/~jnuttall/Treestory.pdf),
eight-page author report, title/abstract and Section3.1, p.6, explicitly
describe numerical minors without independent verification. Its
Section2 identities were located but not audited or imported: this
lead concerns discrete minors, not a uniform smoothing certificate.
No internal version date was established for this report.

Reuse step392 for Nuttall,
[*Cumulants, the Riemann Hypothesis, and Similar Problems*](https://publish.uwo.ca/~jnuttall/cumanal_a.pdf),
20-page author manuscript (internal date unestablished), Lemmas4.1–4.3,
5.1–5.5 and their essential proof cases. Newly rechecked Theorem5.6,
p.17, and Section5.5.3/(5.71)–(5.73), p.19: the theorem fixes r>1,
asserts a sufficiently large smoothing level M and strict signed
Wronskians for every p<=r and u>=0, solely for Theta1. Its base is
exp(u/4-pi exp(u)/12), with remainder separation Q1/Q=25; it is
not full B. The final comparison invokes large mu=m/Q(u) and calls
small mu favorable, without giving effective uniform constants or M.
These statements identify proof obligations, not a transferable bound.
The earlier normalization/display qualifications remain in force.
No source-proof correctness or disproof claim is made.

A stronger-result search also located Larry X.W. Wang and Neil N.Y.
Yang, [*Laguerre Inequalities and Complete Monotonicity for the Riemann Xi-function and the Partition Function*](https://cfc.nankai.edu.cn/_upload/article/files/81/18/f83d37e449ebaf1b2f4141fa59be/9323c2fc-4d6a-4610-a747-1bd985a7be41.pdf),
21-page author-hosted accepted-layout copy, received29October2022;
DOI10.1090/tran/9081. Read the coefficient definitions and
Theorems1.1–1.3, pp.2–4. Theorem1.3 concerns eventual discrete
Laguerre inequalities of gamma(n), with stated n>c r^3, not the
height-dependent tail cumulants. The general criteria require
controlled log-ratio expansions; they do not supply those expansions
for this full-B determinant. No proof or coefficient result is imported.
The cited separate determinant paper [36] remains an unread lead;
its mentioned discrete conclusion is not used as a theorem here.

### Ready bounded difference and decision

DECISION EXPLORE permits a proof attempt, not acceptance of a conjecture.
Use exactly the COVERED_TARGET. First seek a signed integral or
determinant representation for full B, preserving its polynomial
factor, then attempt quantitative comparison with the complete theta
tail. The source's determinant-integral and column-split methods are
precedent; no new representation is derived in this literature turn.
Reproving a matching known sign theorem is not the objective: the
uncovered difference is an effective relative bound, uniform in both
parameters, for the actual full-polynomial base.

The attempt must retain u=0 and control all ranges of x=pi exp(2u)
relative to m, including moving transition heights, rather than infer
uniformity from a fixed-u asymptotic. A large-m argument must include
quantified remainders and an explicit integer onset, or honestly leave
that portion open. Entrywise small errors or positive scalar tails do
not license a determinant-relative estimate without a signed base
lower bound and paid cancellation. The audited fixed r=3,m=5
certificate is useful normalization precedent only.

Continue if the attempt yields a signed representation with an
effective lower bound and a uniform perturbation estimate capable of
reaching 1/2, even if an independent coefficient gap remains. Success
at the full target requires a stated M4>=7 and strict inequalities
for every integer m>=M4 and real u>=0. A certified sign failure or
relative error>=1/2 refutes that parameter/onset; rejecting every
possible onset needs an obstruction surviving arbitrarily large m.
If one regime remains quantitatively unpaid, record it as an
inconclusive attempt and require refined input before repetition.
Finite grids and unquantified pointwise limits are inconclusive.

Essential inputs: L019 K/B and decay; L767/L768 at their fixed scope;
step391's coefficient-interface assessment; step392/393 source limits.
No source conjecture, sampled ratio, or unproved Wronskian sign is an
input. General r, usable order cost, lower-index transfer and all-Xi
signs remain unresolved. No new mathematical DAG node or theorem
import is warranted. Mathlib coverage of the uniform comparison and
supporting asymptotic theorem is unchecked, not known absent.

The route is difficult development of an established method. No
justified creative central mechanism emerged: increasing smoothing
is itself in the primary proposal, and neither a new signed structure
nor exceptional-index control has been obtained. The blocker to a
creative nomination is mathematical, not a scheduling quota.

### Search record, access and bounded reads

New queries included `Nuttall Wronskians cumulants large m asymptotic
Riemann kernel polynomial`, `"Riemann" "cumulants" "asymptotic"
determinant smoothing`, `"Nuttall" "cumulants" "large" "uniform"`,
`"Riemann" "cumulants" "saddle" Wronskians`, `"Nuttall" "cumulants"
"uniform" theta`, `"Riemann" "cumulants" "RR4"`, `"Riemann"
"Wronskians" "fourth" cumulants`, and `"theta" "iterated integrals"
"sign regular"`. Followed primary author-index links to Progrepa.pdf
and Treestory.pdf; bibliography/search snippets were leads only.
The searches establish no novelty or exhaustive absence result.

Accessed all sources2026-11-04. Browser PDF text supplied the relevant
statements and final proof cases. Screenshot requests supplied no
inspectable images (one timed out), and direct shell download failed
DNS; neither prevents this scope comparison through the extracted
text. No visual formula verification is claimed. The Wang–Yang DOI
page returned403; its author-hosted copy supplied the statements.

Local checks read only the named step391–393 assessments, the relevant
transfer ATTEMPT/history/working notes, L019, and the hypotheses and
normalization ranges of L767/L768. Their detailed certificates were
not replayed. Existing work was preserved. No sibling notebook,
mathematical script, new lemma, calculation or proof derivation was
used. The completed review changes coverage from REVIEW_REQUIRED
to EXPLORE; it does not close any RH sign gap.
