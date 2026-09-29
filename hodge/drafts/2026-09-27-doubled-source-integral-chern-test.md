# Doubled cubic source: integral Chern feasibility test

Date: 2026-09-27. Working record for the exact target in the saved
[EXPLORE assessment](literature/2026-09-27-doubled-source-cubic-resolution.md).

The gap is a representative supporting transport in the missing fourth
NS-fixed RM direction. The selected test retains L025's W and common
metric, three presentations by product line bundles, an actual integral
terminal twist, and stability with invariant c_1,c_2. Only the source
changes from I_C to I_C direct sum I_C. A successful bundle would still
leave transverse transport and the universal Hodge conjecture unresolved.

The prior assessment is adequate and reused. L026's one-polarization
exclusion, L027's slope and divisor-span tests, and L028's fixed-coefficient
parity exclusion remain in force within their stated scopes. Known Chern
additivity and invariant-form results are supporting inputs by citation;
no literature gap is being cleared in this research turn.

The discriminating test starts with the forced normalized mixed Chern
operator and the integral twist. Continue construction only for compatible
integral data with a justified map mechanism and a bounded stability test,
or record a scoped obstruction. A rational tensor or the mere disappearance
of L028's parity contradiction is not a bundle or an advance toward a new
algebraic class.

Initial checkpoint: doubling changes the transcendental action to 2U.
The single-source characteristic polynomial used in L028 must therefore
be recomputed; its irreducible cubic modulo 2 cannot be reused unchanged.
Also the final rational chamber conjugation need not preserve the divisor
lattice, so arithmetic in L025's pre-chamber model alone is insufficient.
No conclusion or existence claim has yet been made.

## Completed arithmetic test

The full necessary-condition proof and qualifications are recorded in
[L029](../lemmas/L029-doubled-source-chern-necessary-conditions.md).
For the doubled source, the normalized mixed operator on N is forced
to be 2A+4pi_K. After an integral terminal twist, the actual mixed
ch_2 operator is 2A+gamma pi_K, where gamma=4+q(alpha,beta)/r.
It is integral, and gamma must be even. The scaled cubic is
z^3+2z^2-8z-8, reducing to z^3 modulo 2. An even gamma then gives
z^4, so the old coprime-primary-space contradiction does not extend.

The exact integral tensor condition is stronger than that spectrum
test: the signed original tensor Q must equal the forced tensor B
plus r pi_W(t_1) tensor pi_W(t_2), in the actual lattice
(W intersect NS(S)) tensor (W intersect NS(S)). The rank and both
first moments must be those of the same presentation. This retains
the actual integral twist instead of allowing rational division.

In L025's pre-chamber model the forced doubled tensor is integral.
L029 gives its matrix and an explicit signed sum of product line
bundle classes with zero first moments and trivial twist. This is
only a virtual class: no sequence maps, kernel or stability follows.
For the final rational conjugation g the tensor becomes g B g^T,
which need not be integral. The original positive eigenvector has
not been declared Kahler on S. Thus the example does not clear even
the entire final-lattice part of the saved target.

## Reassessment and remaining threshold

The prior literature turn and this test consume two exploration turns.
The arithmetic has produced necessary equations, but neither an actual
presentation candidate with a map mechanism nor a scoped obstruction
to the doubled recipe. Classify the step EXPLORATION / RESEARCH /
REPRODUCTION. Do not count the new lemma or the formal example as an
advance. The framework is known, and no originality is claimed.

Three possible continuations of the same target were compared. Directly
summing an earlier terminal bundle with itself cannot be slope-stable:
either summand has the same slope as the sum. More Chern-only searches
would not bridge the gap from signed classes to an exact sequence.
The remaining materially different test is an actual mixed presentation
with maps not obtained by doubling an old block, using the generation
tools already inspected in the saved assessment. It must provide integral
data for the final W and an actual twist as well as justified surjections;
the pre-chamber example cannot stand in for either requirement.

Retain the exact reviewed target for at most one final bounded feasibility
turn. If no such presentation mechanism or new obstruction emerges,
complete the stop/continuation assessment and stop this construction
approach by the third exploration turn. Renaming the arithmetic or
adding more formal tensor examples does not renew that budget. This
is a route decision, not a nonexistence theorem for compatible bundles.

The attained 21-dimensional span and three directions against four
required are unchanged. Transverse transport, arbitrary primitive
fourfold classes and higher-dimensional cases remain unresolved. No
complete candidate proof or disproof appeared. Mathlib coverage of
the full statement is not checked, as recorded in L029.

The standard-library certificate passed for the tensor/operator identities,
the scaled polynomial and reduction modulo 2, and the actual signed-line
rank, first moments and degree-four moments. Its command is
`python3 -B scripts/cubic-kahler/check_doubled_source_chern.py`.
These checks certify the finite arithmetic, not bundle existence.
