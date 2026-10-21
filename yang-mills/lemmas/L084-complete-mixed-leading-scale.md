# L084 — The complete mixed cubic response has a nonzero a^-3 coefficient

## Hypotheses

Use L061's actual SU(2) Gaussian in the straight lower-rooted direction-1
forest on the all-face relative fixed-link box (-4,4)^4. Let a=8/N
through sufficiently fine admitted even meshes. Use both original
L010 Wilson-flow probes i=3,6 at tau=1/16, their actual quadratic
matrices B_i, the actual residual matrix A, and the forest covariance S.
Take the bare small-coupling coefficient at each fixed mesh first,
then let a tend to zero. Retain all three colors, every upper transverse
edge, every transverse plaquette at all levels 1<=s<N, pinned end rows,
both residual placements and the complete exterior heat sums.

Write C=S3_top, Y=S3-C and f=f_(i,0), r=r0 with L061's signs.
Define the complete mixed response by

    M_i(a)=kappa(f,r,C,Y).

This notation denotes exactly L061(2)'s four-cumulant, including the
conditional fluctuation and both observable derivatives, with no extra
ordered-pair or 1/2 factor. Write gamma>0 for the full normalized torus
integral in L070(3), and D_i for the absolutely convergent continuum
series in L080(1)–(2). Here D_i is the continuum diagnostic, not L063's
two-term residual-row sum.

For the strict signs only, assume precisely L082's computer-assisted
enclosure qualifications: L037's saved hexadecimal Fourier table and
certified cutoff/node/weight intervals, and L039's IEEE binary64
addition/multiplication/FMA model, arbitrary summation order, no overflow
and stated underflow allowance. The analytic limit identity below does
not need these numerical assumptions.

## Conclusion

For both actual probes the complete mixed response satisfies

    lim_(a->0) a^3 M_i(a) = 12 gamma D_i.                 (1)

With the stated enclosure qualifications this coefficient is strictly
negative for both i=3 and i=6, since

    -237.289643 < D_3 < -237.289642,
     -98.877430 < D_6 <  -98.877429.

Thus M_i(a)=12 gamma D_i a^-3+o(a^-3); in particular this complete
group is not O(a^-2). No O(a^-2) bound on the remainder is proved.

In L059's fixed-original-law decomposition, let M denote its conditional
quartic, T_*=H-M, and E_mix its retained observable corrections. Then

    M_i(a)=kappa(f,r,M)+kappa(f,r,T_*)+E_mix(f,r),
    lim_(a->0) a^3 kappa(f,r,M)=0,
    lim_(a->0) a^3 [kappa(f,r,T_*)+E_mix(f,r)]
                                             =12 gamma D_i. (2)

Only the joint brace is determined here; neither of its two terms is
evaluated separately. The conditional coefficient is accounted for
inside the same cumulant and is not added to (1) a second time.

This is a finite assembly of existing local results under the saved
SPECIALIZE assessment, classified REPRODUCTION. It is local progress
toward the response calculation, with no claim of progress beyond the
sources checked or mathematical novelty. Other/other cubic pairs, all
other action/measure/insertion/flow and nonlinear forest jets, possible
compensation in the full response, N^2 remainders, slower powers and
the complete logarithm remain unresolved. So do finite matching,
interacting reflected error <=c_box/2 along a specified trajectory,
continuum fields and axioms, full reflection positivity, infrared
control and finite positive mass. There is no Yang–Mills candidate.

## Proof

### 1. Preserve the complete identity and its sign

Import L061(2) and its proof section 2, the established application of
the standard Isserlis Gaussian pairing theorem and finite normalized
Gaussian quadratic tilting. Its covariance derivatives are 2U, 2V,
and 4Z with both orders in Z. The identity includes exactly three
same-row replacements and six ordered distinct-row replacements.
No contraction, differentiation or interchange of mesh limits is
reproved here.

Use L062(3)–(4)'s exact polynomial regrouping to the right rows
(c,b,q) and left rows (d,u(v),Tu). This changes the polynomial product
sign to positive, giving tilted expectation (3/2) sum det C'. Its
mixed derivative is therefore precisely

    M_i=6(T_Z+T_UV),                                    (3)

as stated in L062(1), rather than -6 in the original four-edge
triple-selection representation. The original covariance and both
observables are unchanged. L061's row operation holds throughout the
tilt; it does not delete observable derivative terms.

Denote L063(1)'s residual-row-1 sum by E_i^(1) to avoid confusing it
with D_i. The six ordered (probe row,residual row) pairs partition
exactly into {(2,1),(3,1)} and {(1,2),(1,3),(2,3),(3,2)}.
L063(3) gives

    M_i=6(T_Z+E_i^(1)+T_rem).                            (4)

