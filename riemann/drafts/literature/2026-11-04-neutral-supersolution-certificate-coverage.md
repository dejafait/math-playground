# Fixed neutral-window sine supersolution: source comparison

TARGET: Assess whether the positive sine profile h(x)=sin(pi*x/(9log3)) yields an applicable ground-state supersolution certificate for L744(6) on the exact two-moment neutral subspace, retaining every prime-power shift.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the October30 nodal and weighted-localization assessments and slope-gap stop; searched prescribed-reference nonlocal Hardy identities, jump-measure ground-state transforms, and exact Weil/sine/supersolution terms. Read the primary statements and proof cases below; no inspected theorem evaluates this sine residual or supplies a constrained sign certificate.
SOURCE_EVIDENCE: Frank-Seiringer 0803.0503v2 Assumption2.1, Props2.2-2.3, Remarks2.4/2.8 and p=2 proof cases pp5-6,8-11; Frank-Lenz-Wingert 1012.5050v1 Sections2/9, Def3.2, Thms10.1-10.2 and Cor10.4 with proofs pp19-21; refreshed teal-sea b09fa4dd Sections2.6/6. Reused Chen-Weth pure-log scope and L740/L744 normalization; precise citations below.
COMPARISON: The prescribed-positive-reference identity is known, including nonnegative jump measures at the general-form level. A continuum translation atom is not a product-Lebesgue kernel, and the inverse-domain/eigenfunction theorem is not an automatic sine certificate. Use the p=2 domain identity and finite graph identity, retaining killing and scalar terms; the residual sign is a separate test, not a sourced conclusion.
GAP: Carry out the routine complete-form specialization and test the defined pole-free residual at the midpoint; no residual sign, all-interior bound, constrained spectral gap, unrestricted-support positivity or Xi sign has been established.
REASON: Essential source scope is now covered sufficiently for one later standard-mechanism specialization and midpoint obstruction test. No new representation or residual evaluation is proved in this literature turn; no generic-transform discovery is claimed.
SCOPE: One later p=2 specialization for smooth compactly supported complex tests with both exponential moments exactly zero, L=9log3 and the fixed positive interior sine extended by zero; all prime powers, adjoints and exterior terms retained. No full-form contraction, positive unknown ground state, RH or positive complement premise. The covered calculation includes proving the required finiteness and matching the residual to L744(6), not assuming them.
LITERATURE_REASON: Invocation-start coverage was REVIEW_REQUIRED for the changed full-delay prescribed-reference target; the old pure-log/nodal assessment could be reused only in its recorded scope. This turn reads the missing primary cases rather than repeating that stopped slope test.
COVERED_TARGET: Specialize the sourced p=2 ground-state identity for h(x)=sin(pi*x/(9log3)) to L744(6) and rigorously test its complete pole-free residual at x=(9log3)/2, retaining every prime-power shift and zero-extension boundary term.

## Invocation-start nomination and stopping conditions

The following paragraphs preserve the original nomination. Their
prospective source requirements are resolved only to the extent stated
in the completed comparison below; they assert no favourable sign.

The main gap remains unconditional actual-Xi positivity, with complete
neutral Weil signs on unrestricted support independently open. The
intermediate prospect is one explicit lower certificate at L=9log3.
Even a successful certificate leaves all other lengths, the nonneutral
complement, uniform iteration and Xi mixed signs unresolved. It need
not establish an 8log3 positivity seed to be useful as an independent
fixed-window input; neither seed nor extension is assumed here.

Use L740's actual domain and L744(6)'s complete smooth energy. L741
supplies normalization only, not a sign theorem at this length. For
neutral tests both exponential moments vanish exactly, and the pole
term vanishes by those constraints. Every prime-power shift with
log(n)<L and its adjoint must remain. A reference function need not
lie in the neutral subspace: distinguish that fact from permission to
replace the neutral operator or to apply a lattice theorem there.

First reuse the precise prior comparison and
`ATTEMPTS/2026-10-30-weil-nodal-compression-slope-gap.md`. The earlier
failure concerned derivative correlations from static nodal overlaps;
this nomination does not repeat that implication. Its warning about
full-form modulus contraction and its recorded overlap with the
pole-free ground-state transform still apply. Also retain L749's
failed direct resource payment and L750's fixed localization defect
as contrasts. Neither failure says this reference residual has any
particular sign. No such residual is evaluated in step318.

Retrieve a primary ground-state/supersolution theorem with its exact
kernel, measure, domain, zero-extension and boundary hypotheses before
reading larger sections. Compare the stronger recorded transform first.
If it already gives the representation, cite it and assess only the
missing complete residual specialization. No reproof to claim novelty.
An exact form identity alone is not a favourable residual bound.

