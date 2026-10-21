# L066 — The fixed distance-seven column passes the coupled-base energy test

## Hypotheses

Use L061's complete anchored five/six-shell matrix, divided by L053's
unchanged positive singleton rho. Retain every entry of L062's immutable
represented dictionary and every original pair. In particular
p5=1/68881143660, p6=133/9357995374380 and
p7=3539/248922676958508. Fix 68-subsets D,G of a 1024-point ground set
with |D\G|=7. The retained indices are {D} and all {D,E} with
|D\E| in {5,6}.

Use exactly L065's rational column: its anchor entry and new diagonal
are p7, its represented entries are unchanged L062 moments divided by
rho, its forbidden-distance entries are zero, and its free coordinates
are specified by u=v=0,w=-c_4/a^42_4 in L065's affine system. Do not
optimize that three-parameter family. No new scalar upper constraints,
labeled constraints, multiple new columns or global completion are imposed.

## Conclusion

Let C be this normalized retained matrix and b the fixed column. Its
generalized-Schur energy E=b^T C^dagger b satisfies the exact bounds

  3/10^9 <= E/p7 < 4/10^9 < 1.

Consequently [C,b;b^T,p7] is positive semidefinite. Multiplication by
positive rho gives a one-column PSD extension of the actual retained
matrix for every D,G with the stated half-distance.

This is a finite REPRODUCTION/specialization of assessed tools, without
a mathematical novelty claim. It parks exclusion by this fixed-column
energy test only. The separate critical proof review below retains it.
The compatible family is not optimized; simultaneous new columns,
global moments/PSD, other scalar rows, labels, measures, packings and
common-center RS realization remain unproved. Arbitrary-center safety
at 67/68 agreements and the 955–957 bracket remain unchanged.

## Proof

