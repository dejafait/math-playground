# Stable-resolution Chern test — calculation record

The prior SPECIALIZE assessment is
[the compatible-bundle review](literature/2026-09-27-compatible-cubic-rm-stable-bundle.md).
This step tests only its proposed terminal resolutions of I_C using powers
of one ample product polarization, allowing arbitrary line-bundle twists.

## Gap and discriminating test

The missing input is a representative of the cubic action that could reach
the fourth NS-fixed RM direction. Test simultaneous SU(2)-invariance of
c_1 and c_2 before attempting stability at L025's metric. Uniform failure
stops this recipe; formal success would still require actual allowed
resolution choices, stability for that metric and transverse transport.
The known family has 21 algebraic dimensions and three attained directions
against four required. Arbitrary fourfolds remain outside this test.

## Saved calculation

Mistretta's Theorem 3.1 has three presentation terms on a fourfold:
0 -> E -> P_2 -> P_1 -> P_0 -> I_C -> 0. Thus this E is not verbatim
L012's second syzygy. Its K-class is P_2-P_1+P_0-I_C.
For P_i=O_X(-m_i H)^{a_i}, write r=rank(E), c_1(E)=d h and
ch_2(E)=[C]+s h^2/2. The normalized character

\[
\nu(E)=\operatorname{ch}_2(E)-\frac{c_1(E)^2}{2r}
       =[C]+\frac{s-d^2/r}{2}h^2
\]

is unchanged by any line-bundle twist. Invariance of both c_1 and c_2
would force invariance of this class.

On W, rotation preserves the pullbacks of F,O,E,P: the fibre class,
the zero section, the two exceptional components together, and the
constant-coordinate section. These span NS(S)_Q by L019.
Consequently g_0^*=g_1^* there and [C] acts by 2 id_N, while its action
on T is U by L006 and L008. For h=p_1^*ell+p_2^*ell the mixed operator
of nu(E) on N is 2 id_N+(s-d^2/r) ell q(ell,-). Its eigenvalues are
rational, unlike lambda=2 cos(2 pi/7).

The common metric's diagonal SU(2) rotates the holomorphic-form plane
and omega. An invariant mixed correspondence commutes with that action,
so its lambda-eigenvalue on the holomorphic form must also occur on
omega. This is the contradiction formalized in L026. Point-class contributions
act trivially on H^2; the mixed Kunneth summand is itself SU(2)-stable.

The signs, both exceptional components, twist cancellation and
equivariance argument are checked in the completed
[L026 proof](../lemmas/L026-stable-resolutions-fail-common-metric-chern-test.md).
The exact algebra certificate
`python3 scripts/cubic-kahler/check_resolution_chern_certificate.py`
passed for formal indeterminates, without sampling polarizations.
The geometric argument, rather than that calculation, identifies
the divisor action and required Kahler eigenvalue.

The result is a uniform negative answer for this recipe. It leaves
arbitrary compatible bundles and transverse transport unresolved.
No source inspection matched the full specialized exclusion; the
step is conservatively classified as REPRODUCTION of the known
construction and invariant-class framework, with no originality claim.
The primary assessment is reused unchanged. A separate pending source
comparison is required for presentations using several divisor classes;
no calculation for that changed construction was performed here.

## Sources and redundancy

Reused the saved theorem comparison. Reread Mistretta,
[*Stable vector bundles as generators of the Chow ring*,
arXiv:math/0310185v2, Theorem 3.1, pp. 7--9](https://arxiv.org/pdf/math/0310185v2#page=7),
and Verbitsky,
[*Hyperholomorphic bundles*, arXiv:alg-geom/9307008v1,
Proposition 1.2, p. 4, and Theorem 2.5, p. 9](https://arxiv.org/pdf/alg-geom/9307008v1#page=4).
Existence and the conditional invariant-class framework are imported.
The calculation is their scoped application, classified as
REPRODUCTION; no originality is claimed. L012 excludes its specified
second syzygies, but does not by itself give this Chern-data conclusion
for Mistretta's terminal bundle.

## Mathlib

Coverage: **not checked** for the full exclusion or supporting bundle
results. The linked theorems supply the construction and framework,
not this specialized impossibility assertion.
