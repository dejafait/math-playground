# Two-cubic action contraction — working record

Approved scope: the unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md`, applied to L011's
one-half kappa(f_(i,0),r0,S3,S3) at fixed mesh. No logarithmic
asymptotic is assumed. Essential inputs: L011, L018, L025;
L019 forbids interpreting the selected action group as forest invariant.

Main gap: cutoff-uniform interacting matching remains unavailable.
Intermediate target: a complete finite contraction of the two cubic
action vertices for both actual probes, with distinct plaquettes, exact
forest path covariance, and all colors retained. Downstream use: identify
the remaining matrix products whose scaling might compensate L047's
selected noncancellation. Continue if an exact Gaussian consistency
check supports the complete pairing formula; abandon missing-pairing
or curvature-only shortcuts. Full power/log compensation, insertion,
measure/flow jets, finite matching and reflected error <= c_box/2 remain
unresolved.

Prior checks: L025 already treats the quartic action, not this term;
L019's diagnostic tests coordinate-change cancellation but does not
contract the box's cubic pair. ATTEMPTS/011–016 retain the forest-loop,
upper-face, and signed-estimation obstructions. The existing literature
assessment supplies coverage for finite specialization; no new search or
reproof of bulk renormalization is needed.

Initial working algebra (preserved; now justified in L048): a plaquette cubic is
q3(y) = <w1,w2> = -1/2 sum_(r<s<t) y_r dot(y_s cross y_t),
with bracket minus cross product. Its symmetric combined edge/color
tensor is T_((r,c)(s,d)(t,e)) = -omega_(rst) epsilon_(cde)/12,
where omega is +1 on increasing distinct edge triples and alternating.
Color-diagonal forest covariance annihilates T:C. Thus cubic vertices
have no self-pair. Connected degrees (2,2,3,3) give 36+36
same-vertex attachments, 144 split attachments, and 72+72
quadratic-to-quadratic-path attachments. The first two vanish by color.
After the outside 1/2 and color sum 6, the proposed one-color formula is
3 sum_(p,q,r,s,t,u,v,w) omega_(rst) omega_(uvw)
[U_(pq,ru) V_(pq,sv) C_(pq,tw)
 +W_(pq,ru) C_(pq,sv) C_(pq,tw)].
C=Jp Sigma_F Jq^T, U=Jp Sigma_F B_(i,F) Sigma_F Jq^T,
V=Jp Sigma_F A_F Sigma_F Jq^T,
W=Jp Sigma_F B_(i,F) Sigma_F A_F Sigma_F Jq^T.
Ordered p,q includes p=q; no independence or internal heat factor is
asserted. The W term includes both path orientations by exchanging
p,q in the complete sum.

Completed: L048 supplies the analytic proof. The certificate
`scripts/combined-ward-response/two-cubic-action-certificate.json`
passes all 16 exact checks: all 945 pairings, three ordered-product
cubic comparisons, and twelve rational Gaussian cumulant cases with
all four ordered cells. Its full checks and empty failures fields were
inspected. The two surviving classes have coefficients 3 and 3 after
the ordered sum; an individual pair retains both path orientations
with coefficient 3/2 each. This is finite standard-method reproduction,
not an evaluated box response or a cutoff bound.

Continuation within the unchanged approved target: use L048 and
L018's exact forest covariance to estimate the complete cubic-pair
sum, retaining upper-face and cross-plaquette terms. L011, L019 and
L025 fix the interpretation; L030 and L047 supply the selected
a^(-2) comparison. Test for a justified scaled contribution before
any logarithmic claim; abandon estimates deleting cross plaquettes
or replacing internal forest links by curvature-only fields. No
compensation or scaled limit is yet assumed.
