# Isolated-anchor net bound — completed separate audit coverage

TARGET: Critically audit L066's isolated-anchor cubic bound and its necessary profile for thirteen additional triangle recoveries, including degree loss, zero fourth weights and original finite gates.
CHECKED: 2026-10-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the eight triangle/count searches and four both-zero/net searches recorded in the ready assessments; read all of L066, relevant L010/L057/L065 statements and ingredient ranges, ATTEMPTS/025 and history/149; completed the exact audit-scope comparison below.
SOURCE_EVIDENCE: Reused Chojecki author TeX v9.2 (July 17, 2026) DR2 and DR6–DRC, lines 2785–2935, previously inspected with proofs; Hall Theorem 5.1.1 and interpolation discussion pp. 63–65; Marquez-Corbella–Pellikaan section 5 Lemma 5.3 and shortening formula pp. 7–8; Thaler July 18, 2023 manuscript Fact 2.2 p. 16 and qualified Lemma 2.3 pp. 19–20; local source applicability inspected below.
COMPARISON: L066 claims a conditional bound three, improving L065's five/six only in the presence of a full isolated disjoint-P anchor; the hypothetical thirteen-additional case supplies that anchor, but no multiple-isolated-row bound or uniform twelve follows.
GAP: Mathematical audit remains: verify the complete division-free recurrence identity, matrix kernel equivalence, nonzero determinant at the actual full isolated anchor and threshold application; no source supplies the conditional cubic count or a uniform twelve bound.
REASON: Existing discovery and precise ingredient coverage remain adequate under unchanged hypotheses; this separate comparison approves one subsequent audit of the exact TARGET, without certifying L066 or originality.

Essential inputs are L010, audited L057 and audited L065. L066's
direct dependencies are exactly these; L041 enters through L057/L065.
L059 explains the downstream seven-scalar filter but is not needed
for L066's actual-parameter proof. No L060–L064 result is assumed.

Reuse `2026-10-10-triangle-twelve-recovery-bound.md` and
`2026-10-11-triangle-both-zero-classification-audit.md` where their
scope matches. No fresh external browsing is justified solely by this
new audit record. The separate approval must compare the exact net
specialization with those inputs before approving the mathematical audit.

The proposed audit must check the five-node interpolation identity at
all four recurrence rows, including net polynomials with f(P)=0 or
degree below four; independence of the three net generators even for
dependent pair quadratics; signs in M and equivalence with the complete
recurrence; the actual nonzero scaling at the isolated full-weight
anchor; and why a net annihilator would contradict that support's
isolated projected case. The proof must establish Delta(mu_*)!=0,
not simply assume a generic determinant. Verify the degree-three root
count over F and the injective original finite scalar change.

For the threshold application, check that thirteen additional plus
three base parameters are distinct actual bad events; nonpersistence
and L010 supply fullness before the six shared-label incidence count.
At least seven disjoint-P parameters and audited L065's maximum six
then supply a full isolated anchor. Check at most three both-zero,
at least ten isolated total and at least four isolated disjoint-P.
No existence of thirteen, rational original chart, bound on isolated
rows, finite maximum or challenge solution is assumed. Lower-weight
anchors outside this threshold are explicitly beyond the conclusion.

The original proposed audit checklist above is retained. Coverage approval
is completed below; the critical mathematical audit has not occurred.
Full matching Mathlib coverage remains not checked.


## Separate source comparison completed at step 150

LITERATURE_REASON: L066 introduced a new conditional anchor/count claim and saved this exact audit target as REVIEW_REQUIRED; compare its scope separately while reusing unchanged ingredient coverage, without repeating external browsing.

The main gap remains the uniform triangle twelve bound and, independently,
arbitrary-family extraction and challenge-definition certification. The
intermediate target is exactly the stated critical audit. Validating L066
would constrain a hypothetical thirteen-additional case to at least four
isolated disjoint-P rows, giving a possible entry to simultaneous isolated
row analysis. That downstream analysis is not approved or performed here.

Read the full L066 proof for theorem-level scope, not as a correctness
audit. Read L010 hypotheses/conclusions and moment factorization (4)–(5),
L057 hypotheses and imported recurrence (15), and L065 hypotheses,
classification (1), six-evaluation argument and simultaneous-parameter
section. These show that the proposed audit uses only L010/L057/L065;
L041 enters through audited inputs. L060–L064 and rational descent are
unnecessary, and no cross-notebook result is used.

