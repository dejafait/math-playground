# Rank-24 stable-summand calculation — working checkpoint

Invocation-start SPECIALIZE coverage:
`drafts/literature/2026-10-23-twisted-stable-summand-index-bound.md`.
Only its exact rank-24 target is being attempted; no new source search.

Main gap: universal primitive rational Hodge realization. Intermediate
test: improve the conditional upper restriction z<=162 for the actual
M using all stable-type indices; possible downstream use requires an
independent lower comparison, which remains absent. Continue on a
uniform stricter bound, stop this numerical filter at a fully checked
compatible endpoint. F and nonempty Z remain unproved.

Inputs checked: L052's full exact-h perpendicular lattice proof gives
c_1=tk for every zero-slope integral stable factor; L147's actual
character is 24-4k+(z-167)eta; audited L153 supplies its polystability
at the identical real h. Earlier ATTEMPTS/043/047/053 retain compatible
branches and forbid treating all M as simple or omitting repetitions.

Current calculation, not yet independently audited: write a stable type
as (r,tk,d eta), with r>=1, t,d integral. The cited simple Mukai bound
is r^2+rd+7t^2<=1. If a=|t|>=1 and d>=-5a+1, the necessary quadratic
r^2-(5a-1)r+7a^2-1<=0 has discriminant -3a^2-10a+5<0, impossible.
For t=0, the same bound gives d<=0. Thus d<=-5|t| uniformly and,
after multiplicities, z-167<=-5 sum m|t|<=-20: z<=147.

Endpoint to check completely: O^16 plus four copies of a single formal
stable type E with (r,t,d)=(2,-1,-5), v(E)=(2,-k,-3).
v(E)^2=-2, <v(O),v(E)>=1; E has endpoint cohomology zero and
chi(E)=-1. These are formal character/cohomology assignments, not
stable existence or identification with actual M. Complete equality
and pairwise analysis, canonical proof and documentation remain next
within this same attempt. No mathematical script or finite search is
needed if the uniform proof and witness hold.

Completed in canonical L154: the bound is 147, with equality forcing
one stable type repeated four times plus sixteen trivial lines. All
selected pairwise and section indices pass the formal endpoint.
Full proof, citations and qualifications are in L154; this working
checkpoint is superseded by that canonical result. Separate critical
audit remains pending; no existence assertion has been made.
