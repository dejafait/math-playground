# Step65: fixed simplex residual attempt — work in progress

Approved target: Seek one degree-at-most-13 face-preserving polynomial divergence certificate for v'(E)>0 at every zero of L938's actual density on 1/4<=E<=4.

Coverage: unchanged `drafts/literature/2026-11-09-l938-simplex-residual-certificate-test-63.md`, EXPLORE, separately reviewed at step64. Inputs read: L019; L938(5)–(10) and its analytic-kernel argument; L940(1) and its averaging convention. C938a, L937, L940 and L941 are route constraints, not positivity inputs. No new source search or cross-notebook input.

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity. A successful residual would supply only compact-energy upward crossings for this fixed H2 density. Other energies, contacts, degrees, parameter endpoint signs, initialization, realization and continuation remain open.

Bounded test: keep the full 34 rows, twelve factors, factorials and M_0^12; derive the exact unnormalized radial derivative and zero-flux specialization before assessing one polynomial-field construction. Success requires a uniform positive residual margin; a complete dual obstruction would also be informative. A failed subfamily or sampled sign is not a full-class obstruction. Do not enlarge degree, energy interval or affine multiplier class.

Partial reasoning to check: with k(x)=K(sqrt(x)), w(t)=product t_i^(-1/2), W_E=w product k(E t_i), symmetry in L938(9) suggests v(E)=E^17/2^12 integral W_E Pbar. Thus the candidate exact derivative integrand is Pbar(17/E+sum t_i k'(Et_i)/k(Et_i)), with the same positive prefactor E^17/2^12. Analyticity of k at zero is essential for compact differentiation. This paragraph is a working derivation, not a sign claim or a completed certificate.

All earlier changes are preserved. No scheduler state is edited.

## Completed bounded attempt

Canonical proof and qualifications are in
[L942](../../lemmas/L942-actual-simplex-two-field-divergence-obstruction.md).
The derivative was written with the positive common factor E^16/2^12,
so the fixed integrand is D_E=(17+E sum t_i h(E t_i))Pbar. This is the
equivalent Euler normalization of the preliminary formula above.
The chart, uniform differentiation and all face cutoffs were justified.

The tested construction was the degree-13 simplex gradient of Pbar,
with its natural lower-degree gradient-of-sum-of-squares correction.
An exact three-point dual excludes their entire real linear span;
the full approved field class remains open. The finite calculation
uses all original rows and exact rational full-theta bounds. No
floating-point feasibility result, midpoint root, degree increase,
interval enlargement or new affine-multiplier class was used.

This is a scoped NEGATIVE result, not a failure of the actual crossing
claim. The known integration method is a specialization; originality
of the particular obstruction is uncertified. The proof is pending
separate critical review. A meaningful continuation must use field
columns outside the excluded span and verify their response at all
three configurations; the saved original assessment covers that
unchanged full class. A complete field basis and a full-class dual or
strict residual remain unproved. Current routing belongs in PROGRESS.