The first two pairs are in E_i^(1). L064(1) groups (1,2),(1,3) into
its first line, and (2,3),(3,2) into its second line. Its proof
sections 1–2 use the complete pinned endpoint product identity and
co-closed covariance row, with no boundary remainder. There is no
factor 6 in T_rem. This places every one of the nine replacements
exactly once; both covariance orders within each same-row term remain.

### 2. Split the two grouped lines with the actual maps

The first line is linear in the single residual slot W. Split its
right forest lift into its exact direct transverse and axial-prefix
summands. Write their complete signed contributions as F_i^dir and
F_i^ax, keeping the full base row H in both. These are exactly the
first pairs in L074/L083 and L069, respectively. The direct map is
I_T^T; the axial map is J T_ax I_1^T with prefixes r<s<N, as fixed
in L068/L069. No prefix at the separately pinned top vertex is used.

In the second line of L064(1), isolate jointly the two K_1 path/path
monomials. L064(14) defines their alternating path map as
Q_l=M_(t_l,2) B_3-M_(t_l,3) B_2. L064(16) gives their signed
contribution for each exterior product as

    -Tr[K_1 Q_l W_X^T E_+^T M_(Th_k)].                   (5)

This is the sign already present in that second line. Split only
W_X's right lift into the same direct and axial summands. After the
complete heat sum these are exactly S_i^dir from L067(1)–(2) and
S_i^ax from L068(1)–(2). The remaining four determinant monomials,
with their signs and heat sum, are denoted R_i^other. Nothing is
omitted: a three-by-three determinant has six monomials, two are the
K_1 path/path minor in (5), and the other four are those in L064(12).

Consequently (4) has the exact finite-mesh decomposition

    M_i=6[T_Z+E_i^(1)+F_i^dir+F_i^ax
                              +S_i^dir+S_i^ax+R_i^other]. (6)

The splits use linearity in one residual slot, not independent
Gaussian fields or conditional means. They preserve every actual
path operator, covariance weight, upper endpoint and exterior mode.

### 3. Compare every omitted group with the N^3 threshold

L062(2) bounds T_Z=O(a^-3/2). L063(2) bounds E_i^(1)=O(a^-3/2).
L069's conclusion bounds F_i^ax=O(N^2), with the actual complete
base row and all right axial frequencies. L067(2) bounds S_i^dir=O(1),
and L068(2) bounds S_i^ax=O(N^2) using its full level tail before
the adjoint prefix norm. Finally L064(12), summed with its complete
mode majorant (3), bounds R_i^other=O(N^(5/2)). These are estimates
for exactly the slots in (6), with the same box, probes, coordinates,
limit order, pinned rows and level ranges. No stronger full-vector
residual estimate or smooth axial-prefix source is required.

Since a=8/N, the corresponding a^3-scaled bounds are respectively
O(a^(3/2)), O(a^(3/2)), O(a), O(a^3), O(a), and O(a^(1/2)).
All tend to zero. Thus the bracket in (6) other than F_i^dir is
O(N^(5/2))=o(N^3). These bounds are strictly below the current N^3
threshold, although some do not meet the finer N^2 threshold of
the older stopped generic estimates.

### 4. Import the surviving actual trace limit once

L074(9) is the exact identity F_i^dir=bar P_i+bar F_i^circ under
simultaneous exterior and rough-row centering. It is not a frozen
symbol substitution. L083(2) gives bar P_i=O(N^2), so a^3 bar P_i
tends to zero. L079(3) gives
a^3 bar F_i^circ-2 gamma D_(i,a) tending to zero, and L080(2)
gives D_(i,a) tending to its full absolutely convergent series D_i.
The physical weight, positive upper-curvature orientation, constant
axial mode and lower-rooted prefix in these diagnostics are unchanged.
This is exactly L083(3)'s direct-first-pair conclusion in L064's
unmultiplied normalization:

    a^3 F_i^dir -> 2 gamma D_i.

Insert this limit and the six vanishing scaled bounds into (6).
The single prefactor 6 gives 6 times 2 gamma D_i=12 gamma D_i,
proving (1). Gamma is strictly positive by L070(3)'s full torus
integral. L082(1)'s qualified complete enclosures give both strict
negative signs. No finite N=24 sign or newly computed numerical
certificate is used. If those arithmetic qualifications are withheld,
the analytic formula (1) remains, but these numerical sign claims
are not established by this proof alone.

### 5. Account for the conditional term without adding it twice

