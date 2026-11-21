# Fixed prime-gap defect bounds — audit coverage1118

TARGET: Audit C030c's uniform signal, closed-strip admissibility and full/half-sum normalization against its explicit constants and retained zero-occurrence hypotheses.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact-target discovery and overlap comparison1117 and pre-existing quantitative assessment1117; the audit changes no probe, parameter domain or source theorem. Local targeted searches found no duplicate quantitative proof. This is coverage preparation for a separate audit, not another mathematical attempt.
SOURCE_EVIDENCE: Polson, On Hilbert's 8th Problem, arXiv:1708.02653v24, https://arxiv.org/pdf/1708.02653v24, Definition9.1/Proposition9.3 printed pp30-31; Theorem12.2(vi)/(53) printed p36 and its complete Fourier/support proof p37; Tao, 245C Notes2, 6April2009, https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/ Section3 equation(11), Example33/Exercise38. Exact source class, norm, inverse-transform convention and the full/half normalization were reconsulted during calculation1118.
COMPARISON: The source already proves qualitative logarithmic-gap detection; C030c specializes the prescribed bump to explicit positive signal and cubic strip cost. The next task checks that written specialization rather than reproving source stability or claiming new qualitative discrimination.
GAP: Independently check C030c equations(1)-(9), including endpoint flatness, all uniform constants, even entire square-root descent, closed-strip decay, inverse Fourier normalization and repeated removed occurrences. No later audit has yet accepted this proof.
REASON: Separate approval1119 is complete for this unchanged target; primary inputs are accessible and adequate. Proceed directly to the mathematical audit next turn without another coverage approval.
SCOPE: Only C030c and the unchanged fixed family/domain of assessment1117. No all-degree sign bridge, infinite-surgery exclusion, new zero verification, finite-block stability proof, mathematical script or source-discovery campaign is covered.

## Audit test and retained qualifications

The load-bearing estimates are mean>=m, oscillatory error<=M/(2g),
G=max(1000,ceil(M/m)), and the weighted third-derivative estimate with
C=2 exp(27/40)(11/4)^(9/4)(N0+3N1+3N2+N3).
Check the direct integral bound at |Re r|<=1 and the integration by
parts bound at |Re r|>1 throughout |Im r|<=3/4. Real-axis decay alone
is inadequate. Confirm that N0=1, Nj are finite specified L1 norms,
and constants contain no hidden A,B,g dependence.

Check that the fixed support avoids every log n and that Fourier
inversion recovers eta_g in the source convention. Track the measure
defect -2K dx, full sum difference 4I and half sum difference 2I.
Distinguish general real A,B estimates from an entire surgery: exact
line-zero occurrences, including two occurrences when A=B, are needed
only for the latter. The threshold may exceed the original source's
(1000,2000] interval. No assertion that those original choices pass
G is permitted, and no existence claim at every high ordinate follows.

Pass only if every stated bound and applicability condition survives.
A repair must be recorded explicitly; a fatal failure should preserve
the calculation and identify the exact failed inequality. Either result
leaves L030/L032/C032a's all-degree sign gap and common-graph realization
open. The probes are signed, height-dependent and not polynomial squares.

Mathlib matching coverage remains unchecked. There is no cross-notebook
input. The audit is ordinary Fourier/arithmetic and hypothesis checking,
so proof_audit/routine_audit is appropriate; it is not a creative or
candidate-RH audit. Preparation1118 did not approve its own future mathematical audit;
separate approval1119 below approves coverage, without accepting the proof.


## Separate coverage approval1119 — 16 November 2026

LITERATURE_REASON: The invocation requires separate approval of newly
prepared coverage1118; inspect exact primary inputs and reuse the
existing discovery comparison1117 rather than repeating discovery.

Read C030c to match its obligations to this scope; no inequalities
were independently audited and no lemma or script was edited. Reused
assessment1117 and discovery1116's duplicate/failure comparison. The
finite-block obstruction remains parked in its original scope; it
does not prohibit this arithmetic discriminator.

Direct primary reading: [Polson v24](https://arxiv.org/pdf/1708.02653v24),
Definition9.1/Proposition9.3, pp30-31, specify even strip-holomorphic
tests, decay exponent 2+delta and the stated norm. Proposition9.4,
pp31-32, identifies the reflection-paired sum by halving the full sum.
Theorem12.2, pp36-37, requires exact removed zero occurrences and
retains repeated occurrences. Read its entire (vi) Fourier/support
proof on p37: it states the measure defect, full-sum factor and
compact-gap admissibility. Its original height interval supplies no
guarantee for C030c's larger threshold. This approves access and scope,
not the source's heat-stability estimates or C030c's constants.

Direct primary reading: [Tao's notes](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/),
Example33, Exercise38 and Section3(10)-(11), including the Gaussian
approximation proof, supply compact-smooth membership, Schwartz
preservation and inversion for Schwartz functions in the 2pi convention.
They do not supply the uniform complex-strip estimate. The next audit
must verify the explicit weighted integration-by-parts argument;
real-axis inversion alone cannot discharge that obligation.

Decision: retain SPECIALIZE and the identical TARGET. Coverage is ready
for one research audit. No new theorem, stronger bound, novelty claim,
Mathlib finding or independent RH input is established in approval1119.
The existing pass/fail test and occurrence/onset qualifications remain
mandatory. Do not schedule another approval of this same target.
