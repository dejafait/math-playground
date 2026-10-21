# L048 geometric-parameter audit — working record

Approved target: critically audit L048's strengthened-precision split
reduction and geometric Tate valuation, including same-curve retention
of L045–L047. The unchanged SPECIALIZE assessment is
`drafts/literature/2026-10-11-approximating-curve-geometric-parameter-critical-audit.md`.

The main gap is original finite B>=A. Passing this audit validates one
local prerequisite for a subsequent sufficient-initial-data test, not
an IUT-flaw candidate. Fail the audit if any invariant identity, strict
precision bound, general-model minimality, characteristic-3 split-node
test, complete Tate expression or same-curve quantifier fails.

Checks completed before the final write-up: direct expansion of the
general b-invariants gives the stated discriminant; the u=1 square
completion retains it; product tails converge to a unit; M>=31 makes
the discriminant error strictly higher than valuation 30. Unit c4
excludes a lower-discriminant integral general model. The unique
reduced affine singular point and smooth infinity check pass, with
distinct rational tangents. The full Tate j-expression is a unit
after multiplication by q_0. L044/L046 allow the stronger precision
to be fixed before the single choice of curve; L045/L047 then apply
to that same curve. No mathematical correction has been identified.

Essential inputs: L048 and its direct L044–L047 inputs; retain L042's
Omega,H,N through L044. The earlier exact-curve and different-packet
stops remain intact. Sufficient global initial data, native/input/action,
pilot, essentiality and original finite B>=A remain unresolved.
Full evidence and the passing final verdict are now recorded in
canonical L048's separate critical-audit section; this preserved working
note is not a replacement proof or a new lemma. No correction was needed.
