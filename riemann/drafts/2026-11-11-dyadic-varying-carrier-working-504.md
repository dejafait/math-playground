# Dyadic varying-carrier attempt — step504

Work in progress, 11 November 2026. The gate-approved target is exactly
the TARGET in `literature/2026-11-11-dyadic-varying-carrier-coercivity-502.md`.
No new source scope is being approved. Essential inputs are L744,
C744n and C744o's complete polarization; L745 is a scope comparison.

Main gap: L030-L032/C032a actual-Xi positivity. Seek the coefficient
floor E(sum c_j v_j)>=sum log(t_j)|c_j|^2/8 for t_j=2^j R and the
common K_R window. This could pay a finite high block; independent low
signs, non-neutral coverage and a general decomposition remain missing.
Continue if the complete normalized Gram/correction cost is uniform in
J and tends to zero relative to the floor. An uncontrolled J/K cost is
inconclusive failure of this mechanism; an admissible violating sequence
at unbounded R would refute the eventual target.

Retained source tools: finite Schur theorem G.3 (Montgomery--Vaughan),
Plancherel/Fourier differentiation, L744's global digamma bound and
C744n's K-independent correction and entire prime-power mass estimates.
The ready review already compared duplicates and carrier-span, joint-
energy, conditional spatial-summability and corrected-IMS stops; the
four ATTEMPTS records and exact L745 scope were read again narrowly.
None supplies the missing low-block sign or bans this finite trial test.

Current reasoning, not yet a result: put y_j=log(t_j), S=sum y_j|c_j|^2,
f_j=exp(it_j x)w_j, f=sum c_j f_j and h=sum c_j h_j. Bound the m and
positive W Gram matrices after division by sqrt(y_i y_j). For i<j,
d=t_j-t_i>=t_j/2. At each Fourier point r=max(|xi-t_i|,|xi-t_j|)
is at least d/2, and |xi|<=5r. The H2 Fourier weights may thus give a
uniform logarithmic overlap divided by d^2. The dyadic row sums must be
proved, including arbitrarily large j. Separately bound the unweighted
L2 Gram matrix for the full B_L operator payment.

Handle all corrections together using C744n's ||h_j||H2<=H/t_j^2 and
weighted coefficient Cauchy--Schwarz; sum t_j^-4/y_j is summable. A
paid W synthesis upper bound should then control Q_m(f,h) without a
factor J. Both moments of the actual corrected sum vanish exactly;
do not split and estimate poles of the uncorrected terms. All constants
must be independent of K_R,J and the varying profiles. No mathematical
script or numerical claim is planned. Full proof and threshold pending.

Completion: the reasoning above is preserved as a provisional snapshot.
The full proof, all constants and the eventual threshold are now in
C744p(1)-(16). Its full error tends to zero independently of J and the
profiles, attaining the nominated 1/8 floor. The proof is unaudited;
the sole continuation is the separately nominated conceptual audit.
