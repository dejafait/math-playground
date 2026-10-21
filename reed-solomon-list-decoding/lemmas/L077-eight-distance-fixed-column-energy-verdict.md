# L077 — The fixed distance-eight column passes the whole-base energy test

## Hypotheses

Use L021's original pairs, L053's positive singleton rho and L075's entire
unchanged represented dictionary. Let C be L073's included-anchor PSD
matrix in its normalization by rho. Its indices are {D} and every {D,E}
with |D\E| in {5,6,7}, where D,E are 68-subsets of a 1024-point set.
Thus C has anchor diagonal 1 and anchor/layer-l entry p_l.
The excluded-anchor matrix of L075 is not substituted for C.

Fix a 68-subset G with |D\G|=8. Let b be exactly L076's rational column,
with anchor entry and proposed diagonal

    p8=16792471/1181138102168120460>0.

Retain the original RREF at (0,v_dagger,w_star), all 28 forced and 36
completed seven/seven entries, all represented lookups and forbidden
zeros, and precisely L076's active-set (27,33,56,63) solution. There is
no parameter optimization, retuning, simultaneous new column, new scalar
constraint or other-anchor condition in this statement.

## Conclusion

The full-space generalized-Schur energy E=b^T C^dagger b obeys

    1461591/10^12 <= E/p8 < 1461592/10^12 < 1.

Consequently [C,b;b^T,p8] is PSD. Multiplying the entire enlarged matrix
by positive rho gives one PSD extension of the original retained matrix,
for every D,G with the stated half-distance.

This is a finite REPRODUCTION/specialization of assessed known tools,
without a claim of progress beyond the sources as original mathematics.
The separate critical proof review below retains this calculation.
This parks exclusion by
this fixed-column energy test only. Simultaneous columns, other anchors,
unrepresented/global moments, representing measures, packings and RS
realization remain unproved. The arbitrary-center 67/68-agreement gaps
and the 955–957 bracket are unchanged.

## Proof

