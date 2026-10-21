# Fixed nonunitary-cusp exact recovery — source approval

TARGET: Recover the exact rational value of Re(A_f({1/6,infinity}))/Omega(E) for y^2=x^3+1 from L051's audited interval and an independently justified denominator bound.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: BSD-171 searched fixed-model/nonunitary denominator terminology and X_0(36) model/differential identification; compared L048/L049/L050/L051, prior effective-denominator coverage and ATTEMPTS/025. Read the primary genus-one identification and the cube-free Manin theorem; inspected Wuthrich's arbitrary-cusp statement and complete proof cases. Queries and qualifications appear below.
SOURCE_EVIDENCE: Cai--Chen--Liu, Trans. AMS 370 (2018), 3721--3743, Section 3 opening p.3732 https://archive.ymsc.tsinghua.edu.cn/pacm_download/632/12220-Heegner_points_on_modular_curves.pdf#page=12; Cesnavicius--Neururer--Saha, author PDF 2022-01-28, Theorems 1.2/7.2 pp.3,45--46 https://maths.qmul.ac.uk/~asaha/research/manin-paper.pdf#page=3; Wuthrich arXiv:1608.06423v2 (2017-03-23), Proposition 1 and complete proof pp.3--4 https://arxiv.org/pdf/1608.06423v2#page=3; reuse audited L048/L049's Cremona total-period convention.
COMPARISON: Known sources cover an independent degree-one normalization input for this exact CM/additive curve and an arbitrary-cusp torsion-reduction denominator mechanism. This avoids assuming a database optimality label or a general Manin conjecture. The remaining work is a fixed known-method specialization and exact enumeration, not a new denominator theorem or BSD result.
GAP: No fixed denominator or rational value is derived here. Later work must apply the model identification and cube-free theorem, certify selected split-prime counts, transfer the total-period/orientation conventions and enumerate every admissible rational in L051's exact interval. Rational proximity and interval width alone remain insufficient.
REASON: This separate literature-only review approves BSD-170's unchanged proposed target; newly inspected primary identification fills its essential scale coverage. Mathematical specialization and recovery are deferred to the next invocation.
LITERATURE_REASON: The saved REVIEW_REQUIRED target lacked a usable fixed denominator and independent model/scale coverage; the general L048 assessment alone did not meet this fixed-interval scope.
SCOPE: Exact globally minimal E=[0,0,0,0,1], N=36, CM allowed, additive reduction at 2 and 3, oriented {1/6,infinity}, total minimal real period; existing audited interval only, with no full generator table or non-CM application.

Essential inputs are audited L048/L049 for general rational-recovery
context, L050 for the exact minimal model [0,0,0,0,1], Delta=-432,
conductor 36 and additive factors, and audited L051 for the fixed
{1/6,infinity} orientation, target total-period convention and interval.
No cross-notebook input is proposed. Reuse these ready assessments for
their unchanged hypotheses; inspect only the additional sources needed
for a usable fixed denominator. Any needed optimality, differential
scale, cusp order or period index must be independently supplied, not
inferred from an apparent nearby rational or an expected curve label.

The main gap remains arbitrary analytic-order-at-least-two rank equality.
This intermediate target could convert the audited nonunitary interval
into an exact normalization input. It would still give only one path,
with no entire integral generator table, all-level coefficient, rational
direction, Sha result or arbitrary complex-order comparison.

The eventual discriminating test is an independently justified bound
followed by complete exact rational enumeration in the existing interval,
requiring exactly one admissible value and justified existence. A bound
that does not isolate a value does not license rounding. If sources
require unsupported optimality/Manin/non-CM/unitary assumptions, record
that obstruction and reassess before any dependent calculation. Preserve
both schedules and the audit evidence. No new lemma or recovery
calculation is asserted by this assessment.

## Primary comparison completed in BSD-171

The main gap, intermediate target, downstream use and discriminating test
above are unchanged. This is the separate approval of the previously saved
target, not discovery and proof of an uncovered result in one turn.

