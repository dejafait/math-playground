# One-upper-plaquette cubic pairs — working record

STEP_ID: YM-20261007-074-top-other-cubic-regression

Approved scope: unchanged SPECIALIZE assessment
`literature/2026-09-26-current-target.md`, for the exact saved combined
response. This is one bounded proof attempt within its cubic action term.
Main gap: the complete cutoff coefficient and interacting matching are
uncomputed. Intermediate target: retain every pair with exactly one upper
axial plaquette and reduce its conditional action product to a full-spectrum
transverse operator, keeping corrections from both quadratic observables.
Downstream use: test compensation of C057a before logarithmic extraction.
Continue on an exact covariance identity with uniform symbol control;
abandon action-only conditioning as a substitute for the actual cumulant.

Inputs inspected: L011's coefficient and cumulant convention; L048's
complete contraction; L049's global regression and derivative directions;
L026's exact forest lift; L050's boundary spectral operator. L019 constrains
the interpretation. C057a is the comparison, not an identity premise.
L028's consistency estimate does not control these undamped mixed pairs.
L048 and L049 do not compute this conditional mixed product. The recorded
ATTEMPTS/011–017 and histories 063–064/073 forbid loop locality, deleting
other plaquettes, or assuming a small defect. Ready source coverage is
reused; no new literature premise or bulk renormalization reproof is needed.

Saved before proof completion: put C=S_(3,top), D=S3-C. Interior axial
plaquettes have only two nonzero edges, so their cubic is zero. Conditional
on u, transverse mean links at axial level s are (s/N) T3 u. Their mean
circulation vanishes, and their quadratic BCH logarithm is expected to be
-(s/N)^2 D_(1,T) Q/2. The retained covariance of eta_top with a transverse
circulation is -g_N(N-1,s;Delta_T) D_(1,T)^T. This suggests
E[C D |u] = (1/4) sum_c <Q_perp^c, chi_N(Delta_T) Q_perp^c>,
chi_N(lambda)=lambda sum_(s=1)^(N-1) (s/N)^2 g_N(N-1,s;lambda).
The interval recurrence suggests 0<=b_N-chi_N<=2/N on the whole spectrum.
Signs, boundaries and all connected corrections still require checking.

No a^2 limit, actual-probe sign, cancellation, logarithm, finite matching,
reflected error <=c_box/2, continuum axioms or finite mass is assumed.

Completed: L058 proves the proposed conditional operator and, more
precisely, 1/N<=b_N-chi_N<=2/N over the entire spectrum. With the
actual rough product Q it obtains 2q_A/N<=2Z-M<=4q_A/N. It also retains
the exact mixed cumulant as kappa(f,r,M)+kappa(f,r,H-M)+E_mix, with
H=(1/2) sum Q_j mathcal D_j(S3-C) and explicit derivatives of f and r.
All non-upper plaquettes remain; their interior axial cubics are zero
by the forest's two-nonzero-edge structure, not by truncation.

The 46 exact checks and empty failures field in
`../scripts/combined-ward-response/top-other-cubic-certificate.json`
were inspected. The Gaussian surrogate has nonzero observable corrections
(-549/8 and 22761/16); its fluctuation cumulants happen to vanish. Neither
is an actual-box evaluation. The interval cases check exact rational
symbols; uniformity is established analytically. This is local
REPRODUCTION of standard finite Gaussian/spectral methods, not a result
beyond the inspected sources or an originality claim.

Continuation within unchanged approved response coverage: test the a^2
scale of L058's complete retained mixed cumulant, jointly with its
conditionally centered quartic and observable derivatives. Essential
inputs are L011, L019, L028, L048, L049, L050, L058 and C057a. No
negligibility of H-M or E_mix, signed-cumulant transfer of the pointwise
bound, covariance locality, separate forest invariance or compensation
is assumed. A useful continuation needs a full-spectrum bound or limit;
an action-only positive sign is insufficient. Other/other cubic pairs,
measure, insertion/flow jets, subleading powers/logarithms and all exact
Yang–Mills construction obligations remain open. Prior stops are preserved.
