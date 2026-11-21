# Analytic cap test1876 — working checkpoint

Authorized target: assessment1875's exact three-width cap test, with no
scalar evaluator. Main gap remains L030-L032/C032a; even cap2 only supplies
one finite feasible input to C033w. Inputs read: C034j (including1874),
C034b (including1841), C034i's assembly and quantitative conclusion,
C033m's exact excision and rescaling, C033w's exact law/finite minimax,
source-notes1875/1797 and stops1798/1839/1843/1847/1866.

Unfinished reasoning: set x=k_1(sigma), y=k_2(sigma), with x strictly
decreasing. The real inverse theorem should give f=y composed with
x^{-1}, and f''=(x'y''-y'x'')/(x')^3>0. De Boor (44)-(45) then
turns a quantitative f'' bound and three x-spacings into det M.
Reverse node order must be retained. Normalize both nonconstant
columns by their values at width1 to avoid absolute transform losses.
The residual in these normalized coordinates is exp(B_P(j))-1;
C033m(3) expresses B_P using p_a(0), a in[7/6,5/4], so the full
Gaussian divisor permits an exponentially small upper allowance.
Relevant cofactors should use differences, not independent unit bounds.
No resulting bound or cap is yet claimed.

Potential unpaid point: global upper d_j proportional to S4 can be
derived from C034b's complete member formula, but turning width ratios
into numerical constants may need an explicit upper bound on S4. The
retained hypotheses state displacement zero through100 and a tail bound;
they do not yet supply an inspected numerical count through100. Do not
silently assume a remembered count. First test what follows from the
already available quantitative bounds. Stop if the comparison remains
unpaid or loses the cap; no claim of a genuine TV obstruction then.

All source-wide and finite-zero qualifications remain; no RH, spatial
profile positivity, global Sobolev premise or Xi realization is added.

Completed analytical comparison, to be written canonically in C034k:
the weighted Gaussian constant in C034b(7) improves from6 to2 by splitting
x at gamma/2 and3gamma/4. This gives d_j<20*j*S4. Put S=S4,
A=50*S*S8+S^3/5, alpha=1/(5*10^12), and normalize x,y at width1.
The intended fully justified bounds are

    |det M_normalized| > exp(-100*S)*A/512000,
    0<=B_P(j)<alpha*S,
    TV < 1+92160000*alpha*S*exp((100+alpha)*S)/(50*S8+S^2/5).

Using S8>15^-8, S<=1/100 makes the last excess <0.46656<1/2.
An explicit count N(100)<=100 would imply S<1/100 using gamma>14
and the inherited reciprocal-square tail. That finite count has NOT
been supplied or verified by this attempt. The quantitative comparison
is the partial result, pending independent audit; no actual cap or
feasible measure is claimed. Stop at that missing input, nominate its
source review, and do not add an unassessed zero-count theorem now.