**Exact modular curve input.** Cai, Chen and Liu, *Heegner points on
modular curves*, Trans. AMS 370 (2018), 3721--3743, DOI
10.1090/tran/7053, [Section 3 opening, p.3732](https://archive.ymsc.tsinghua.edu.cn/pacm_download/632/12220-Heegner_points_on_modular_curves.pdf#page=12),
explicitly identify (X_0(36),[infinity]) as the elliptic curve with minimal
equation y^2=x^3+1. The paragraph was read in the publisher's offprint.
This is a published model identification, not a new proof or a label-based
guess. It supplies the origin-preserving isomorphism input. Its L-value,
rank and Tamagawa assertions are not recovery inputs.

Dasgupta--Voight, *Heegner points and Sylvester's conjecture*,
[author preprint, Section 3.2 p.6 and Section 3.5 p.8](https://sites.math.duke.edu/~dasgupta/papers/clay.pdf#page=6),
independently display the same isomorphism and specify that infinity maps
to the origin. Those passages were read as corroboration; no Heegner-point
or twisting result is imported. An explicit eta parametrization is not
needed for this target.

**Differential theorem.** Cesnavicius, Neururer and Saha, *The Manin
constant and the modular degree*, [2022-01-28 author PDF, Theorems
1.2/7.2, pp.3,45--46](https://maths.qmul.ac.uk/~asaha/research/manin-paper.pdf#page=3),
treat every surjection X_Gamma -> E at E's exact conductor, with
Gamma_1(N) contained in Gamma contained in Gamma_0(N). For the minimal
Neron differential, phi^*omega_E=c_phi omega_f with nonzero integer
c_phi. The theorem gives c_phi dividing deg(phi) when 8 and 27 do not
divide N, and unconditionally gives the factor-six version. The theorem
statement and complete final proof were inspected, including the integral
differential pullback and exceptional-prime branches. No CM exclusion or
semistability assumption occurs. The supplied conductor 36 lies within
the stated cube-free case. Future work may specialize this theorem to the
published isomorphism to establish the exact absolute differential scale;
the general factor-six bound need not be used. No reproof is justified.

**Arbitrary cusp theorem.** Wuthrich, *Numerical modular symbols for
elliptic curves*, [arXiv:1608.06423v2, Proposition 1 and full proof,
pp.3--4](https://arxiv.org/pdf/1608.06423v2#page=3),
assumes c_0=1 and defines delta^2 as the largest square dividing N.
For good primes ell>2 with ell=1 modulo delta, let t_0 be the gcd of
their point counts; t^+ is the numerator of t_0 q^+, where
q^+=Omega_E^+/Omega_E0^+. The arbitrary-cusp conclusion is
[r]^+ in c_infinity(E_0)/(2t^+) Z. The proof uses cusp fields,
Manin--Drinfeld, unramified torsion injection (Silverman VII.3.4) and
both period-lattice cases. These cases were read, and earlier L048 source
coverage is reused. No unitary hypothesis belongs to this first conclusion;
the stronger rational-torsion shortcut must not be applied to r=1/6.

**Remaining specialization, not a completed calculation.** The published
isomorphism has degree one and is the input for identifying the optimal
curve; the Manin theorem will justify its scale rather than assuming
Wuthrich's c_0 premise. Later work must spell out this applicability and
the period ratio. Use L050's one real component and audited L048/L049's
total-period convention, not an unexamined sign-to-lattice sentence in
Wuthrich's introduction. Wuthrich integrates from infinity to r; L051
uses the reversed path. The sign reversal affects the interval, not the
denominator, and must remain explicit.

Good split primes 7 and 13 are a concrete proposed finite test. The
existing L050/L051 production evidence contains their point-count inputs,
but this turn did not inspect or replay the complete selected counts,
form their gcd, obtain a numerical denominator or enumerate fractions.
The research step must retain complete count evidence, primality/good
reduction/splitting checks and all exact isolation inequalities. If that
bound fails to isolate, stop this fixed-interval recovery attempt without
rounding. A future bound may clear a lattice or merely bound reduced
denominators; the enumeration must match the bound actually proved.

## Search, overlap and limits

Queries included `Wuthrich numerical modular symbols denominators non
unitary cusp 36a1`, `X0(36) y^2=x^3+1 modular parametrization Manin
constant`, `"X_0(36)" "y^2" "x^3" isomorphism`,
`"X0(36)" "cusps" "torsion"`, and fixed differential/cusp variants.
The last variants gave no essential additional coverage. No novelty is
inferred from a search failure. A Najman torsion paper and explicit eta
formula leads remain unread and unnecessary; no torsion-group assertion
from their snippets is used. The inspected primary identification plus
the already assessed Manin and arbitrary-cusp theorems suffice for the
proposed specialization without those leads.

L048 already proves a coarse general denominator, and L049 already proves
conditional terminating recovery. Neither duplicates a completed exact
value for this path. L050 preserves the failed rectangle schedule;
ATTEMPTS/025 concerns its error propagation, not denominator impossibility.
Audited L051 repairs that representation but claims no rational recovery.
The historical stop therefore does not prohibit this distinct test.
No sibling notebook or cross-notebook mathematical input was read.

Full matching Mathlib coverage for this fixed rational recovery and the
source model identification was not checked; no absence claim is made.
Canonical proofs and source imports belong in a later lemma if the
specialization succeeds. No lemmas, mathematical scripts, DAG or main
argument were changed in this literature-only turn. Coverage does not
establish practical success, the exact value, a complete normalized
functional, an all-level coefficient or any missing BSD comparison.
