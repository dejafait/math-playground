# Fixed-input word-count optimization — working record

Approved target: Determine the maximal word-count cutoff obtainable by combining L041's r-dependent represented-length inequality with Simons–de Weger Corollary 2, using rigorous bounds and retaining primitive-to-represented counts.

The pre-invocation assessment is
`drafts/literature/2026-10-08-postspell-word-count-cutoff.md` (SPECIALIZE).
This is one REPRODUCTION calculation; no new literature is needed.
Universal eventual descent is the main gap. The downstream use is a
finite restriction on closed postspell itineraries, with entry,
unrestricted counts, other cycles and divergence still unresolved.

Work saved before certificate/proof preparation: the floating-point
preview suggests cutoff 12 if L041's positive cycle linear form is
retained, whereas the weaker K<N comparison stops at 11. No preview
is proof. Let T=225640000 and C=3T/2=338460000. Positivity gives
N>(3/2)K>C using 3^2>2^3. At r=12, log C<20 and log12<3 would
give A(12)log C+B(12)<(8334/5)Q_12+828/1034<C.
Also A(12)<C. Monotonicity in r and in real length would exclude
all 3<=r<=12. These exact comparisons remain to be certified.

For the limitation test, the proposed scalar counts at r=13 are
K=225640001, L=131990940, N=357630941 and d=1. They can use
J_0=4, J_i=2 (i>0), H_0=225639881, H_i=3 (i>0),
a_0=131990888, a_i=2 (i>0). The preview linear form is about
0.5214656; rigorous logarithm enclosures must establish its positivity
and the L041 bound 23r/517. The scalar length inequality can be
verified using log N>17 and 17A(13)>N. This is a test of the
fixed scalar comparisons, not a parity realization or a cycle.

Continue if the exact inequalities and integer restrictions certify
12 and a feasible scalar tuple at 13; otherwise report the failed
comparison and preserve the evidence. Attempt 019's guard failure
and history 069's minimum-count mismatch remain intact. Full proofs
will be canonical; the calculation certificate will record exact
rational bounds rather than rounded previews.

Completed: L043 gives the exclusion for 3<=r<=12 and certifies the
r=13 scalar limitation, with the precise retained restrictions stated
in its Conclusion. The full proof is canonical in
`lemmas/L043-postspell-word-count-cutoff.md`; the exact certificate is
`scripts/postspell-word-count/cutoff-certificate.json`, reproduced by
`python3 scripts/postspell-word-count/certify_cutoff.py`. All 23 checks
passed. Complete selected r12/r13 certificate values were inspected,
including exact margins and the linear-form interval; no preview
was used as evidence. The r12 conservative margin exceeds 54971760;
the r13 certificate proves 1/2<Lambda<53/100<299/517. The analytic
monotonicity proof supplies the global exclusion. The preserved early
preview above is working history, not a separate proof or claim.

ADVANCE, RESEARCH/REPRODUCTION, actual task calculation: local fixed-input
optimization and restricted application, without claiming a new general
cycle theorem or progress beyond the sources checked. L041 is the sole
direct local input; L042's audited bridge is a method comparator because
L041 already supplies the all-r period argument. Separate critical
audit remains pending, as do every universal-target gap named above.
