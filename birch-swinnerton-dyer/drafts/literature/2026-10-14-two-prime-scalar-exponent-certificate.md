# Two-prime scalar as an exponent certificate — source comparison

TARGET: Assess whether one certified two-prime Kurihara scalar of exact valuation v<m modulo p^m certifies p^v(D/D_div)=0 under every L026 premise, with the actual coefficient ideal and period conventions checked.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the finite-depth witness and positive-valuation restricted-index assessments; targeted searches for Kurihara scalar upper bounds, coefficient ideals and finite-quotient exponents located Kim's exact definitions and structural theorem. Local comparison with L021--L023/L026/L061/L062 and ATTEMPTS/021/029--031 found no completed standalone finite-input exponent certificate; no originality claim follows.
SOURCE_EVIDENCE: Directly inspected Chan-Ho Kim, The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves, publisher-hosted author text dated 2025-05-12, https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf, Sections 1.2.2/1.4/1.5.1, Theorem 1.8(1)--(3), Theorem 1.10 and its primitivity proof, printed pp. 3/5--7/32; inspected Section 5.4's deep-index setup and paired-factor comparison, pp. 29--31. Reused L021's previously checked terminal-valuation specialization.
COMPARISON: Kim explicitly allows mod-p^m reduction at N in N_m and expresses finite-quotient length by a minimum of scalar valuations minus the terminal valuation. His discussion after Theorem 1.8 explicitly permits computed structural upper bounds. This covers the source mechanism for the proposed conditional certificate, not its input production or an exact finite-length calculation.
GAP: A later mathematical step must transfer the certified nonzero residue valuation to the actual I_N coefficient, compare it in the upper-bound direction with the minimum, and convert a finite-length bound to annihilation. No scalar, exponent instance, successful class, rational Kummer membership or complex-order comparison is established here.
REASON: Essential new coefficient and precision coverage is now inspected; approve a bounded known-source specialization, without re-proving Kim or selecting the localization branch in this literature turn.
SCOPE: Every L026 premise and the audited L061/L062 classical conventions; m>=1, two distinct good primes in Kim's P_m, the actual Neron-normalized Kurihara residue modulo p^m, and an independently certified exact valuation 0<=v<m. Stronger P_(m,0) eligibility is sufficient but unnecessary; an arbitrary index in N_1 alone is insufficient for reduction to depth m.
COVERED_TARGET: Specialize Kim's finite-quotient formula to one certified two-prime scalar modulo p^m of valuation v<m, proving p^v(D/D_div)=0 and stating its conditional L062 use.
LITERATURE_REASON: The saved target changes from a supplied exponent to a finite scalar certificate; its actual coefficient-ideal reduction, period normalization and bound direction were expressly excluded from the previous ready assessment.

The main gap is arbitrary higher-order rational/complex rank equality.
The intermediate question is exactly TARGET. A finite exponent certificate
could discharge one input of L062 while leaving successful classical-class
production and strict rational Kummer membership unresolved. The threshold
for the later attempt is the conservative exponent e=v, not an exact
minimum or an optimal exponent. No claim is made that the desired scalar
exists or can be found in bounded time.

Essential local inputs for the review are L021's finite-quotient formula,
L026's full premises and period matching, audited L061's definitions of
D and its divisible subgroup, and audited L062's exponent requirement.
The proposed scalar is an additional independently certified input at
an eligible square-free index with exactly two primes, and v<m must
denote a genuinely determined nonzero residue valuation.
All L026 arithmetic, central-vanishing, sign, residual and quadratic-
coefficient premises remain supplied. No cross-notebook input is needed.

## Inspected definitions and theorem scope

Use Kim's [Section 1.2.2, printed p. 3](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=4):
\[
\mathcal P_m=\{\ell\nmid N_Ep:\ell\equiv1\pmod{p^m},
 a_\ell\equiv\ell+1\pmod{p^m}\},\qquad
I_N=\sum_{\ell\mid N}(\ell-1,a_\ell-\ell-1)\mathbf Z_p.
\]
Here N_E is the conductor and N=ell_1 ell_2 is the auxiliary index.
The sum is the actual coefficient ideal, not a product. Certify each
congruence: I_N must be contained in p^m Z_p for the quotient map from
Z_p/I_N to Z/p^m to exist. Equality I_N=p^m Z_p is not required.
The stronger cyclic-torsion condition used in L023 is outside the needs
of this certificate; its actual rank-zero scalar is not automatically
the present modular-symbol scalar without its normalization comparison.

