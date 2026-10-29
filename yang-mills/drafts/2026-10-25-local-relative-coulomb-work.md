# Fixed-mesh local quotient specialization — work checkpoint

Approved target: the unchanged SPECIALIZE target in
`literature/2026-10-25-local-quotient-density-specialization.md`.
Inputs read: L003 section 1; L279 hypotheses, (7), (20)–(22),
(31)–(34), and its finite-dimensional Laplace input. The parent
assessment and ATTEMPTS/047 were checked; no additional source needed.

Main gap remains interacting control toward a nonzero continuum sector
and positive finite mass. The immediate target is an exact alternative
representation of the fixed-mesh coefficient, for possible later
elliptic-covariance estimates. It does not supply such estimates.

Working conventions: variable links E include all normal links; interior
vertices I carry gauge parameters, extended by zero on the boundary.
For the action h_tail U_e h_head^{-1}, set B u=u_tail-u_head,
M u=u_tail+u_head, Delta=B*B, H=ker B*. Logs use L279's generators.
The proposed chart is Psi(v,h)=h.exp(v), v in a small ball in H.
At zero its derivative is [H,B]. Freeness along the boundary-rooted
forest and compactness should upgrade local inverse-function uniqueness
to uniqueness among all h for sufficiently small v,w.

For the derivative D(v) of log(h.exp(v)) in h at identity, the candidate
expansion is D=B-(ad_v)M/2+(ad_v)^2 B/12+O(|v|^3).
The exact positive quotient density should be
rho(v)=c0^(|E|-|I|) sqrt(det Delta) product_e j(v_e)
times det(Delta^{-1}B*D(v)), with normalized gauge Haar and
c0=1/(16 pi^2). All determinants include three colors.
Let A1=Delta^{-1}B*[-ad_v M/2] and
A2=Delta^{-1}B*[(ad_v)^2 B/12]. Then tr A1=0 by color trace,
and the candidate degree-two log density is
ell2=-sum_e |v_e|^2/12+tr A2-tr(A1^2)/2.

Remaining checks in this attempt: exact product density and its sign;
global-in-h local orbit uniqueness; source localization using positive
plaquette weights; equality of unnormalized asymptotic coefficients
with L279(22), including source-independent constants. Continue only if
all pass. No global section or nonlinear Hodge transfer is proposed.
This is unfinished reasoning, not an established lemma.

Completion: the obligations above are proved in canonical L280,
`lemmas/L280-local-relative-coulomb-source-coefficient.md` (relative to
the notebook root). This pre-proof checkpoint is preserved as written;
L280 supplies the final statement, normalization and qualifications.
The result is a REPRODUCTION of the source-covered quotient mechanism,
with separate critical audit still pending. No numerical script was
needed; checks included the two normal-link endpoint cases, the color
trace, and an exact two-edge normalization consistency check.
