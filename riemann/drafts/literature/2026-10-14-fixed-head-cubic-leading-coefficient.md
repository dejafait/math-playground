# Fixed-head cubic leading coefficient: completed coverage review

TARGET: Determine the fixed-N leading coefficient of L407's signed arithmetic expression at scale H(log H)^2, retaining every rational twist and analytic weight.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 112 searched rational additive twists, shifted ternary divisors, generalized Estermann functions, sharp Perron scope and source corrections; inspected Fazzari 2306.15553v1 and DLMF 25.11/2.5, reusing steps 103/107/111 exclusions and carrier coverage; no matching evaluation of the complete local signed expression was found in the inspected records.
SOURCE_EVIDENCE: Fazzari 2306.15553v1 (27 June 2023), (1.3), Theorem 1.1, Lemmas 2.1–2.2, Lemma 3.2, exact identity (3.5) p. 10 and Section 4's opening contour step; DLMF 25.11(i), 25.11.1, 25.11.5 and 2.5.2. Primary coverage is the finite shifted Hurwitz decomposition and Mellin tools, not a signed cubic moment theorem.
COMPARISON: These known inputs cover every fixed rational additive twist with three independent shifts. Specialization must still evaluate the local logarithmic jets and analytic weights and justify sharp endpoints; neither the source nor audited L407 computes this signed coefficient. The smooth Voronoi formula alone does not supply a sharp asymptotic.
GAP: Mathematical application obligations are the coalescing-pole calculation for all ordinary jets, controlled weight replacement, sharp endpoint transfer and complete signed assembly; no essential source remains inaccessible for this bounded fixed-N attempt. Full tails and clipping are outside coverage.
REASON: Approve one later mathematical specialization using the exact finite Hurwitz representation, with the application obligations below; do not import the unproved Bui cubic theorem or the source's inconsistent expanded polar-factor proof. No coefficient or new lemma is derived in step 112.
LITERATURE_REASON: The newly proposed signed asymptotic needs shifted rational-additive divisor coverage beyond the already audited carrier reduction; Fazzari's exact three-shift decomposition is a specific new relevant lead.
SCOPE: Fixed positive integer N independent of H; L407 equations (4), (8), (9), both S and T terms, all ordinary jet coefficients and sharp endpoints. No growing head, full-response limit, lower-order asymptotic if the coefficient vanishes, clipping or RH claim.

The main gap remains global actual-theta mixed positivity. The proposed
intermediate target asks whether the audited finite signed expression
has a limit after division by H(log H)^2 and, if so, for its coefficient
as a function of fixed N. A coefficient equal to zero is an admissible
answer; no nonzero cubic main scale is assumed. Its downstream use
would be deciding whether this test scale can support a later complete
signed statistic. Full-tail passage and clipping are independent gaps.

Essential local input is audited L407, with L369's actual reality/phase,
L390's d_N, L391's ordinary-jet and contour tools, and audited L405's
B0_N as needed for interpretation. L406 is downstream physical-transfer
context, not a license to exchange the limits H and N. All constants
in the new target may depend on fixed N. The existing reduction leaves
the actual additive phases exp(-2pi i vj/u) and w(t_j-i11/20) intact.

The proposed literature turn should search the exact weighted divisor-sum
statement, stronger fixed rational-twist results and known obstructions;
retrieve the needed primary hypotheses and proof cases before deciding
IMPORT, SPECIALIZE or EXPLORE. Standard additive divisor/Dirichlet-series
residue methods are candidate search terminology only, not imported
theorems or a derived asymptotic. Reuse the existing carrier sources for
the reduction and do not repeat their already completed source audit.
The excluded unproved Bui cubic theorem remains excluded. L394/L399/L400
stop evidence concerns other weights and remains intact.

Continuation test: coverage must justify every cubic logarithmic
coefficient, fixed rational phase and analytic-weight contribution with
total error o(H(log H)^2) on the sharp interval. A citation must not
omit a surviving resonance or assume a nonzero leading coefficient.
If essential coverage is inaccessible, record the exact blocked input
and choose an independently testable target under the recovery rules;
do not approve an unproved signed moment or repeat the completed audit.

Unresolved assumptions/obligations: existence and value of this fixed-N
limit, any lower signed scale if it vanishes, uniform full-tail passage,
clipping, regulator choice, total L367 margin/remainder, actual common-zero
upper counts and global mixed positivity. Full matching Mathlib coverage
is unchecked. The preceding proposal was written in step 111; the
completed step-112 decision below supersedes its pending-review language.

## Completed source comparison — 2026-10-14, step 112

This is LITERATURE / literature_comparison, with no lemma or mathematical
script writes. ADVANCE denotes newly established source coverage for the
bounded local attempt; it is not a signed asymptotic or progress beyond
the mathematics in the inspected sources.

### Discovery and local overlap

Queries included `ternary divisor function rational additive twist shifted
divisor function asymptotic fixed modulus`, `generalized Estermann function
shifted triple divisor additive twist pole residue`, `"shifted triple
divisor" "asymptotic" "additive"`, `"divisor" "fixed" "additive twist"
"Perron" ternary`, and `"Fazzari" "2306.15553" erratum`.
Shifted-convolution and arithmetic-progression results returned by search
were locators, not imported theorems. Convolution of two divisor sequences
at different arguments is not the single additive twist in L407 (8).
No failed search establishes novelty or absence of corrections.