**Imported singular criterion.** Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-14-seven-distance-fixed-column-energy.md`.
Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, Acta Scientiarum Mathematicarum, version of record
27 February 2026, DOI 10.1007/s44146-026-00231-y,
[Section 2, Theorem 2.6, Corollary 2.2 and Lemma 2.7](https://link.springer.com/article/10.1007/s44146-026-00231-y).
For a finite real symmetric C, the block [C,b;b^T,d] is PSD exactly
when C is PSD, b is perpendicular to ker C, and d>=b^T C^dagger b.
The proof of Lemma 2.7(ii) identifies the inverse on the range and zero on its orthogonal
complement. Finite-dimensional ranges are closed; no nonsingularity or
maximal-rank hypothesis is required. Foundations/10 records the inspected
proof cases. No source theorem is reproved. L061 supplies PSD of the
full retained matrix, and L065 supplies full-kernel compatibility of
this exact nonnegative b. Computing this column's energy is a necessary
specialization because the sources do not evaluate the prescribed data.

**Full-space weighted realization.** Keep the original anchor, without
a congruence in the primary computation. Use L065's ordered 86 orbits:
o0=(0,0,0), then (l,i,j) lexicographically with l=5 followed by l=6,
0<=i,j<=l. Their actual sizes are

  W0=1,
  W_(l,i,j)=binomial(7,i)binomial(61,l-i)
             binomial(7,j)binomial(949,l-j).

These are all positive. Let J send an orbit-coordinate vector to its
orbit-constant full vector, and W=diag(W_a). Then J^T J=W. L065's
complete subset counts give CJ=JQ for its exact anchored action Q.
The anchor entries are Q00=1, Q0a=p_l W_a and Qa0=p_l on layer l;
the remaining entries use all unchanged five/five, five/six, six/five
and six/six coefficients. In particular WQ=Q^T W. This quotient is
not treated as a Euclidean symmetric matrix. Its rank 37 is not the
rank of C. Write b=J*b_hat, where b_hat is the entire fixed L065 column.

We compute one rational solution z of Qz=b_hat. Then CJz=Jb_hat=b.
By the proof of Sano Lemma 2.7(ii) and L065's compatibility, x=C^dagger b also satisfies
Cx=b. Thus Jz-x lies in ker C, and L065 gives b^T(Jz-x)=0. It follows
that the exact full-space energy is

  E=b^T C^dagger b=b^T Jz=b_hat^T W z
    =sum_(a=0)^85 W_a*b_hat_a*z_a.

This argument licenses any exact inverse-action solution. We do not
claim z itself is the weighted Moore-Penrose inverse vector; it need not
be orthogonal to ker Q. There is no Euclidean pseudoinverse of Q, no
pseudoinverse congruence assertion, and no multiplicity substituted for
the actual orbit norms. Coupled singular and anchor directions remain
in every original residual.

**Exact rational specification and solve.** All entries of Q, W and
b_hat have L065's finite recipes and immutable inputs. Retain precisely
its u=v=0,w=-c_4/a^42_4 column, including anchor entry p7. The selected
coordinate list, in its original order, is

  P=(0,1,2,3,4,5,7,8,9,10,13,14,15,19,20,21,25,
     37,38,39,40,44,45,46,47,51,52,53,54,58,59,60,
     65,66,72,73,79).

Let R=Q_(P,P). Solve R*z_P=(b_hat)_P and put z_a=0 for a outside P.
This specifies exact fractions, rather than an unspecified solution.
Fraction-free elimination clears denominators separately in each
augmented row and divides out its nonzero integer gcd. Each subsequent
row replacement is row_s <- (x row_s-y row_j)/g, with x nonzero and
g a nonzero gcd; row swaps are invertible. The resulting 37-by-37
coefficient matrix is triangular with every diagonal nonzero, so R is
invertible. Exact rational back substitution gives the complete z saved
below. Its 37-coordinate solve alone would not prove full inverse action:
all 86 residuals sum_b Q_ab*z_b-b_hat_a are additionally checked to be
exactly zero. All 49 weighted original kernel residuals are also retained.

The certificate saves all 86 individual energy contributions, their
exact rational sum E, E/p7 and p7-E. Full substitution gives the displayed
rational interval. This is an exact integer cross-multiplication check,
not a decimal approximation. E>=0 and p7-E>0. Applying Sano's criterion
to the normalized matrix proves the stated one-column PSD extension.
Multiplying the entire enlarged matrix by positive rho preserves PSD;
there is no need to transport a pseudoinverse under scaling. L065's
point-bijection equivariance gives the same conclusion for every D,G at
half-distance seven, without actual-label averaging.

**Complete certificates and independent arithmetic.** Run

  `python3 scripts/finite-support/seven_distance_fixed_column_energy.py`.

Its full certificate is
`scripts/finite-support/seven-distance-fixed-column-energy-results.json`.
It consumes the complete L065 constructor and critical-audit certificates,
checks immutable input hashes, reconstructs all 121 base entries from
L062's full dictionary and every quotient entry from L065's subset counts,
and compares every action entry, weight and column coordinate. It
reconstructs every free coordinate from the fixed affine parameters,
checks every weighted symmetry identity and kernel residual, and saves
the complete square solve, echelon trace, inverse vector, all original
residuals and actual-versus-required energy values. The additional
identity z^T WQz=b_hat^T Wz holds exactly. All 11378 checks pass, with
no failures. The initial back-substitution implementation attempted
integer division before Fraction conversion and raised an OverflowError;
it produced no certificate. The corrected implementation uses explicit
Fraction arithmetic in the last row and throughout back substitution.

Independently run

  `python3 scripts/finite-support/verify_seven_distance_fixed_column_energy.py`.

This imports no constructor, notebook module, optimizer or decimal
arithmetic. It reconstructs L056's coefficients from its manuscript,
L059's affine column at L060's manuscript minimizer, and L061's six/six
completion, comparing all 121 entries with the unchanged L062 dictionary.
Every represented column key is looked up by all six atom presentations,
all forbidden zeros are retained, and the entire fixed affine witness
is checked. For independent action counts, fix actual seven-set U and
l-set X with |U intersection X|=i. Enumerate every subset Z of U union X.
An m-subset with that intersection with U union X is uniquely Z union T,
where T lies outside U union X, giving
binomial(n-|U union X|,m-|Z|) choices. Sort by |Z intersection U| and
|Z intersection X|. Tensor these two independent count tables for
n=68,956 to reconstruct every action entry, including the anchor.
All 86 original inverse residuals vanish for the saved full z.

As a further anchor check, set r_a=b_hat_a-p_l*p7 for shell orbit a in
layer l and H_ab=Q_ab-p_l*p_m*W_b on the two shell layers. The full
anchor equation gives z0+sum_(b>0) p_m*W_b*z_b=p7. Substituting it into
each remaining row gives H*z_shell=r, and hence

  E=p7^2+sum_(a>0) W_a*r_a*z_a.

The verifier checks all 85 transported residuals and this energy identity
exactly. This is a change of the entire enlarged block with its column
retained, not a pseudoinverse transport. Both shells and the positive
anchor term p7^2 remain present. Every energy contribution, ratio and
Schur remainder agrees with the constructor. All 7931 independent checks
pass, with no failures. Complete evidence is
`scripts/finite-support/seven-distance-fixed-column-energy-verification.json`.
The full failure lists, exact interval and full residual summaries were
inspected. Verification consumes complete action, column and inverse
arrays and compares the entire energy fractions; previews are not proof.

This arithmetic verification alone is distinct from the critical proof
review below. No full SDP, optimal compatible-family energy, new-column scalar
rows, global extension, representing measure or RS list is inferred.
A passing one-column extension does not establish unsafety or improve
the 955–957 boundary. ATTEMPTS/041–043,046,047 retain their original scopes.

**Separate critical proof review — step 225, 2026-10-14.** Reuse the prior
SPECIALIZE assessment
`drafts/literature/2026-10-14-seven-distance-fixed-column-energy-critical-audit.md`.
This review retains the fixed hypotheses and one-column conclusion, with
no mathematical repair or novelty claim. Sano's Theorem 2.6 applies to
the finite real symmetric full matrix C, not to its nonsymmetric quotient.
L061 supplies PSD at these exact entries; L065 supplies full-kernel
compatibility at exactly the specified parameters. The source's range
inverse is identified in the proof of Lemma 2.7(ii); this attribution is
made explicit above. No general source theorem is reproved.

The lift has no missing noninvariant energy component. Actual orbit counts
give CJ=JQ and J^T J=W. Hence Qz=b_hat implies C(Jz)=b. Subtracting
C^dagger b leaves a vector in the full kernel, and its inner product
with b vanishes. This proves the weighted energy formula even though
the chosen sparse z need not be orthogonal to ker Q. Finite point
bijections transport the entire fixed construction to any D,G; they do
not transport any RS label constraint. The two retained shells, anchor
and positive original rho match the hypotheses of the source criterion.

The rerun independent verifier reconstructs every action entry from
actual-subset enumeration and every old coefficient from the imported
manuscript prescriptions. All 7931 checks pass. The separate audit
consumes both complete energy certificates and the audited L065 input.
It constructs actual 68-subsets on 1024 points for all 121 base types and
85 column orbits, counts all eight atoms in all six support orders, and
checks the complete unchanged dictionary, Boolean entries, forbidden
entries, free-key ordering and exact affine parameters. All orbit weights
are positive, their layer sums are the full shell cardinalities, and all
7396 action entries agree with both independent reconstructions and the
audited kernel action, in both rectangular directions. Every weighted
self-adjointness identity is checked.

Starting from the reconstructed selected augmented matrix, clear each
row's rational denominators and divide by its positive gcd. Replay all
666 saved elimination operations. Every row replacement has nonzero
multiplier, every integer division is exact, every saved echelon entry
agrees, and all 37 triangular pivots are nonzero. Independent rational
back substitution reproduces all selected inverse coordinates; all
other coordinates are zero. All 86 original residuals, 49 weighted
kernel residuals and 85 anchor-transported residuals vanish exactly.
The transported column is checked coordinate by coordinate, retaining
the subtraction p_l*p7 and both shell layers.

Recompute every one of the 86 weighted energy terms and all 86 terms
in the anchor-transported energy, including p7^2. Their sums, the
bilinear expression z^T WQz, and both certificates' full energy, ratio
and remainder fractions agree. For the reduced ratio N/D with D>0,
the audit checks 10^9*N-3*D>=0 and 4*D-10^9*N>0 as integer inequalities.
The exact remainder p7-E is positive. Thus the source criterion proves
the claimed normalized PSD extension, and positive-rho scaling gives
the actual matrix. Neither a compatible-family optimum nor simultaneous
distance-seven columns follow.

Run `python3 scripts/finite-support/verify_seven_distance_fixed_column_energy.py`
and `python3 scripts/finite-support/critical_audit_seven_distance_fixed_column_energy.py`.
All 18216 additional audit checks pass with no failures. Complete exact
evidence, actual presentations, replayed echelon, inverse vector, residuals,
energy terms and integer comparison gaps are saved in
`scripts/finite-support/seven-distance-fixed-column-energy-critical-audit.json`.
The initial audit report, preserved at
`scripts/finite-support/seven-distance-fixed-column-energy-critical-audit-initial.json`,
has one bookkeeping failure: raw JSON compared reduced 1/250000000 with
unreduced 4/10^9. Its mathematical inequalities and residuals all passed.
Canonical rational encoding repairs that comparison; it changes no
mathematical input, inverse coordinate or energy. The complete passing
summary and empty failure list were inspected after the corrected run.
This retains only the fixed one-column result and ATTEMPTS/048's bounded
stop; all simultaneous, global, scalar and RS limitations remain in force.

## Mathlib

Full matching prescribed fixed-column mixed-shell energy theorem: not
checked. Supporting singular PSD, Moore-Penrose range inverse, finite
orbit actions, weighted linear algebra and exact solve coverage: not
checked. Unknown availability is not evidence of absence.
