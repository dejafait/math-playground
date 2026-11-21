# Working calculation1596

Target is unchanged assessment1595; ready SPECIALIZE coverage reused, direct source URLs present. No new source work. Main gap is actual-Xi all-degree positivity and H_d=o(d); only this reference diagnostic is attempted.

Set c=sigma*cot(phi), r=sigma^2/(4*sin(phi)^2), so r>c^2/4. Imported monic recurrence gives Jacobi diagonal m-(n+lambda)c and beta_n=r*n*(n+2lambda-1). Norm expected h_n=r^n*n!*(2lambda)_n.

Finite trace calculation gives necessary/sufficient three-match equations:
 m-c*(lambda+(d-1)/2)=-b1,
 v=c^2*(d+1)/12+(2*r/3)*(d+3lambda-2),
 tau=c*r*(d+2lambda-1)/2.
Hence c>0. Write k=r/c^2>1/4 and V=(d+1)/12+(2*k/3)*(d+3lambda-2).
Then rho=tau^2/v^3=f(k,lambda)=k^2*(d+2lambda-1)^2/(4*V^3).
Candidate exact supremum for lambda>0,k>1/4:
 f< (d-1)^2/((d+1)*(d-2)^2), approached lambda->0 and k->(d+1)/(4*(d-2)).
For fixed k, d(log f)/d(lambda) has numerator d+1-2*k*(5*d+6lambda-1)<0 for d>=5. At lambda=0, derivative in k changes sign at k* above. Sufficiency below supremum by continuity and k->infinity; reconstruct signed sigma and angle, no boundary point admitted.

These statements are unfinished pending exact finite checks and full proof. If confirmed, eventual infeasibility stops before higher cost: supremum<=16/(9*(d+1)) for d>=5. No actual height lower bound follows. Sympy unavailable; use standard-library exact rational checks, with full certificate saved to disk. Existing unfinished work preserved.

Completion1596: The initial reasoning above is preserved as the pre-proof checkpoint. Full proof, exact feasibility converse, source qualifications and all-parameter stop are now canonical in C028k. The exact-check script completed with 224 passing rational checks and no failures; its certificate is scripts/affine-pollaczek/feasibility-1596.json. No higher coefficients or costs were computed. Independent audit is the single nominated continuation, not completed here.
