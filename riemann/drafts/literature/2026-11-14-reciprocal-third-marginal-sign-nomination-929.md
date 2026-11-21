# Third determinant: common-frequency cancellation review930

TARGET: Assess source coverage for nonnegativity of the opposed-frequency marginal K(r) for every real r at x=B'(1) in C466a's signed N=3 inversion, retaining full normalization and absolute-integrability requirements.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Step930 searched triple-product Fourier inversion, conditional characteristic functions given a sum, nonnegative characteristic functions, and exact reciprocal-Xi marginal terminology; screened the named local reviews925/914 and stop927. No inspected matching all-r sign theorem was found; failed searches imply no novelty claim.
SOURCE_EVIDENCE: Heil Fall2009 convolution notes Theorem1.23 pp16-17 full proof; Jerison MIT18.103 Fall2013 Fourier-integral notes Proposition2 pp3 and Corollary4 p2 with Theorem2 pp3-4 proof; Iksanov Xi'an2019 Proposition117/Corollary119 pp65-66, Example140(b)/Lemma141 p76, Theorem162 pp86-88 full proof, Definition177/Theorem179 pp96-98 necessary direction; reuse review925's complete Andreief comparison and C466a/C466k's qualified density/inversion. Direct URLs and scope below.
COMPARISON: Convolution and bilinear determinant integration supply representation tools subject to absolute convergence, not this marginal's sign. A characteristic function of a symmetric positive density can change sign; the independent-difference modulus-square theorem requires independence under the law actually used. Review914's finite exponential core and ordered-test hypotheses do not identify the full actual three-copy marginal. No cited theorem settles K(r)>=0 or refutes it.
GAP: The actual N=3 marginal normalization, change of variables, absolute Fubini application and any conditional-law identification remain to be derived separately; the all-r sign is an uncovered actual-law test. A slice sign would still leave the full two-frequency domain, D3 signing, higher orders, all x and Xi transfer open.
REASON: Essential representation and sign-distinction coverage is now adequate for a bounded mathematical test of this same observable; automatic sign import is unsupported. This review derives no identity, inequality, actual-law counterexample or new lemma. A newly prepared ready continuation is subject to separate next-turn approval.
SCOPE: Completed literature-only comparison for C466a's normalized p=theta_1, actual h, x=B'(1) and original Re(z)=1 line. No PF-infinity, residual PF, Gaussian-mixture assertion, extra verified zeros, contour deformation or generic-law replacement is admitted. The original nomination text below is retained as provenance, not a current source blocker.
LITERATURE_REASON: The next turn changes from a ready product-contour obstruction audit to an uncovered frequency-marginal sign question; the ready determinant identity and symmetry assessments do not cover this representation or sign.

## Completed source comparison930 — 14 November 2026

Outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. The saved
target was kept fixed. Coverage now permits a mathematical attempt;
neither an actual-law sign nor its failure was established. No
mathematical exploration attempt or counter reset is claimed.

### Primary statements and relevant proof cases

