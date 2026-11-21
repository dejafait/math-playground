# Expanded finite-matrix attempt, step488

The exact approved target and saved EXPLORE assessment from step483 are
unchanged. The main gap remains L030-L032/C032a actual-Xi positivity.
A full common neutral E+/-2X margin could pay nearest-neighbor
interactions through C744i(6); remote, non-neutral, odd and all-window
questions remain independent. Prior failed budgets are preserved.

Use C744j(1)-(9), C744k(1)-(12), C744l(1)-(9)/Section6 and the saved
step487 coefficient evidence. This bounded implementation expands the
certified principal section from indices2,3,256 to indices2,...,17,256,
retaining all257 projection rows and all mutual interactions in this
section. The contiguous low modes test the small finite margin that
the isolated lowest two columns could not test. Save all exact
coefficient and matrix interval operands. A shifted interval LDL
factorization, rather than diagonal dominance, will test the bound
I/25. Its pivots certify the shifted matrix only if every interval
pivot is strictly positive; an unenclosed eigenvalue decides nothing.

Continuation test: both expanded blocks enclose >=I/25 with arithmetic
widths <1e-30. Failure of this sufficient budget alone is inconclusive
about the full fixed target. Only a certified exactly neutral smooth
ratio>=1/2 refutes that target. Success of a principal block is still
insufficient for the full255-dimensional matrices; all omitted columns
and their couplings remain unpaid. No new mathematical mechanism,
source import, cross-notebook input or audit of C744i/j/k/l is claimed.

If computation is interrupted, preserve this draft and any completed
coefficient/matrix artifacts. Do not promote a partial artifact to a
complete certificate.

## Implementation details retained during computation

The head matrix can use already enclosed projection moments:
<z_n,T_m>=<p_n,T_m>-r_n<p_(n mod2),T_m>. This is precisely the
definition of z_n, in the real unitary-coordinate basis. It avoids
repeating a separate polynomial-product integral; it deletes no term.
Gram products are evaluated once in the upper triangle and reflected
to the lower triangle, using their exact real symmetry. The complete
projection covariance still subtracts all257 rows before the head is
symmetrized. All saved step487 subblock operands will be compared.

For A=S_T,s|_I-(1/25)I the exact LDL recurrences are

    D_j=A_jj-sum_(k<j) L_jk^2 D_k,
    L_ij=[A_ij-sum_(k<j)L_ik L_jk D_k]/D_j, i>j,
    L_jj=1, L_ij=0 for i<j.

Provided earlier pivots are positive, ordinary finite Gaussian
elimination proves A=L diag(D_j)L^T by induction over columns.
Outward interval arithmetic encloses these exact recurrences; division
occurs only after the pivot's lower endpoint is positive. Thus all
positive enclosed pivots imply A positive definite. This proves a
lower bound1/25 for this principal matrix, not a spectral lower bound
equal to the smallest pivot and not a bound for any omitted direction.
This elementary argument explains the implementation of the assessed
finite square-completion method; it is not a new general theorem.

The completed minus-sign calculation is saved in
`scripts/adjacent-neutral/matrix-enclosure-488.json`: all17 shifted
pivots have positive lower endpoints (minimum>0.2947), and all
head/Gram/covariance/Schur interval widths are <1.044e-236. The
plus-sign calculation and complete saved-operation replay remain
pending at this intermediate checkpoint. No full-matrix conclusion.

## Completed bounded attempt

Both sign calculations completed. C744l Section7 is the canonical
proof and qualification record: both17-dimensional principal matrices
are >=I/25. All10 computation and35 full saved-operation replay checks
pass, including every shifted factorization operand, old subblock
comparison and the exact reported width/pivot thresholds. The maximum
matrix width is <1.046e-236 versus1e-30 required. The replay uses the
same interval routines and does not independently audit the analytic
inputs or regenerate all coefficients. The previously pending plus
calculation and replay above are now complete.

The full255-dimensional inequalities remain unproved: columns18,...,255
and every interaction involving them are absent. This is local
implementation progress using assessed known tools, not a full margin
or a new mathematical discovery. C744i/j/k/l remain independently
unaudited. Continue the unchanged ready full-certificate target;
preserve the sufficient1/25 threshold and all earlier failed budgets.
