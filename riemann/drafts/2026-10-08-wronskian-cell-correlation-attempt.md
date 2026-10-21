# Fixed response-cell correlation attempt — 2026-10-08

Completed: the full proof and qualifications are canonical in
[L383](../lemmas/L383-fixed-response-cell-correlation-positive.md).
The leading correlation is positive, so the fixed negative-correlation
diagnostic is stopped. The checkpoints below preserve the unfinished
reasoning as it stood during the attempt; they are superseded by that
complete proof, which still requires a separate critical audit.

Work in progress under the pre-existing EXPLORE assessment
`drafts/literature/2026-10-08-wronskian-cell-correlation-test.md`.
The exact target, shift and cutoff are unchanged. Main gap: global
actual-theta mixed positivity and the total L367 margin. The intermediate
test seeks a negative log-height-scale C_H; its downstream use would be
opposite Wronskian signs in one response cell. Independent positivity,
common-zero-count and zero-exclusion gaps remain.

Read L366's exact pair, L368's complete response bounds, L372's full
phase/count proof, L380's exact complex Wronskian identity, L381's full
finite-twist, tail and projection proof, and L382's pointwise envelope.
Reused the assessed primary inputs and the recorded first-mean and
response-cell comparisons. No new external theorem is assumed.

The bounded attempt first checks localization, then the two-height
projection and fixed cutoff harmonics. Continue only with a fully
dominated signed margin or a rigorous obstruction; stop if a retained
harmonic cannot be bounded at that scale. Do not change shift/cutoff.

Pending calculations: use Phi'=log(t/(2 pi))/2+O(1), so the prescribed
shift has phase increment pi/2+O(1/log H); the cutoff's pi/8 buffer
should make the same-cell indicator exact on its support. Incomplete
end cells have length O(1/log H), and L382's envelope should control
their contribution. Retain both C(t)conj(C(t+h)) and C(t)C(t+h).
No correlation value or harmonic estimate was assumed at this checkpoint.

## Working calculation, pending complete justification

Put ell=log H and r=e^(i phi)U real, so F_0=-Ar. The exact Wronskian is
|bZ|/(T^2 L) times (-r' cos Phi-r Phi' sin Phi+r a cos Phi), where
a=(log|bZ|)'. Thus the leading normalized two-height product uses
W=-(|Z|/(4 pi))[(r'/ell)cos Phi+(r/2)sin Phi]+an L2-small error.
The shift changes Phi by pi/2+O(1/ell).

For the zero cutoff harmonic the Young specialization predicts the
four |Z|^2-weighted Hardy jet correlations, divided by H ell, as
S times (2/pi, 2/pi^2, -2/pi^2, 1/(2 pi)-4/pi^3), ordered as
(r r_h, (r'/ell)r_h, r(r'_h/ell), (r'/ell)(r'_h/ell)). Here S is
L381 (15). These must be proved by holomorphic shifts, not by
differentiating a real error. Their product assembly predicts
S/(16 pi^2) times the phase average of
chi(x)[1/pi^2+4 sin(x)cos(x)/pi^3], which is strictly positive.

Potential complete control of nonzero harmonics: write E=e^(2i phi)
as the exact gamma ratio and K=e^(2i(Phi-phi))=bZ/(bar b bar Z).
For a Hardy pair the k-th harmonic has carrier E^(k+1) times two
positive-height zeta factors. For k<=-1 shift height downward by one;
both zeta factors then have real part 3/2 and E^(k+1) is bounded.
For k>=1 reflect both Hardy factors first, obtaining E^(k-1) times
two negative-height zeta factors, and shift upward by one. The right-line
Euler ratios stay on Re s>=3/2 in both rectangles. At the borderline
k=+/-1 the carrier cancels, so these terms are retained as O(1),
not discarded as oscillatory. Vertical edges use L381 (18)-(19).
Every fixed nonzero mode should therefore be o(ell); the uniform
Fourier remainder is handled by the jet L2 norms before its limit.
This is still one fixed diagnostic, with no changed shift/cutoff.
