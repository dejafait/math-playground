# Fixed-pair branch comparison

The sole target is the exact TARGET in
`drafts/literature/2026-10-28-pair-branch-annihilator-test.md`, whose
prior SPECIALIZE gate is reused without a source refresh. Main gap:
residual primitive Beal solutions are not excluded; the accepted
genus-two bound is rank<=2+c<=4, versus the sufficient bound one.

Intermediate target: decide whether the nonzero rational branch Kummer
class lies in the span of L147's masks 165 and 132102. This could retire
an unsuitable Cassels–Tate pair before further covering construction.
Essential inputs are L138's actual odd model and field, L139's Kummer
interface, and L147's exact pair, branch evaluation and independence.
No scalar quotient is taken. ATTEMPTS/065 and unfinished work are preserved.

Test exactly branch/epsilon, branch/eta_class and
branch/(epsilon*eta_class). A nonsquare rational or local component
settles nonmembership; a displayed exact root in both components settles
membership. Otherwise use the already assessed complete field square
algorithm, retaining completeness evidence. Bound the attempt to these
three ratios and 8192-bit rational coefficients; an incomplete computation
is unresolved, never evidence of nonsquareness. Continue pairing work only
if this obstruction is absent; membership forces the pairing on this
two-dimensional span to vanish by the imported radical/alternation facts.

Completed: L148 gives the exact square roots proving branch=epsilon.
A negative real component excludes eta_class and odd rational 3-adic
valuation excludes their product. The nonzero rational branch is in the
pair's span, so the proposed nonzero pairing is forced zero. Independent
maximal-order arithmetic replay passes all 130 checks; the separate
critical review is still pending. Full certificates and direct identities
are canonical in L148. No rank improvement, covering model or global basis
is supplied. This is local obstruction evidence, not progress beyond the
general source theorems.

The initial producer lacked SymPy. That execution failure is preserved;
the replacement uses exact rational arithmetic and direct square-root
certification. Decimal interpolation proposed one root and is not proof.
No installation, backend probe or larger witness pool was used. Both
nonsquare decisions are complete exact obstructions, not failed searches.
