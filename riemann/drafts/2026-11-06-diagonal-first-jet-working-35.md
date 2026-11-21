# Diagonal first-jet diagnostic, step35 — work in progress

Approved target: Test the diagonal first-jet constraints forced by actual F's quadratic zero in L868's full C1 class for an additional restriction on A in K=A+H, beyond C868a's value-trace identities.

Prior coverage: drafts/literature/2026-11-06-actual-f-diagonal-first-jet-test.md (EXPLORE, supplied before invocation). Inputs read: L847 actual coefficient; L868 full C1 system; C868a/b full relevant Fourier and mean proofs; retained diagonal/fixed-fiber ATTEMPTS stops. No new source review or scripts.

Provisional calculation, not yet canonical: compact logarithmic charts give |F|<=B*((x1-x2)^2+(y1-y2)^2). Hence q=r=0 and dq=dr=0 on the diagonal by coordinate difference quotients, with no C2 assumption. Closure gives h_xj=0 there. Thus h(s,s,v,v)=b(v)>=0 is independent of s; angular first derivatives are not individually forced to vanish.

Candidate bounded obstruction to the necessary-data reduction: set V=z1^2*(z1-z2)^2/z2^2, W=F*V=-C*G(z1)*G(z2)*(z1-z2)^4/z2^4. For real lambda and H>=0 set q-ir=lambda W, h=H. Holomorphic differentiation directly verifies both closure equations globally. W retains every F zero; all its first derivatives vanish on the diagonal. On the open set |lambda V|<1 containing the whole diagonal, actual domination holds. Mean W should be -C*a0^2: only z1^0 in (z1-z2)^4*G(z1) contributes z2^4*a0, then the z2 mean is a0. Thus A=-lambda*C*a0^2 arbitrary, with identical diagonal first jets at fixed H. This would demonstrate failure of the reduced necessary-data test, not failure of a full-class bound. For lambda!=0 domination fails on positive z1=t,z2=R with t large, since |lambda V|>1 and F!=0. Verify signs, mean and all cases before writing canonical proof.

Do not claim global feasibility, strict gain, RH, arbitrary-jet extension or independence of the original system. Required threshold remains K>=-|M|; the test can only locate missing information away from the diagonal. Next direction must not repeat this local mechanism without new global input.

Completed: the calculation, all parameter cases and the precise relaxation are written in canonical C868c. The provisional calculation above is preserved as work history, not a second proof or an independent accepted input. Outcome NEGATIVE stops the local mechanism; independent audit is nominated separately.
