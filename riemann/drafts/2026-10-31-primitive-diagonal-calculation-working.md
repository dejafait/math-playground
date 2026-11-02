# Primitive diagonal calculation — 31 October 2026

Invocation target: justify the primitive-pair regrouping of L233's first
associated kernel and determine the eventual Fourier sign of the full
diagonal (1,1) family. Prior gate: SPECIALIZE in
`literature/2026-10-31-primitive-diagonal-boundary-test.md`.

Main gap: actual-Xi all-degree positivity at unbounded heights. This
bounded specialization tests separate primitive-family positivity as a
sufficient mechanism for the first sign; higher degrees are independent.
Negative full diagonal spectrum stops that mechanism only. Nonnegative
tails would leave finite frequencies/other families; unsummable errors
would be inconclusive. Reused the parent source comparison and the full
L019/L233/L234/L356 proofs; no external source refresh is needed.

Saved partial reasoning before final proof assembly:

- Write B_nm(t)=integral s^2 k_n(s+t)k_m(s-t) ds. All summands are
  nonnegative. Under u=s+t,v=s-t, the double-integral mass majorant is
  (1/8) integral integral (u+v)^2 k(u)k(v) du dv < infinity. Unique gcd
  extraction partitions every ordered pair; retain both orientations
  when a<b, and only B_dd for the primitive diagonal.
- For F_n=Fourier(k_n), d_n=q_n'(0), obtain independent integral-based
  expansions F_n=-2d_n/x^2+r0_n, F_n'=4d_n/x^3+r1_n,
  F_n''=-12d_n/x^4+r2_n. L356's envelope controls the sum of boundary
  derivatives and weighted L1 derivative norms, so seek l1 sequences
  a,b,c with |r0_n|<=a_n/x^4, |r1_n|<=b_n/x^5,
  |r2_n|<=c_n/x^6 for all x>=1.
- Candidate summed coefficient: -2 sum_n d_n^2 / x^6. Do not replace
  sum of self-pair spectra by the spectrum of sum k_n. Need explicit
  error bound and a strictly positive sum before asserting negativity.

No numerical or finite-truncation sign is evidence for the infinite
family. Completed proof: `lemmas/L603-primitive-regrouping-negative-diagonal-fourier-tail.md`
(not yet independently audited). All three remainder sequences are
summable, the squared boundary coefficient is strictly positive, and
the full diagonal tail is negative. Canonical proof and constants live
only in L603; the initial notes above preserve the attempt's starting
reasoning. Separate-family positivity is stopped; total signs remain open.
