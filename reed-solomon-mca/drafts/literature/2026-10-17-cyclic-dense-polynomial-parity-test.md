# Dense polynomial product parity — source assessment

TARGET: Test whether a hypothetical L088–L089 cyclic plane admits a nonconstant polynomial R of degree at most four such that (h(i)R(h(i)))_i annihilates every product from Ann(P), retaining all twenty-one bilinear equations.
CHECKED: 2026-10-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded polynomial-weight/product-dual and conductor searches, followed to Barelli–Couvreur arXiv:1805.05429v1 Section 3; reused the saved Randriambololona/BSZ/MZ/CPTZ assessments and checked L097, ATTEMPTS/035 and history/267 for duplicates and stopping scope. No inspected theorem settles the specified polynomial family.
SOURCE_EVIDENCE: Reused Randriambololona Proposition 2.38/Corollary 2.39 and BSZ Theorem 3; newly read Barelli–Couvreur arXiv:1805.05429v1 Definition 20, Propositions 21–22 with the latter's complete proof (p. 10), Theorem 26 with proof and Heuristic 27's discussion (pp. 12–13). Primary arXiv access resolves the failed ePrint PDF request.
COMPARISON: The general conductor identity covers the existing product-dual test, while the same-support/same-multiplier GRS formula has unestablished hypotheses for C. L097 gives only constant R and a support obstruction; neither implies a nonconstant direction or excludes this family.
GAP: Decide the nonconstant-R question from all simultaneous cyclic-plane conditions; no inspected result supplies existence, exclusion or uniform rank for this restricted family.
REASON: Coverage is adequate for one separate bounded attempt on the unchanged target; EXPLORE is a search/scope decision, not a parity theorem or a novelty claim.
LITERATURE_REASON: The proposed bounded-degree common polynomial multiplier was outside the prior sparse-transfer assessment; conductor comparison was essential before attempting this changed target. Ready adjunction, lower-bound and audit coverage were reused.
SCOPE: k=F_97, the fixed order-sixteen subgroup H, arbitrary bijection h, and the hypothetical rational two-plane of L088/L089 with every full block-intersection condition. Put W=Ann(P), C=ev_h(W). Test z_i=h(i)R(h(i)), R in k[X], deg R<=4, modulo the already known constant polynomials. Retain zeros of R on H and every bilinear equation; do not assume plane existence, an MDS projected code, or an original affine chart.

This was proposed for future routing in step 267. Step 268 completes only
its source review; it performs no mathematical attempt.
Essential inputs would be L088/L089 and L097, with L010's subgroup
power-sum facts through them. The separate assessment must compare the
exact polynomial-weight ansatz with known product-dual descriptions and
the recorded attempts before deciding IMPORT, SPECIALIZE, EXPLORE or a
source blocker. No new source import or derived parity appears here.

The main challenge gap remains unresolved. A nonconstant direction
could be one input toward the previously missing dense product
constraints for the cyclic subfamily; it would not supply the six
independent directions required for the old square upper target.
An exclusion of this ansatz would stop this particular dense mechanism,
not disprove the conditional upper bound or the existence of a plane.
Other support families and the uniform triangle bound remain separate.

ATTEMPTS/035 stops the sparse transfer and requires a specific dense
mechanism before reopening. Here the specified test is the common
polynomial R, subject to every equation

    sum_i h(i) R(h(i)) f_a(h(i)) f_b(h(i)) = 0,
    1<=a<=b<=6,

for a basis of W. The equations are L097's existing exact test after
specifying the proposed family; they are not asserted to have a new
solution. The degree cutoff defines one bounded question. No additional
parity follows merely from the standard constant-R example or from
the support lower bound. Preserve all zero and rank-deficient cases.

Continuation test after coverage: obtain a rigorous nonconstant parity
under the full hypotheses, a rigorous exclusion of this ansatz, or a
specific unresolved obstruction. A formal restatement of the twenty-one
equations, a generic rank guess or sampled label failures is insufficient.
Stop after one bounded attempt if the required new identity is absent.
The proposal received no calculation or source approval in step 267.
The separate source decision below does not perform that calculation.

## Reviewed source scope — step 268, October 17, 2026

The main local gap is excluding L010's sixteen-count equality; the
uniform triangle twelve bound and challenge-definition qualifications
also remain unresolved. This target concerns only the hypothetical
cyclic subfamily. The degree cutoff, field, arbitrary bijection and full
plane relations in SCOPE are unchanged. The desired intermediate input
is a nonconstant R satisfying the complete existing bilinear test;
its possible downstream use and its bounded stop test are stated above.