[Section 1.4, printed p. 5](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=6)
defines the finite sum
\[
\widetilde\delta_N=\sum_{a\in(\mathbf Z/N)^\times}
[a/N]^+\prod_{\ell\mid N}\log_{\eta_\ell}(a)
\quad\text{in }\mathbf Z_p/I_N.
\]
Its depth-m reduction is explicitly defined for N in N_m. The symbols
are p-integral under residual irreducibility and prime-to-p Manin
constant. The source period is the total real Neron period of a global
minimal model, matching L026's retained compatible convention. Thus a
table normalized by a connected-component period, an optimal-source
period, or an arbitrary eigenvector needs a certified conversion first.
The positive imaginary vertical integral in Kim's definition must also
match the table's orientation. Before identifying a table entry
F({infinity,r}) with [r]^+, check its defining oriented integral and
normalization against Section 1.4.1; path reversal must be accounted for.
Primitive-root changes affect
valuation only by units; no nonunit scaling can be ignored.

[Section 1.5.1 and Theorem 1.8(1)--(3), pp. 5--6](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=6)
give
\[
\operatorname{length}_{\mathbf Z_p}(D/D_{\rm div})
=\partial^{(\operatorname{ord}(\widetilde\delta))}
 (\widetilde\delta)-\partial^{(\infty)}(\widetilde\delta).
\]
Their hypotheses are p>=5, residual surjectivity, a prime-to-p Manin
constant and a nonzero collection. L026 supplies them and corank two;
L021 supplies the checked residual-primitivity terminal value zero.
The source's finite-Sha clauses (4)--(6) are unused. The passage immediately
after Theorem 1.8 discusses upper bounds from computed scalar valuations;
it does not require computing all indices to obtain an upper bound.

[Theorem 1.10, p. 7, and its proof, p. 32](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=8)
retain local p-torsion vanishing and prime-to-p Tamagawa factors in the
residual-primitivity comparison. L026 retains both. The proof begins
with a nonzero residual scalar implying a primitive Kato system;
this is not a unit scalar at the first integral index. Do not invoke
Conjecture 1.9 outside its theorem-supported zero-Tamagawa specialization.

The inspected [Section 5.4, pp. 29--31](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=30)
chooses deep indices attaining the minimum to prove the structure theorem
and compares the paired largest factors in both cyclic-cokernel cases.
Those proof choices are not extra certificate inputs for a later
application of the already proved theorem. No such minimizer is supplied.

## Precision, duplicate comparison and approval boundary

The later proof must use a certified residue in p^v(Z/p^m) outside
p^(v+1)(Z/p^m), with v<m. It must show why this determines the same
valuation in the longer actual coefficient ring, even when I_N is
strictly smaller than p^m Z_p. A zero residue cannot do this, and an
integer lift of a scalar computed at inadequate coefficient depth is
not a replacement. The comparison is a minimum bounded above by one
eligible value, never an equality inferred from one value. The standard
finite Z_p-module structure theorem suffices for the subsequent
length-to-annihilator step; L021 already records that structure.
These are approved proof obligations, not a proof executed here.

L021 already proves the infinite-minimum formula. L023 supplies an
existential specially selected scalar with valuation the granted finite
length at sufficiently deep m; it does not provide an independent
numerical upper bound before that length is known. L062 already proves
the localization implication given an exponent and a successful class.
The present assessment connects those scopes without claiming a new
source theorem or redoing any of those proofs. Preserve ATTEMPTS/021 and
029--031: neither primitivity nor ordinary semisimplicity alone eliminates
the finite quotient or selects k=1.

Continue to the separately approved bounded specialization only if the
specified quotient, normalization and nonzero residue conditions suffice
for e=v, without an exact infinite minimum, k=1 or F=0. Abandon the
certificate inference if its reduction or inequality fails. Even a
successful conditional proof leaves actual scalar production, a class
at depth n>v with p^v loc_p(c)!=0, strict rational Kummer membership and
arbitrary complex-order/rank comparison unresolved. A zero localization
test remains inconclusive. No sharper exponent is proposed in this step.

Searches on 2026-10-14: `"Kurihara numbers" "upper bounds" Selmer Kim valuation`;
`"Kurihara" "I_n" "partial" Selmer structure`;
`"Kurihara" "finite" "exponent" valuation`;
`"Kurihara" "finite quotient" "valuation"`.
Only the inspected Kim source supports this decision. Other search hits,
including a refined-nonvanishing paper and unrelated exponent results,
were not used or treated as inspected theorem coverage. The ready
finite-depth witness and positive-valuation restricted-index assessments
were reused within their unchanged scopes. Full and supporting Mathlib
coverage remain not checked; unknown availability is not absence.
