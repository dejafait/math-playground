# Explicit-formula reliability audit — source comparison1191

TARGET: Assess primary coverage for independently auditing Polson v24 Section 4.3's explicit formula under C030e's Gaussian-polynomial hypotheses and Fourier normalization.
CHECKED: 2026-11-16
DECISION: IMPORT
SEARCH_EVIDENCE: Review1191 searched the exact IK theorem reference and Guinand-Weil strip formulation; read the primary Carneiro-Milinovich and Carneiro-Milinovich-Soundararajan statements below; reused1184/1188, C030e and scoped stops1117/1181 and working1121. Searches do not establish novelty or a confirmed book miscitation.
SOURCE_EVIDENCE: Read Polson1708.02653v24 Section4.3/(3) and reference[12]; Carneiro-Milinovich2403.17803v1 (26March2024) Section2.1 Fourier definition and Section2.2 Lemma4/entire one-line proof p5, and published2024 Section2.2 Lemma2.2/entire proof p7, Fourier definition p5; CMS author PDF dated14August2017 Lemma6/entire proof pp16-17 and Fourier definition p2. IK Chapter5 itself was not retrieved.
COMPARISON: The inspected unconditional named Guinand-Weil theorem already states the required complex-ordinate identity in a stronger test class. C030e already checks the narrower Gaussian test. A standard-theorem import with the Fourier conversion suffices; these papers refer back to IK and are not an independent contour-proof certification.
GAP: Only a canonical citation/applicability update remains for this analytic input; the primary book theorem-number discrepancy is unresolved and need not be assumed away. No independent reproof is licensed. Actual-Xi all-degree positivity, far-time source claims and realization remain open.
REASON: Direct inspected coverage changes the proposed route from independent explicit-formula reproduction to a bounded known-result import. Retain the book-access limitation explicitly and cite the precise accessible named theorem instead of treating a search snippet as the book.
LITERATURE_REASON: Nomination1190 changed the scope from heat convergence to the retained explicit formula; its primary standard-theorem interface was essential unread coverage at invocation start.
SCOPE: Import the standard Guinand-Weil identity only, for C030e's fixed real finite-degree polynomial of fixed parity and fixed positive t; reuse its existing admissibility/normalization, C030g convergence and C030d/C030f bounds. No independent contour audit, uniform-in-order limit, far-time sign or RH consequence.
COVERED_TARGET: Import the standard Guinand-Weil explicit formula into C030e from Carneiro-Milinovich Lemma 2.2, reusing its audited Gaussian admissibility and Fourier normalization.

## Original nomination1190 — retained historical scope

The main gap remains L030-L032/C032a all-degree actual-Xi positivity.
This nomination seeks reliability of one retained analytic input only;
no new arithmetic sign mechanism is proposed. The exact local input is
C030e's h(r)=q(sqrt(t)*r)^2 exp(-t*r^2), q of fixed parity and finite
degree, positive t, with g(b)=(2*pi)^(-1) integral h(r)exp(-irb)dr.
C030g gives absolute convergence of the spectral side and derivatives;
C030d/C030f pay the already audited polynomial/gamma bounds. These
facts do not themselves prove the contour identity.

The separate source review should reuse assessment1184's formula and
C030e's already checked test admissibility rather than repeat assembly.
Retrieve the exact identification of Polson source[12] and Theorem5.12,
then its primary theorem hypotheses and any essential proof cases
needed for a reliability audit. First compare the existing formula
against that named theorem. A precise citation plus applicability may
suffice; justify any independent reproof by a concrete remaining
reliability qualification. Do not undertake it during the review.

Continuation/abandonment test: source coverage must account for both
polar evaluations, the 1/(2*pi) gamma integral, the factor2 prime term,
actual nontrivial zeros with multiplicity off the line, and the stated
strip/decay requirements. If these are covered, approve only the
identified remaining audit; if a mismatch or access blocker remains,
record its effect on C030e rather than assume the formula. A persistent
source blocker requires parking this dependent audit and choosing an
independently testable target, with its own coverage gate.

Stops1117/1181 do not prohibit this analytic check, but remain relevant
to any later all-degree extension. No ready central creative target
follows from this audit: discovery1121's arithmetic-to-square payment
is still missing. Full matching Mathlib coverage remains unchecked.
The current mathematical outcome is retained regardless of the later
approval decision for this new continuation. No next-turn mathematics
has been derived or approved here.

## Completed source comparison1191 — 16 November 2026

The original nomination above records the question at invocation start.
The current decision is IMPORT, not approval of a new contour reproof.
The newly covered continuation still receives separate supervisor
approval before mathematical invocation. No lemma or script changed.

### Exact inspected theorem and normalization

