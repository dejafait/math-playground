# Triangle two-row compatibility — completed audit coverage

TARGET: Critically audit L064's two-row triangle compatibility bound, including both-zero degeneracies, shared-singleton-pair exclusion and distinct original finite recovery parameters.
CHECKED: 2026-10-12
DECISION: EXPLORE
SEARCH_EVIDENCE: Three targeted two-support/two-row/syndrome-pencil searches supplied no inspected matching theorem; reused the ready triangle-count comparison and stronger-result searches. Read full L064, relevant L010/L041/L057/L059 statements and source/audit passages, L065's overlapping common-pair proof/audit, history/144–145 and ATTEMPTS/025; scoped local search found no completed L064 audit.
SOURCE_EVIDENCE: Reused Chojecki author TeX v9.2 (July 17, 2026), DR2/DR6–DRC statements, proofs and zero cases, lines 2785–2935; Hall Theorem 5.1.1, printed pp. 63–64; Marquez-Corbella–Pellikaan section 5, Lemma 5.3 and GRS shortening formula, printed pp. 7–8; Thaler July 18, 2023 manuscript Fact 2.2, printed p. 16. Previously inspected primary passages and applicability records were reused, with no new primary retrieval.
COMPARISON: The sources cover individual support recurrence, standard distance/shortening and polynomial root bounds, not L064's simultaneous elimination. L065 already audits the overlapping common-pair obstruction, but not the bound two or isolated-row bound one. L064 restricts normalized weights to G^3 over F_97 while retaining arbitrary extension-field original charts; it is not an arbitrary-normalized-weight or simultaneous-support bound.
GAP: Critically verify L064's reversible elimination and all constant-coordinate/quadratic-identity cases, with distinct eligible scalars, both-zero lifts, zero fourth weights and original finite gates; coverage is ready but no correctness audit or seven-scalar exclusion is completed.
REASON: Approve exactly TARGET for one subsequent bounded proof audit using unchanged ready ingredients; the finite normalized-weight scope is now explicit and no essential unread source is needed. No new mathematics, stronger count or originality is certified.
SCOPE: Exact TARGET only: F=F_(97^20), F_0=F_97, fixed order-sixteen H, RS dimension eight, pinned cell, nine distinct triangle labels, w=(p,q,r) in (F_0 minus {0,1})^3, distinct fixed K,L in H minus P and mu,nu in F_0 minus {0,-1} with mu!=nu. Original finite gamma_i are distinct in F, lambda!=0, rho!=0,1; retain both-zero pivots, zero fourth weights and each original E gate. Essential inputs L010/L041/L057/L059; L064 is the audit object, not an assumed theorem.
LITERATURE_REASON: The concrete two-row critical audit was a changed REVIEW_REQUIRED target outside the census gate; this separate approval reuses unchanged recurrence, distance, shortening and finite-chart coverage.

Main gap: exclusion of arbitrary sixteen-count equality families. Intermediate
target: critical verification of L064, not a new count theorem. Its plausible
use is a checked pair-compatibility constraint in a later triangle simultaneous
count argument. The fixed-pair bound alone does not exclude seven-scalar fibers
or prove the uniform twelve bound. Other patterns, extraction and challenge
qualifications remain unresolved.

Essential local input IDs are L010, L041, L057 and L059; L064 is the audit
object, not an established premise. Its full hypotheses and proof were read
for coverage. The proposed boundary's unqualified phrase “arbitrary
extension-field weights” is corrected: L064 requires rational normalized
weights w in G^3. Actual errors still have the unrestricted F-valued factors
lambda/alpha_i, and the original finite chart remains unrestricted. Extending
the conclusion to arbitrary normalized w would be a different target;
L058's conditional descent is not needed for this audit. No rational original
chart or full recovered weight is assumed. No computational census or
sibling-notebook result is an input; Mathlib coverage is not checked.

Continuation/abandonment test: ingredient coverage now permits the separate
audit below. Continue only if the elimination and every apparent
positive-dimensional branch verify with the stated gates. A specific defect
requires recording and repairing that defect before using the bound; if no
defect is found, record only a checked fixed-pair input. Sampling support
pairs cannot replace the uniform argument. No proof audit, coefficient
expansion, new algebra or mathematical script was performed in this review.

Duplicate/failure screen to reuse: history/144 records L064's partial result;
later scoped histories continue to list L060–L064 audits as pending. L068's
separate audit is already history/158 and is not a fresh continuation.
ATTEMPTS/025 preserves the stopped formal-common-root/sampled-label route;
this proposed audit is a check of an existing uniform argument, not its
reopening. Retain all existing unfinished work and original stop evidence.

## Precise source reuse and boundary comparison at step 185

Reuse `2026-10-10-triangle-twelve-recovery-bound.md` and the completed
L057/L059 audit coverage; the target is verification of an existing partial
restriction within that assessed triangle mechanism. No source is imported
as the whole fixed-pair theorem.

