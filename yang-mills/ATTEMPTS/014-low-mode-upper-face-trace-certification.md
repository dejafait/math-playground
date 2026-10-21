# Low-mode/global-norm certification of the upper-face trace

WHY IT FAILS: The signed-response verification in
[L029](../lemmas/L029-upper-face-axial-action-loop.md) retains all six
channels and evaluates a 36-mode deterministic partial trace, but
the omitted heat-trace norm bound exceeds its values by about 19–21
orders of magnitude. The retained heat-trace fraction is below 0.001
at both admitted meshes. Thus this partial sum and global operator
bounds do not certify a sign or cancellation. Full-mode sampled HH
dominance is only diagnostic; it cannot repair the deterministic
tail certificate. Stop this particular low-mode/global-norm shortcut.
The exact zero-axial-mode kernel and signed residual consistency give
a different mechanism to test; improved deterministic contraction
algorithms remain possible. No signed asymptotic or full-response
obstruction is proved.
