# PF2 adjacent-ray propagation stop

The single approved degree-five ansatz passes its exact obstruction test:
[L837](../lemmas/L837-degree-five-pf2-adjacent-shift-countermodel.md)
uses P=(1+4z)(1+3z)(1+2z)(1+z+z^2). The full rational certificate is
`scripts/fixed-shift-overlap/adjacent-degree-five-exact.json`.
This is a known-method specialization. The separate independent audit
passed on 6 November 2026; its full reasoning and certificate references
are recorded in the canonical L837 proof.

WHY IT FAILS: the proposed generic bridge from PF2 and an eventual
positive shift3 ray to eventual shift4 nonnegativity is false. The
exact Widom expansion has one positive dominant triple, but two
conjugate dominant quadruples with a strictly negative period-six
residue; the canonical proof controls every remaining term uniformly.
This blocks that precise abstract inference. It does not block a
bridge requiring much higher finite PF order, stronger overlap or
additional actual-Xi structure. Preserve those independent gaps and
the earlier L772/step659/step667 stops. Repeating finite samples or
renaming this same PF2 bridge supplies no new test.