L061 proof section 2 identifies the same M_i with L059's complete
conditional decomposition, not just its first summand. L059(4)
gives a^2 kappa(f,r,M) tending to the finite value -192 d_* S_i.
Multiplication by the additional factor a therefore gives
a^3 kappa(f,r,M) tending to zero. Subtract this summand from (1)
using the exact decomposition to obtain (2). Neither conditional
centering nor pointwise positivity was used to delete the brace.
Its nonzero joint leading coefficient does not determine its two
individual components or their N^2 coefficients.

The proof uses only the ready exact-target assessment
`drafts/literature/2026-10-08-complete-mixed-leading-scale.md`.
The cited general Ward and flow results cover the framework, not
this bare fixed-boundary coefficient; they are not reproved or used
to force its cancellation. The previous failed generic norm closures
and bulk-profile substitutions remain valid stop evidence within
their own scopes. No complete forest-independent coefficient is
inferred from this forest-coordinate action group. In any later
comparison of overlapping quartic/cubic groups, subtract the shared
quartic once; it has not been added in (6).

### 6. Separate critical audit, 2026-10-10

The approved audit YM-20261010-109-complete-mixed-critical-audit found
no defect in (1)–(2) within their stated scope. This is a separate
analytic check of the existing coefficient, not a new coefficient,
a stronger remainder bound or an independent numerical certification.
The precise audit assessment is
`drafts/literature/2026-10-08-complete-mixed-leading-scale-audit.md`.
The following checks record the mathematical obligations actually
examined; they do not assume that a structural checker verifies proofs.

**Cumulant, sign and exhaustive placements.** In L061's normalized
finite Gaussian tilt, parity leaves exactly

    E[frCY]-Ef E[rCY]-Er E[fCY]-E[fr]E[CY]+2Ef Er E[CY].

This is both the four-cumulant and the mixed derivative of the
normalized expectation of CY. L058(2) has already combined the two
ordered mixed regions, each with factor 1/2. Hence there is no remaining
factor 1/2 or extra multiplicity 2. Internal color contractions vanish;
the six cross permutations give 6 det. The upper triple becomes
-det(d,u(v),Tu)/2 and the right triple is -det(c,b,q)/2. Their product
therefore has expectation +(3/2) det C'. The derivatives of its covariance
are 2U', 2V', 4Z', where Z' retains both inverse-covariance orders.
Each determinant derivative thus has factor four and the common factor
is +6. The three same-row terms, the ordered pairs (2,1),(3,1),
and the ordered pairs (1,2),(1,3),(2,3),(3,2) partition all nine
placements. The base zeros in the curvature column are never used
for a differentiated block.

For the last two pairs the exact identity
h(v)TW-(Th)W_v=T(hW)-(Th)(W_v+W_w) holds also on a pinned end
edge. The full base row has T^T K=0; summing every upper edge kills
only the T(hW) term. Expansion of the remaining determinant gives
the negative K_1 minor in (5), with
Q_l=M_(t_l,2)B_3-M_(t_l,3)B_2. Its other four monomials stay in
R_i^other. Thus the regrouping introduces no boundary remainder,
missing placement or independent conditional term.

**Actual maps and discarded scales.** The residual slot uses precisely
I_T^T+J T_ax I_1^T, with (Jz)_s=sum_(r<s)z_r for 1<=s<N.
The full base H_s=sGT^T stays unchanged in both split contributions.
The upper lift is sqrt(N)E_0^T and its covariance is sqrt(N)G E_0^T.
No physical a or volume weight is added to these ordinary coordinates.
The axial circulation vanishes before residual insertion, since
D J T_ax=0. L069 consequently keeps exactly its four t_1 monomials;
its bound is a^4 N^3 N^3=O(N^2). Its scalar residual norm uses all
right axial frequencies, as verified in L065's polarized form proof.

L067's direct minor retains its actual composed source. Its local
forcing estimate, global four-dimensional L2_a bound and discrete
interior regularity precede residual consistency: the resulting
residual column norm is O(a^3), its paired endpoint column is O(1),
and O(N^3) endpoints give O(1). L068 instead uses the full level tail
||K_(1,N-d)||_HS<=C N^(3/2)d^(-5/2) before the adjoint prefix.
Its factors are sqrt(N), aN^2 and aN^(3/2), giving a^2N^4=O(N^2).
It never assumes that the prefix source is smooth. Both complete
proofs, including their earlier audit sections, were checked here.

