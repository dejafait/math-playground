# Primitive remainder audit2091: checkpoint

Approved target: review2089, SPECIALIZE, unchanged GC13/GC18 finite-scale
reproduction for C034r's input. Main gap: actual-Xi mixed positivity.
No upper bound for either signed sector is being attempted.

The complete tagged primary proof GC12-GC18, lines11613-11717, was
retrieved through the web tool (shell DNS failed; source access itself
worked). The square has coefficient X^(-1/2)(ab)^(-1/4) outside the
divisor sum, not (ab)^(-1/2). The latter coefficient appears only after
the continuous substitution. Nonempty slots require max(a,b)<2min(a,b).

Working verification: with D(M)=2^omega(M), the square-divisor expansion
and the coprime floor count give |A_M(Y)-rho(M)Y|<=3D(M)sqrt(Y) for
every Y>0, retaining (k,M)=1. On alpha=X/(2min(a,b)), beta=X/max(a,b),
the weight v(t)=t^(-1/2)log(X/(ta))log(X/(tb)) satisfies
|v|<=Q^2 t^(-1/2), |v'|<=(Q^2/2+2Q)t^(-3/2).
Stieltjes summation on (alpha,beta] therefore costs at most
3D(ab)[2Q^2+(Q^2/2+2Q)Q]. Empty intervals contribute zero to both terms.
Completed in canonical C034u: the dyadic bound includes the singleton
and last partial block; the entire X>=1 range is covered. Constant
C_*=B_Q S_Q is explicit there. For the fixed bump the prescribed
eventual integer cutoff gives o(1), conditionally transferring to
the completed vector only if the separate GC6 energy premise holds.

No mathematical script, numerical claim, gamma-energy proof or
cumulative-energy bound. Actual task type proof_audit; REPRODUCTION.
The next invocation can independently replay the same approved target
against C034u; no changed scope or new literature assessment is needed.
