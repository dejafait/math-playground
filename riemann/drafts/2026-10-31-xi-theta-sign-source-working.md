# Exact-theta Fourier-sign source review — retained working notes

Literature-only step. The supplied target is the three-mechanism comparison,
not a proof of a new sign inequality. No lemma or mathematical script is edited.

L019/L020 fix k(u)=K(|u|), F=2Xi. L233's already-proved normalization is
A(z)=integral_R s^2 k(s+z)k(s-z) ds on the real axis, with
Ahat(2t)=Xi'(t)^2-Xi(t)Xi''(t). Extension to the open complex strip must
be justified if used later; L239 provides closed-substrip bounds for k.

Existing failures screened: L560 and L562 concern reciprocal densities,
not the exact theta correlation; C567a excludes three complete finite
Hermite discriminants from global SOS, outside their certified height
intervals; L569 obstructs generic absolute-error compensation at multiple
zeros, not actual signed cancellation. L233, L234 and the September 23
associated-kernel records already stop automatic autocorrelation and raw
finite-theta positivity. The October 31 translate review already read the
remaining Dimitrov–Xu proof and found no approximation/error interface;
its phase warning remains unresolved here. These assessments are reused.

New primary reading: E. O. Tuck, On positivity of Fourier transforms,
Bull. Austral. Math. Soc. 74 (2006), 133–138,
https://doi.org/10.1017/S0004972700047511 . Read pp.133–137, including
the pairing argument (3)–(4), contour conditions (5)–(7), the bounded-shift
warning pp.135–136, the simple-pole case (8)–(10), and the eventual-sign
discussion (11)–(13). Read p.138's application warning separately:
its V and inverse kernel differ from Xi and the present A. It reports
other singularities on the proposed boundary, not a verified theta
boundary positivity theorem. No identification with its u is made.

The bounded-shift warning and simple-pole restriction give a concrete
source-applicability question: test whether delta*A(i(pi/4-delta)) tends
to +infinity. This is a proposed radial growth test, not a computed bound.
Its success would rule out only radial O(delta^-1) models at this point;
it would NOT rule out arbitrary integrable boundary traces, stronger
singularity methods, regularization or contour subtraction. All horizontal
boundary limits, other singularities and sign conditions remain unproved.
No essential singularity or nearest-singularity classification is claimed.

This is an ordinary analytic discriminator. A creative central sign
attempt is not justified by the checked sources: no control of the
boundary signed transform, especially through zeros, has been identified.