L062's three same-row determinants retain both Z' orders and use
complete-array norms. Their worst product is a^3N^(9/2)=O(N^(3/2)).
L063's two residual-row determinants use the separated upper source
||A_0 x_d||<=Ca^5, full right-link variances including normal end
edges, and the O(N^7) pair count; their worst product is
 a^5N^(13/2)=O(N^(3/2)). L041's source proof was checked through
its complete relative axial kernels and consistency application.
For the four non-K_1 monomials, L064 retains either
 a^3N^(3/2)N^4 or a^2N^(3/2)N^3, both O(N^(5/2)).
Every estimate has its polynomial exterior-mode majorant summed
against the full heat coefficients before its constant is used.
Multiplying by a^3=(8/N)^3 removes all these groups. None requires
an O(N^2) estimate for the last four monomials.

**Surviving trace and the unmultiplied normalization.** L074's
simultaneous determinant-one shear changes the path/path allocation
by delta and the circulation/path allocation by -delta. Their sum
is exactly the direct first pair. In particular the O(N^2) exterior
defect is not mistaken for an o(N^2) error. L083 keeps the full
projection Pi=L_0 Sigma in L_0 I_T Sigma_T=Pi I_T. Applying
||K_a x||<=C a^(-1)||D_1 x|| to the columns of E_0G gives
||K_a E_0G||_HS^2<=C a^(-2)Tr G. The leading direct row is
therefore O(N^3). The remainder row is also O(N^3), by the
source-independent operator estimate L078(15). L078's proof of that
estimate uses axial summation by parts and both actual curvature
forms, and does not require a co-closed path source. Consequently
the centered path/path trace is bounded by a^4N^3N^3=O(N^2).
This checks the key applicability point in L083.

L078 cancels the right inverse only on the separate co-closed
circulation source and obtains its exact signed J. In L079's diagonal
proof, the right source is a bounded finite sum of centered differences.
Its low-spectral squared norm is O(sqrt(epsilon)); polynomial spectral
approximation then gives uniform l2 convergence in compact interiors.
The left undifferentiated monopole uses energy convergence, not an
invalid infinite l2 norm. Its undifferentiated coefficient-difference term is
O(a sqrt(N))=o(1), and its differentiated energy tails permit freezing.
The opposite incidence signs in V and T give the local tensor
-4 gamma u R.v; J's prefactor -a^2/2 and the level/vertex sums
produce +2 gamma D_(i,a) after a^3 scaling.
The remaining scaled diagonal error has bounded prefactor a^5N^5
and vanishes after the complete exterior heat tail is controlled.
L080 then uses the correctly normalized columns a f_k/sqrt(lambda_k,a),
positive upper curvature, and actual lower-rooted cosine prefix,
including its zero mode. Its summable double-mode majorant justifies
the continuum limit. Thus the unmultiplied first-pair limit is
2 gamma D_i, and the one common +6 gives (1).

**Conditional bookkeeping, numerical qualification and audit limits.**
L058(8),(20)–(21) were checked alongside L059's complete proof. They
identify the same four-cumulant with its fixed-law conditional quartic
and retained corrections. Its finite a^2 limit in L059 implies
 a^3 kappa(f,r,M)=a [a^2 kappa(f,r,M)] -> 0.
Subtraction establishes only the joint brace limit in (2); it supplies
no limit for either brace component separately. Shared-quartic
subtraction is still required in any later overlapping comparison.

The strict signs are imported from L082(1), whose full canonical proof
and arithmetic qualifications were inspected. The saved audit's complete
result intervals and qualification were read, and its recorded certificate
SHA-256 matches the current certificate:
`1b0c68484a06d041cea7a27ce429e047f5cb91159dd278d743bf8d7891024375`.
This checks artifact identity only. No tensor operation, primitive
interval audit or processor arithmetic was independently rerun here.
The saved-table/IEEE assumptions therefore remain essential to the signs;
this audit does not promote them to an unconditional formal result.

No stronger analytic conclusion is added, and no underlying result is
claimed as a new discovery. The direct-input DAG is unchanged: checks
of L065/L078 and earlier estimates verify the existing imported proofs
rather than insert new premises into the assembly. The old N^2 norm
failures remain valid in their scopes. Complete response cancellation,
the finer remainder, logarithm and all interacting/continuum/infrared
requirements stated above remain unresolved.

## Mathlib

Coverage of the complete specialized mixed-response coefficient:
**not checked**. Supporting finite determinant multilinearity,
Gaussian cumulants, incidence identities, finite trace and
Hilbert–Schmidt inequalities, and elementary limit algebra:
**not checked**. No full matching theorem, absence claim or formal
verification is asserted. The numerical signs keep the explicitly
qualified informal computer-assisted status of L082.
