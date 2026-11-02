# Offset periodic test: unfinished calculation

Approved scope: drafts/literature/2026-10-31-offset-periodic-bulk-clipped-threshold.md (EXPLORE), unchanged target.

Main gap is actual-Xi all-degree signs. Test only h=a+b cos(omega s), 0<b<a, 0<omega<=1/2. With A=a^2, r=b/a and x=omega^2, C(h)=A A(0)+(A r^2/2)A(omega). The clipped mean is
x A r [sqrt(1-r^2)-r acos(r)]/pi. The joint residual must lie in int_V C_I, not just be PSD. Continue only on a strict residual and mean >=1/288; uniform upper bound below threshold stops this family. L473 (6)--(9), L585 (1), L586 (3)--(11), L587 fixed dictionary are inputs; actual-Xi transfer and later probability assembly remain independent.

Elementary necessary same-height Hankel constraints allow an exploratory upper value about .00617 at the frequency endpoint, so do not decide the target. This was a diagnostic float grid, not proof. Next test uses exact lag-one constraints; preserve earlier wave/packet stops. No complete result yet.

## Completed outcome

The even same-height and even lag-one PSD diagnostics allowed values
above threshold; neither is a certificate. A full entry-space dual
function instead gives the uniform obstruction in canonical L588.
The first high-precision diagnostic failed because mpmath is unavailable;
no package was installed. Decimal-based diagnostics were only exploratory.

The canonical proof uses no numerical optimization: exact Fraction
arithmetic proves uniform Taylor error <11/5000<1/400 for the explicit
dual function; the full exact value was inspected. Then a^2<=4194/19649
and phasewise clipping gives mean <=2097/628768<1/288, gap 97/707364.
All proof details are in L588; the certificate/script preserve the full
finite computation. Abandon this family, pending separate critical audit.
No positive-cone sufficiency, L587 extension or Xi transfer was proved.