Reused `2026-10-16-cyclic-projected-code-schur-square.md` and
`2026-10-16-cyclic-product-dual-obstruction-audit.md` in this directory.
The former records the inspected primary statements and essential proof
cases; the latter and L097's completed step-256 audit justify reuse under
the same field and plane hypotheses. Randriambololona, *On products and
powers of linear codes under componentwise multiplication*, Contemp.
Math. 637 (2015), 3–78, DOI 10.1090/conm/637/12749, Proposition 2.38 and
Corollary 2.39, printed p. 28 of the
[author manuscript](https://perso.telecom-paristech.fr/randriam/maths/HR_AGCT-14.pdf),
give coordinate adjunction without an MDS hypothesis. Substitute the
specified z into L097's already established full-product test; no source
theorem reproof is needed. This identifies the test, not its solution.

New primary comparison: Élise Barelli and Alain Couvreur, *An efficient
structural attack on NIST submission DAGS*,
[arXiv:1805.05429v1](https://arxiv.org/pdf/1805.05429v1), 14 May 2018,
Definition 20 and Propositions 21–22, printed p. 10. Definition 20 calls
the multiplier space Cond(A,B); Proposition 21 identifies it with
(A*B^perp)^perp. With A=C and B=C^perp this is exactly L097's D.
Proposition 22 assumes two full GRS codes on the same distinct support
with the same nonzero multiplier and 1<=k<=k'<n; it returns RS_(k'-k+1).
Its full proof uses GRS duality and products, including cancellation of
the multiplier via the locator derivative. These GRS hypotheses are not
established here. Theorem 26 (p. 12) gives an inclusion for a specified
pair of nested alternant codes over a quadratic extension, not this
arbitrary annihilator subcode. Heuristic 27 and its ensuing discussion
(pp. 12–13) are explicitly heuristic and supply no uniform substitute.
None of these conclusions decides the requested family.

The GRS issue is substantive: L089 gives nonzero dependencies among four
generator columns of C, of dimension six. The saved MZ assessment
(arXiv:1501.06419v2, Lemma 2.1) already explains why calling this C MDS
would be invalid. Being a subcode of RS_8 does not supply the missing
full-GRS hypotheses for C or C^perp. We make no claim about identifying
C with some alternant code under changed parameters.

The unchanged lower comparison is imported from Bachoc–Serra–Zemor,
*Revisiting Kneser's Theorem for Field Extensions*,
[arXiv:1510.01354v2](https://arxiv.org/pdf/1510.01354v2), Theorem 3
(pp. 2–3) and stabilizer remark (p. 9), exactly as specialized and audited
in L097: multiply W in k(X), then use injective evaluation of degree at
most fourteen products. It gives eleven, not a guarantee about where
product-dual directions lie. Reuse the saved CPTZ assessment,
[arXiv:2412.15160v1](https://arxiv.org/html/2412.15160v1), Proposition 6
and Proposition 10 with its polynomial-setting hypotheses; these concern
square dimensions and do not identify the requested polynomial-weight
parities. No new specialization of their bounds is attempted here.

## Search, failures and readiness limits

Queries included `"Reed Solomon" "conductor" "dual" Schur product
subcodes polynomial`, `"polynomial subspaces" "weighted" "Schur" dual
Reed Solomon`, `"Randriambololona" "2.38"`, `"conductor" "GRS"
"Proposition" Couvreur Otmani Tillich`, `"codimension two" "Schur square"
Reed Solomon`, `"cyclic" "plane" "polynomial" "Schur square" Reed Solomon`
and `"Reed-Solomon subcodes" "dual" "conductor"`. The conductor lead
was followed to the primary version pinned above, rather than used from
search snippets or a thesis. The ePrint record was accessible but its
PDF request failed; the exact arXiv theorem statements and relevant
proofs were accessible. No essential source remains blocked.
The discovered theses and newer attack papers are leads only, not
additional theorem inputs. No novelty follows from unsuccessful queries.

Scoped local searches of drafts/literature, ATTEMPTS and history found
the step-267 proposal but no completed bounded-degree-R test. L097 and
ATTEMPTS/035 concern sparse transfers and an unresolved general dense
combination; the present common polynomial multiplier is a specified
dense mechanism. ATTEMPTS/033–034 preserve stopped joint-gate
elimination, and ATTEMPTS/036–037 preserve the distinct isolated-row
failures. No route is restarted merely by renaming it. No cross-notebook
input is used, and no unfinished work is removed.

EXPLORE authorizes only the exact TARGET in a later research turn,
subject to the supervisor's separate approval of this changed assessment.
Essential inputs remain L088/L089/L097, with L010 through them. All
twenty-one bilinear equations, zeros of R on H, deficient ranks and full
plane conditions must remain. Plane existence is an unresolved premise,
not an output of this review. A valid result would prove a nonconstant
direction or a uniform ansatz exclusion, or isolate a specific remaining
obstruction after one bounded attempt. A restatement, a generic-rank
guess or sampled failures is insufficient; absent a new usable identity,
stop this ansatz and preserve its evidence. Even a positive result would
not by itself supply the old six-direction threshold or cover arbitrary
equality support families. No challenge bound changes.

Mathlib coverage of the full target was not checked. Existing local
qualifications are retained; no matching theorem or absence is claimed.
This literature-only step writes no lemma or mathematical script and
does not derive any additional polynomial identity.