**Imported criterion.** The prior SPECIALIZE assessment is
`drafts/literature/2026-10-17-distance-eight-fixed-column-energy.md`.
Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, Acta Scientiarum Mathematicarum, version of record
27 February 2026, DOI 10.1007/s44146-026-00231-y,
[Section 2, Theorem 2.6, Corollary 2.2 and Lemma 2.7(ii)](https://link.springer.com/article/10.1007/s44146-026-00231-y).
For finite real symmetric C, the enlarged scalar block is PSD exactly
when C is PSD, b is perpendicular to ker C, and p8>=b^T C^dagger b.
The proof of Lemma 2.7(ii) identifies C^dagger with the inverse on the
range and zero on its orthogonal complement; finite-dimensional ranges
are closed. No nonsingularity or maximal-rank assumption is required.
Foundations/10 records the inspected proof cases. This source theorem
is imported, not reproved. L073 supplies PSD of precisely C and L076
supplies whole-kernel compatibility of precisely b. Neither input gives
the new energy, so the finite specialization is necessary.

**Weighted lift, including the anchor.** Use L076's complete orbit order:
anchor first, then lexicographically (l,i,j), l=5,6,7 and 0<=i,j<=l.
There are 150 coordinates. Their actual positive sizes are

    W_0=1,
    W_(l,i,j)=binomial(8,i)binomial(60,l-i)
                 binomial(8,j)binomial(948,l-j).

They sum on each layer to binomial(68,l)binomial(956,l). Let J lift orbit
values to their orbit-constant full vectors. L076 gives CJ=JQ and
J^T J=W, with W the diagonal matrix of these sizes. Its complete action
Q retains Q_00=1, Q_0a=p_l W_a and Q_a0=p_l. Both rectangular directions
of every shell action are retained and WQ=Q^T W. Write b=J*b_hat.

As in L066's reviewed lift, an exact solution Qz=b_hat gives C(Jz)=b.
By the cited range-inverse property, C(C^dagger b)=b. Thus
Jz-C^dagger b lies in the full ker C. L076's full-space compatibility
then gives b^T(Jz-C^dagger b)=0, proving

    E=b_hat^T Wz=sum_(a=0)^149 W_a*b_hat_a*z_a.

This argument includes noninvariant directions of the original matrix.
It does not identify the nonsymmetric quotient with a Euclidean Hermitian
matrix, claim z is the weighted Moore–Penrose vector, or replace the
actual orbit sizes with product-mode multiplicities. The anchor remains
in the primary solve and energy; no pseudoinverse congruence is used.

**Exact inverse specification.** L076 gives the monic orthogonal factor
bases h_(n,l,a)(i), with weights binomial(8,i)binomial(n-8,l-i), their
positive squared norms N_(n,l,a), and all 64 exact action blocks B_ab.
These bases and blocks are mathematical inputs with complete finite
recipes and reviewed action identities. On mode (a,b), retain each layer
l>=max(a,b) in {5,6,7}; retain the anchor only for (a,b)=(0,0).

For each retained shell layer define the column coefficient

    beta_(ab,l)=sum_(i,j=0)^l W_(l,i,j)*b_hat_(l,i,j)
                  *h_(68,l,a)(i)*h_(956,l,b)(j)
                  /[N_(68,l,a)*N_(956,l,b)].

For the constant-mode anchor put beta_(00,0)=p8. In each block solve
B_ab*v_ab=beta_ab by exact Gauss–Jordan elimination: in increasing
column order choose the first nonzero remaining pivot, swap it into
place, divide by its pivot and eliminate that column from all other
rows. Set every nonpivot variable to zero. All resulting zero rows have
zero right side. This fixes a rational solution, including singular and
zero-block cases. Define

    z_0=v_(00,0),
    z_(l,i,j)=sum_(a,b=0)^l v_(ab,l)
                       *h_(68,l,a)(i)*h_(956,l,b)(j).

The complete local right sides, local solutions and all 150 coordinates
are saved. The modal equations produce a candidate inverse action, and
the decisive certification checks every original row of Qz=b_hat.
All 150 exact residuals are zero. Thus the weighted lift applies without
relying on an unverified projection normalization or a selected subsystem.

The complete 150 individual energy terms and their full rational sum are
saved. Write the reduced exact ratio E/p8=N/D with D>0. Integer arithmetic
verifies

    10^12*N-1461591*D >= 0,
    1461592*D-10^12*N > 0.

It also verifies E>=0 and p8-E>0. These checks give the displayed strict
upper bound and hence the source criterion's PSD conclusion. Positive-rho
scaling is applied to the entire enlarged matrix. L076's ordinary point
bijections transport this fixed construction to every D,G at distance
eight; no actual-label constraint is transported or averaged.

**Complete evidence and independent reconstruction.** Reproduce from
this notebook, with no floating point or optimizer:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/eight_distance_fixed_column_energy.py --prepare-only
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/eight_distance_modal_inverse.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/eight_distance_fixed_column_energy.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_eight_distance_fixed_column_energy.py

The constructor consumes the complete relevant L076 constructor,
verification and critical-audit certificates and immutable L075 inputs.
It checks their hashes, original rho/pairs, parameters, RREF column,
completion and all 270 base types. It reconstructs the active-set column,
all actual orbit weights, all 118 factor transitions and the complete
150-by-150 action directly from subset counts, matching every entry to
L076's audited action. It checks weighted symmetry and all 90 original
weighted kernel residuals. The full inverse and every original residual
are consumed; complete energy terms, ratio, diagonal and remainder are
saved in `scripts/finite-support/eight-distance-fixed-column-energy-results.json`.
All 514 constructor checks pass with no failures.
The block solve and its full residual check are separately retained in
`scripts/finite-support/eight-distance-modal-inverse-results.json`.

The independent standard-library verifier imports no notebook module,
solver or decimal arithmetic. It reconstructs rho and p8 from L021/L053,
all 270 immutable base types from L075 with actual support sets and all
six presentations, and every new column lookup from full unordered atom
keys. A fresh four-by-four rational solve recovers exactly the active-set
point; every original compatibility equation and sign is retained.

For each factor n=68,956 fix an actual eight-set U and l-set X meeting it
in i points. Enumerate every subset Z of U union X and count
(|Z intersection U|,|Z intersection X|,|Z|). Completing Z outside this
union contributes binomial(n-|U union X|,m-|Z|). These independent actual
subset histograms reconstruct every action entry, including both
rectangular directions and the anchor. Every original residual for the
saved inverse is then checked with this reconstructed action. This is
an independent certificate of inverse action, not reliance on the modal
solve status or a summary of its output.

For a further normalization check, put r_a=b_hat_a-p_l*p8 on shell l
and H_ab=Q_ab-p_l*p_m*W_b on shell layers l,m. The anchor equation is
z0+sum_(b>0) p_m*W_b*z_b=p8. The verifier checks all 149 equations
H*z_shell=r directly, and the full energy identity

    E=p8^2+sum_(a>0) W_a*r_a*z_a.

The positive anchor term is retained; this transports the entire enlarged
matrix and column, without transporting a pseudoinverse. All 90 weighted
kernel residuals, all 150 original and 149 transported inverse residuals,
every energy contribution, the bilinear z^T WQz, and the entire rational
ratio/remainder agree. Full independent evidence is
`scripts/finite-support/eight-distance-fixed-column-energy-verification.json`.
All 23837 independent checks pass with no failures.
The complete summary, exact interval and empty failure lists are inspected;
the programs consume the complete relevant arrays, not bounded previews.

The initial direct 60-coordinate elimination was stopped during costly
rational back substitution, before producing any energy verdict. The
original implementation remains available with `--direct`. The first
Fraction-by-Fraction full residual evaluation was likewise stopped before
a verdict. Clearing the inverse and each action row's denominators permits
exact integer dot products without that intermediate growth. No coefficient,
column or test changed; the working record preserves these computational
interruptions. There is no failed mathematical sign or residual hidden by
the change of solver. The arithmetic verification within that attempt is
distinct from the separate critical review below.

**Separate critical proof review — step 270, 2026-10-17.** Reuse the
prior SPECIALIZE assessment
`drafts/literature/2026-10-17-distance-eight-fixed-column-energy-critical-audit.md`.
This review retains the exact hypotheses and conclusion without retuning
or a mathematical repair. It verifies a local reproduction, not an
original result beyond the checked sources. Sano Theorem 2.6 and the
range-inverse argument in the proof of Lemma 2.7(ii) are used with the
finite real symmetric full C. PSD of precisely the included-anchor base
is imported from L073; the immutable dictionary comes from L075 and
whole-kernel compatibility from L076. This review checks their matching
normalizations and arrays, rather than claiming new audits of those
entire input proofs. The excluded-anchor matrix is never used as C.

For completeness of the lift, the full indices are partitioned by the
four regions D\\G, D intersection G, G\\D and outside D union G, of
sizes 8,60,8,948. Each orbit-indicator column of J has disjoint support
from the others, and its squared norm is exactly its actual size W_a.
This gives J^T J=W, with the anchor column of norm one. For a fixed
support in orbit a, summing the entries of C over orbit b counts the
head and tail choices independently by L076's displayed four-region
subset counts. This is Q_ab, so every row, including both rectangular
orientations and the anchor, gives CJ=JQ. These statements concern the
full matrix, not just an invariant quadratic form. Thus the saved exact
Qz=b_hat implies C(Jz)=b. Subtracting C^dagger b leaves a full-kernel
vector; its inner product with b vanishes by L076. No noninvariant energy
term can remain. This justifies E=b_hat^T Wz without treating Q as a
Euclidean Hermitian matrix or z as a Moore–Penrose vector.

Rerunning the independent actual-subset verifier gives all 23837 checks
passing. It reconstructs every old/new actual six-presentation lookup,
the original p8 and positive rho, the unchanged active-set column, all
150 actual weights and every entry of the original action. It checks
all 90 original weighted kernel residuals, all 150 original inverse
rows and all 149 transported shell rows. Every exact energy contribution
and the full ratio and remainder agree with the original certificate.
The original RREF parameters, all 28 forced/36 completed seven/seven
entries and every full-key lookup are unchanged.

The additional audit consumes all three complete L077 certificates and
the canonical L076/L075 input arrays. It reconstructs the six factor
polynomial bases from their moment equations: for degree a solve for
the coefficients below the monic leading term against powers 0,...,a-1.
The moment matrix is positive definite because a nonzero polynomial
of degree less than a cannot vanish at all l+1 distinct nodes and all
node weights are positive. Every reconstructed value, orthogonality
equation and positive squared norm agrees. The product bases, with the
anchor retained, exhaust all 150 invariant coordinates.

Let S denote these product-basis columns in orbit coordinates and B the
direct sum of the 64 saved mode actions. The audit checks every one of
the 22500 coordinates of Q S=S B directly, using the independently
reconstructed full Q; it does not rely only on block summary ranks or
projected residuals. It recomputes every right-side projection with the
actual weights and positive factor norms. Independent forward elimination
and back substitution, with the first available nonzero pivot in each
column and nonpivot variables zero, reproduces the prescribed modal
inverse. All 60 nonzero pivots, every singular or zero row, complete
echelon arrays and every original block equation are retained. The
resulting 150-coordinate lift agrees exactly with the constructor, modal
and verifier inverse vectors. Uniqueness of the pivot-variable solution
with free variables fixed at zero identifies it with the manuscript's
Gauss–Jordan prescription; no inverse on a singular block is assumed.

Using this freshly reconstructed z, the audit checks all original
Qz=b_hat rows again. Eliminating the anchor row from the entire enlarged
matrix gives H*z_shell=r with r_a=b_hat_a-p_l*p8 and
H_ab=Q_ab-p_l*p_m*W_b. All 149 original transported rows agree exactly.
Substitution of the anchor equation into the complete weighted sum
gives E=p8^2+sum_(a>0) W_a*r_a*z_a. All 150 terms on both sides are
checked individually, including the strictly positive p8^2 term; their
sum also equals z^T WQz. Individual signed terms are not asserted to
be positive. The complete reduced rational E/p8=N/D, D>0, satisfies
the two manuscript integer comparisons 10^12*N-1461591*D>=0 and
1461592*D-10^12*N>0. The exact scalar slack p8-E is strictly positive.
Sano's criterion therefore gives precisely the stated one-index PSD
extension, followed by positive scaling of the entire matrix by rho.

Run the separate audit after the independent verifier:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_eight_distance_fixed_column_energy.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_eight_distance_fixed_column_energy.py

All 23866 additional exact checks pass, with no failures. Full evidence
is `scripts/finite-support/eight-distance-fixed-column-energy-critical-audit.json`:
complete reconstructed factor values, all modal right sides and solves,
every pivot and elimination stage, all 22500 action residuals, the entire
inverse, all original/transported residuals, actual weights, energy terms
and exact integer comparison gaps. Programs consumed the complete
relevant arrays; full summaries and empty failure lists were inspected
after completion. An initial invocation stopped at a missing closing
parenthesis before executing any calculation; correcting that syntax
changed no mathematical input or prior certificate.

This retains ATTEMPTS/059's stop on the fixed energy exclusion only.
The construction is equivariant under ordinary point bijections, not
transport of RS label constraints. It supplies no simultaneous-column
completion, other-anchor verdict, global moment assignment, representing
measure, packing, RS realization or improvement to the 955–957 bracket.

## Mathlib

Full matching prescribed distance-eight weighted energy/PSD extension:
not checked. Supporting singular PSD, Moore–Penrose range inverse,
finite-group averaging, orbit lifts and exact rational solve coverage:
not checked. Unknown availability is not evidence of absence.
