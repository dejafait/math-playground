# Lagarias finite-zero contour estimate — bounded audit coverage

TARGET: Audit Lagarias's published Theorem6.1 in ordinary zeta normalization, checking the finite-zero residue sign and whether (6.10)-(6.12) justify its O(sqrt(n) log n) remainder without RH.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step213's finite-zero source review searched exact Li truncation, contour remainder, sign and correction terminology; the local exact-source screen found criterion uses, not a previous contour audit. Reuse drafts/literature/2026-11-10-zero-extracted-signed-inverse-review-212.md for complete searches and scope limits; no novelty claim.
SOURCE_EVIDENCE: Inspected Lagarias AIF57(5)(2007), Definition4.3/(4.5), Lemma4.4/(4.6)-(4.13), Theorem1.1/(1.17), Theorem6.1/(6.1)-(6.14) and every contour proof case, pp.1693-1694,1708-1709,1721-1726; arXiv math/0404394v4 Section6 read completely. DLMF1.10(i),(iii)-(iv), especially zero multiplicity and (1.10.8), inspected for the finite residue audit. L975/L968 normalization and L976 statement read; step171/186 comparisons reused.
COMPARISON: The published source states exactly the polynomial growing-height residual sought, but its residue-sign and horizontal-estimate passages need verification. DLMF supplies standard residue calculus, not the requested remainder. A bounded audit of a suspect source claim is justified; no independent reproof of its whole theorem or RH is authorized here.
GAP: Replay signs, normalization, zeta pole removal and the actual horizontal majorant; decide precisely which displayed assertions are justified and whether the stated bound is safe to import. A source-proof failure would not itself disprove the theorem or its possible repairs.
REASON: Concrete mathematical audit after a changed-target source comparison, independent of the parked source and failed b_m envelope. Known analytic tools are ready; this newly written continuation requires separate supervisor approval before invocation.
SCOPE: Ordinary undivided zeta Li coefficients, positive integer n, arbitrary zero multiplicities, possible off-line zeros, fixed zeta function, source rectangle and T in [sqrt(n),sqrt(n)+1]. No RH, simple zeros, effective zero list, arbitrary-set uniformity, or repaired contour estimate is assumed. Stop after one bounded audit; do not launch a second repair mechanism.

## Purpose and discriminating test

The main gap is L030-L032/C032a positivity and L966 signed forcing.
L968's every-epsilon ordinary-Li lower threshold is the downstream
benchmark; L975 identifies the complete inverse to which any signed
estimate would apply. L976 stops the old coefficientwise payment.

An exact finite extraction with a trustworthy remainder could isolate
the remaining signed obstruction. Before developing that mechanism,
test the cited source's signs and bound. Accept only the statements
whose conventions, contour singularities and estimates survive replay.
An explicit sign mismatch or unjustified inequality is informative
negative evidence. Preserve the theorem's truth status as unresolved
unless the audit actually establishes more. Do not infer a theorem is
false merely because one proof step fails, or silently correct it and
then claim a known import. A successful audit still leaves the growing
incomplete-zero sum unsigned and does not prove RH.

## Precise source locations and permissible tools

The canonical source is J. C. Lagarias, *Li coefficients for automorphic
L-functions*, Ann. Inst. Fourier **57**(5) (2007), 1689-1740,
[published PDF](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=34).
The inspected [arXiv v4 Section6](https://arxiv.org/html/math/0404394v4#S6)
is an accessible cross-check; its equation numbering differs. Retain
the published numbering in any canonical audit. Source statements and
version/access limits are recorded in review212; avoid renewed browsing
unless a changed hypothesis or an essential unread passage appears.

The standard residue theorem is
[DLMF1.10(iv), (1.10.8)](https://dlmf.nist.gov/1.10.E8): a positively
oriented simple closed contour enclosing finitely many isolated
singularities of an otherwise analytic function, continuous and regular
on the contour, gives its normalized integral as the sum of residues.
[DLMF1.10(i),(iii)](https://dlmf.nist.gov/1.10.i) provide local zero order
and Laurent coefficients. Verify these hypotheses for each finite
contour; no infinite contour, logarithm branch across zeros, or exchange
with an n-limit is covered automatically.

## Audit obligations

Use Definition4.3, Lemma4.4, the ordinary zero sum (1.1) and incomplete
sum (6.1) as the convention contract. Inspect the local zero factor of
the actual zeta function for a zero of arbitrary order and compute the
residue of the printed kernel times the negative logarithmic derivative.
Keep the normalized contour orientation, s+1 shift, reflected zero and
trivial-zero terms explicit. Check the origin separately: zeta has a
pole, whereas Definition4.3 subtracts delta/s. Its product with the
finite kernel must be examined, not declared harmless from memory.
Compare (6.5)-(6.7) with the resulting identity. The separately printed
zeta formulas (4.12)-(4.13) also require a convention check.

For the remainder, replay (6.10)-(6.12) using the kernel actually defined
in (6.4), the same s+1 argument, and T's stated interval. Determine
whether the displayed bounds imply the asserted geometric decrease on
the right horizontal segments. Distinguish failure of that inference,
failure of an absolute majorant, and failure of the oscillatory integral
bound. Do not conflate these three conclusions. Track the final left
segment's O(sqrt(n)log n) cost and endpoint cutoff comparison if needed
to classify the result, without reproving unrelated automorphic theory.

If an elementary failure is decisive, stop the audit there after recording
its exact extent; do not spend the turn repairing the horizontal bound
or moving to a different cutoff. Any proposed repair receives its own
source gate. No mathematical script is needed unless a rigorous
certificate would materially settle an unresolved part; a numerical
preview cannot validate an asymptotic or all-n bound.

## Scope limits and continuation requirements

L018 supplies actual xi/zeta correspondence if required, L975 ordinary
germ normalization, L968 the signed threshold, and L976 the old stop.
Read only the local proofs actually used. This audit does not need the
October zero-free baseline: no improved strip is being proposed.
No cross-notebook theorem is used. Full matching Mathlib coverage is
unknown; generic residue calculus would only be supporting coverage.

Recommend proof_audit/conceptual_audit: signs, meromorphic pole removal,
and n-dependent contour estimates interact, so a source citation alone
cannot settle the application. No creative proof target is ready while
this load-bearing residual remains uncertified. After the audit, require
a materially identified estimate or a refined mechanism before reopening
the signed-residual research target.
