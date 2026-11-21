# Fixed-band payment working checkpoint — step819

Approved target is assessment817's exact first-sine residual test. Main
gap remains L030-L032/C032a mixed positivity; parity, even sign/simplicity,
other windows and Xi realization remain independent. Inputs C759a/d/f and
L741 have been read in the relevant ranges; comparison816 and the local
primitive stops show no duplicate of this payment evaluation.

Plan: use g=-1-cos(pi*x), so Ps1=g/pi and h=3/pi^2. Compute
R=E(g)/3-E(s1), retaining both poles and all five prime powers. Use the
finite correlations in C759f; their simplification is to be checked in
the canonical calculation. Certify Fourier masses on [0,1] and [0,2]
with a complete compact quadrature error and Plancherel. Evaluate m(1),
m(2) through the assessed DLMF series with a proved remainder. Only
R-B at zero decides this test: positive stops the proposed bound;
nonpositive passes this input only; inconclusive stops without a sweep.

No full-domain covariance inequality or correction payment is assumed.
No actual-Q gamma integral or existing matrix certificate will be replayed.
The default Python environment has no mpmath; use audited local outward
Decimal arithmetic with explicit analytic remainders. A floating diagnostic
is not verification. Save full evidence under scripts/spectral-triples/.

Completed: C759g and `scripts/spectral-triples/fixed-band-payment-819.json`
certify 1.17039531<R-B<1.17043653 with all12 checks passing. The exact
fixed-band sufficient estimate is stopped. Canonical proof, complete
errors and limitations supersede this working plan; independent audit
is nominated in assessment819, subject to separate approval.
