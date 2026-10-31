# Hardy-space residual source review: working checkpoint

Literature-only review of the exact TARGET in
`drafts/literature/2026-10-29-fixed-square-residual-hardy-l1-coverage.md`.
No mathematical attempt or new lemma is authorized in this turn.

Read L477 in full and the relevant L318/L319 statements and failure record.
The target is the complete real residual on [T,2T], with
M=floor(sqrt(T/(2pi))), both cosine sums, and actual theta. A positive
c T(log T)^3 absolute lower bound would reject the fixed square as a
little-o approximation; it would not disprove RH or the negative-mass
target. L477's separate critical audit remains outstanding.

Primary sources located and partly inspected:

- Helson, Studia Math. 176 (2006), 85--92: (2.10), pp. 89--90,
  gives the divisor-weighted coefficient bound for analytic functions
  on the infinite torus. Read Lemma 1 and the finite-variable iteration.
  Primary article accessible through the SciSpace PDF mirror; DOI access
  failed. No finite-height theorem was identified there.
- Bondarenko--Heap--Seip, arXiv:1405.6516v3 (9 January 2015):
  Theorem 2, (6), (11), pp. 3--8; finite Bohr lift uses Haar integration
  and the norm is an infinite-time mean. No simultaneous growing-length
  averaging rate is asserted by these statements.
- Jaming--Kellay--Saba, arXiv:2303.10919, Theorem 1.1(iii):
  fixed separated linear frequencies, normalized interval length >=72,
  coefficient lower bound with constant 1/122. Read the finite-interval
  auxiliary correlation, bounded-dual construction and the N-uniform
  correction in Remark 2.13. This theorem includes all terms of a fixed
  exponential polynomial, but states no chirped-phase extension.

Completed decision: the inspected tools do not directly supply a
full-residual lower bound. Do not replace the height interval by Haar
measure, discard the product sum, or freeze theta. Finish the exact
source comparison and record the scope mismatch; do not infer a bound
on E(T). A separate first audit of L477 is a concrete fallback using
the existing analytic input rather than another Hardy-source search.

Final source statements, qualifications and decision are recorded in
`drafts/literature/2026-10-29-fixed-square-residual-hardy-l1-coverage.md`.
This working checkpoint is preserved; no residual bound was derived.
