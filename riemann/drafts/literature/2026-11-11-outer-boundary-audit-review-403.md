# Nomination for conceptual audit of the outer boundary obstruction

TARGET: Critically audit C999c's bilinear boundary certificate, endpoint contour deformation, unique-saddle asymptotic and universal capped two-window obstruction.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step404 reuses review400's bounded discovery and review401/step402's source approval; read the full C999c proof, C997c(4)-(6), C997s hypotheses, C997x/y/z conclusions and spectral-tail341. No changed approximation target or new discovery claim; this separate audit comparison finds no essential uncovered tool.
SOURCE_EVIDENCE: Directly retrieved 2026-11-11: Baratchart-Leblond-Seyfert, author manuscript 22 March 2017, Section3 (2)-(7), printed pp2-4, Theorem1 proof (15), p6, https://www-sop.inria.fr/members/Juliette.Leblond/Papiers/BLSFields2017.pdf ; NIST DLMF 2.4(iii) assumptions (a)-(c), (2.4.11)-(2.4.13), and 2.4(iv) (2.4.14)-(2.4.16) including branch paragraph, https://dlmf.nist.gov/2.4 . Live release number not independently checked; Olver book not directly retrieved.
COMPARISON: Source contracts cover the Hardy/outer construction and fixed simple-saddle expansion, conditionally on verified local hypotheses. They do not certify C999c branch calculations, deformation, saddle dominance, noncancellation or coefficient-uniform rate. Review400 fixed-data convergence and C997x/y/z or stop341 do not settle this obstruction.
GAP: Source coverage is adequate for the exact conceptual audit; mathematical correctness of C999c remains unaudited. Every local analytic hypothesis and the Delta_n-only implication must be checked next; no E_n lower bound or actual-Xi transfer is supplied.
REASON: Separate step404 approves auditing the existing proof using inspected contracts, without validating its conclusion or deriving new mathematics. EXPLORE describes the local proof audit, not novelty certification. No further source gate is needed while this exact scope remains unchanged.
SCOPE: C999c's single pair lambda=1/4, eta=0, fixed arc7/16<theta<9/16, original n>=64 and complex coefficient cap exp(sqrt(n)); only the stronger two-window sufficient objective, with C997c's exact T_U and T_L.

The main unresolved RH input remains L030-L032/C032a actual-Xi
positivity, L966/L968 forcing and unpaid L984(H). The audit's downstream
purpose is to determine whether the capped Delta_n construction is
rigorously excluded, directing any later bridge work toward integrated
cancellation. It does not seek or presume an obstruction to C997s's E_n.

Essential local mathematical inputs are C997c(4)-(6), C997s's original
hypotheses and the full proposed C999c proof. C997x/y/z and stop341 are
scope comparisons only. No cross-notebook result is involved.

After separate coverage approval, check in particular the sign in
H_J(exp(iz))=-i L(z)/pi; the factor y and bilinear circle normalization;
product membership and endpoint boundary limits; exact cap-to-circle
conversion; existence and location of the fixed upper saddle; the
concavity argument proving Q'>0 on its entire interval; every corner
limit and both vertical integrals; and DLMF's analytic, compact-gap,
simple-saddle, amplitude and square-root hypotheses. Check that the
leading term is nonzero and the remainder is smaller in modulus,
rather than merely deriving a favorable absolute upper bound.

The decisive comparison is the proposed uniform lower bound
Delta_n>=C(n+2)n^(-1/2)exp((1/32+5v/6)n), with v fixed and positive,
against a single unspecified big-O constant times exp(-n/64). Verify
that the constants and eventual onset do not depend on the capped
polynomial and that the fixed spectral arc lies in the original closed
upper window. Success accepts only this sufficient-objective stop;
failure must preserve the proof and identify the exact invalid step,
its repair requirements and how far the claim must be restricted.

Capped E_n, C997a(8), selected/both-sign transfer, assay/reconstruction,
complements/regulators, L993, L984(H), L966/L968 forcing and Xi signs
remain unresolved. Full matching Mathlib coverage is unknown/unchecked.
The mathematical audit has proof_audit/conceptual_audit purpose because
the branch, boundary-limit and noncancellation issues are analytic,
not a routine numerical replay. The next invocation must first resolve
this new REVIEW_REQUIRED source gate; no independent audit is claimed
in step403 and no runtime scheduling state is edited here.

## Separate source approval — step404, 11 November 2026

This section supersedes the nomination's pending-gate statements above.
The exact TARGET is now source-approved for a later conceptual audit.
This literature-only step neither performs that audit nor changes C999c.

Reused bounded discovery queries and comparisons in review400 and the
separate approval in review401; no repeated general search was needed.
The full proposed proof was read to identify its actual external tools.
C997x stops a prescribed family, C997y a scalar propagation mechanism,
C997z an exact functional norm target; spectral-tail341 is inconclusive.
None is an all-polynomial two-window obstruction or an integrated E_n
obstruction. Their canonical evidence and qualifications are preserved.

### Inspected contracts and audit obligations

[BLS manuscript](https://www-sop.inria.fr/members/Juliette.Leblond/Papiers/BLSFields2017.pdf),
Section3 (2)-(7), pp2-4, supplies finite-p Hardy boundary convergence,
Cauchy representation and the outer construction for positive rho with
integrable log rho; H^p membership requires rho in L^p. Theorem1 proof
(15), p6, explicitly exponentiates an indicator's Herglotz transform.
These permit step boundary data, without endpoint continuity. The next
audit must distinguish bilinear dtheta integration from the source's
sesquilinear pairing and Cauchy line integral. No extremal-rate theorem
is imported; review400's fixed-data comparison remains adequate.

[DLMF 2.4(iii)-(iv)](https://dlmf.nist.gov/2.4), read through the paragraph
after (2.4.16), requires analytic phase/amplitude along the path,
appropriate local expansions, absolute uniform endpoint convergence,
and a strict real-part minimum with an endpoint gap. Equation (2.4.14)
splits at the interior saddle. A simple saddle yields (2.4.15), with
b_0=q/sqrt(2p'') and branch |theta+2omega+arg p''|<=pi/2, omega taken
toward b. A steepest descent path is unnecessary. The auditor must
verify these hypotheses for the proposed p=-Phi and q=exp(iz), rather
than assume a maximum of the modulus suffices. Olver pp121-127 is a
source reference, not a separately inspected proof.

The local proof, not these contracts, must pay logarithm branches,
corner limits and vertical pieces, verify its saddle and global gap,
and obtain a nonzero leading term dominating leakage uniformly in the
capped polynomial. These are the unchanged audit obligations above.
No source blocker remains for this audit; a genuinely additional tool
would require its own review before use. Full matching Mathlib coverage
remains unchecked. No new lemma, mathematical script, rate, or RH input
was produced. Outcome STALLED records source-gate completion honestly;
it does not reset mathematical exploration or claim a new discovery.
