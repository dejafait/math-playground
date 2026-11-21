# Prescribed prime97 pulse test — working1142

Authorized target: assessment1140, exact TARGET unchanged, EXPLORE before
invocation. Main gap: L030-L032/C032a actual-Xi all-degree positivity.
Only the prescribed real two-endpoint indicator is tested; no width or
allocation retuning. Inputs: C750f/C750g conventions, assessment1140's
Laptev-Weth domain coverage, Plancherel and elementary integration.

Put a=9/4, b=log101/2, r=(a/b)log97, w=2a-r, c=a-w/2.
The two intervals have length w and centers +/-c. Their displacement
is r=2c. Hence C_f(r)=w and the dilation gives C_(U_b f)(log97)=w.
Fourier transform: F(t)=4 sin(wt/2)cos(ct)/t, F(0)=2w.
Thus J=(16/pi) integral_0^infinity log(2+t)sin²(wt/2)cos²(ct)/t² dt.
The integrand is bounded at0; for t>=T>0 its integral is at most
(16/pi)[log(2+T)/T + (1/2)log(1+2/T)].
This upper tail retains all interference through a positive envelope.
Pending: exact activation arithmetic, directed finite integral,
complete error and tail enclosure, threshold comparison. No current
numerical result is evidence. Passing/inconclusive ends this one-pair
test and leaves the full complex allocation open.

Completed1142: all pending checks above are now recorded canonically
in lemmas/C750h-prescribed-prime97-pulse-full-energy-enclosure.md and
scripts/prime-collar/certificate-1142.json. The ratio is strictly
below1/8; this exact witness cannot refute the uniform allocation.
The prescribed test is closed, not pending a wider pulse search.
