# Coverage for the L097 critical audit

TARGET: Critically audit L097's conditional product-dual support obstruction, including its small-support rank bounds and full-support parity, under L088/L089's surviving-plane hypotheses.
CHECKED: 2026-10-16
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the bounded product-code searches and primary extractions in drafts/literature/2026-10-16-cyclic-projected-code-schur-square.md; scoped searches of local literature, ATTEMPTS and history found L097 and its unaudited step-252 report, not an independent completed audit.
SOURCE_EVIDENCE: Reused Randriambololona Proposition 2.38 and proof (printed p. 28), BSZ arXiv:1510.01354v2 Theorem 3 (pp. 2–3) and stabilizer remark (p. 9); compared L010's opening proof, L088's hypotheses/conclusion and separation certificate, and L089's hypotheses/conclusion and existing Mathlib qualifications.
COMPARISON: The inspected primary inputs cover adjunction and the polynomial lower comparison, but do not assert the cyclic support threshold twelve; that finite-dimensional specialization is the object of the separate audit, with no new external technique or changed field hypotheses.
GAP: L097's complete small-support rank argument, isotropic-dimension application and full-support parity still require mathematical audit; source adequacy does not establish correctness, a surviving plane or a cyclic exclusion.
REASON: Existing source coverage suffices for the exact bounded audit without reopening the stopped product-upper-bound search; EXPLORE permits checking the local specialization and makes no originality claim.
LITERATURE_REASON: The newly proposed exact critical-audit target was REVIEW_REQUIRED; this turn compares its scope with ready saved primary evidence rather than repeating discovery on the old product target.
SCOPE: Arbitrary bijective H-labelings, k=F_97, F=F_(97^20), and a hypothetical rational two-plane meeting all sixteen cyclic block spaces; all full coefficients and all support sizes 1–11, with no MDS, plane-existence, original-chart or product-upper-bound assumption.

## Reused primary coverage

The earlier [assessment](2026-10-16-cyclic-projected-code-schur-square.md)
contains the queries, source versions, inspected theorem and proof passages,
and applicability qualifications. They are reused, not freshly fetched in
this turn. No essential unread source or persistent access blocker was found.
No additional broad external search is needed for this unchanged algebraic
scope. The earlier unread function-field Freiman and random-code leads remain
unread and are not inputs.

Hugues Randriambololona, *On products and powers of linear codes under
componentwise multiplication*, Contemporary Mathematics 637 (2015), 3–78,
DOI 10.1090/conm/637/12749,
[author manuscript](https://perso.telecom-paristech.fr/randriam/maths/HR_AGCT-14.pdf),
Proposition 2.38 and proof, printed p. 28 (no manuscript version identifier
inspected), supplies coordinate adjunction. Its specialization recorded in
L097 is z in (C*C)^perp exactly when z*C is contained in C^perp.
This requires all products, equivalently the twenty-one unordered basis-pair
tests for a six-dimensional code; it does not turn a linear block parity
into a product parity. No MDS hypothesis enters this source input.
The support threshold is not a conclusion imported from that proposition.

Christine Bachoc, Oriol Serra and Gilles Zemor, *Revisiting Kneser's Theorem
for Field Extensions*, [arXiv:1510.01354v2](https://arxiv.org/pdf/1510.01354v2),
24 February 2017, Theorem 3, printed pp. 2–3, and the stabilizer remark
before Corollary 14, p. 9, cover the ancillary lower comparison. The saved
assessment includes the relevant final proof cases on pp. 15–16. It applies
to nonzero finite-dimensional subspaces of an arbitrary field extension;
the deficient-product alternative has a larger stabilizing subfield.
The existing specialization uses W inside k(X), whose algebraic constants
are k, then injective evaluation of products of degree at most fourteen
at sixteen distinct labels. The later audit must verify this specialization
as written, rather than identifying function-field stabilizers with those
of coordinatewise products in k^16. The comparison eleven is imported
mathematics, not the new support assertion.

The saved MZ comparison (arXiv:1501.06419v2, Lemma 2.1 and Theorems 2.5,
3.3, 4.2) already records the MDS and stabilizer qualifications. The saved
CPTZ comparison (arXiv:2412.15160v1, Propositions 6 and 10) already separates
polynomial products from evaluated products and does not give the upper
threshold ten. Neither classification is needed for this audit; neither
licenses calling C MDS. No fresh reproof of these sources is proposed.

## Local input scope, duplicates and stopped routes

The supplied DAG records L010, L088 and L089 as L097's direct inputs.
L010's opening proof supplies distinct-column Vandermonde independence and
the subgroup power sums, independent of its later nonpersistent-pencil
hypotheses. L088's separation subsection supplies disjoint containing blocks
for every pair of abstract indices; its index translations assume no symmetry
of the H-labeling. L089's conclusion supplies the absence of contained moment
columns and the full four coefficients of every block-intersection line.
These are precisely the local hypotheses invoked by L097. Its passage from
a rational plane over k to the kernel setting over F and back remains an
audit obligation; it is not an extra assumption of source coverage.

The targeted reads locate the necessary statements, not a second audit of
those established inputs. Their saved step-223 and step-226 audits are reused.
The L010/L088/L089/L097 Mathlib notes report matching coverage not checked;
this review makes neither an absence claim nor a Lean-verification claim.

History/252 records the original support obstruction and explicitly leaves
its critical review open. ATTEMPTS/035 stops the sparse-product transfer,
not the validity check of its negative evidence. History/254 selected this
independent audit after the four-anchor mechanism stopped. No duplicate
completed L097 audit was located. No cross-notebook result is used.

## Approved audit and discriminating test

The exact TARGET is ready for one separate RESEARCH/proof_audit turn.
Check L097's written proof, not a replacement upper-bound construction:
retain exact support S=supp(z), all nonzero diagonal entries, every bilinear
basis-pair equation, the support cases 1 through 11 (including possible
three-column dependencies), and the full-support vector z_i=h(i).
Check the block-hyperplane example and the cancellation conclusion against
those same hypotheses. The polynomial lower comparison and the gap between
one known parity and six needed directions must retain their stated limits.

The downstream use is validated negative evidence against sparse transfers,
or a precise correction/withdrawal if an essential case fails. Continue with
the obstruction only if every support case and parity step is justified;
otherwise record the exact defect and stop using the affected conclusion.
Neither outcome proves plane existence, gives dense constraints, improves
11/q–16/q, or settles arbitrary-family and challenge-definition gaps.
The audit does not reopen ATTEMPTS/035 or authorize a labeling census.

This literature-only step approves coverage; it does not perform the audit,
derive a new result, modify lemmas or scripts, or certify originality.