- P. Chojecki, *Shortening Bounds for Reed–Solomon MCA*,
  [author TeX v9.2](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
  July 17, 2026, DR2 (`drc:lem-locator-recurrence`) and DR6–DRC
  (`drc:thm-exact-compiler`), lines 2785–2935, statements/full proofs and
  zero-direction cases inspected October 10. Distinct weighted Vandermonde
  columns, nonzero multipliers and t<R are required. L057 uses R=8,t=4,
  multiplier x, eta_j=s_(j+1); H is nonzero and distinct. The full-vector
  recurrence theorem does not discard both-zero projected rows: L057's
  restored equations and nonzero-pivot theorem remain essential. No general
  recurrence reproof is justified. This mutable version is not certified
  identical to ePrint 2026/1463; no fresh source-version claim is made.
- J. I. Hall, *Notes on Coding Theory*, undated author-hosted GRS chapter,
  [Theorem 5.1.1 and full proof](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
  printed pp. 63–64, reused from the October 5 two-block assessment.
  Distinct evaluation points, nonzero multipliers, 0<k<=n hold for
  n=16,k=8 and unit multipliers over F. L010's supporting eight-column
  shifted-Vandermonde argument and sparse-error uniqueness are read locally;
  L064 does not need L010's sixteen-count equality as an assumption.
- I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
  that have an error correcting pair*, FFAA 40 (2016), 224–245,
  [accepted manuscript, 2016-02-29](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
  section 5, Definitions 5.1–5.2, Lemma 5.3 and subsequent unnumbered GRS
  shortening formula, printed pp. 7–8. L041's source-specialization passage
  identifies the seven deleted labels, successive dimensions 8-r>=2 and
  nonzero multiplier differences. The final one-dimensional kernel on U
  has multipliers c_x=Q(x). The MDS condition 16-7>=8 holds. The local
  converse, not the equality-premised direction, supplies L064's auxiliary
  pencil; no shortening theorem is reproved.
- J. Thaler, *Proofs, Arguments, and Zero-Knowledge*,
  [July 18, 2023 author manuscript](https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.pdf),
  Fact 2.2, printed p. 16, any-field nonzero-polynomial root bound, previously
  inspected in `2026-10-11-triangle-both-zero-classification-audit.md`.
  It supports only the nonzero degree-at-most-two branch. The simultaneous
  polynomial-identity branch remains a local obligation; a root bound cannot
  settle it. Thaler's separately inspected prime-field interpolation lemma
  is not invoked for arbitrary triangle labels.

The stronger compiler, design, random-evaluation and average-radius
comparisons in the ready triangle assessment remain unchanged. They require
missing fixed-core/design/random-domain premises or give weaker constants;
none was read as a source for the simultaneous fixed-pair bound. No fresh
extraction or new specialization of those results is needed.

Read L059's table statement and successful rational-pivot, original-chart
and nonprime-chart audit cases. They cover a scalar union rather than a
support-witness count, give the exact disjoint-P row formula, and allow
realization of all rational retained scalars in a newly constructed
nonprime chart. That construction does not change the chart of a given
pencil. For a given chart both E gates still apply and only delete rows.
L057's restored-coefficient proof explicitly distinguishes beta values
computed from the first rows from full separate systems: the latter are
available for both-zero rows, precisely where L064 uses them.

## Duplicate screen and bounded discovery

New queries issued October 12:

- `"Reed-Solomon" "two" "supports" "compatibility" pencil`
- `"mutual correlated agreement" "two-row"`
- `"Reed-Solomon" "syndrome" "pencil" "quadratic"`

Returned results included unrelated hardware manuals/patents, general
coding materials and a secondary paper-summary repository. No relevant
primary theorem statement was retrieved from these hits; snippets and the
secondary summary are unread leads, not mathematical support or evidence
of originality. This bounded search supplements, rather than replaces,
the broader previously completed syndrome-pencil/count comparison.

History/144 records L064's completed partial restriction and pending audit.
History/145 and ATTEMPTS/025 record the unsuccessful three-row formal-root
and selected-label test. The exact fixed-pair audit is not a repetition of
that experiment. L065's “Simultaneous parameters and all gates” proof and
its separate audit already verify the overlapping same-singleton-pair
kernel obstruction, even with relaxed weights. This is a duplicate part,
not an independent verification of L064's equations or bound two. Read it
for comparison only; no new DAG input or reproof is introduced here.
The scoped histories still list L064's full audit as pending. Restricted
L060–L063 tables, blocked census files and L068's completed witness audit
are not necessary inputs. Preserve all their evidence and pending work.

## Approved next-turn audit obligations

Approve exactly TARGET for one RESEARCH proof-audit turn. Reuse this
EXPLORE assessment without further discovery while the scope is unchanged.
Read the complete L064 proof and needed L010/L041/L057/L059 passages;
check, without assuming L064's conclusions:

1. Reversibility of all three weight-equality equations, z=mu nu, scalar
   gates and retained projected/weight tests, including rejected rows.
2. The auxiliary nonprime-chart construction and distinct finite recovery
   parameters; common-pair exclusion must retain zero fourth weights and
   nonzero base weights. Compare the already audited overlap without
   treating it as verification of the whole theorem.
3. The constant-coordinate iff statements only for both-zero rows, the
   full restored systems and the use of the nine-label kernel identity.
4. The isolated-row case, both zero/nonzero u_c cases and the two
   degree-at-most-two polynomials; check all identically-zero coefficient
   cases and exclusions, without dividing by a possibly zero coefficient
   or assuming the three-by-three matrix invertible.
5. The given original chart's two E gates and precise counting unit:
   compatible triples for a fixed ordered pair, with rational normalized
   weights. No bound on simultaneous supports, seven-scalar fibers,
   arbitrary normalized weights, uniform twelve or extraction follows.

The audit may validate an existing partial input or expose a specific
defect. It is not a new simultaneous-count attempt or an approval of a
complete candidate. Full matching and supporting Mathlib coverage remain
**not checked**, with no absence claim. This literature turn changes no
lemma, mathematical script, DAG or main argument; the global interval
remains 11/q–16/q and the challenge qualifications remain unresolved.
