# Reverse connecting-class representation attempt

2026-10-26, step 513. RESEARCH under the pre-existing SPECIALIZE
assessment `literature/2026-10-26-reverse-isogeny-quartic-class-representation.md`.
The exact target is the current checkpoint's quartic coefficient
representability question; no independent descent computation is authorized.

The main gap is residual-system point control, with the existing genus-two
rank bound at most nine versus the sufficient bound one. The intermediate
target is an exact interface for the reverse connecting map, potentially
usable on separately retained quotient classes. Continue on a verified
representation formula or a specific applicable Brauer obstruction; stop
an affirmative proof at a failed map or rational-cycle hypothesis.
Representation alone is not an additional exclusion.

Starting inputs: audited L142 and L127, L110/L111/L113's actual curves,
maps and origins, and L138's quartic transport. Reuse the assessed
Bruin–Poonen–Stoll coefficient sequence and fake-descent comparison.
ATTEMPTS/062 stops only the exact same-T shortcut. Existing unfinished
work, especially L108, is preserved; no cross-notebook input is used.

Checkpoint before detailed proof: test the factorwise functorial diagram
δ_G = F_* δ_2 on Jac(B)×E. Both curves have rational basepoints, so
rational degree-zero divisor representatives may supply the coefficient
classes. For each factor the proposed fake datum is β_i equal to its
quartic branch point, D its T-infinity fiber, and f_i=T−θ_i. The key
unverified comparison is between the Cartier-dual branch-difference map
and L142's actual maps on two-torsion. This route would avoid assuming a
polarization identification of the transported Prym. Check all these
claims, scalar quotients and exceptional evaluations before asserting
representability. No conclusion is yet recorded here.

## Completed attempt

The full proof is canonical in
[L143](../lemmas/L143-reverse-isogeny-quartic-class-representation.md).
The target is affirmative: δ_G(x,e) is the coefficient injection of
λ_B(x)λ_E(e) for every rational target pair. The product datum is
explicit, rational cycles cover the entire target, and the finite
branch pairing identifies the map with F on A[2]. Its cocycle
comparison then identifies the actual δ_G. The coefficient boundary
vanishes on these classes; no claim about all H¹ is needed.

The proof also checks the scalar transport from L138's odd quartic
component and moving conventions for exceptional divisors. The old
same-T test remains redundant, since its two factors are identical.
No numerical computation, global class enumeration or new rank bound
was attempted. The achieved interface falls short of a nonredundant
mixed filter, and the main point/integer-control gap remains.

Outcome ADVANCE / REPRODUCTION: a relevant instance of the assessed
general theory is established, not a new general descent result.
The exact finite divisor/module/cocycle verification is in L143;
there is no mathematical script or numerical certificate. The new
input requires a separate conceptual audit. Its next assessment
reuses the same sources and is newly ready, subject to the supervisor's
separate approval. No new mathematical mechanism is approved here.
