# Transverse H: projected alternating-kernel moment test

Work in progress under the unchanged complete other/other EXPLORE
assessment `drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
Main gap: interacting ultraviolet control; immediate gap: cubic control
and a limit for R_H,tr. This step tests the sufficient parity-transfer
strategy that bounds each complete projected alternating kernel's first
absolute spatial moment before multiplying the remaining trace factors.
The actual trace remains L099(2), with min(s,t), both exterior levels,
all heat modes, pinned rows and the full generator unchanged.

Import L088(11)--(13), not a centered-path replacement. For normalized
constant exterior v set w_j=v_j cos(theta_j/2), d_j=2sin(theta_j/2),
lambda=|d|^2, P=d d^T/lambda, Q=I-P. Summing all transverse planes
suggests S_v=2[2(w dot d)I-d w^T-w d^T], hence the complete gh symbol
alpha_v=P iS_v Q=-2i d w^T Q. This identity and the following test
are being checked, not yet an established bound or obstruction.

The proposed necessary estimate for this factorwise absolute method is
sum_z |z| |(alpha_v)^vee_jj(z)| < infinity for each v and j. Its diagonal
symbol should be -2i[v_j sin(theta_j)-(d_j^2/lambda) sum_l v_l sin(theta_l)].
It vanishes on coordinate axes but on theta_j=t, theta_k=sigma t is
-i sin(t)(v_j-sigma v_k). For nonzero v a diagonal is therefore not
C^1 at zero. Absolute first Fourier moments would imply C^1 by uniform
termwise differentiation. Check this implication and finite-periodic
truncations explicitly before recording a route decision.

Plausible use: determine whether a coefficient difference O(a|z|)
can be bounded uniformly by separate projected-kernel moments. Failure
would stop this sufficient estimate only. It would not stop a joint
closed-trace moment estimate, prove signed growth, or replace the
physical boundary analysis. Continue only on a finite full-spectrum
moment or a rigorously failed necessary condition of this stated
method. Existing stops 028--031 remain; this is not a repeat of the
individual-generator-filter commutator or symmetric-generator test.

Essential inputs: L088 L095 L099 L108. L028 controls actual coefficient
smoothness. L085 L091 define the complete sector assembly. Other limits
L097 L098 L100 L101 L104 L107 remain unevaluated; L084/L079/L080/L082
fix the comparison and arithmetic qualifications. No actual finite-box
parity reduction, boundary gain, cubic limit or compensation is assumed.

Completed: L109 establishes the exact projected symbol, proves that
every nonzero v has a diagonal kernel with infinite first absolute
moment, and proves divergence of its finite periodic diagnostic
moments without a rate. The argument uses all original paths and
planes. ATTEMPTS/032 stops the factorwise absolute estimate only.
It supplies no actual pinned commutator lower bound or signed growth.
The proof above is now canonical in L109; the initial proposed
calculation is preserved as the attempt record.

Continuation within the unchanged approved complete-group target:
test a joint circulation/covariance energy estimate directly in
L099(2). Start from the exact six-term Omega identity L088(3) and
P D^T=0, keeping its exterior-circulation terms. Determine whether
the two surviving circulation factors can be combined with K_h
before estimating coefficient differences, so that only quadratic
kernel sums are needed. This differs from assigning a finite first
absolute moment to either projected alternating map. It is a
proposed proof mechanism, not an established decomposition estimate
or an assertion that a signed commutator gains O(a).

The bounded test is an O(N^3) bound for the actual R_H,tr, including
the coefficient-difference and pinned-boundary errors, with all
min(s,t), both coefficient levels, generator cross terms and exterior
heat modes retained. Continue on a controlled joint energy estimate
or a specific failed necessary condition; abandon the proposed energy
placement if it loses a derivative to an unbounded unsandwiched
projection or simply reproduces the O(N^4) absolute bound. Generic
above-threshold estimates alone imply no signed growth. The a^3
limit and comparison with -12 gamma D_i remain the approved goal,
not assumed consequences of a cubic upper bound.

Essential inputs: L009 L028 L085 L088 L091 L095 L099 L108 L109;
L097 L098 L100 L101 L104 L107 retain the other sector limits.
L084 with L079 L080 L082 fixes the reference and IEEE qualifications.
All coefficient values, compensation, finer powers/logarithm, other
jets, matching, interacting error <=c_box/2, continuum fields/axioms,
reflection positivity and infrared/finite-mass control remain open.
The target and saved assessment are unchanged; no new literature
approval is asserted for a different target or set of hypotheses.
