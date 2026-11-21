# Fixed exponential-momentum domain attempt, step160

Approved target: the exact TARGET in the unchanged step159-approved
assessment `literature/2026-11-09-hedenmalm-exponential-momentum-domain-test.md`.
Main gap: L030-L032/C032a actual-Xi mixed positivity. This attempt tests
only domain inclusion for the fixed form; symmetry remains independent.

Checkpoint before completing the estimates: write
W(z)=exp(z/2) sum P0(pi n^2 exp(2z)) exp(-pi n^2 exp(2z)),
P0(v)=2v^2-3v. For Re z>=0 and |Im z|<=1/4, set
R=pi exp(2 Re z), a=Re(pi exp(2z)); a>2 and R>3.
The n=1 term has modulus at least exp(Re z/2) R^2 exp(-a).
The relative remaining tail is at most
3 sum_(n>=2) n^4 exp(-2(n^2-1)); proposed bound 40/333<1/8.
Verify the entire geometric tail, then use analytic evenness on the
negative half-strip. This could remove the W-denominator obstruction.

For alpha=a0+ib with Xi(alpha)=0, L908(1), not its real-only norm
claims, supplies zero total transform. A contour rectangle with
superexponentially vanishing vertical sides should preserve this at
each horizontal height. The two horizontal primitives then give
|U_alpha(x+iy)| <= 4 pi^2 C_b exp(9|x|/2-c exp(2|x|)),
c=7pi/8 and C_b=integral_0^infinity
exp((|b|+9/2)s-c(exp(2s)-1)) ds < infinity.
If q=W'/W is bounded by 24pi exp(2|x|), the L-image has a uniform
integrable envelope of order exp(13|x|/2-c exp(2|x|)).
Finally a justified contour shift to y=1/8 would give
F(G(.-plus-i/8))(k)=exp(-k/8) F(G)(k); Plancherel then pays the
exact exp(-k/4) weight. All these claims remain working estimates
until the canonical full proof is written and checked.

Essential inputs: L906 defining series/inversion, L907 primitive/ODE,
L908(1) complex normalization; prior Teschl spectral/Fourier assessment.
L908 step154 and L909 are not mathematical inputs. No RH, simplicity,
zero indexing, symmetry, completion or cross-notebook input is assumed.
Continue only on a full bound for every complex zero; a suspected
singularity or an arbitrary nonzero parameter is not an exclusion.

Completed checkpoint: the estimates above close in canonical
[L910](../lemmas/L910-all-complex-zero-exponential-momentum-form-domain.md).
Its full proof includes the denominator bound, both complex primitive
tails, contour endpoints and exact weighted norm identity. The local
domain prerequisite passes; independent critical audit remains pending.
No symmetry calculation was undertaken. This draft preserves the
unfinished checkpoint, not an additional canonical proof.
