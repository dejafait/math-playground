# Retained-plus complete-integral attempt — step 514

2026-10-26. Completed mathematical exploration; no vanishing or
rationality claim. The in-turn scratch below is retained as recorded.
Prior gate: `drafts/literature/2026-10-26-plectic-retained-plus-cancellation.md`
(EXPLORE, unchanged). Actual task: proof_attempt / creative.

Main gap: rational rank versus complex order for arbitrary curves.
Bounded target: the exact checkpoint test for D^{++}, for F=Q,
K imaginary quadratic, inert split-multiplicative p>=5, S={p},
w=infinity, conductor one and trivial character, with all the source
conductor, residual-image and incoherence hypotheses retained.
The intended application additionally assumes complex order two for
A and a nonzero central value for its K-twist; these do not enter the
definition of the class and supply no rational points.

The supplied assessment and step-512 source notes have been read.
L005 and L122 have been read with their full hypotheses and proofs;
ATTEMPTS/003, /004, /030, /058 retain the rationality obstructions.
The first two are downstream motivation, not inputs asserting
strictness or a valid multiplicative-prime rank criterion here.

Plan within this one attempt: fix compatible conjugation lifts, prove
the restriction identity on cocycles, and track the scalar and
coefficient actions through the complete integral, diamond invariance,
CM sum and descent. Apply pr_A only after integration. A local scalar
norm expression, if obtained, must retain the transformed measure and
cannot itself be reported as cancellation.

Continue only with a proved cancellation or a fully specified arithmetic
residual having a discriminating test. Park a formal-sign-only route if
it leaves an uncomputed coefficient action with no such test. Nonzero
rational Kummer membership, the multiplicative extension of L005 and
general complex-order comparison remain independent even on success.

## Unfinished reasoning

The scalar calculation gives f_tau + sigma(f_tau) = log_p N_tau,
where N_tau([(x,y),z])=(x-tau*y)(x-bar(tau)*y)/z. Thus the first
plus projection contributes one half of this logarithmic norm moment.
The kernel is unchanged by tau <-> bar(tau); it is not constant, since
[(1,0),1] and [(1,0),1+p] give 0 and -log_p(1+p).

Choose d in the p-decomposition group inducing the nontrivial element
of Gal(K/Q). On raw coefficients C=d need not satisfy C^2=1. Only
after descent to H^1(K,V) does it induce the involution c. Do not call
(1+C)/2 a raw eigenspace projector. The candidate exact residual is
one quarter of the localization of the descended pr_A image of the
complete log-norm moment of mu+C*mu, with mu the full finite CM sum.
The quarter accounts for the two separate plus projectors.

For a cocycle a and g in the local subgroup, (d*a)(g)=d a(d^{-1}gd);
the restriction identity is exact on cocycles. Changing d by an element
of G_K changes its action by a coboundary: for h in G_K,
(h*a)(g)=a(g)+(g-1)a(h). This also explains why a p-decomposition lift
can represent global outer conjugation without being order two itself.

Source Corollary 3.9 supplies a possible independent arithmetic handle:
on a cell xi X_m, the raw CM measure is the sum over t of
j_m phi_m([z_w,h_t xi]_{K_m}). Coefficient conjugation replaces each
point by its actual d-conjugate; phi_m and j_m are defined over Q.
No unproved reindexing or sign formula for these points is available.
The norm pushforward to principal units converts the residual to a
single first logarithmic moment. Its full proof, domain checks and
limitations are being written canonically; no arithmetic moment has
been evaluated, and D^{++}=0 remains unproved.

## Mathlib

Coverage of the construction and this diagnostic: not checked.

## Disposition

The canonical statement, proof, citations and qualifications are now in
L123, lemmas/L123-retained-plus-norm-moment.md. It records a complete
norm-moment residual with the factor 1/4, rather than a cancellation.
No CM coefficient or projected local moment was evaluated. The scalar
exchange/constant-mass shortcut stops, while the specified arithmetic
residual remains available subject to a separate critical audit within
the unchanged assessed diagnostic. This is EXPLORATION, not a claimed
new arithmetic input or progress beyond the checked sources.
