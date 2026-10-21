# Source comparison for limits of bounded-index pairs

TARGET: Assess whether L024's bounded-index pairs at unbounded depths admit a subsequence whose coefficient reductions stabilize to a Z_p-independent pair in T_p S, without assuming compatibility of the selected primes or classes.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Focused searches of finite-set inverse limits, p-adic sequential compactness, classical Selmer coefficient maps and PID determinant bounds; reused the all-depth coefficient assessment, checked L024 and relevant L023/L018 passages, and inspected primary statements and essential proof cases listed below.
SOURCE_EVIDENCE: Stacks tags 086J and 0597; Mazur--Rubin (2004), Section 3.5 and Lemma 3.5.3, pp. 27--29; Kim author text 2025-05-12, Section 5.3.1, p. 27; Milne EC2 (2021), IV.5, pp. 128--130; Elman preliminary Lectures, Theorems 43.5/43.8, pp. 255--258; Breuning LTCC 2010, Theorem 2.22/Exercise 2.25, pp. 10--11; Conrad maximal-compact notes, Theorem 1.2 proof, p. 2.
COMPARISON: Standard finite-set compactness and elementary-divisor theorems cover the mechanisms, and existing coefficient coverage applies unchanged; no inspected theorem directly states subsequence extraction preserving independence of these varying actual prime-deletion pairs.
GAP: Apply the known inputs to the selected pairs, verify downward coefficient maps and finite-quotient disappearance, construct stabilization of the same ordered pairs at every fixed depth, and justify a uniform exterior nonvanishing threshold. These deductions are reserved for a research turn.
REASON: Approve only the unchanged saved target as a specialization of known compactness, coefficient and matrix results; no new limit theorem, arithmetic hypothesis, novelty claim or BSD candidate is established in this review.
LITERATURE_REASON: The changed target concerns limits of varying actual pairs, beyond the earlier finite-depth extraction audit; essential compactness and nonvanishing coverage had not been inspected.
SCOPE: Retain all L021/L023/L024 hypotheses, granted Selmer corank two, residual-family nonvanishing, S=Sel(Q,E[p^infinity]), F=S/S_div and h=length_Z_p F. Use one actual L024 ordered pair at each unbounded depth m>2h, with span index <=p^(3h). Permit varying primes and tensor generators; conclude only subsequential coefficient limits if the specialization succeeds.

This is a completed literature-only comparison. No lemma, mathematical
script, DAG or argument overview is changed. SPECIALIZE approves a
later proof attempt; it does not establish the proposed conclusion.

## Relevance and bounded test

The main gap remains rank E(Q)=m(E) for analytic order at least two.
On this conditional branch, rational Kummer membership and comparison
of the granted Selmer corank with complex order are missing. The
intermediate target is exactly TARGET: track the actual finite-depth
ordered pairs into T_p S, rather than merely recover its granted
abstract rank. Its downstream use would be a nonzero integral exterior
class with specified finite-depth ancestry, before any rationality test.
Finite Sha, rational rank two and the complex comparison remain open.

Seek eventual stabilization of p^(m_j-k)c_(i,m_j) for each fixed k and
both i, along one increasing subsequence m_j. Seek a nonzero exterior
product of the limits, with a depth-independent valuation bound; a bound
of at most 3h would suffice, and a fixed detecting depth k>3h is a
concrete proposed test. These are requested thresholds, not achieved
estimates. No improvement of L024's p^(3h) bound is being claimed.

Continue if the specialization proves stabilization and preserves
independence using only the retained hypotheses and actual pairs.
Abandon this passage if uniform index cannot supply a finite detecting
level after the finite part disappears, or if compatibility of selected
primes/classes has to be added. In either case do not infer rationality
from an integral Selmer limit. No auxiliary-prime relation at a single
fixed index is requested of a limit.

## Local overlap and recorded failures

L024 was read in full, including its critical audit. It gives classical
membership and the uniform index bound, retaining the strict kernel F.
L023's hypotheses and finite-depth structure/coefficient passages were
read. L021's statement supplies the paired finite quotient. The relevant
L018 coefficient and inverse-limit passages were checked for overlap:
L018 fixes a depth-two basis after eliminating F. It does not already
prove this positive-F, varying-pair subsequence statement. Its stronger
arithmetic hypotheses are not transferred here.