Christopher Heil, author-hosted *The Fourier Transform on L1(R)*,
[Fall2009 convolution extract](https://heil.math.gatech.edu/7338/fall09/convolution.pdf),
Theorem1.23(a)-(d), printed pp16-17 (PDF pages3-4): for complex
Lebesgue-integrable f,g, convolution is defined almost everywhere,
belongs to L1 with norm at most the product of the norms, and its
Fourier transform is the product. Read the complete proof: product
measurability under a linear map, the absolute double-integral bound,
Tonelli/Fubini and translation in the transform. His kernel uses
exp(-2*pi*i*xi*u). The notebook uses angular frequency; that convention
must be converted explicitly. This is adequate complex-valued
convolution coverage; positivity of f,g is not required. Almost-everywhere
existence alone does not justify evaluation at the selected x.

David Jerison, MIT18.103 Fall2013,
[*Fourier Integrals on L2(R) and L1(R)*](https://math.mit.edu/~jerison/103/handouts/fourierint1.13.pdf),
Corollary4 p2 and Proposition2 p3: inverse L2 Fourier transform agrees
with the absolutely convergent inverse integral on L1 intersect L2,
with factor 1/(2*pi) and positive inverse exponential. Read Theorem2's
full truncation proof pp3-4, including the L2 tail convergence and
consistency propositions. The notes state their first Schwartz/L2
facts without proofs; those are standard imported Fourier inversion,
not a new argument to reproduce. A future complex convolution
application must verify its L2 membership and identify the continuous
representative before making a pointwise statement. Theorem3's L1
Fejer convergence was also read; it is not misquoted as unconditional
pointwise convergence of unweighted truncated integrals. No
distributional delta-function manipulation is licensed here.

Alexander Iksanov, *Characteristic functions and their relatives in
probability theory*, [Xi'an2019 notes](https://do.csc.knu.ua/wp-content/uploads/2023/01/Char_funct_XIan2019.pdf):
Proposition117 and Corollary119 pp65-66 give products for independent
sums and the modulus-square transform for independent identical
differences. Their full proofs were read. Conditioning on a shared
sum does not come with an independence assertion in these theorems.
Any use of the square formula after conditioning needs a separately
proved factorization. Example140(b), p76, gives the symmetric uniform
law's transform sin(a*t)/(a*t); Lemma141 and its full proof give
real/even symmetry, not nonnegativity. These source examples already
prevent inferring a nonnegative transform merely from a positive,
symmetric, compactly supported law. They are not counterexamples to
the actual K and are not substituted for the actual law.

Iksanov Theorem162, printed pp86-88, assumes an absolutely integrable
characteristic function and supplies its bounded continuous density
by inversion with factor 1/(2*pi). Read the full proof, including
continuity of the distribution, dominated difference quotients and
continuity of the recovered density. It applies to probability
transforms, so it cannot by itself invert arbitrary complex modulations;
the separate complex Fourier tools above supply that coverage.
Definition177 pp96-97 includes continuity in positive semidefiniteness.
Theorem179 pp97-99 is Bochner's criterion with normalization at zero;
read its necessity proof through the integrated modulus square.
Its sufficiency proof is not needed or imported for this test.
Neither criterion establishes pointwise signs of the characteristic
function. No conditional characteristic-function formula for K is
claimed to have been found in these sources.

Reuse completed review925 in
`2026-11-14-reciprocal-density-common-contour-nomination-924.md`:
Forrester [arXiv1806.10411v1](https://arxiv.org/pdf/1806.10411v1),
(1.7), Section2.2, and Ruzza's [4May2022 notes](https://webpages.ciencias.ulisboa.pt/~gruzza/introRMT.pdf),
Lemma3.1.1 pp27-28. Their complete relevant proofs were inspected in
that ready assessment and are not re-read here. In Ruzza the functions
may be complex but every cross-product must be L1; the identity is
bilinear, without conjugation, with the factorial shown there. For
N=3 the actual specialization, polynomial degrees, signed algebraic
Vandermonde, real coordinate Jacobian and p/Theta powers are future
obligations. A positive conjugate Gram determinant answers another
question. No specialized N=3 identity is derived in this review.

### Exact overlap, duplicates and search limitations

Read C466a's full proof and C466k's inversion and audit, rather than
extrapolating the former's large-s limit to s=1. C466k(6)-(7) is the
available all-polynomial fixed-line integrability input. The three-copy
and changed-variable Fubini application remains to be written in the
mathematical turn. All external strip, symmetry, paired-product,
counting and verified-low-zero qualifications are retained. No
strengthening of these inputs is needed for the planned source scope.

Reused completed conditional-simplex review914 in
`2026-11-14-conditional-simplex-contact-cone-nomination-913.md`:
Oudghiri's ordered-test/PF hypotheses and Sra's finite exponential-core
formulas concern different observables. They do not import a sign for
three copies of the full actual p. C466j/review914 remain contrasts,
not premises. Stop927 remains valid for simultaneous pointwise phases;
it does not exclude integration on the original line before signing.

A narrow primary overlap screen of Sra,
[*On some positivity properties of the Riemann Xi function*,
arXiv2611.02944v1, 2November2026](https://arxiv.org/html/2611.02944v1),
read Theorems1.1-1.3 and Section2.1's input declarations and searched
the full primary text for marginal/opposed/conditional/Fourier.
The finite-order PF theorem asserts ordered spatial minors; it does
not state pointwise nonnegativity of this frequency marginal.
Its all-dimensional radial positive-definiteness assertion is also
a different observable. No inference from that assertion or the
Gaussian-mixture claim is imported. This screen is not a new audit
of the source's PF certificates. Review914/925's inspected versions
and C466a's qualified one-sided assertion remain the actual inputs.

Queries included `Fourier transform triple product conditional
characteristic function sum zero positive nonnegative`, `Fourier
transform product convolution theorem L1 Fourier inversion theorem
conditional density`, `"conditional characteristic function" "integral"
"sum" Fourier`, `"conditional" "characteristic function" "nonnegative"
"sum" independent identically`, `"conditional difference" "characteristic"
sum`, `"triply positive" functions Fourier positive definite`, and
`"reciprocal Xi" "marginal" OR "frequency"`. Exact reciprocal-Xi
and Sra searches were checked as well. No matching sign theorem was
located within this bounded search. Search snippets and unrelated
distance-correlation, financial and lattice papers were not read as
theorem evidence. No claim of exhaustive search or novelty is made.

The guessed Heil inversion.pdf endpoint failed retrieval; his
convolution source and Jerison's accessible inversion statements resolve
that tool need. No essential source blocker remains for an analytic
attempt. A later numerical certificate would additionally need explicit
effective tail, quadrature and special-function error enclosures:
C466k's existential decay constants alone are not such a certificate.
This review does not approve a numerical-only sign claim.

### Decision and mathematical continuation

EXPLORE: known integration results supply enough coverage for the
same observable's bounded representation-and-sign test, but no direct
sign import. The prospective conditional law of three full tilted
copies at their total is a tool to investigate, not an established
identity for K. In particular, normalization at a single conditioning
value needs a specified continuous density version and positive
normalizer, not an arbitrary regular conditional distribution there.

Continue with a separate mathematical attempt only after the newly
prepared continuation assessment receives its next-turn approval.
The main sign test is one rigorously negative value at a nonzero r,
or a constructive sign representation valid for every r. An identity
alone is a routine specialization, not a creative sign advance. If no
sign mechanism survives the identity and source-hypothesis checks,
record that limited outcome and preserve the unresolved all-r target.
Finite positive samples are inconclusive. Neither a negative slice
nor its positivity settles an actual determinant or RH.

The precise proposed continuation and its bounded stopping test are
in `2026-11-14-third-marginal-full-law-test-930.md`. No new mathematics
is approved and performed in this turn. Full matching Mathlib coverage
for K or the N=3 specialization has not been checked; general Fourier
or integration support would not by itself establish the sign.

## Original nomination929 (retained)

## Exact proposed object and bounded discriminator

Use C466k's notation A_x(z)=exp(x*z)/h(z), with x=B'(1).
The proposed object to compare with the literature is

    K(r) = Re integral over real t of
           A_x(1+i(t+r)) A_x(1+it) A_x(1+i(t-r)) dt.

This defines the target, not a proved sign formula for a determinant.
The prospective claim is K(r)>=0 for every real r. A future rigorous
strict negative value at one nonzero r would reject this necessary
slice of a pointwise nonnegative marginal mechanism. Finitely many
positive evaluations would not establish the claim. A representation
or inequality proving it for every r would pass only this slice test.
An inconclusive finite search would stay inconclusive, with all
parameters and errors retained; no new calculation is run in step929.

The intended operation is to integrate the common frequency in the
signed three-variable Bromwich determinant before seeking a sign on
the two remaining difference frequencies. Retrieve and check the full
N=3 determinant normalization, its algebraic Vandermonde, the real
change of variables and absolute Fubini hypotheses. Do not infer these
applications from a formal oscillatory integral. C466k's all-polynomial
fixed-line tail is an available input, but the changed three-variable
application has not been derived here. No logarithm across a zero or
deformation is proposed.

Read exact primary theorem hypotheses and relevant proof cases for
Fourier marginalization/conditioning and any sign-preservation claim.
Search for the exact statement, stronger known conclusions and
counterexamples, including overlap with existing reciprocal-Xi
results. A conditional probability density being positive would not
by itself imply that its characteristic function is nonnegative.
Review914's finite-core conditional comparison is reusable only within
its stated scope. Do not retry its inaccessible, nonessential leads or
replace the full actual p by that finite core.

Continue only if the comparison yields a precise import, a fully
specified specialization, or a bounded uncovered sign test supported
by adequate sources. If the sign claim is already known, import it
with hypotheses; if the proposed identity needs the missing PF or
zero geometry as an assumption, abandon that circular mechanism.
Persistent essential source failure parks this nomination. The first
source review must distinguish these cases rather than approve an
unread theorem. No mathematical approval is given by this file.

## Recovery comparison: three mechanisms

1. A coupled nonproduct contour could evade C466k's exact hypotheses,
   but no explicit global surface, end estimates or sign discriminator
   is presently specified. The November6 joint-angular-contour source
   comparison warns that local phase optimization does not supply
   global signs. It is not selected merely as a relabeling of a stopped
   contour construction.
2. A smaller invariant chamber cone would require explicit new
   actual-law constraints and a preservation test absent from C466j
   and review914. Repeating the unrestricted minimum-principle or
   finite-factor conditional-sign arguments supplies neither. It is
   not selected without those new inputs.
3. The selected common-frequency marginal uses exact cancellation on
   the original integration domain. Its single opposed-frequency
   slice has a concrete sign threshold and a one-value negative
   discriminator, requiring neither scalar phase matching nor a
   chamber-cone assertion. Its identity and sign remain unproved.

The main gap remains L030-L032/C032a actual-Xi all-degree
algebraic-square positivity. Plausible downstream use is a signed
integral mechanism for density determinants that retains cancellations
discarded by the stopped pointwise contour approach. Passing this
N=3 slice would leave the full two-frequency domain, all orders, all x
and density-to-Xi transfer independently unresolved. A local finite
sign alone would not close the main gap.

Essential prospective inputs are C466a and C466k, inheriting L018's
conventions and the external strip, symmetry, product, counting and
verified-low-zero qualifications. C466j and review914 are failure
comparisons, not sign premises. No residual PF property, actual contact
or cross-notebook theorem is assumed. Full matching Mathlib coverage
is unchecked; general integral support would not prove the target sign.

A creative mechanism is due, but essential marginal/sign source
coverage is missing. Prepare that coverage before routing mathematics.
If the resulting task is only an identity specialization, do not call
it creative. Any later genuinely new sign mechanism needs its own
bounded test and escalation tied to the remaining all-degree gap.
