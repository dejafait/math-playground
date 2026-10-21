# Complete quartic endpoint: diagonal-difference test

Approved target: the unchanged complete quartic response in
drafts/literature/2026-10-16-complete-quartic-probe-jet-scale.md.
Main gap: the ultraviolet-uniform interacting reflected comparison
and the continuum/infrared construction. The intermediate test is a
subcubic bound for the complete C212b endpoint, which by C212h would
give a zero cubic coefficient for the complete quartic response.
It would not establish compensation or finer asymptotics.

Duplicate/failure check: C212b bounds the five triples absolutely by
O(N^3); C212h reduces the complete target to them. The relevant local
draft/history search found no endpoint diagonal-difference reduction.
ATTEMPTS/044 and 045 rule out factorwise covariance commutation and
smoothness of a projection prefix, respectively. This test uses neither:
only the contracted external product modes are smooth. Reuse the saved
EXPLORE assessment and C212b's full color/tilt formula.

Initial unfinished reasoning, saved before completion: let v=phi_tail,
w=phi_head, h=(v+w)/2, d=w-v. Substituting u=z+v-w into all five
C212b triples leaves, at z=0, c_0=-[h,[h,d]]/3. Every other nested
bracket contains a direct z slot. Its variance is O(1), whereas
prefix variances are O(N); the signed tilt then suggests O(N^(5/2))
for all those terms. For c_0, its internal tilted contraction is
-4 sum_e(E_h K_hd-E_d K_hh), with
K_hd=(k_head-k_tail)/2 and k_v=(Phi M Phi^T)_vv.
The potential route is exact pinned summation by parts on this
diagonal difference, using O(N^-4) external coefficient differences
away from the upper pin and an O(N^3)-row upper collar with the
unimproved O(N^-3) coefficient. Both would yield O(N^2).

Continue only if the complete external difference and divergence
bounds include all normal end rows, all product modes and the actual
upper jump; abandon any argument treating k as smooth, commuting
M with Phi, or dropping a boundary contribution. No estimate or limit
is yet claimed by this working note. Essential inputs: L028 L185
L212 C212b C212h, with C212b's imported L182/L186 covariance bounds.

Completed in [C212i](../lemmas/C212i-complete-quartic-probe-response-subcubic.md):
the full endpoint is O(N^(5/2)); its pure-prefix internal tilt is
O(N^2) by exact diagonal-difference summation by parts, including the
entire O(N^3)-vertex boundary collar. C212h then gives
O(N^(5/2)log(eN)) and a zero cubic limit for the complete quartic.
The summation-by-parts sign is fixed by the canonical proof's
Dk(e)=k_head-k_tail and positive transpose identity.
The rational word certificate checks all 27 cubic words and all four
checks pass. The analytic estimates are not numerical certificates.
Full compensation and the independent construction gaps remain.
Continue with a separate critical audit under the unchanged approved
target, concentrating on (3)--(4), (8), the complete incidence
divergence (14)--(15), both actual external heat sums and C212h(6).