Reuse the coefficient-source coverage in
[the all-depth assessment](2026-10-04-central-vanishing-all-depth-classical-lifting.md).
Do not repeat the Sakamoto or prime-selection audits, or use L015--L017's
error model as a global ban. ATTEMPTS/021 and L021 stop removal of F from
primitivity; the present target keeps F and does not challenge that stop.
The L019 overview's divisible-Sha limitation still applies. No sibling
notebook was consulted. Failed discovery searches do not establish novelty.

## Inspected inputs and qualifications

**Finite inverse systems.** The Stacks Project, live version checked
2026-10-06, [Lemma 4.21.7, tag 086J](https://stacks.math.columbia.edu/tag/086J),
states nonemptiness of the limit of a cofiltered diagram of finite
nonempty sets. Read its full subsystem/minimality proof. Surjective
transition maps are not assumed. Independently selected pairs are not
such a diagram until a suitable system of finite admissible reductions
is constructed; this application is deferred. [Lemma 10.86.3, tag
0597](https://stacks.math.columbia.edu/tag/0597) is an alternative for
countable Mittag-Leffler systems, also requiring a genuine system.
It is not a theorem asserting independence of limit vectors.

**Coefficient identification.** Chan-Ho Kim, *The structure of Selmer
groups and the Iwasawa main conjecture for elliptic curves*, inspected
publisher-hosted author text dated 2025-05-12,
[Section 5.3.1, printed p. 27/PDF p. 28](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=28),
uses Sel(Q,E[p^k])=S[p^k] and cites Mazur--Rubin Lemma 3.5.3.
Its surrounding rank-zero argument is not imported. The earlier
assessment's printed-p.28 label is off by one for this PDF; the section
and PDF-page anchor are the reliable locators.

Mazur--Rubin, *Kolyvagin Systems*, Mem. AMS 168 (799) (2004),
[Section 3.5 and Lemma 3.5.3, printed pp. 27--29/PDF pp. 33--35](https://webusers.imj-prg.fr/~christophe.cornut/ES/Ref/KolySys.pdf#page=34):
read (H.1), (H.3), the complete principal-ideal proof and the induced
local-condition diagram. The lemma assumes absolute residual
irreducibility and two specified Galois H^1 vanishings, with induced
Selmer structures. Do not replace (H.3) by local torsion vanishing.
For this target reuse L023's already justified classical identification:
global E(Q)[p^infinity]=0 and the local Kummer-kernel comparison.
Its argument does not need local H^0=0. The next attempt must explicitly
check naturality under [p], using the same coefficient diagrams; separate
abstract isomorphisms at each depth are inadequate.

**Downward maps and rationality limitation.** J. S. Milne, *Elliptic
Curves*, second edition (2021),
[IV.5 coefficient diagrams and Proposition 5.1, pp. 128--129](https://www.jmilne.org/math/Books/EC2.pdf#page=134),
and [Remark 5.2, p. 130](https://www.jmilne.org/math/Books/EC2.pdf#page=135).
Read the diagrams, proof and compactness footnote 7. The maps reduce
point quotients and multiply Sha by p. Proposition 5.1's rational-image
equality requires absence of nonzero elements divisible by every power
of p. Compactness in the footnote supplies compatible sequences;
its displayed constraints do not themselves exclude the zero sequence.
Thus that footnote is not imported as a nonzero-vector criterion.
The current target requires a separately verified exterior constraint.
No rationality criterion from this source applies without its hypothesis.

**Compact p-adic matrix space.** Manuel Breuning, *p-adic numbers,
LTCC 2010*, [Theorem 2.22 and Exercise 2.25, pp. 10--11](https://kconrad.math.uconn.edu/math5020f11/breuningnotes.pdf#page=11):
read the digit-expansion proof and the sequential-compactness hint.
Exercise 2.25 is an exercise, not a worked proof of our target.
Keith Conrad, *Maximal compact subgroups of GL_n(Q_p)*, undated author
notes retrieved 2026-10-06, [Theorem 1.2 proof, p. 2](https://kconrad.math.uconn.edu/blurbs/gradnumthy/maxcompact.pdf#page=2),
uses compactness of M_n(Z_p), the sup-norm topology and continuity of
determinant. These support a fixed-coordinate compactness approach.
GL_n(Z_p) itself covers only unit determinant and must not be substituted
for the positive-valuation matrices relevant here. The next attempt may
instead use a countable finite-reduction argument citing tag 086J.

**Elementary divisors and determinant length.** Followed Stonek's
*Smith normal form* notes to their primary textbook reference, Richard
Elman, *Lectures on Abstract Algebra*, Preliminary Version, UCLA author
PDF retrieved 2026-10-06 (no edition date inferred from the secondary
citation). Read [Lemma 43.3, Theorem 43.5's unit and nonunit cases,
Corollary 43.7 and Theorem 43.8, pp. 254--258](https://www.math.ucla.edu/~rse/algebra_book.pdf#page=263).
Over a PID, matrices are equivalent by invertible changes to Smith
normal form, with invariant factors unique up to units. Use this known
theorem over Z_p and reduce the resulting matrix as needed; Z/p^m is
not a PID domain. Reproving diagonalization would be redundant.

Also inspected Stacks [Lemma 15.126.3, tag 0ASL](https://stacks.math.columbia.edu/tag/0ASL),
for finitely presented modules over generalized valuation rings, and
[Lemma 42.68.41, tag 02QB](https://stacks.math.columbia.edu/tag/02QB),
including its diagonal proof case. The latter identifies determinant
order with cokernel length over a one-dimensional Noetherian local
quotient domain, subject to its filtration and generic-isomorphism
hypotheses. It is not directly a statement over Z/p^m. Retain those
restrictions if cited; Smith normal form suffices for the planned
finite-coefficient matrix calculation.

## Why a later specialization is needed

No inspected statement mentions L024's specified actual components,
their changing primes or tensor generators. The standard inputs cover
compactness, natural coefficient identifications and matrix bounds;
what remains is their application without replacing the selected pairs
by arbitrary independent Selmer vectors. Check the finite quotient's
behavior under repeated [p] and the projected span index before using
any exterior bound. Compactness alone gives no nonvanishing, and no
unjustified inverse-limit exactness or full-tower surjectivity is allowed.
This is ordinary specialization of known mechanisms, not a proposed
new source theorem. No result is derived or reproved in this turn.

## Search record and access

Queries actually submitted included the following groups:

- `site.stacks.math.columbia.edu inverse limit finite sets compact countable subsequence`; `site.stacks.math.columbia.edu countable product finite discrete metrizable sequential compact`.
- `Selmer p^n Selmer p infinity p n Tate module multiplication transition Kummer exact sequence`; `site.jmilne.org EC2 Selmer Tate Shafarevich 129`.
- `site.stacks.math.columbia.edu elementary divisors principal ideal domain matrix determinant cokernel length`; `bounded index generators Z_p compactness subsequence determinant`; `site.stacks.math.columbia.edu Smith normal form PID matrix`.
- `site.math.uconn.edu Conrad p adic integers compact sequential compactness pdf`; `site.maths.gla.ac.uk Baker p adic theorem 4.21`; `sequential compactness p adic integers theorem site:kconrad.math.uconn.edu pdf`.
- `Elman Lectures Abstract Algebra Theorem 43.8 Smith Normal Form pdf site:math.ucla.edu`.

The primary sources above were inspected, rather than treating snippets
as theorem statements. The Nekovar *Selmer complexes* PDF lead exceeded
the browser's size limit; it is not essential because the coefficient
sources are accessible. Shell downloads failed at DNS resolution;
browser text retrieval succeeded. No persistent essential source blocker
remains. The arXiv countable-product paper and AFP p-adic formalization
were discovery leads only and are not imported as inspected proofs.

## Mathlib

Full matching subsequence theorem with actual Selmer-pair ancestry:
not checked. Supporting compactness, inverse limits, Smith normal form,
exterior powers and coefficient cohomology: Mathlib coverage not checked.
No absence claim or formal verification is inferred.
