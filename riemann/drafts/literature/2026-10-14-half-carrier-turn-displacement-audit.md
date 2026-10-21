# Half-carrier-turn displacement critical-audit coverage

TARGET: Critically audit L412's half-carrier-turn fourth-displacement asymptotic, including moving-shift transfer, Hardy phase factors and the complete five-term coefficient.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the unchanged exact/stronger-statement searches and duplicate/failure comparison in 2026-10-14-half-carrier-turn-displacement.md; narrowly read L412, its step-130 draft/history/stop and step-129 history. No completed separate L412 audit is recorded in those files; no new broad search or novelty inference.
SOURCE_EVIDENCE: Directly rechecked Bui--Hall arXiv:2304.05178v1 (11 April 2023), Hardy definition, Theorem 3 and preceding asymptotic, Section 4.2 Proposition 3, Section 4.1 (17)--(20), Section 5 Cauchy passage and complete Section 7 deduction; reused the prior Hughes--Young Theorem 1.1 comparison, without a new retrieval. Read L389's (2)--(3) and L390's gamma-phase input for scope.
COMPARISON: Sharp constant complex shifts bounded by C/log H, including coincident shifts, and fixed ordinary Hardy orders zero and one cover every requested source input. The phase-defined moving shift, all five carrier factors and coefficient remain local specialization claims to audit; no new moment theorem, sign symmetry or growing parameter is needed.
GAP: Source coverage is ready; independent verification of L412's moving-shift FTC/Fubini estimate, exact reflection/orientations, absolute phase-error budget and all five source-integral evaluations remains outstanding. Coverage approval does not certify the asymptotic or clipped pairing.
REASON: This separate literature comparison approves only the saved critical-audit scope using adequate primary coverage; no mathematical audit, coefficient derivation or lemma/script change is performed here.
SCOPE: Only L412's fixed actual f=F_0/A, gamma phase of Q, implicit positive half-turn shift and sharp [H,2H] fourth displacement for all sufficiently large real H; ordinary orders zero and one, bounded constant complex shifts, no RH or new zero/sign assumption.

The exact statement to audit is L412's asymptotic with coefficient
(pi^2-3)/pi^4 and O((log H)^3) error, on the original sharp [H,2H]
interval and for the phase of Q. Its mathematical premises are L389's
zero-safe Hardy identification and ordinary moments and L390's gamma
phase bounds. The audit must check the rectangular FTC/Fubini argument
rather than a moving-supremum bound, the (-1)^k factors in all five
monomials, and the imported constant-small-complex-shift formula.

## Separate source-scope approval — 2026-10-14, step 131

LITERATURE_REASON: The newly proposed L412 critical audit needs separate scope approval; reuse the ready scalar assessment and recheck its primary theorem rather than start a different displacement calculation or repeat discovery.

This section completes the approval left pending above. The main gap is
global actual-theta mixed positivity; the actual negative-Bcal clipped
signed mean is also unresolved. The intermediate target is a reliable
audit of the recorded scalar obstruction. Its downstream use is to
decide whether the scalar-small-displacement implementation should stay
stopped, without attributing a clipped-sign consequence to that stop.

### Primary input and limits

H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1](https://arxiv.org/html/2304.05178v1#S4.SS2),
11 April 2023, Section 4.2 Proposition 3, states a sharp [T,2T]
two-positive-height/two-negative-height zeta integral for constant
complex shifts O(1/log T), uniformly, with error O(T log^3 T).
Its four-dimensional main integral has prefactor T log^4 T/(2 zeta(2));
the full expression permits coincident shifts. Its proof is omitted,
with the preceding derivation cited as the method. Section 4.1
(17)--(20), including (19) and the final factorization, was inspected
as supporting cancellation evidence, not as a separate proof of
Proposition 3. The Hardy definition, Theorem 3 and its defining
asymptotic cover fixed ordinary orders, with one lower logarithmic
degree in the remainder. Section 5 explains uniform Cauchy transfer;
Section 7 retains the negative-height derivative signs and completes
the fourth-product deduction. None of these statements supplies a
height-dependent shift or actual sign symmetry.

Reuse the supporting Hughes--Young Theorem 1.1 comparison in
[the scalar assessment](2026-10-14-half-carrier-turn-displacement.md).
That smooth-weight theorem need not replace the directly available
sharp formula. It was not newly retrieved in this turn. No reproof of
either known moment theorem is justified. Full matching Mathlib
coverage remains not checked; elementary integration and inequality
support would not replace the analytic input.

### Exact application obligations for the next research turn

The full L412 proof was read to identify its demands, not to certify
its derivation. Its five rows request only constants 0, ih and -ih
with h=2pi/log H, within the fixed-C complex-shift scope. Its absolute
envelopes request ordinary orders zero and one, already imported in
L389 (2). The zero-safe constant Hardy branch sign in L389 (3) and
the separate phase bounds in L390 are the essential local inputs.
No higher moment, enlarged shift regime, twisted carrier theorem,
response head limit or endpoint smoothing theorem is requested.

The mathematical audit must check the actual phase of Q, uniqueness
and measurability of the implicit shift, the uniform shift comparison,
and the fixed enclosing FTC/Fubini strip. It must retain the exact
two-orientation reflection at critical zeros, verify every row's
carrier exponent and its absolute replacement error, and recompute
each finite integral and the complete binomial combination. Restriction
of nonnegative cumulative moments to the enlarged interval must be
justified; a moving supremum or signed endpoint change is not licensed.
The claimed coefficient and O(log^3 H) error are hypotheses of this
audit target, not results established in this approval.

Continue accepting the local scalar stop only if these checks reproduce
the claimed positive coefficient with the complete error for every
sufficiently large real H. A missing phase, nonuniform bound, endpoint
case or different coefficient requires a specific repair and withholding
the affected conclusion; it does not establish small displacement or
disprove RH. Coverage is adequate for this independently testable audit.

### Duplicates, failures and continuation

The exact duplicate is L412 itself, whose verification is explicitly
requested. Step 130 and its stop record leave that verification pending;
step 129 approves only the calculation's source scope. Reuse that
assessment's comparison with L383 and the recorded step-99 sign-symmetry
failure. L383 concerns a different cell correlation, not this fourth
displacement. Preserve L394/L399/L400 and L410's independent obstructions;
none excludes an audit or rules out every other pairing.

Essential direct input IDs are L389 and L390; L383 is precedent, while
L411/L405 motivate downstream use only. The scalar stop remains pending
mathematical audit. The clipped mean, regulator scale, total L367
margin/remainder, common-zero upper counts and global positivity remain
unproved. No new mathematical result, canonical dependency or main
argument changes in this literature-only step.
