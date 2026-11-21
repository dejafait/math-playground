# Two-root reciprocal residual — one symbolic interface nomination

TARGET: Determine whether, for k=2 and r=3 under the stated analytic grouping hypotheses, the complete residual is explicitly congruent to a root-independent 2-by-2 Hankel block of the local coefficients u_0,...,u_5 of 1/g.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse step456's rational Bezoutian/Hankel, Loewner, reciprocal Taylor and exact-title searches and its targeted L784/L781/L783 and step443/448/444 comparisons; no inspected theorem identifies this analytic residual with a specified local reciprocal block. No novelty inference or new formula.
SOURCE_EVIDENCE: https://www.tu-chemnitz.de/mathematik/preprint/2008/PREPRINT_09.pdf ; https://arxiv.org/pdf/1004.4208v3 ; Heinig-Rost, Bezoutians, Chemnitz preprint2008-09, Proposition7.15/(7.11) and full proof p.45, n-by-n real rational congruence; Proposition9.1/(9.3)-(9.4) and proof p.54, square Vandermonde reduction; Jouve-Rodriguez-Villegas, arXiv:1004.4208v3, Section2.3, Lemmas2.5-2.6 and Remark2.8 pp.5-6, sign/convention check. Exact hypotheses, direct links, source qualifications and unread leads are recorded in the parent assessment below.
COMPARISON: Rational coefficient/evaluation transformations are standard, while the exact local-inverse block and congruence for the prescribed analytic residual remain unidentified. L784 gives only one fixed complete-tail cancellation, not this symbolic result. L781 tests different coefficients, and L783 excludes an automatic inertia conclusion from the local premises.
GAP: Identify the exact fixed block/order/sign within u_0,...,u_5 and an explicit real invertible congruence, or a precise obstruction to that proposed reduction; no block formula or signature is asserted. Actual-Xi signs and global grouping remain independent.
REASON: One symbolic finite-jet reduction could remove root-isolation data from a future coefficient sign test; it has a useful algebraic purpose despite leaving the central sign inequality open. It does not revive automatic positivity or the closed model diagnostics.
SCOPE: Separate literature approval completed in step457 on 2026-11-05; ready EXPLORE coverage for the exact TARGET and unchanged hypotheses. One k=2,r=3 symbolic attempt only; no model tuning, numeric parameter sweep, repeated fixed-sign audit, all-k assertion or actual-Xi sign theorem. Source coverage is EXPLORE, not a claim that the missing identity is known.

The main gap remains actual-Xi all-degree mixed positivity. The target is
an algebraic interface, with possible downstream use in replacing a
root-dependent finite test by a coefficient-dependent one. It does not
promise an inequality. Root grouping at every radius, coefficient signs,
all orders and other mixed minors remain unproved. No new creative sign
mechanism has been identified; an independent actual-theta signed input
is still missing.

Reuse the completed primary comparison in
`2026-11-05-root-eliminating-reciprocal-bezoutian-review.md`.
Essential local motivation is L784(6)-(8) and its step455 audit.
L777/L782 are convention comparisons only; L781/L783 and the earlier
automatic-class/linked-factor stops are contrasts, not inputs to a
general signature theorem. No cross-notebook input is needed.

The proposed scope is a real holomorphic g on a neighborhood of the
closed disk |z|<=sigma, sigma>1, with g(0)>0 and exactly two distinct
simple roots alpha_1,alpha_2 in(-1,0), and no other zeros in that disk.
Define P=(z-alpha_1)(z-alpha_2), F=g/P, p=z^-2 P, b=p/F,
d_i=alpha_i^2 F(alpha_i)/P'(alpha_i), and beta_m as the complete
Laurent coefficients of b on its annulus containing the unit circle.
Set h_3=sum_(n>=0)beta_(4+n)z^(n+1),
K_ij=(h_3(alpha_i)-h_3(alpha_j))/(alpha_i-alpha_j),
K_ii=h_3'(alpha_i), E_ii=sqrt(|d_i| |alpha_i|^3),
and J=diag(sign(d_i)). The target matrix is J+E K E.
All removability, convergence, reality and nonzero denominators must be
justified for arbitrary data; the fixed model is not an imported proof.

