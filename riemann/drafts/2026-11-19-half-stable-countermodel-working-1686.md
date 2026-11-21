# Half-stable countermodel attempt1686: interruption checkpoint

Research/REPRODUCTION under the unchanged SPECIALIZE assessment1685.
Exact target: its supplied TARGET, a single half-stable density with
all-fixed-order boundary minors and an exact negative global minor.
Main gap remains L030-L032/C032a; this only tests a generic bridge.

Promising exact identity, still being checked: set a=s^(1/4),
x_s=1/(2a^2), sigma_s=1/(2a^3), f_s(u)=exp(sqrt(s)-su)p(u),
and g_s(z)=sigma_s f_s(x_s+sigma_s z). For real z>-a, algebra gives

    g_s(z)=(2pi)^(-1/2)(1+z/a)^(-3/2)
           exp(-z^2/(2(1+z/a))).

The analytic extension on each fixed complex disk tends uniformly to
the standard normal density. Cauchy's formula would therefore give
every fixed derivative at zero, avoiding Fourier inversion entirely.
Need check density normalization, tilt/scale determinant congruence,
Gaussian Gram sign, whole boundary interval, and both Wronskian domains.

Prospective global witness: increasing x=(2,3), y=(0,1), giving
p(2)^2-p(1)p(3). Its ratio is (3/4)^(3/2) exp(1/12), expected <1;
prove this exactly rather than evaluate numerically. Import the law
and self-decomposability from Simon1302.0956v1 p2 and Section3.2.

Continue only if the same p satisfies every nominated premise. No
actual-Xi realization, entire reciprocal, or global log-concavity is
asserted. No mathematical script is needed. Earlier unfinished work
and the finite-Carleman stop remain preserved.

Completed: the exact identity, complex-disk convergence, determinant
congruences, interval transfer and negative witness all pass this
attempt. The complete proof is canonical in C028m; this checkpoint
preserves the partial reasoning rather than an outstanding task.
The new write-up still awaits a separate conceptual audit. No
numerical experiment or mathematical script was used.
