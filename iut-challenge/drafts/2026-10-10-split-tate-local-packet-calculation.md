# Split Tate packet calculation checkpoint

Approved target: compute the full N=H(E_q[7]), H=Q_3(zeta_60), q=3^30, and full rational 30-torsion. Use the supplied SPECIALIZE assessment.

Working calculation, not yet audited: Tate kernel classes are zeta_n^a q^(b/n). For n=7, Galois fixes all classes iff it fixes both zeta_7 and alpha=q^(1/7); the quotients have valuation zero, so cannot be nontrivial q-powers. Thus N=H(zeta_7,alpha). For n=30, mu_30 and q^(1/30)=3 lie in H, so all torsion is rational.

U_20 is unramified of degree 4; adjoining zeta_3 uses X^2+3X+3 Eisenstein. U_140 is unramified of degree 12 (orders 4 and 6); H(zeta_7)=U_140(zeta_3) has e=2,f=12. Over this base alpha has integer-normalized valuation 60/7, forcing relative ramification divisible by 7; polynomial degree bounds it by 7. Proposed N has e=14,f=12, degree 168 over Q_3 and 21 over H. Also alpha^4/3^17 is a seventh root of 3. Full canonical proof and exact source hypotheses remain to be written in L042; no global realization or IUT conclusion follows.

Prior stops ATTEMPTS/022,025,026 concern distinct fields and stay preserved. Continuation test: all local torsion/degree obligations must pass, then independent critical review; failure stops this packet. Remaining global F/F_0, prime-to-7 global degree, actual/native action/input, pilot and essentiality obligations are not supplied.

Completed this calculation in canonical L042. The working calculation above is preserved; the full proof is in lemmas/L042-split-tate-local-torsion-packet.md and remains pending independent critical audit.