Use u_j=the coefficient of z^j in 1/g only as a local Taylor jet. No continuation of this
uncancelled inverse series to the selected roots is allowed. The task is
to determine the precise Hankel shift, possible sign/reversal and explicit
real change of basis, if such a reduction exists. The coefficient matrix
must be independent of the selected root coordinates; its change of
basis may depend on them. An uncomputed congruence inferred solely from
matching inertia is not the requested interface. Do not silently replace
a 2-by-2 form by a higher-dimensional compression or Schur complement.

First justify a symbolic version of the complete-tail cancellation,
then test the resulting finite bilinear form using the cited polynomial
coefficient/evaluation interfaces. The sources' expansion at infinity,
ordinary inverse and polynomial inverse modulo a denominator are distinct.
Keep the minus sign in Jouve-Rodriguez-Villegas Remark2.8. Use only the
unambiguous n-by-n formula of Heinig-Rost Proposition7.15, not its
reciprocal-ratio corollary or unsigned interlacing shorthand.

Continuation test: an explicit finite congruence with every scalar
denominator nonzero under the exact hypotheses, valid also when the
coefficient block or residual is singular, is a useful interface result.
It must record equality of full inertia including nullity, without
assuming a positive determinant or using actual-Xi zero geometry.
If the reduction instead retains an additional root-dependent form,
identify it and its unpaid condition precisely; that is an informative
obstruction to the proposed fixed-block interface, not a general proof
that no congruence can exist. If neither is obtained in one coherent
attempt, save the partial algebra and stop. No automatic repeat, larger
matrix or model sweep is authorized by this nomination.

Even a successful interface closes without further sign inference:
it must not assume its coefficient form has the desired inertia, or
relabel that inertia as an independently paid Xi estimate. A later sign
mechanism would require its own source coverage and discriminating test.
This is finite symbolic development using known algebra, not a creative
central sign attempt or a new class theorem. Full matching Mathlib
coverage remains unchecked. No symbolic calculation or lemma was made
in preparing this assessment.

## Separate source-gate approval — step457

This literature-only recovery repairs missing direct URLs in the ready
assessment. The exact TARGET is unchanged. Reused step456's discovery and
failure comparison rather than repeating its searches. Directly reopened
[Heinig–Rost, *Bezoutians*, preprint2008-09](https://www.tu-chemnitz.de/mathematik/preprint/2008/PREPRINT_09.pdf#page=45)
and [Jouve–Rodriguez-Villegas, arXiv:1004.4208v3](https://arxiv.org/pdf/1004.4208v3#page=5)
on 2026-11-05. Read the complete coefficient-comparison proof of
Proposition7.15, printed p.45, with its preceding degree/padding hypotheses;
Proposition9.1, printed p.54, including its full off-diagonal and diagonal
limit proof and the square Vandermonde convention; and Lemma2.5's proof,
Lemma2.6 and Remark2.8, printed pp.5–6. Lemma2.6's proof is left to the
reader in that source; no missing proof was supplied in this turn.

The source match remains restricted to real rational coefficient/evaluation
interfaces. Proposition7.15 permits unreduced fractions and supplies its
n-by-n identity without a coprimality assumption. This is the relevant
source scope for a future singular-case test. Proposition9.1 requires the
stated distinct roots of its polynomial pencil; its Vandermonde is square.
Remark2.8 is stated for coprime polynomials and retains a minus sign; it is
only a convention comparison here, not coverage for a singular residual.
Neither source directly identifies the requested analytic residual with a
particular 2-by-2 local-inverse block. Thus EXPLORE, rather than IMPORT,
is appropriate. No additional essential rational-interface source is
missing for the single bounded attempt; the analytic identification is
exactly the research question, not a theorem silently imported.

Checked the relevant canonical L784 hypotheses and full equations(6)–(8),
plus step455's audit record and step456's source-stop record. L784 remains
a fixed example, not a general cancellation theorem. The existing L781/L783
and linked-factor contrasts are reused within their recorded scope. No
new duplicate or obstruction was established, no new sign input was found,
and no novelty claim is warranted. Full matching Mathlib coverage remains
unchecked. Further retrieval of already inspected material would add no
coverage for the unchanged target.

Approval is for one symbolic attempt with the supplied continuation test:
explicit real invertible congruence including nullity, a precise remaining
root-dependent obstruction, or saved incomplete algebra and closure. No
model sweep, automatic sign inference or all-k extension is approved. The
independent actual-theta signed inequality still blocks nomination of a
justified creative central-gap attempt. This is a source-gate repair and
separate approval, not mathematical progress or a renewed exploration budget.
