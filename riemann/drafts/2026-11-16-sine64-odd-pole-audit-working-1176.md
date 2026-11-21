# C750p audit checkpoint1176

Exact approved target and assessment: audit C750p on unchanged complex
QH; drafts/literature/2026-11-16-sine64-odd-pole-audit-1174.md,
separately approved1175. No source refresh or changed hypothesis.

Full C750p and C750m hypotheses/Sections1-2 read. Checked by hand:
linear-first inner product gives QBQ f=2<f,Qs>Qs; its norm is
2||Qs||^2 by Cauchy-Schwarz and the normalized Qs test. The pole
cross terms are purely imaginary and disappear after real part.
Odd-index basis functions are even; phi_(2k)=(-1)^k sin(k*pi*x/b)/sqrt(b).
Differentiation of the displayed antiderivative cancels both cross
terms. Endpoint numerator difference is -2 alpha*sinh(b/2)*(-1)^k;
the basis sign gives the stated negative coefficient. Squaring and
rescaling gives (3). Standard complete sine Parseval holds in L2,
without endpoint trace conditions. Exactly k=1,...,32 is removed.
All k>=33 are bounded by 1/k^2; comparison on [k-1,k] is strict,
with the first positive gap retained in the infinite sum.

The sinh identity uses e^b=sqrt101 and positivity, so replacing
sqrt101 by10 has the required direction. The positive degree8 exp
sum bounds log101, and the 64-term alternating arctan endpoint sum
is below pi/4 with next term 1/129. No analytic issue found.
Independent exact verification and replay are now complete:95 checks
pass, no failures, original certificate reproduced byte for byte.
Full audit and analytic justification are canonical in C750p; complete
arithmetic evidence is scripts/sine64/odd-pole-audit-1176.json.
The previously pending audit accepts the original bound with no repair.

Main gap and limitations unchanged: this can pay only one odd-pole
component; signed multiplier floor, head/coupling, all-support and
actual-Xi transfer remain open. Preserve C750m/n and1173 stops.
