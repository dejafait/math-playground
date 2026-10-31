# Explicit local circle count: bounded attempt

2026-10-30. Approved target and source scope are unchanged from
`drafts/literature/2026-10-30-explicit-local-circle-count-coverage.md`.
This is a quantitative reproduction/specialization, not a new mechanism.

Main gap: all-degree positivity for actual Xi and finite positive-time
collision exclusion. Intermediate target: the single real/simple zero
count at the stated phase centers, radius and closed time band. Its
plausible downstream use is an explicit tail after a separate exhaustion
argument. It leaves exhaustion, spatial edge transfer, finite collisions
and zero-time control unresolved.

Continuation test: prove a strict total boundary comparison, including
the reflected residual in one holomorphic normalization. If the error
does not beat the model, preserve the failed inequality; failure of a
coarse estimate would not refute the count.

## Reasoning checkpoint before canonical write-up

Write A(z)=M_t((1+iz)/2), B(z)=M_t((1-iz)/2), so G_t=log A-log B
with L491's fixed logarithms. This explicitly reconciles the opposite
s_+ conventions in L490 and L491. Both A and B are holomorphic and
nonzero near the closed disk. Use B throughout, not a modulus factor.

L490 gives |(H_t-A-B)/B|<d=153/10^6 for Im z>=0. At Im z<0,
conjugate the inequality at conjugate(z): conjugation swaps A and B,
so |(H_t-A-B)/B|<d*|A/B|. The ratio is exp(G_t).

Put L=log(X/(4*pi)), w=z-X, v=iLw/2. At an integer phase center,
L491 gives G_t=i(2*pi*n-pi)+v+epsilon, |epsilon|<5010/10^12.
For |w|<=1/L, |v|<=1/2; hence |exp(G_t)|<3. The one-normalization
residual is <3d. The model is F_0(w)=1-exp(v), and its gamma error
is <4*(5010/10^12). Their sum is <1/1000.

On the boundary |v|=1/2, the exponential series gives
|1-exp(v)|>=1/2-sum_(k>=2) (1/2)^k/k!>1/4.
The model's only disk zero is w=0 and is simple; its other zeros are
4*pi*k/L. Rouché counts multiplicity one, and conjugation in a disk
centered on the real axis forces the H_t zero real. Disk containment,
strict scalar bounds and the source hypotheses still need to be
written explicitly in the canonical proof. No conclusion is based on
finite sampling or a numerical evaluation of exp(10000).

## Completion

The attempt passes its stated comparison test. The complete proof,
exact constants, domain checks, multiplicity conclusion and source
qualifications are now canonical in
`lemmas/L492-explicit-local-circle-real-simple-count.md`. The preceding
checkpoint is preserved as unfinished reasoning from before that
write-up. No mathematical script was needed. The result awaits a
separate critical audit; the current route is recorded only in
PROGRESS.md.
