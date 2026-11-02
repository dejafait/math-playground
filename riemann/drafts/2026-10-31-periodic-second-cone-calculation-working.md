# Periodic second-cone specialization: working checkpoint

Approved target: test L473's K for relative interiority in the actual
lag-one periodic second cone and eventual absorption of the fixed L585
carrier covariance. The invocation-start SPECIALIZE assessment is
`literature/2026-10-31-periodic-second-cone-interior.md`; it is unchanged.

Local inputs read: L473 (6)--(7), and L585 hypotheses/conclusion (1).
The saved occupation comparison and the L585 audit retain the fixed
packet, exact-law and absolute-budget stops. No duplicate second-cone
result was located in the targeted local search. No external source
refresh or mathematical script is needed for the assessed application.

Proposed proof, not yet a completed canonical result:
use v_(r,j)(u)=(iu)^j exp(iru) and A(u)=Re(v(u)v(u)*).
For u nonzero, sqrt(2) cos(us) has covariance A(u); at u=0 use
the constant path 1. Each entry of A is real analytic and even.
An annihilator on [-1/2,1/2] therefore annihilates all real frequencies,
so both spectral curves have the same linear span W.

K integrates A against Lebesgue measure on [-1/2,1/2]. On the actual
function space of restricted spectral entries this functional is
strictly positive on nonzero nonnegative functions. Apply the already
assessed Blekherman--Fialkow Corollary 2.2 in that function space,
transported to W. This should place K in the relative interior of the
finite spectral cone, not merely in its closure or in the PSD cone.

Outstanding verification before recording a result: give the ordinary
derivative/translation Parseval formula with absolute convergence;
identify the actual periodic cone (Bayer--Teichmann Corollary 2 can
compress the resulting integrable spectral measure); explicitly check
the dual-space identification; then apply a fixed interior ball to
K-R/ell uniformly for all sufficiently large real ell. R is finite,
with trace R bounded by L585's nonnumerical W. No quantitative onset,
probability normalization, fourth-error control, clipped mass or Xi
transfer is claimed. Arithmetic source qualifications persist.

Completed: the proposed proof passes these checks and is recorded in
`../lemmas/L586-periodic-second-cone-interiority-and-absorption.md`.
That canonical file contains all hypotheses, Fourier/zero-mode factors,
integrability, common-span and function-space identifications, precise
source citations and the eventual-ray bound. No numerical experiment
or new mathematical script was required. This working proposal is
retained as a checkpoint, not a second proof or a continuation record.
