# Fixed signed mixed covariance — step567 working record

Reuse the exact SPECIALIZE562 target and separate approval563. No
predictor, reference, input cutoff K=65536 or quarter allocation changes.
The main gap is actual-Xi positivity L030-L032/C032a. This attempt pays
the exact-predictor error in the mixed map, an obligation in the approved
fixed test. Downstream use is a certified finite signed map and eventual
Schur assembly; the independent complementary lower form remains open.
Continue if the complete normalized error is below .01, useful compared
with the .5 required norm threshold; otherwise retain the bound as
inconclusive. A full quarter pass or finite-column excess is still the
ultimate test. No diagnostic eigenvalue decides either claim.

Unfinished reasoning saved before calculation: write Y for C999l's
exact free Galerkin predictor and Yhat for its saved dyadic proposal,
with exact neutral Z in both. Then

    v(Y)-v(Yhat)=(I-R^-1 L)Z(Y-Yhat).

The raw-head part is H^-1(H-PLP)Z, small because the reference H is
close to PLP. Propose a finite solve with the saved Hhat,Mhat,Zhat and
verify the full equation residual. Pay H-Hhat, PLP-Mhat, Z-Zhat and
the solve residual explicitly. The raw complementary part is exactly
-2 D_Q^-1 QW0P Z. C999k's complete order
(QW0P)*(QW0P)<=Chat+.0046 I pays its entire infinite norm. Check
Chat<=.172 I by full factor reconstruction. Combine these orthogonal
raw outputs, then use the bounded T/T* pair and C999m's neutral
coordinate norm to bound the mixed-map error on ALL free inputs.
This uses C744v/w, C999k Sections1-2/6, C999l Sections1-7 and C999m
Sections1-4, not a new inverse or FFT theorem. No literature refresh
is needed; the existing source/duplicate/failure review is reused.

The preliminary floating probe gave head-defect Frobenius norm
.017309410429111983 and Chat largest eigenvalue .17079609097894738.
These are proposals only. The script must certify the complete finite
equation and factor and use directed scalar bounds before claiming a
result. Earlier artifacts and the unfinished input decomposition566
remain intact. The full inverse-input tail, finite signed entries and
FFT accuracy, complementary coercivity and whole-core/c_* qualifications
are not resolved by predictor stability.

## Completed calculation and continuation

C999m Section8 is now canonical. The complete operator E=(I-R^-1 L)Z
has norm <.139202988: its raw-head defect is <.018408464, and the
whole raw complement is <.137980434. This gives the normalized
mixed-map predictor error <.007245510<.008 for both the complete map
and its fixed K output truncation. The certificate567 has23 passing
checks and saves the complete proposed head solve and covariance factor.
This is an unaudited local REPRODUCTION estimate under inherited
contracts. The preliminary eigenvalues were not used as evidence.

The failed JSON inspector pointer `/predictor` was corrected after
reading the source schema; the needed field is
`/finite/predictor_free_error`. No certificate check failed. The
earlier large notebook-scoped status output was truncated; subsequent
inspection stayed on the exact relevant files. No existing work was
discarded or shared infrastructure changed.

For the unchanged next target, (23) pays the exact Y versus Yhat
change with exact Z in both maps. Do not also charge that same change
through a separate triangle estimate for g and R^-1 Lg. The saved
locator still needs exact-Z conversion, head-solve, entry and FFT
errors, and the complete local/T/inverse input tail. The output565
and remote-input566 bounds retain their qualifications. A new FFT
accuracy theorem outside ready562 would require separate source
coverage. No refined inverse-output calculation was completed this
turn; the unfinished fixed-J decomposition in working566 remains the
continuation, now with the predictor error separated and paid.
