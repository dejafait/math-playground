# Quotient and lifting attempt — working record

2026-10-20. Approved target: determine the normalization genus of L106's
quotient by v -> −v and the precise square-class −3 lifting condition.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-minus-three-unmarked-quotient.md`.

Main gap: both L095 integer systems and global factor compatibility remain
unresolved. This intermediate geometry could support a later rational-point
method; it supplies no such method or emptiness result itself. Inputs are
audited L106 and the quotient/Kummer/normalization sources in the assessment.
ATTEMPTS/045–046 concern independent mechanisms and remain preserved.

Provisional calculation, to be certified and written canonically: the
quotient labels are (r,{a,b}), giving degree 495. The three branch cycle
histograms should be {5:99}, {1:168,3:109}, {11:45}, hence ramification
396+218+450=1064 and genus 38. Each branch permutation has odd order,
so no power fixing an unordered pair can exchange its two entries.
Thus both ordered lifts have the same local degree at every boundary
point: the proper double cover should be étale everywhere.

Invariant coordinates are (r,u,z), z=v², with quadratic factor
(T−u)²+3z and discriminant Δ=−12z. The explicit even equation and F1/v
give the invariant ring after inverting
z*((r−u)²+3z)*phi(r)*(phi(r)−1). On this open, rational lifting should
be equivalent to [Δ]=[−3], or z a nonzero rational square.

Boundary obligation: prove that ord_P(z) is even at every point of the
proper quotient. For a rational point P and a uniformizer τ, set
η=z*τ^(−ord_P(z)); the normalized local equation is h²=η. Its residue
square class, rather than substitution of z=0 or infinity, must give
the reversible rational-lifting criterion. No rational boundary-point
enumeration is required by the approved assessment.

Continuation test: complete the invariant-ring identification, full
branch-action arithmetic and reversible normalized lifting argument
within the 1000-label cap; otherwise preserve the precise obstruction.
No point arithmetic, other quadratic field or integer elimination is
part of this step.

Completed: canonical L107 contains the invariant-ring identification,
genus 38, everywhere étale proper double cover and reversible open and
normalized-boundary lifting criteria. The full finite certificate is
`scripts/global-fiber-genus/quotient-certificate.json` (863 checks, no
failures; degrees 495/990 against cap 1000). The provisional calculations
above are confirmed. This is relevant local geometry by specialization
of the ready sources, not an integer exclusion or a claim of novelty.
A separate critical audit remains required before choosing point
arithmetic; the previous independent route stops remain unchanged.