Continuation test: approve one later mathematical test only if the
source comparison supplies a well-defined residual for this exact h
and complete form, with all endpoint/remainder/finite-delay terms paid,
and a sufficient pointwise lower threshold of zero (or a precisely
sourced weaker constrained condition). A rigorous negative residual
at a specified interior point can decisively reject the simple
pointwise-supersolution test, without rejecting neutral positivity.
Do not divide by h at its zero endpoints or assume h is an eigenvector.
If the method requires a positive full ground state, full-form modulus
contraction, an unknown positive complement, or merely restates the
missing energy sign, park this implementation. Do not enlarge the
profile family or repeat a ground-state-identity turn without new input.

This was a proposal for source review, not a new supersolution theorem,
representation, sign prediction or creative proof authorization. Full
matching Mathlib coverage is unchecked. No justified creative proof
target has yet emerged: the independent signed residual and its domain
are the missing evidence. If a genuinely different sign mechanism is
found, give it its own source gate and a bounded creative test; a
routine specialization of a known transform is REPRODUCTION.

## Completed comparison, step319

### Primary theorem scope

[Frank and Seiringer, *Non-linear ground state representations and
sharp Hardy inequalities*, arXiv:0803.0503v2, 14 November2008](https://arxiv.org/pdf/0803.0503v2),
Assumption2.1 and Propositions2.2-2.3, pp5-6, use a positive measurable
reference, symmetric nonnegative kernels, dominated regularizations,
locally weak-L1 potential convergence and finite indicated energies.
At p=2 the remainder formula (2.5) is an equality. Remark2.4 permits
domains and weighted graphs; Remark2.8 localizes potential convergence
to the test support. Read the complex p=2 scalar case of Lemma2.6,
the symmetrization (2.17), limit (2.19), and the authors' abbreviated
Proposition2.3 proof, pp8-11. The result is a prescribed-reference
identity, not an assumption that the reference is an unknown positive
ground state. It does not evaluate a residual or eliminate boundary
killing. The continuum atom issue needs explicit specialization.

[Frank, Lenz and Wingert, *Intrinsic metrics for non-local symmetric
Dirichlet forms and applications to spectral theory*,
arXiv:1012.5050v1, 22 December2010](https://arxiv.org/pdf/1012.5050v1),
Section2, allows a symmetric Radon jump measure off the diagonal.
Sections9-10, pp19-21, require a regular Dirichlet form,
nu^+ in M0, nu^- in M1 (relative form bound below one), and a
generalized eigenfunction. Definition3.2's Dloc* condition includes
the full K-times-X jump integral. Theorem10.1 requires the inverse
in Dloc*; Corollary10.4 also requires local boundedness of the
inverse. Local positivity alone does not discharge this nonlocal
condition. Theorem10.2 avoids an inverse hypothesis by retaining
compact product-domain tests. Read both complete Leibniz-rule proofs
and the corollary proof. These results cover singular jump measures,
but an arbitrary sine has not been shown to satisfy their eigenfunction
and measure-perturbation hypotheses. They are not a direct sign import.

The previously assessed [Chen-Weth v6](https://arxiv.org/pdf/1710.03416v6)
Proposition3.2/Lemma3.3, p13, concerns the pure logarithmic Laplacian;
its boundary potential and modulus comparison do not identify this
digamma-plus-prime residual. Reuse that scope exclusion. No reproof
of any of these standard identities is warranted.

### Overlap and normalization

The [teal-sea theory notes](https://zeta.teal-sea.com/read/hunts/weil_propagation/theory/RESULTS.html)
now report compilation02 Nov2026, revision b09fa4dd. Read Section2.6's
complete jump-form identity and scalar C_ell and Section6's transform
and comparison failure. They already include the digamma density
K(u)=2exp(-u/2)/(1-exp(-2u)) and both prime-power jumps with weights
Lambda(n)/sqrt(n). Their transform uses an actual positive pole-free
ground state and leaves a spectral gap estimate unpaid. The notes
grade the argument ordinary/unreviewed; no measured bound, simplicity
claim, propagation theorem or novelty assertion is imported. This
is an overlap, not the sought sign input. The source explicitly
retains killing at jumps outside the interval. A comparison that
silently replaces a killed form by its regional part would change
the target.

Use the audited canonical L740 domain and L744(6), with L741's scalar
normalization only. The complete neutral quadratic form is the
restriction of the pole-free form Q0(f)=<m(D)f,f>-<B_Lf,f> to
M_+(f)=M_-(f)=0. This is precisely L744(6)-(7); no pole-free sign
theorem is assumed. L749's failed resource payment and L750's
negative corrected-localization defect remain distinct failures.

### Exact residual to test; no evaluation in this turn

Let I=(0,L), L=9log3, let h be the prescribed sine on I, and let
htilde denote its zero extension. Define the candidate residual
using the already fixed operators, without an asymptotic replacement:

    H0 h = (m(D) htilde)|_I - B_L h,
    m(t)=Re psi(1/4+it/2)-log pi,
    (B_L h)(x)=sum_(2<=n<exp L) Lambda(n)/sqrt(n)
                    *[htilde(x-log n)+htilde(x+log n)],
    R_h(x)=(H0 h)(x)/h(x),                 0<x<L.          (S)

(S) defines the proposed test quantity, not a claimed new ground-state
formula. The continuous operator means the full Fourier multiplier
on the zero extension, not a regional integral on I. It thereby
includes the exterior killing and the complete scalar normalization.
The finite sum includes all prime powers; a delay equal to L has
zero overlap. No scalar compensation from a difference-kernel
rewriting may be lost. A future kernel computation must match (S).

The source-applicability route is specific. Use Frank-Seiringer's
p=2 identity on the open domain for the continuous positive
difference kernel, keep its multiplication/killing term, and apply
the same source's two-vertex weighted-graph identity to each finite
translation edge before integrating its position. A translation
atom is not being treated as a density in dxdy. This is a routine
specialization obligation, not a new theorem announced here.
For each compactly supported smooth test f, f/h has compact support
inside I. Thus only interior quotients enter these tests. Verify the
continuous cutoff limit and every edge integral there; no inverse
condition at the zero endpoints is presumed. The htilde used in
(S) is compactly supported and piecewise smooth with zero endpoint
values. Standard Fourier integration by parts and L744(8)'s
logarithmic multiplier bound give the direct route to defining its
interior multiplier by an absolutely convergent Fourier integral;
check that matching explicitly in the specialization. This avoids
any need to apply Theorem10.1 to an unverified inverse-domain vector.

At the general identity's level the sufficient threshold is R_h>=0
throughout I: the transformed remainder has nonnegative weights.
The later specialization must establish that statement for Q0
with the exact boundary terms before using it for neutral f.
No positive full-form reference, lattice structure of the neutral
space, or positive nonneutral complement is required by this route.
The reference h need not itself be neutral; the pole is removed
because the tested f is neutral, not by asserting its value on h.
For complex tests retain the modulus-square p=2 identity.

Only one bounded test is covered next: match that identity and (S),
then rigorously enclose R_h(L/2) against zero. No value has been
computed, predicted as a theorem, or enclosed here. A strictly
negative upper bound rejects this sine as a pointwise supersolution,
without rejecting neutral positivity. A nonnegative midpoint value
alone is not a certificate and leaves the rest of I unchecked;
an enclosure crossing zero is inconclusive. Endpoint quotients and
new profile families are outside this test. Preserve any derivation
and use new evidence before reopening an unsuccessful implementation.

The source identities are known and their local application is
REPRODUCTION. The literature comparison supplies coverage for this
bounded calculation, not new mathematics or a claim of novelty.
There is no justified creative target yet: an independent signed
residual or a different arithmetic sign mechanism is still missing.
One fixed-window success would still leave other windows, support
iteration and actual-Xi mixed signs unresolved. No RH candidate.

### Search and access record

Queries on04 Nov2026 included `Frank Seiringer non-linear ground
state representations Proposition2.3 positive kernel supersolution
measure`, `nonlocal ground state representation jump measure
supersolution positive function Hardy inequality`, `Frank Lenz Wingert
intrinsic metrics non-local Dirichlet forms ground state transformation`,
`Weil supersolution sine zeta`, and `Weil ground state sin positivity
interval`. The exact-target searches gave window-spectrum and
heuristic ground-state leads, not an inspected matching sine theorem.
Those leads are unread and are not used for a sign or novelty claim.
The primary results just cited supply the representation comparison.

Frank-Lenz-Wingert's guessed v2 URL returned404; v1 was read.
Fitzsimmons' author-hosted Hardy PDF failed with502/timeouts; its
search result is an unused lead, not evidence for a theorem. It is
not essential once the domain p=2 and finite-graph route above is
used. No source blocker is carried forward and no further access
loop is proposed. No cross-notebook result was read or imported.
Full matching Mathlib coverage remains unchecked; the sources checked
here do not establish its absence.
