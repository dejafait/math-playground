# Fixed actual-E Rice calculation1657 — working checkpoint

Approved target: assessment1656, SPECIALIZE; REPRODUCTION calculation.
Main gap: actual-Xi all-degree positivity, equivalently the unpaid
C028b height condition. Test only x=-1, c=-1/4, each fixed d>=3.

Inputs read: L829 definitions; L828 Section2 unconditional entire
construction; C048a normalization/principal Lambert bounds; C048j
full relative contract and audited assembly; C028b coefficient definitions;
L021 moment coefficients; assessment647 factorial interface; source-notes1656.
Preserve old L718 and reciprocal-kernel stops: neither decides this test.

In-progress reasoning: P=Phi=K/2, Z=integral_R P=I(1/2).
Consequently E(s)=sqrt(pi)4^(-s)I(s+1/2)/(Z Gamma(s+1/2)).
Duplication should give E(k)=gamma_k/gamma_0. A positive finite
rectangle has residues (-1)^(d-k)binom(d,k)E(k); all four edges stay.

For p=1/4+it, C048j applies eventually with error tending to zero.
Writing W_0(2p/pi)=U+iV, modulus and argument identities suggest
U~log t, V->pi/2, arg(w)~pi/(2log t). The proposed outcome is
log|I(p)|=-(pi+o(1))t/log t, while the reciprocal gamma contributes
+pi*t/2. Need finish both-sided estimates, compact-line continuity,
conjugation and the integral lower bound before declaring divergence.
No convergence or unbounded-contour formula has yet been certified here.

Completion: the reasoning above was finished in canonical C048k.
Its two-sided bound proves the proposed positive logarithmic rate and
absolute divergence; finite residues are normalized explicitly. This
working checkpoint preserves the pre-completion reasoning, not a second
proof. An independent critical audit remains pending.

Continuation test: a positive limit of log|weighted E|/|t| stops
this absolute opening. Finite residues remain valid; conditional
regularizations, other interpolants, closing edges and signed
degree-uniform transfer are outside this calculation.
