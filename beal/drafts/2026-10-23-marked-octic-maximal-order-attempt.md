# Approved maximal-order calculation working record

Target: Determine and certify a maximal-order basis and field discriminant for L115's degree-eight field.

The ready assessment is `drafts/literature/2026-10-22-marked-octic-maximal-order.md` (SPECIALIZE). This is one RESEARCH/REPRODUCTION implementation attempt. Essential inputs are audited L115's entire field and L114's polynomial discriminant; the original marked interpretation stays in L113. No other notebook is used.

The main gap remains rational-point control and subsequent integer lifting. The intermediate threshold is a full maximal-ring basis, exact signed field discriminant and independent arithmetic replay. This could support later supported class/unit computations, but does not perform them or remove any point. Known infinity points prevent an empty fake-Selmer shortcut. ATTEMPTS/050–051 and unfinished L108 are preserved.

Plan saved before implementation: use the cited nonmonic equation order with basis 1,T_1,...,T_7 inside Q[t]/(F). For each possible index prime compute the complete Frobenius kernel in A/pA, its inverse-image lattice I, and the joint kernel of A/pA acting on I/pI. Recover the multiplier overorder from that second kernel, and verify full lattices and closure exactly. Repeat within floor(v_p(disc(initial))/2) strict steps. Independently reconstruct the arithmetic, kernel completeness and inclusions from the saved evidence. No trace-radical substitution or polynomial-order maximality assumption is permitted.

Continue only if all initial index primes are covered and final stability, trace determinant and replay pass; otherwise preserve exact failures and park an infeasible implementation. Supported square classes, class two-torsion, local images, rational-point completeness, degree-nine root recovery, remaining factors, both L095 systems and minus-eleven remain independent unresolved assumptions.

Completed: [L116](../lemmas/L116-marked-octic-maximal-order.md) records the entire basis, full proof/citations and reproduction commands. The exact all-prime method succeeds with 15 strict steps, final multiplier ranks (8,8,8,8), and signed discriminant 2^8*3^7*5^4*11^7. Independent arithmetic replay reconstructs all 16 orders and 23 radical/multiplier checks; all 1,331 comparisons pass, no failures. The canonical basis and Gram matrix were also checked entry by entry against the certificate. This is REPRODUCTION, not new general mathematics or point control. The proposed critical audit receives REVIEW_REQUIRED for separate approval; no further target is attempted.
