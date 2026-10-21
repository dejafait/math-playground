# Quadratic-component specialization — working record

Approved target: Determine the complete list of imaginary quadratic field components compatible with L103's degree-ten complement using L093's ramification support and whole two-adic factors.

Prior coverage: `drafts/literature/2026-10-20-complement-quadratic-components.md`
(SPECIALIZE, unchanged). Inputs: audited L093 and L103; L095 identifies
the branch but its two integer systems are not assumed solved.

The main gap is integer elimination of both L095 systems, with independent
residual signatures still open. A necessary quadratic direct-component
list could constrain the (8,2) and (4,4,2) branches. Continue only if the
finite squarefree enumeration is exhaustive and each retained completion
matches whole local factors; abandon any use of a quadratic subfield of
U4/U10 as a direct factor, or of special-coefficient local tables.

Saved before final write-up: squarefree d<0 with discriminant supported
on {3,5,11} must have d in {-1,-3,-5,-11,-15,-33,-55,-165} and d=1 mod 4.
The latter condition leaves {-3,-11,-15,-55}. At two the first two are
inert and the last two split. Since the complement has no Q2 factor,
only Q(sqrt(-3)) and Q(sqrt(-11)) remain, each consuming its whole U2
factor in the (5,3,2) or (4,4,2) local type. The (10) type has no
quadratic direct factor. Verification and qualifications will be canonical
in L104; no field-product or fiber realization is claimed.

Write-up complete: the full argument and citations now reside in
`lemmas/L104-complement-quadratic-direct-components.md`. All eight
discriminants and four complete two-adic products are displayed there;
the result awaits its separate independent application audit.
