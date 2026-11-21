# Fixed five-cell penalty attempt — step455

The supplied EXPLORE assessment `drafts/literature/2026-11-11-five-cell-moment-penalty-test-454.md` is the unchanged gate for this attempt. No source numerical certificate or RH-conditional input is used.

Main gap: L030–L032/C032a actual-Xi positivity. Intermediate target: a positive complete-energy margin on L743's U_5 via E_L+256||C u||², at ell=log(3)/2, L=5ell, a=L/2. A success supplies only a constrained single-window input; support propagation, moment complements and actual-Xi transfer remain open.

Fixed test: responses 0<=j<128; modes 0<=q<4096 in each parity; covariance prefix 4096<=q<16384, with the entire remaining complement paid. The ten moment representers are the unnormalized locally centered exponentials in the supplied assessment. No parameter retuning is authorized. A positive finite compression is insufficient. A rigorously negative direction of this fixed lower comparison may end the test before full matrix construction, without implying negative actual energy.

Inputs read: L743 (1)–(2), L744 (5)–(6), C744a (1)–(4). L740/L741 are inherited through L744's normalization. The unchanged primary analytic coverage is Li paper45 displayed v2 (9 November 2026), (2.1)–(2.5), Lemma3.1 and its full Green-kernel/monotone-convergence proof, and (4.3)–(5.5), https://rstation.ai/problems/riemann_hypothesis/papers/45 . Its numerical endpoint, source-specific constants and blocked supplement are not inputs. Existing prime-only and certificate-access stops were checked.

Pending specialization: translation to (-a,a), parity and complex moments; complete bounded physical operator including all prime powers, pole and penalty; positive full-complement floor; exact covariance including the penalty; and any sign certification. The first discriminating calculation will screen subspaces of the fixed 4096-mode retained block for a negative direction of the 128-response comparison. Such a screen is not evidence until enclosed rigorously. If the block survives, the paid Schur criterion still requires full tail control.

## Saved intermediate calculation

`scripts/five-cell-penalty/screen-455.py` assembled the complete 128-response lower comparison on the first 64 of the fixed 4096 modes. The float-only even and odd Rayleigh proposals are approximately -2.32885e-8 and -6.73108e-9. The screen includes all nine prime powers 2,3,4,5,7,8,9,11,13, the signed pole and all ten moments; its full vectors are in `scripts/five-cell-penalty/screen-455.json`. These are not sign certificates.

Next within this attempt: round the even vector to exact dyadic coefficients and evaluate its scalar form with outward Decimal interval arithmetic. The imported convergent digamma expansion permits a finite sum with a monotone-integral remainder, so no unverified special-function call is needed. If the scalar upper endpoint is negative, it refutes positive definiteness of the fixed retained matrix and therefore every paid Schur lower matrix beneath it. No covariance assembly would then be necessary. The source's omitted positive responses mean this would not refute the complete penalized energy or U_5 positivity.

## Completed attempt

The pending calculations above are preserved as working history. The exact dyadic even vector was enclosed with directed Decimal arithmetic and complete digamma-series tails. Its energy is in [-2.367700e-8,-2.288342e-8]; both infinite-complement diagonal floors are strictly positive. The retained matrix therefore cannot have a positive Schur lower matrix. Full proof, all formulas, precise source imports and qualifications are canonical in C744b; certificate: `scripts/five-cell-penalty/certificate-455.json`. No parameter was changed, no covariance was omitted from a positive claim, and no sign of the actual complete energy was inferred. The odd floating proposal remains uncertified. Outcome NEGATIVE; separate audit is pending. PROGRESS.md owns the sole current continuation.
