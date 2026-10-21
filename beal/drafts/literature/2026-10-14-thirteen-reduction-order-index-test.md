# Thirteen-adic reduction-order prerequisite — completed source review

TARGET: Determine whether 13 divides the exact order of E1(F_(13^12)) and whether Bruin Lemma 4.2's reduction-order hypothesis holds at thirteen.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched exact extension-field counting terminology and targeted local history, assessments and scripts for 13^12, extension counts and reduction-order tests; no completed duplicate count was located. Reused the inspected Bruin/FNS assessment and ATTEMPTS/029–030; read Milne's primary extension-count statement and its proof context.
SOURCE_EVIDENCE: J. S. Milne, Elliptic Curves, second edition (2021), author-hosted EC2.pdf, Chapter IV Section 9, Theorem 9.10 and Remark 9.11(a), printed p.156 (PDF p.161), with Proposition 9.9 and proof on p.155; Bruin 2003 Lemma 4.2 p.45 and FNS Section 7.2 coverage reused from 2026-10-14-fixed-class-elliptic-chabauty-scope.md.
COMPARISON: Milne determines every extension-field point count from the complete projective base-field count; the remaining work is exact finite arithmetic for L033's E1 and L064's full degree-twelve residue field. Bruin's order condition is only one sufficient-index-test prerequisite and does not supply finite-index generators.
GAP: No base-field count, extension count or divisibility decision is established in this literature turn; one bounded research calculation is now covered, while rank, generators, coset bounds, other classes and global power lifting remain unresolved.
REASON: The essential missing counting source is now inspected and matches the smooth finite-field elliptic-curve hypotheses; specialize its known formula rather than reprove Frobenius theory or enumerate the full extension field.
SCOPE: Exact complete projective count on E1 over F13, its extension to F_(13^12), and comparison with only Bruin Lemma 4.2's prime-to-thirteen reduction-order hypothesis; REPRODUCTION, without new Chabauty claims.
COVERED_TARGET: Determine whether 13 divides the exact order of E1(F_(13^12)) and whether Bruin Lemma 4.2's reduction-order hypothesis holds at thirteen.
LITERATURE_REASON: The prior REVIEW_REQUIRED assessment lacked the essential primary extension-count statement; this review fills that specific source gap, without repeating general Chabauty research.

## Relevance and stopping test

The main gap remains positive primitive integer emptiness, locally focused
on the 54a1 branch of ordered (3,4,11). The intermediate target is the
exact order of E1 over the full residue field at thirteen. Its downstream
use is to retain or park Bruin's prime-to-thirteen-order shortcut for
subgroup index control on the translated covering. Coprimality would
retain only this prerequisite, subject to independent finite-index
formal-kernel generators and their relation test. Divisibility parks
this shortcut at thirteen; it neither invalidates L067 nor excludes
other saturation methods or Chabauty. No integer exclusion is expected
from this calculation alone.

## Imported counting theorem and inspected evidence

[Milne, *Elliptic Curves*, second edition (2021), author-hosted PDF,
Chapter IV, Theorem 9.10 and Remark 9.11(a), p.156](https://www.jmilne.org/math/Books/EC2.pdf#page=161)
assumes an elliptic curve E over F_p. Set N1=#E(F_p), including the
origin. The theorem gives

    Z(E,T)=(1+(N1-p-1)T+pT²)/((1-T)(1-pT)).

Remark 9.11(a) writes the numerator as (1-alpha*T)(1-beta*T), with
alpha*beta=p and alpha+beta=p+1-N1, and states, for every m>=1,

    #E(F_(p^m))=1+p^m-alpha^m-beta^m.

The complete proof of Theorem 9.10 and Proposition 9.9 (p.155) was
read, together with the projective zeta identity preceding it. The
proof counts positive divisors via Riemann–Roch and the degree-zero
Picard group, sums their generating function, then compares formal
logarithms. There is no ordinary/supersingular restriction or need to
know the group's structure. The author PDF identifies itself as the
second edition and gives 2021 publication data; numbering and pages
here refer to that PDF, not another edition.

This known theorem is imported by citation. Reproving it would add no
needed input. A future exact arithmetic implementation may evaluate
its root power sum using the quadratic relation, without numerical
complex roots; this turn supplies no recurrence derivation or count.

## Applicability and retained assumptions

The canonical input model in L033 is exactly

    E1: Y²+Y=X³-X²-7820X-263580.

The relevant model/field passages in L033, L064 and L067 were checked.
L067 uses discriminant -11 for this E1 model, a unit at thirteen.
Its smooth projective reduction is thus the elliptic curve to which
the counting theorem applies; use the displayed integral model,
including its origin, and no twist. L064 proves that K tensor Q13
is one unramified degree-twelve field. Therefore the required residue
field is F_(13^12), and there are no other completions above thirteen
to leave untested. This applicability comparison uses the existing
canonical inputs and does not independently reprove their certificates.

The [existing Bruin/FNS assessment](2026-10-14-fixed-class-elliptic-chabauty-scope.md)
is reused unchanged for Bruin, *Chabauty methods using elliptic curves*,
J. reine angew. Math. 562 (2003), 27–49, Lemma 4.2 p.45, and FNS's
same-field generator limitation. No broader theorem is inferred from
the finite-order test. The hypotheses p>2, unramifiedness and good
curve reduction have canonical inputs; finite-index global generators
and their formal-parameter relation test remain unavailable. The
translated map's good reduction is audited L067; it is not a substitute
for those arithmetic hypotheses.

## Duplicate/failure check and approved calculation boundary

Targeted searches of local histories, literature notes and scripts
located the proposed assessment and recent reduction audits, but no
already-completed exact E1 extension-order test. Earlier q=29 trace
calculations concern different curves and do not supply this count.
ATTEMPTS/029–030 stop fixed-class removal by the stated finite-prime
filters; this index prerequisite is a different mechanism and does
not reopen those stopped exclusions. FNS's generator failure remains
an independent bottleneck even if the order test succeeds.

The next research turn should record every affine solution over F13
and the origin, obtain the exact extension count from the cited
formula using integer arithmetic, and compare its remainder modulo
thirteen with the required nonzero remainder. Save all arithmetic and
checks in a local certificate; print only the count, remainder,
pass/fail conclusion and artifact paths. A second exact evaluation
of the same power sum is an appropriate bounded consistency check;
a library point-count call or a preview alone is not a certificate.
No group structure, rank, index, coset zero bound or integer conclusion
is approved. No new lemma or mathematical script was written here.
Full matching and supporting Mathlib coverage: not checked.

Searches included “elliptic curve finite field extension number points
alpha beta Silverman theorem V 2.3 pdf” and “site.jmilne.org elliptic
curves finite fields number points extension Frobenius”. Silverman's
search hit was an unread alternative lead, not an imported input.
Milne's theorem and proof were retrieved before any larger passage;
no theorem is inferred from a search snippet. No cross-notebook input.