Read L407 through its complete (9), absolute bound and audit qualification;
the step-111 history; step-103 cubic source comparison; and the relevant
step-107 and older unequal-orientation source passages. Narrow searches
in recent local assessments found no Fazzari/shifted-Estermann evaluation
of this target. L394/L399/L400 remain different-weight stop evidence.
Their conclusions do not ban this intermediate calculation. Existing
uncommitted notebook work is preserved. The carrier audit is reused,
not repeated, and its O_N(H^(71/120)) error remains the input threshold.

### Primary inputs and qualifications

A. Fazzari, *A Voronoi summation formula for the shifted triple divisor
function*, [2306.15553v1](https://arxiv.org/html/2306.15553v1),
defines three complex shifts in (1.3). Theorem 1.1 assumes a Schwartz
test function and coprime integers. Read its statement, coalescence
qualification, Sections 2–3 through (3.5), and Section 4's opening
contour step. The finite residue-class identity (3.5), p. 10, retains
all classes, including nonunits. Lemma 3.2 supplies progression-zeta
continuation. Separate simple-pole formulas require distinct shifts;
at coincident shifts the combined polar contribution must be used.

The PDF pp. 6–7 and HTML both show phi(d) in (2.5), but phi(K/d)
in (2.7) and the following display. Do not rely on that inconsistent
expanded formula. Use (3.5) directly. No correction was established.

[DLMF 25.11(i)/25.11.1](https://dlmf.nist.gov/25.11#i)
gives the Hurwitz series and its sole pole, residue one.
[25.11.5](https://dlmf.nist.gov/25.11.E5), sourced to Apostol (1976),
(25), p. 269, requires a>0, Re s>0, s!=1 and integer N>=0.
[2.5.2](https://dlmf.nist.gov/2.5.E2) supplies Mellin inversion on
an admissible strip. These support the proposed contour application;
the full Voronoi dual is unnecessary.

### Exact specialization scope and remaining proof obligations

The source's modulus is u and its additive numerator is -v for each
reduced r=u/v in L407. Both are fixed with N, and (-v,u)=1; u=1
is included. The progression parameter is a=L/u in (0,1], including
L=u for the zero residue class. This is an applicability identification,
not a computation of the complete arithmetic mean. Residue-class phase
factors must be retained through the calculation; coprimality of the
numerator does not permit restricting the three divisor variables to
unit classes.

L407 (8) is covered by differentiating the three independent shifts
in the absolutely convergent defining series, each at most twice, then
using the finite Hurwitz identity. That operation is covered at the
Dirichlet-series level, not by differentiating a nonuniform sharp
asymptotic or individual singular residues. A common contour enclosing
the merging poles, or the Laurent expansion after the exact derivatives,
is the proposed way to handle coincident shifts. Any claimed signed
limit still needs the proof below.

The identified difference from the known inputs consists of:

1. Establishing a logarithmic divisor-sum leading term for every C_nu
   and fixed phase, with error small after its ell^(-d(nu)) weight.
   A smooth compactly supported Mellin application, polynomial growth
   controlled from the cited Hurwitz formula and Cauchy on fixed disks,
   is an assessed mechanism to test. It must give actual bounds for
   all horizontal segments and shifted derivatives; no unproved sharp
   Perron estimate is assumed.
2. Handling H<t_j<=2H. With a fixed relative endpoint width first,
   positive smooth majorants for the unsigned d_3 boundary mass and
   |C_nu|<=d_3(log j)^d from L407 are an assessed transfer mechanism.
   Take H to infinity before shrinking that width. The signed sum or
   a complex analytic weight cannot be bracketed by positivity. An
   absolute boundary estimate is required. No uniform vanishing-width
   formula, microscopic short-interval theorem or source Schwartz
   hypothesis for an indicator function is imported.
3. Retaining w_(e,nu)(t_j-i11/20). Use its exact definition in L407
   (4) and the existing polygamma tools to justify any leading-weight
   substitution with a uniform remainder on this fixed strip. Control
   that remainder by L407's complete absolute divisor bound, rather
   than asserting that bounded variation alone determines a limit.
   Keep all Omega' contributions until their scale is justified.
4. Assembling every nu and (m,n,k), including the exact T resonances,
   r^(-1/2), 2pi, c^3, ordinary-jet signs and final real projection.
   A zero coefficient is admissible. Any cancellation must be checked
   before identifying a lower signed scale, which is outside TARGET.

These are application obligations for the later research turn, not
results proved here. A direct finite-Hurwitz/Mellin specialization is
justified because it avoids an inconsistent polar-factor display and
keeps the local logarithmic jets, weights and endpoints explicit.
There is no reason to reprove the source's full functional equation
or full Voronoi theorem. The choice of a smooth-first endpoint argument
is a proposed test, not a substitute for its eventual estimates.

### Decision and continuation test

SPECIALIZE approves the exact TARGET for one mathematical attempt with
fixed N. The strongest imported input is the shifted rational-twist
Dirichlet-series representation, not the full local statistic. No source
theorem states the complete signed coefficient; no originality is claimed.
Full matching Mathlib coverage remains unchecked, as do implementations
of this weighted endpoint specialization; unknown coverage is not absence.

Continue if every differentiated polar contribution, analytic-weight
remainder and sharp boundary term has a proved total o(H(log H)^2)
error and the complete signed coefficient is retained. Stop the claimed
asymptotic if any such error remains uncontrolled; record that precise
obligation instead of importing the unproved cubic moment or treating
a smooth preview as proof. A coefficient equal to zero settles this
scale only. Full-response passage, clipping, regulator choice, total
L367 margin/remainder, actual common-zero upper counts and global mixed
positivity remain independent gaps. No RH candidate is obtained.
