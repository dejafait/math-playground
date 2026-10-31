# Nonzero-row character presentation — source review

Literature-only, 2026-10-31. Source comparison completed; no mathematical
audit verdict, new lemma or script. The saved target remains unchanged.

The main gap is actual-Xi all-degree positivity. The intermediate target
is the literal fixed-family presentation assumed in L553 and L548.
It could discharge that presentation premise in their conditional
reflection applications; coefficient/Gauss imports, arithmetic-uniform
closure and a sign bridge remain separate. No cross-notebook input.

Primary source inspected so far: OpenAI, *The Quasi-Riemann Hypothesis*,
30 September 2026, commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a,
[pinned TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
Read all of `lem:reflection-row-sectors` and its proof (2320–2380),
`lem:fixed-numerator-ray` and proof (593–643), the reciprocity statement
and relevant proof (860–927), fixed-ray discussion (928–961), common
modulus hypotheses (1561–1588), and marked application (6873–6907).
Source statements and proof explanations are evidence of coverage,
not an independent verification of the application.

The initially pending Milne, DR and periodicity/application reads below
are now complete. Retained reciprocity is distinguished from an audited
application; no source assertion is certified by this literature review.
The continuation test requires all unit/S-valuation sectors, a modulus
chosen before good primes vary, every exponent-zero mask, shared-prime
and mark collision zeros. A moving modulus or uncovered reciprocity
domain requires narrowing or parking the corresponding implication.

Scoped local duplicate search found earlier phase, cusp, Mellin and
marked assessments expressly excluding this presentation. Their source
comparisons are reused; L553 explicitly assumes it. No matching local
completed presentation audit was located. Existing changes are preserved.

External discovery queries so far: `"reflection-row-sectors"`;
`"sextic" "ray class" "reciprocity" Eisenstein`;
`site.jmilne.org CFT "5.3" "power residue" Artin`;
`"Eisenstein" "sextic reciprocity" "ray" character fixed numerator`.
Mirrors and derivative posts are not independent theorem evidence.
No novelty is inferred from these bounded searches. Shell download
failed DNS; the pinned primary TeX is accessible through the web tool,
so there is no essential source blocker from that shell failure.

## Independent primary input and exact domains

J. S. Milne, *Class Field Theory*, version 4.03, 6 August 2020,
[author's PDF](https://www.jmilne.org/math/CourseNotes/CFT.pdf),
Chapter VIII, Section 5, printed pp. 244–245 (PDF pp. 253–254).
Read the power-residue definition and ideal extension, (5.3) and its
proof, and (5.5) and its proof. The field K must contain a primitive
n-th root of unity. For a in K^*, S(a) includes all prime divisors of
n and all primes where a has nonzero valuation; the ideal argument
avoids S(a). Equation (5.3) identifies the multiplicative power-residue
symbol with arithmetic Frobenius on K(a^(1/n)); (5.5) supplies a ray
modulus supported in S(a). Its proof invokes VII A.5 and Artin
reciprocity V (3.5). These named results are imported, not reproved.

The specialization requested for the next audit is K=Q(omega), n=6
and each nonzero, unit-times-S-supported numerator specified in the
source. The symbol normalization must be matched to the unique sixth
root with the prescribed residue-field power, including arithmetic
rather than inverse Frobenius. Milne supplies neither a numerical
conductor exponent nor a modulus independent of a moving numerator.
It does not prescribe any value when an ideal meets the numerator.
These limits matter for the source's literal, zero-extended presentation.
The later audit must justify the finite-family/common-modulus application,
rather than importing a statement about arbitrary moving numerators.

Dunn–Radziwill, *Bias in cubic Gauss sums: Patterson's conjecture*,
Annals of Mathematics 200 (2024), no. 3, 967–1057,
[arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3), 14 May 2024,
Section 1.2, definitions and (1.4)–(1.5), were inspected at HTML
133–147. Import ordinary cubic reciprocity on coprime primary inputs
and the supplementary laws for units and lambda, with denominator
d=1+alpha_2 lambda^2+alpha_3 lambda^3 modulo 9 as stated there.
The cubic symbol has exponent (N(p)-1)/3. No GRH-dependent asymptotic
or large-sieve lower bound from that paper is an input here.

Reuse the base-quadratic assessment's inspected
`lem:quadratic-four-term`/`eq:reciprocity-four-class` as the explicit
retained Gaussian identity; its independent analytic proof audit remains
outside scope. Read the sextic-reciprocity proof's distinct-prime CRT,
cubic-reciprocity and multiplicative-extension cases (899–927).
The use of that identity to obtain the needed reciprocity correction
may be reproduced in the next audit. Its definition on noncoprime
pairs must remain a separate bicharacter, never a quotient of zeros.

## Coverage comparison and bounded next audit

Additional primary reads: source notation/defining moduli (519–588),
the earlier row reduction (974–1012), fixed common modulus (1561–1588),
periodicity verification (1873–1880), and all mark/puncture/application
definitions (6825–6907). The full `lem:reflection-row-sectors` already
claims the target for nonzero rows; this is reproduction, with no
novelty assertion. A direct import of that conclusion would bypass the
requested local check of L553's explicit presentation premise.

Approve only the following applicability work after the separate gate:

1. Check primary-generator and ideal conventions, arbitrary unit and
   S-valuations, and the unit row/empty good radical. Match Milne's
   symbol and its domain to each retained numerator representative.
2. Check the reciprocity correction and its fixed ray group, including
   the distinction between an ideal ray class and a generator's residue
   square class. Specify exactly which Gaussian formula remains imported.
3. Check the finite family and one E,L chosen before good primes, row
   sizes, squarefree labels and puncture primes vary. Include the full
   defining-modulus zero mask and the supplementary factor in phi.
   Fixed S/family dependence is permitted; varying-S or effective
   conductor claims are not covered.
4. Check the union of good primes of k,f and the puncture, exponents
   combined modulo six, and every local support factor when the
   combined exponent is zero. Check both shared and distinct primes
   without cancelling a zero. Keep the off-primary/off-S branch
   piecewise, evaluated before any undefined symbol.
5. Check the presentation on the whole primal A=nb^3, including n,b
   sharing primes, and its literal match to L548/L553. Retain the
   stipulated independence and product form of finite marked lists;
   check colliding tuples before using L553's disjoint-list formula.

These are audit obligations, not derived results. Continue only if every
case survives with this fixed family; a required moving modulus,
missing reciprocity domain, or lost zero is a reason to narrow or park
the implication. The row k=0 is excluded by the source lemma and stays
excluded. Do not enlarge the primal statement to the unmasked dual
lattice, derive an energy estimate or claim uniform global closure.

The local ATTEMPTS search for reflection-row-sectors, row-character
presentation, row-sector and fixed-numerator-ray returned no recorded
target-specific failure. The L553 critical-review record explicitly
leaves this premise open. Its completed finite recombination and the
cusp/Mellin/phase comparisons are reused, not repeated. Derivative
mirrors and rStation leads returned by search were not read as inputs.
No independently inspected stronger theorem substitutes for the whole
application. This bounded comparison makes no claim of exhaustive
literature coverage or mathematical novelty. Matching Mathlib coverage
has not been checked; no absence is asserted.

Decision: SPECIALIZE, sufficient source coverage for a separate
REPRODUCTION audit conditional on the identified standard arithmetic
and retained quadratic identity. No lemma, mathematical script, PROOF
or DAG changed. All prior unfinished work is preserved.

## Direct-URL recovery, 2026-10-31

The supervisor reported that the ready assessment lacked a direct source
URL. Its SOURCE_EVIDENCE now contains all three primary URLs above.
Web retrieval succeeded for the pinned TeX (including the row-sector
label at 2321), Milne v4.03 (including VIII (5.5) at PDF page index 253),
and DR v3 (including Section 1.2 reciprocity). This checks accessibility
and locators only; the earlier full source reads and exact-domain
comparison are reused. No mathematical audit was performed and no
new source conclusion is asserted. The SPECIALIZE decision, target,
five-case test, imported quadratic identity and open premises are unchanged.
