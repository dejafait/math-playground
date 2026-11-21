# Fixed Fourier-deficit trace — working step802

Gate: unchanged SPECIALIZE assessment `literature/2026-11-13-weighted-fourier-deficit-trace-800.md`.
Target: Test whether the fixed positive Fourier-deficit trace on C759a's W is below 4-C-P_120-11/200, using weight (4-m(t))_+ and every omitted sine mode.

Main gap remains L030-L032/C032a actual-Xi mixed positivity. This target may pay C759a's shifted complementary prerequisite, leaving form-dual coupling, finite Schur sign, parity, simplicity and Xi realization unresolved. Continue only on a rigorous complete upper bound below the fixed threshold; a rigorous lower bound meeting the threshold stops this majorant. An inconclusive upper bound is no miss.

Inputs read: C759a Sections1-3,5-6; L744 scalar estimate(8); recorded C759b stop and assessment793. Existing unfinished work is preserved. No further literature review is needed for this fixed reproduction.

Attempt in progress: use m>=m_* globally and m(t)>=log(|t|/(2*pi))-2/t^2 for |t|>=1 to certify a deficit cutoff T<121*pi. Test the entire sine tail using C759a(8), with sin^2(t)<=1 and a monotonically increasing denominator majorant. An outward rectangle enclosure of the nonnegative weighted integrand may suffice without evaluating digamma or truncating sine modes. Pending: certify cutoff, all rectangle errors/normalizations, bounded positive compression and trace finiteness, and applicability of the resulting shifted lower form on the closed domain. No numerical value or sign is asserted yet.

Completion: the fixed majorant succeeds. Full proof/citations/qualifications are canonical in C759c; complete arithmetic is in `scripts/spectral-triples/weighted-fourier-deficit-802.py` and `.json`. The original pending notes above preserve the precomputation reasoning rather than assert a second proof. The bound is local and unaudited; the separately nominated audit has REVIEW_REQUIRED coverage.