The accessible primary reference is E. Carneiro and M. B. Milinovich,
*On Littlewood's Estimate for the Modulus of the Zeta Function on the
Critical Line*, Constructive Theory of Functions, Lozenets2023,
Professor Marin Drinov Publishing House of BAS, Sofia,2024, pp1-16,
[Section2.2, Lemma2.2, p7](https://www.math.bas.bg/mathmod/Proceedings_CTF/CTF-2023/files_CTF-2023/05-Carneiro-Milinovich.pdf#page=7).
The same statement is Lemma4, p5, in
[arXiv:2403.17803v1, 26March2024](https://arxiv.org/pdf/2403.17803v1#page=5).
The paper explicitly separates this unconditional lemma from its
RH-dependent subsequent inequalities. Its proof is a reference to
IK Theorem5.12, not a written independent contour argument.

Hypotheses: h is holomorphic on a strip of half-width 1/2+e, e>0,
with uniform horizontal decay O((1+|z|)^(-1-d)), d>0.
Using its Section2.1 convention hhat(y)=integral h(r)e^(-2*pi*i*r*y)dr,
the displayed identity is

    sum_rho h((rho-1/2)/i)
      = h(1/(2i))+h(-1/(2i)) - hhat(0)log(pi)/(2*pi)
        + integral_R h(r)Re psi(1/4+i*r/2)dr/(2*pi)
        - sum_(n>=2) Lambda(n)n^(-1/2)
            [hhat(log(n)/(2*pi))+hhat(-log(n)/(2*pi))]/(2*pi).

This is a zero sum, with the standard multiplicity convention, not a
sum of distinct critical-line ordinates. No simplicity assumption is
stated. Retain that convention explicitly in the canonical import;
the displayed lemma does not separately spell out the word multiplicity.
Polson's inspected residue description sums over every nontrivial zero,
including off-line ones. No real-zero replacement is authorized.

For comparison only, C030e already uses the narrower entire even h and
proves rapid decay on |Im r|<=1, for each fixed q,t. Its existing bound
thus supplies the displayed strip/decay interface without any uniform
constant as degree grows or t tends to0. The Fourier conventions compare
as hhat(b/(2*pi))=2*pi*g(b). Evenness identifies the two prime
frequencies, accounting for the factor2; the zero-frequency term combines
with the gamma integral to give C030e's m(r). The two polar arguments
are precisely {-i/2,i/2}. These are normalization comparisons with the
existing C030e calculation, not a fresh theorem or an all-degree limit.

An independent inspected statement is E. Carneiro, M. B. Milinovich
and K. Soundararajan, *Fourier optimization and prime gaps*,
[author PDF dated14August2017, Lemma6 pp16-17, Fourier definition p2](https://home.olemiss.edu/~mbmilino/PrimeGaps.pdf#page=16).
It gives the same strip hypothesis, complex argument, two polar terms,
gamma term and two Fourier frequencies. Its entire proof likewise cites
IK Theorem5.12. It corroborates the interface, not an independent proof.
Neither theorem imposes bandlimitedness on h; that restriction appears
in later applications and must not be added to the theorem or confused
with the present Gaussian-polynomial test. Both statements allow the
present real-even subclass; neither supplies a positivity conclusion.

### Book access, searches and bounded decision

Polson reference[12] is H. Iwaniec and E. Kowalski, *Analytic Number
Theory*, AMS Colloquium Publications53,2004. Queries included
`Iwaniec Kowalski Analytic Number Theory pdf Theorem 5.12 explicit formula`,
`Iwaniec Theorem 5.11 explicit pdf`, and
`Guinand-Weil h 1/2 Carneiro Lemma explicit formula`.
Some results identify5.11 as an explicit formula and5.12 as PNT;
these search leads are not a primary check of either book statement.
The two inspected primary articles themselves cite5.12. Therefore no
confirmed correction of the book number or edition is asserted here.

Publisher access to bookstore.ams.org/coll-53 and
www.ams.org/books/coll/053/coll053-endmatter.pdf returned403; the
coll053.pdf endpoint was inaccessible. The author-hosted
[ik-ant-exp-sums.pdf](https://people.math.ethz.ch/~kowalski/ik-ant-exp-sums.pdf)
contains Chapter11, not the requested chapter. The inspected Chapter5
entries in the authors' [errata dated8March2010](https://people.math.ethz.ch/~kowalski/corrections-ant.pdf)
do not resolve this reference. No unread book theorem hypotheses or
proof cases are represented as inspected. Screenshots yielded no visible
images; complete relevant primary text, not a screenshot preview, is
the evidence above. No further book-access search is needed to import
the precisely named Guinand-Weil theorem; an independent book-proof
audit remains unperformed and is not the continuation.

This overlap changes the route: citation plus C030e's already audited
specialization answers the retained-input reliability question at the
standard-input level. No suspect residual contour claim has been isolated
to justify reproof. The next bounded task is the covered canonical import,
retaining off-line multiplicities and documenting the source limitation.
Continue only if the theorem application preserves each displayed term
and hypothesis; otherwise isolate the exact mismatch before further work.
No new source-sign mechanism, central creative target or complete RH
argument follows. Stops1117/1181 and working1121's unpaid arithmetic-to-
square bridge still block automatic all-degree extensions. Full matching
Mathlib coverage was not checked; unknown does not mean absent.
