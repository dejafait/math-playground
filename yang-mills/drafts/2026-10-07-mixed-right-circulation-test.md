# Retained mixed right-circulation test

STEP_ID: YM-20261007-081-mixed-right-circulation-test

Reuse the supplied SPECIALIZE assessment
`literature/2026-09-26-current-target.md` for its unchanged full response
target. The immediate gap is L064's retained K_1 path/path subgroup.
Test its right plaquette circulation and L061's fractional cross bound
jointly, with the actual smooth probe paths and rough mixed residual.
The threshold is O(N²), or an exact reduction to a quantitatively
smaller subgroup. Such a bound would exclude stronger powers in this
part of the complete mixed response. The first pair, the other four
endpoint monomials, the scaled limit, and the full logarithm remain
independent requirements.

Inputs inspected: L061–L064, ATTEMPTS/019 and history/080.
L061–L063 supply the full curvature reduction and five subleading
placements; L064 already supplies the left pinned endpoint cancellation.
Do not repeat that result or the stopped generic absolute-array norm
closure. Do not delete differentiated base-law zeros. All transverse
levels and pinned end edges remain. The standard finite matrix and
cochain methods are reused, with no new general flow theorem or source
claim.

Unfinished reasoning: expose K_1=-g_s(Delta_T)(I-P)D^T rather than
estimate its entries first. Its circulation factor may give an
unweighted operator bound stronger than its Hilbert–Schmidt bound.
The paired right paths appear as t_b W_q-t_q W_b. Test whether that
actual local alternating path map annihilates a transverse gradient,
or whether its retained gradient contribution still costs a power of N.
Any fractional estimate must include the local smooth multipliers;
they cannot simply be commuted through Delta_T or P. A mixed relative
residual form bound is not available. Continue only on a demonstrated
bound or reduction; failure of an absolute bound is not signed growth.

Completed test: full proofs are in
[L064, proof section 5](../lemmas/L064-mixed-pinned-endpoint-regrouping.md).
The actual K_1 has ||K_1||²<=sqrt(12)/2. The paired trace with its
smooth alternating right map still gives only O(N^(7/2)), versus
O(N²), because the full right-lift trace is O(N^5) and ||R_a||=O(N).
The exact local gradient stencil survives whenever either interior
path coefficient is nonzero; no claim of nonzero full signed response
follows. Outcome: EXPLORATION / REPRODUCTION, second exploration since
L063. ATTEMPTS/020 parks this closure, preserving ATTEMPTS/011–019.

Reassessed continuation within the unchanged approved response target:
test the actual component-1 residual between an axial-zero input row
and all axial modes, rather than improve another generic covariance
inequality. In L040's dimensionless notation let E_0 embed the
normalized constant axial component-1 mode, let I_1 embed all
component-1 links into full links, let Sigma_1=I_1^T Sigma I_1, and
let G=(T^T T)^(-1). The concrete operator to test is

    R_01=G^(1/2) E_0^T A_0 I_1 Sigma_1^(1/2).

Seek an N-independent operator bound, or an explicit retained-mode
obstruction to it. The latter must concern this operator, not the
complete response. The generic bound is O(N); a bounded R_01 could
remove that loss for the right axial-root part of the mixed residual
and make a sharper signed contraction test possible. It would not
alone prove O(N²) or control the direct transverse component.

L040(4),(10)–(11), L041(12)–(13), and L054(10) cover only the double
axial-zero compression E_0^T A_0 E_0. Their primary stencils and
commutator argument were inspected for this distinction. Extending
them to R_01 is unproved. Essential inputs for this continuation:
L018, L020, L026, L028, L040, L041, L054 and L060–L064. Preserve all
axial modes and pinned rows, the actual clover/endpoint averages and
coefficient derivatives. No mixed relative form bound is assumed.
All four remaining placements, the five previously subleading terms,
other/other cubic pairs, L011/L019's response jets and compensation,
finite matching, reflected error <=c_box/2 and the continuum/mass gaps
remain unresolved. No changed assessment or uncovered target is
approved by this note; the saved full-response assessment is reused.