Reuse the primary source extractions in
`2026-10-10-triangle-twelve-recovery-bound.md` and
`2026-10-11-triangle-both-zero-classification-audit.md`:

* Chojecki, *Shortening Bounds for Reed–Solomon MCA*,
  [author TeX v9.2, July 17, 2026](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
  DR2 (`drc:lem-locator-recurrence`) and DR6–DRC
  (`drc:thm-exact-compiler`), lines 2785–2935, statements and full proofs
  inspected October 10. Distinct labels, nonzero weighted-Vandermonde
  multipliers and t<R are essential. L057 uses R=8,t=4 and multiplier x;
  H has distinct nonzero labels and the syndrome can lie anywhere in F.
  L066 changes none of these hypotheses. The source concerns the full
  recurrence, not the quotient's both-zero case. Restoring the shared
  columns remains necessary. No cubic net determinant count is supplied.
  The mutable version is not certified identical to ePrint 2026/1463.
* Hall, *Notes on Coding Theory*,
  [GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
  Theorem 5.1.1 and proof pp. 63–64, interpolation discussion p. 65;
  and Marquez-Corbella–Pellikaan, FFAA 40 (2016), 224–245,
  [accepted manuscript 2016-02-29](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
  section 5 Lemma 5.3 and following shortening formula pp. 7–8.
  The recorded n=16,k=8 distinct-label/unit-multiplier specialization and
  seven shortenings supplying Q(x) remain unchanged. The standard named
  Lagrange interpolation formula applies to five distinct nodes over F;
  degree at most three in the coefficient identity does not require a
  degree-four net polynomial or nonzero f(P). These are audit obligations
  for the written identity, not a new interpolation theorem or derivation.
* Thaler, *Proofs, Arguments, and Zero-Knowledge*,
  [author manuscript July 18, 2023](https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.pdf),
  Fact 2.2 p. 16 supplies the nonzero-polynomial root bound over any field.
  The previously inspected Lemma 2.3 and proof pp. 19–20 restrict nodes
  to 0,...,n-1 in a prime field p>n; it is supporting reading only and
  is not imported literally for these five labels. The standard named
  Lagrange formula and Hall coverage suffice. Root counting requires
  proving Delta nonzero first; it supplies no anchor nonvanishing.

The additional restriction to the three-generator net, determinant/kernel
equivalence and nonvanishing at a full isolated anchor are local work
requiring audit, rather than a reproof of the general recurrence. L010's
factorization supplies the exact full-weight Vandermonde ingredient;
its scope includes all eight moments and cannot be replaced by a
lower-weight relaxed anchor. L065's net equivalence is stated over F
as well as F_97, so coefficient descent is not an essential new input.
Dependent pair quadratics do not by themselves establish dependence of
the quartic generators. The audit must inspect this distinction.

The ready wider-result comparisons (proximity, subspace designs,
average-radius bounds and fixed-core/circuit compilers) retain their
recorded missing hypotheses or insufficient thresholds. This exact
conditional bound does not acquire those hypotheses. Their unread leads
are not essential inputs. No newly inspected external theorem or new
search result is claimed; search failure never establishes novelty.

Duplicate and failure comparison: L065 gives five/six without the full
anchor, not three; L057 supplies recovery rather than simultaneous
counts, and L010 supplies sixteen-total equality consequences rather
than this net restriction. ATTEMPTS/025 and history/149 were read: the
selected-label/formal-resultant route remains stopped, while this proposed
uniform analytic audit tests an actual full-weight anchor. No finite
sample or unaudited pair/table bound enters. No independent local duplicate
of L066's whole conditional claim was established in these scoped records.

Approve exactly TARGET for one subsequent RESEARCH proof_audit. Continue
if all four identity rows, all net degree/vanishing cases, the full anchor
scaling and annihilator argument, and the original finite threshold
application verify. If any fails, preserve the evidence and repair or
restrict the claim before using it; a lower-weight uniqueness argument or
merely generic nonzero determinant fails the test. No new isolated-row
bound or computational search is authorized by this assessment.

This completed coverage comparison derives no mathematics, performs no
critical audit and edits no lemma, mathematical script, DAG or PROOF.md.
Full matching and exact supporting Mathlib coverage remain not checked;
no absence or formal-verification claim is made.
