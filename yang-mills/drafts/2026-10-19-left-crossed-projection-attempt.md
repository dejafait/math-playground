# Local left crossed trace: projection attempt

Approved target: Establish an O(N^(5/2) log(eN)^2) bound for L100's complete left crossed trace R_L for both actual probes.
Reuse the prior EXPLORE assessment `literature/2026-10-19-left-crossed-quantitative-remainder.md`; this is a mathematical attempt, with no new literature turn. Main gap: interacting reflected comparison and continuum/infrared construction with finite positive mass. This intermediate projection error could support a later quantitative L011 assembly; independent component and interacting gaps remain.

Essential inputs: L088 L089 L090 L100 L226 L237 L238, with their exact relative spectra, full heat expansion, gh/hh order and endpoint/clover filters. L237 and L238 remain unaudited. No co-closed final trace estimate is transferred. The reviewed ATTEMPTS/029--032 prohibit only their specific commutation, fixed-mass substitution and separate absolute-moment shortcuts.

Set R=(Delta_E+epsilon)^(-1), D=Q_delta-Q=P-P_delta. L226(4)--(8),(10)--(11) supply gradient range, commuting spectral factors, ||D||_HS<=CN^2 delta^(3/4), and the unprojected derivative/collar estimate. Test both ||Omega R D||_HS and ||R Omega D||_HS against E=N delta^(3/4)epsilon^(-1/2)+sqrt(N log(eN)). Retain F by ||F||<=Ca^2 p and ||R||_HS<=CN^2 sqrt(log(eN)).

Exact grouped factors, using unnormalized Omega:
X_0=R Q Omega^T P, Y_0=R Q Omega Q;
X_delta=R Q_delta^2 Omega^T P_delta,
Y_delta=R Q_delta^2 Omega Q_delta;
A_0=P G-T sum H_av U C, A_delta=P_delta G-T sum H_av U C,
where G=aG0. The trace is a^-1 sum c Tr(X A Y). Q_delta^2=Q+D^2 because QD=DQ=0, not because Q_delta is idempotent.

Candidate telescoping: differences of X and Y cost E by the two composite bounds. A_delta-A_0=-DG; group X_delta D, using P_delta D=D P_delta, then the right-gradient composite bound. All other X/Y factors cost N and both A norms are bounded. Desired total error is CN^2 E, hence within N^(5/2)sqrt(log(eN)) at epsilon=N^-1, delta=N^(-4/3).

Continuation test: accept only after checking the complete finite products and every projection occurrence, including P inside A_loc, without restricting sources or commuting through Omega or G. An upper bound missing the target is a failed sufficient estimate, not signed growth. No complete local trace bound, finite-boundary transfer or solution candidate is established by this saved reasoning.

Completed: [L239](../lemmas/L239-left-crossed-ordered-projection-error.md)
proves the proposed uniform projection error. The middle projection
change fits the same budget through X_delta D; the two adjacent Q_delta
factors are retained using Q_delta^2=Q+D^2. Combining with L238 leaves
exactly L239(3) at the stated schedules. This is a partial REPRODUCTION,
not the complete local bound or an independent upstream audit. Continue
under the unchanged ready target; localization, freezing and relative
boundary transfer remain unresolved.
