# Approved odd-carrier test — working record, step798

Completed13 November2026: the partial calculation below was verified
and superseded by the full canonical proof in
`lemmas/C759b-odd-carrier-joint-arithmetic-bound-stop.md`.
Its rational certificate is
`scripts/spectral-triples/odd-carrier-scalar-798.json`.
The historical provisional wording below records the pre-check state;
it is not the current proof or a pending task. Separate review remains
pending in the current checkpoint.

The exact target and SPECIALIZE coverage are in
`drafts/literature/2026-11-13-odd-carrier-prime-bound-test-796.md`,
saved before this invocation and separately approved in step797.
Only the fixed constant-envelope family is being tested.

Inputs read: C759a Sections1-4 (fixed W, weighted Fourier form domain,
zero extension), L743 Sections1-2 (bounded arithmetic form and
arbitrarily large finite-list phase returns), L744(6) (negative
arithmetic sign). Comparison795 and the neutral-prime-only stop were
reused; the complex cell-neutral equality is not applied to W.

Partial reasoning, awaiting complete verification: for
g_t(x)=sin(tx)/sqrt2 on(-1,1), its norm squared is
1/2-sin(2t)/(4t). Its jth sine coefficient for t>120*pi is
sqrt2*(-1)^j*j*pi*sin(t)/(t^2-j^2*pi^2). Thus exact finite
projection preserves odd parity and has vanishing L2 norm.
Direct product integration on(-1,1-a) gives
C_g(a)=((2-a)*cos(ta)-sin((2-a)*t)/t)/4.
Along L743's simultaneous returns for log2,log3,log4,log5,log7,
the proposed normalized limit is sum a_n*(2-log n), with
a_4=log2/2. Its strict comparison and weighted-domain justification
are not yet certified here. No full-Q sign or bounded energy follows.

Continuation/abandonment test: finish this one limit and rigorous
scalar comparison; >3/2 rejects only the proposed arithmetic upper
coefficient on W. Otherwise stop this family. No envelope/cutoff search.
