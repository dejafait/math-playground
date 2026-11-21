# Odd-kernel global-growth attempt1536

18 November 2026. Approved target: assessment1535's exact common
Paley-Wiener bound. Inputs read: C032j/k/m, finite stop1302,
source-ledgers1532/1535. No new source coverage is claimed.

Working reduction (not yet a completed proof at this checkpoint):
fix sigma=1 and a0=1/4. On w>=0,
2*K(w)=exp(-B(w^2))*(exp(2*O(w))-1).
A polynomial upper bound for |K(w)| would imply
O(w)<=D*(1+w^2), since B(s)<=B(1)*max(1,s).

Candidate discriminating calculation, to verify before use:
for a>a0, Gaussian integration and integration by parts should give

    L(a):=integral_0^infinity exp(-a*x)*O(sqrt(x)) dx
      =pi/(a*sqrt(4*a-1))*H(a/(4*a-1)).

The retained first-ordinate/counting inputs suggest every right
derivative of L tends to zero at a0. If q(x)=O(sqrt(x)) has the
above upper bound, h(x)=D*(1+x)-q(x)>=0. Monotone convergence
of all weighted moments of h at a0, then the exponential series,
would extend its Laplace integral below a0. This would make L
analytic at a0 with all derivatives zero, contradicting H>0.

Unpaid checks at this checkpoint: full infinite Gaussian sum/Fubini
domination including off-line shifts, exact constants, integration
by parts at infinity, all-order flatness, and the positive-moment
analytic extension. No finite zero truncation may replace H. This
tests only the direct transform growth condition and stops there;
signed-width uniqueness and the main actual-Xi signs remain open.

Completion1536: all listed interfaces were checked in the full proof
of C032o, `lemmas/C032o-odd-kernel-direct-compact-transform-growth-stop.md`.
The exact transform above is correct. A hypothetical polynomial bound
for K_1 gives h>=0; its exact boundary moments give exponential
integrability at a1=1/8, making L analytic across a0=1/4. Flatness
then contradicts its strict positivity. The direct growth condition
fails; no new script or finite-divisor approximation was needed.
This completes the bounded attempt; separate conceptual audit remains.
