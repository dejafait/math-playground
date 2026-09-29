# Ample complete-intersection union: saved reasoning

The following interim notes were saved before completing the argument.
Their pending checks are resolved by the completion note below; they are
retained to distinguish the initial mechanism from its proved scope.

The saved SPECIALIZE target is unchanged. The main gap is a transverse RM
embedded lift beyond the three Dickson-family directions. Adding an ample
complete intersection could change the normal-pole problem while retaining
the action of C modulo divisor products. The test is an actual lift, or an
obstruction applying to a precisely stated degree regime; local smoothing
sections alone are insufficient.

Write f in H^0(I_C(nH)), g in H^0(O_X(mH)), m>n>0, and
J=I_(C union V(f,g)). Provided g is a nonzerodivisor on O_C and (f,g)
is a regular sequence, basic double linkage gives J=(f)+g I_C and

    0 -> O_X(-m-n) -> I_C(-m) direct sum O_X(-n) -> J -> 0.

This is the known construction reviewed in the saved assessment, not a
novel ideal identity. The working recovery mechanism is to lift this
extension from a lift of J, then lift the O_X(-n) summand inclusion and
take its flat quotient. Crucially, no component or filtration in the
initial lift is assumed to persist.

Checks still being completed: Ext^2(J,O_X(-m-n)) vanishes if
H^1(C,O_C(nH))=0, using Serre duality on the fourfold and the displayed
sequence twisted by m+n. The summand inclusion should then lift because
H^1(X,I_C((n-m)H))=0 and H^1(X,O_X)=0. A resulting sheaf lift of I_C
must be reconstructed as an embedded ideal, as in L012; this needs a
finite locally free resolution and determinant/Hartogs over the dual
numbers. Serre vanishing would supply the required positive-degree
hypothesis for sufficiently large n, not every n in the saved target.

An admissible smooth B and smooth D should be obtained by first choosing
large n and a general containing divisor with only finitely many bad
points on C, then choosing large m>n avoiding those points. This
applicability check is still pending. No transverse lift or complete
kernel claim has yet been established in this draft.

The expected scope, if the recovery works, is a negative result for the
sufficiently high-degree regime. It would not decide the existential
target at smaller n. The prior assessment already warns about this
quantifier distinction. The standard tools are imported; coverage of
the specialized recovery statement was not established in that review.

## Completion on 2026-09-27

[L018](../lemmas/L018-high-degree-complete-intersection-unions-retain-obstruction.md)
completes the recovery. The two required Ext vanishings lift the
basic-double-link extension and the line-summand inclusion, without
assuming either is preserved. The quotient is a flat sheaf lift of I_C;
a finite locally free resolution, determinant and two-layer Hartogs
recover its embedding. Bertini supplies smooth B and smooth ample D in
the stated high-degree regime, retaining the old singularities.

The resulting outcome is NEGATIVE for every admissible n with
H^1(C,O_C(nH))=0. With the additional H^1(I_C(nH)) vanishing the kernel
is exactly V_D. Both hold for all sufficiently large n; no effective
threshold was computed. This does not rule out the saved existential
target at smaller n. No mathematical script was needed: the relevant
checks are the two exact-sequence cohomology calculations, lifting of
the extension via derived restriction, and reconstruction of an actual
flat embedded ideal, all written out in L018.
