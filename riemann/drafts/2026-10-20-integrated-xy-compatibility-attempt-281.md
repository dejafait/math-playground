# Step 281 — exact integrated xy compatibility attempt

The approved target is the unchanged TARGET of
`drafts/literature/2026-10-20-complete-x-second-integrated-xy-compatibility.md`
(prior SPECIALIZE). Main gap: global mixed positivity. This bounded
attempt tests only the necessary scalar compatibility of L445's complete
q_H with all temporal x-squared tests and exact zero integrated xy.
Failure at arbitrarily large real H stops this unchanged-density extension;
compatibility would remove only one obstruction before covariance work.

Known-source and duplicate checks reuse the supplied assessment, L445's
audited formula (6), L444 (3), L443 (17), and the two corresponding
ATTEMPTS records. Neither the bounded-repair stop nor the closed
singular-variation test decides the exact integrated constraint.

Initial calculation: weak-derivative uniqueness forces r=q_H'/(2L)
a.e.; Hunter's endpoint integration by parts gives

    2 integral_H^(2H) r
      = q_H(2H)/L(2H)-q_H(H)/L(H)
        +integral_H^(2H) q_H L'/L^2 =: J(H).

This criterion alone is incomplete. All parameters depending on H
are fixed in this derivative. The positive integral is O(1/log H),
using exact integral q_H=H log H. Neither endpoint may be discarded.

Proposed evaluation, still to check: use the original stage interval
[B_j,2B_j), wholly inside stage j because B_(j+1)>=2B_j.
Average J(H) cos(H log 2) over that interval. L440's finite Fourier
truncation should give coefficient 1/sqrt(2) for P_j(H), but zero for
P_j(2H): a doubled integral prime exponent cannot equal the odd
prime-2 exponent. The anticipated limit is -1/sqrt(2).

Obligations before claiming this limit: retain N_H via its uniform
stage bound and an L1 endpoint bound for P_j; do not multiply an
unquantified o(1) by its growing supremum. Bound high endpoint terms
by L421's actual fourth moment on [B_j,2B_j] and [2B_j,4B_j],
with log H comparable to log B_j. Bound both intermediates, the
constant correction and translation uniformly; retain w's high loss.
Check the doubled-frequency rational separation and full Fourier tail
under the original M_j bound, with no new threshold choices.

No mathematical script or numerical sample is planned. No covariance
feasibility, inter-H consistency, actual sine limit, other occupation
identity, clipping, capped nondegeneracy, L413 full-error margin or
RH consequence is assumed. The final result and complete proof, if
successful, will be canonical in a lemma rather than this draft.

Completed: [L446](../lemmas/L446-complete-x-second-integrated-xy-incompatibility.md)
proves the anticipated signed limit with all listed obligations
discharged. The normalization is handled in L1, the high endpoints
by the actual fourth moment on both doubled intervals, and the entire
Fourier tail by the original cutoff bound. The resulting positive-measure
sets of incompatible heights stop the unchanged-density eventual-ray
extension. This is an informative NEGATIVE research outcome, pending
a separate critical audit; it is not a numerical test or an RH result.
