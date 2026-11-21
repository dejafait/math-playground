# Lower-power first-mode allowance: reproduction scope1633

TARGET: Reproduce Kawano v1's lower-power first-mode allowance T_low(p)<=2 L^(3/2)/r on C048c's full sector, with T_low the normalized finite horizontal integral defined in the assessment.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step1633's exact title/low-order and Kawano/Mellin/lower-power/B_low queries located the primary manuscript; scoped local Mellin searches found earlier exclusions rather than a matching proved bound. L799's full hypotheses and amplitude proof were compared; no automatic transfer. Search limits and preserved failures: 2026-11-19-mellin-lower-power-source-notes-1633.md. No novelty inference.
SOURCE_EVIDENCE: K. Kawano, Preprints.org202611.0383v1, posted4November2026, DOI10.20944/preprints202611.0383.v1, https://www.preprints.org/manuscript/202611.0383/v1 , Section5.2(28)/Lemma5.1(i)/reflection; AppendixA.2(A3); AppendixB local definitions/absorption/normalization and B_low display after B_g; AppendixC opening estimates and lower-power allowance between distant-left-tail and other local modes. Essential cases read19November2026; full extraction in source-notes1633. Reuse DLMF7.7.6 https://dlmf.nist.gov/7.7.E6 coverage from source-notes1630 and C048c.
COMPARISON: AppendixB's B_low=M[3W_*/(4r)]exp(2d)sqrt(mathcal A/b_*) is a local absolute allowance; AppendixC assigns2L^(3/2)/r at width1/(3L) on the saved sector. The operational T_low below isolates that same correction and normalization. C048c already proves local amplitude, absorbed curvature and branch premises; its conclusion and C048d exclude this correction. L799 has a different saddle/rotated contour/width and cannot supply the bound directly.
GAP: Write out the operational finite-integral majorization, correction-factor identity, real Gaussian integration with modulus normalization and uniform effective constant2. Source scope is assessed; no inequality or scalar comparison for T_low has yet been proved locally. Finite-band AppendixB cell data and width are not inputs for this sector.
REASON: Reproduction checks an unverified effective preprint component rather than discovering a new Gaussian method. Essential source cases are accessible and covered; the changed ready continuation requires separate next-turn approval before invocation. No further discovery search is needed while target and assumptions stay unchanged.
SCOPE: Only the negative lower-power n=1 finite horizontal contribution below; no full-path/full-theta estimate, zero count, inversion, sufficient mixed signs or RH claim. Full matching Mathlib coverage is unchecked.

## Exact target and permitted inputs

Let p be complex, r=|p|, L=log r>=12, Re p>=-r/(4L).
Use C048c's principal w=W_0(2p/pi), u_0=w/2, d=1/(3L),
h_p(u)=2p Log u-pi exp(2u), g(u)=8pi^2 exp(9u/2)/u,
K(s)=g(u_0+s)/g(u_0), A_0=4p(1+w)/w^2. With real s, set

    T_low(p)=|integral_(-d)^d K(s) [-3/(2pi exp(2(u_0+s)))]
                  exp(h_p(u_0+s)-h_p(u_0)) ds|
                  / |sqrt(pi/A_0)|.

The square root is principal; orientation is left to right. The exact
threshold is2L^(3/2)/r, not a relaxed full-remainder scale. C048c's
audited equations(3),(9)-(19) supply normalization, geometry, amplitude
and absorbed curvature. Its(19) uses b_*=(799/300)r/L^2>0;
its Lambert identity is pi exp(w)=2p/w. Its Gaussian paragraph supplies
the covered standard integral. If connection to the actual theta
kernel needs documentation, use C048a's actual-kernel normalization,
not an assumed full remainder. No cross-notebook input is involved.

## Bounded reproduction and decision test

Write a uniform analytic proof, or record a rigorous failure, of this
single source-claimed component. Check the exact negative first-mode
factor, all denominators, segment, normalization and conjugation.
Extend only a positive real majorant when using the full Gaussian;
do not replace a complex integral by an equal absolute integral.
Use C048c's established premises instead of reauditing them.
Verify the constant2 for all L>=12, including the base radius,
unbounded L, both sector boundaries and real p. A symbolic/rational
comparison suffices when available and does not require a new script.
Any useful certificate must retain complete evidence; a grid or
floating-point preview is not proof.

Continue if the local majorization yields the exact threshold on that
full domain. Preserve any failed sufficient majorant and distinguish
it from a counterexample to T_low. Stop at a rigorous unresolved
scope/constant obstruction rather than importing full(29) or widening
to other modes. A violating T_low refutes this allowance, not RH.

The main gap remains L030-L032/C032a actual-Xi all-degree algebraic-square
positivity. Success would pay another local first-mode term toward a
full actual-theta Mellin remainder. Higher modes, horizontal tails,
assembly, zero counts, inversion and a sufficient sign bridge remain
independent. ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md
preserves the global automatic-import stop; this target does not
reopen it. No new central signed mechanism or RH candidate follows.
This is established-method reproduction, not creative research or a
claimed beyond-source advance.

LITERATURE_REASON: Completed coverage for the changed lower-power target, whose essential source cases were unread at invocation1633. After separate approval, reuse it for the exact reproduction without renewed browsing absent changed hypotheses or evidence.
