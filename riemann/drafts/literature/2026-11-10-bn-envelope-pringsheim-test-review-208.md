# Actual-b_m Pringsheim application — source coverage approved

TARGET: Test whether Pringsheim's theorem rules out L975's every-delta actual-b_m lower envelope by a positive-coefficient correction, allowing all zero multiplicities and finite exceptional prefixes.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed step208 exact actual-b_m/Pringsheim comparison in 2026-11-10-bn-envelope-singularity-compatibility-review-207.md; exact coefficient, stronger-result, duplicate and failure searches found no inspected matching actual-xi obstruction theorem. No novelty claim.
SOURCE_EVIDENCE: Flajolet-Sedgewick, Complex Asymptotics, zeroth edition 8May2004, TheoremIV.3(i)-(ii) and complete proof pp15-16/PDF23-24, https://algo.inria.fr/flajolet/Publications/ch4567.pdf#page=23 ; analytic tools https://dlmf.nist.gov/1.10.i , https://dlmf.nist.gov/1.10.ii , https://dlmf.nist.gov/1.9.vi (1.9.53-57); unconditional zero existence/symmetry https://dlmf.nist.gov/25.10.i ; direct passages rechecked 2026-11-10 in step209. Local L013/L018/L021/L024/L026/L975 applicability and downstream-only L968 reuse step208; no additional theorem is imported.
COMPARISON: The known positive-coefficient boundary theorem and local analytic tools cover the method; actual coefficient correction, radius, logarithmic singularity and branch verification are the identified specialization. None is proved by this nomination or supplied as a premise.
GAP: Determine whether the corrected germ can have nonnegative coefficients, a finite radius strictly less than its correction's radius, and analytic continuation across its own positive-radius point; verify or reject every condition for actual xi without RH.
REASON: Test the feasibility of L975's sufficient hypothesis before investing in payment; this is a bounded established-tool specialization, preserving all prior stops. Separate literature approval completed in step209 with direct source URLs; no mathematical invocation in that turn.
SCOPE: Only the exact actual-b_m hypothesis H in L975 and its eventual-prefix variant. No claim about a weakened envelope, cancellation-sensitive replacement, necessity for RH, Coffey's conditional asymptotic, or a new central mechanism is preapproved. No RH, simple zeros, radius2, coefficient positivity or removable logarithmic zero is assumed.

## Bounded mathematical test, not a completed derivation

Use w=z+1 and the actual germ G(w)=F(w-1) from L975. Determine its
maximal Taylor radius using unconditional xi data, with a separate
argument for the nonremovability of a zero singularity. Establish the
needed strict comparison with 2, rather than assume it from a plot or
the inner map's pole. A known zero and L018's symmetry are permitted
inputs; DLMF25.10(i) supplies unconditional existence. Alternatively,
L021's nonconstancy data and L024's product are available for a local
existence argument, which has not been performed here.

Under the hypothetical envelope, test the candidate correction
G(w)+C/(1-w/a), where a=2-delta, with constant/prefix adjustments if
needed. Verify its coefficients and exact radius before invoking
Pringsheim. In particular, establish that adding this correction does
not remove the relevant singularities; do not infer its radius merely
from the upper bound supplied by Taylor's theorem. These instructions
nominate a calculation and analytic argument; they assert no result.

Check continuation of the original logarithm along the positive real
segment to the radius point using L013/L018 (or L021 positivity), and
show agreement with the corrected Taylor germ on overlaps. Track all
multiplicities and logarithm constants. A finite exceptional prefix
must be accounted for explicitly. No global branch around zeros or
unjustified zero-sum exchange is allowed.

Continue to an obstruction conclusion only if every hypothesis of
the inspected theorem is verified. Otherwise identify the precise
failed condition and preserve the unfinished reasoning. Stop this
test after that bounded application; do not branch into a replacement
coefficient mechanism or a reproof of Pringsheim. A proved failure of
H would stop that payment route and leave L975's conditional inverse
and RH intact. Nothing in this source preparation proves failure.

Import the named theorem by the direct citation in the completed
assessment. Reproof is unnecessary. The actual-xi application needs
proof because the source theorem does not identify this signed germ,
its radius or its branch. Expected research classification is
REPRODUCTION, with no claimed advance beyond the sources checked.

The main gap is L030-L032/C032a positivity, including L966's unpaid
signed inequality. L968 supplies the downstream Li criterion but is
not a premise for a coefficient-sign obstruction. A useful result
here would prevent pursuit of an inadmissible sufficient hypothesis;
it would not resolve the independent positivity gap. Full Mathlib
coverage is unknown and no Mathlib theorem is imported.

## Step209 source-link recovery and separate approval

On 2026-11-10 the direct PDF and DLMF URLs in SOURCE_EVIDENCE
were opened successfully. Rechecked Theorem IV.3 and its two proof
cases on printed pp.15-16: the general boundary argument uses
Cauchy bounds; the positive-coefficient case recenters and reorders
nonnegative terms to force convergence beyond the supposed radius.
This confirms the prior comparison, rather than establishing a new
application. The theorem is imported by citation; no reproof is needed.

Rechecked DLMF 1.10(i) zero multiplicity, 1.10(ii) continuation,
1.9.53-57 local reciprocal/logarithm expansions and 25.10(i)
unconditional strip-zero existence and symmetry. The logarithm
expansion is local and normalized; it supplies no global branch.
The continuation statement must be used on connected overlaps.
No zero multiplicity restriction or RH assumption is added.

Reuse the completed exact-target searches, duplicate/failure comparison
and local input inspection in the step208 source comparison. No new
search for unchanged coverage is needed. Ready SPECIALIZE coverage
now applies to the unchanged TARGET, with expected REPRODUCTION
classification. Exact radius, nonremovability, branch agreement,
coefficient signs and finite-prefix adjustments remain research
obligations. No obstruction or coefficient bound has been proved.
Full Mathlib coverage remains unknown; no Mathlib result is imported.
