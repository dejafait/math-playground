# Fixed signed actual-residual quadrature ends inconclusively

9 November2026, step106. Assessment104's fixed4096-node test was executed
with the original precision200, kernel, polynomial, full epsilon and
response prefix. Canonical result and qualifications:
[L953](../lemmas/L953-fixed-actual-residual-quadrature-endpoint-stop.md).

WHY IT FAILS: all4096 signed evaluations and the analytic quadrature,
pointwise complement and full higher-replacement payments are retained,
but the achieved finite-sum radius is over101 times the polynomial
endpoint margin. The complete v(8) enclosure contains zero. A saved
node has a sharply enclosed actual residual but a wide zero-containing
response interval, illustrating finite evaluation overestimation.
The rule's tiny analytic error does not bound that evaluation width.
This is neither an actual-error lower bound nor a density-sign theorem.
End this fixed test without changing the evaluator, nodes, precision,
prefix, kernel or polynomial. Preserve L952's distinct norm-test stop
and the earlier coarse/integrated/saddle-onset evidence. This stop is
local to the fixed test, not a global ban on future new mechanisms.
