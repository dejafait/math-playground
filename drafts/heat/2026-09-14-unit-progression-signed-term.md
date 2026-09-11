# Unit-progression signed term checkpoint

Date: 2026-09-14. Scope: the k=j=1 term in the L221 interior box.
Earlier changes are preserved; L222 is complete.

Plan: use layer integration of L220's exact f_m. For t in [A_m,B_m],
the inverse interval is [(m²+t+1)/(a(v+1)),(m²+t)/(av)].
The interior margin makes clipping redundant eventually. Its length
is positive since m²+t>v. Integrate its integer discrepancy as a
sawtooth difference, then use the periodic Bernoulli primitive to get
an exact four-endpoint expression. Check signs with rational tests.

Unproved at this checkpoint: any aggregate cancellation estimate.
Resume by proving the inverse-interval identity and its bounds, then
record the remaining aggregate endpoint-sum problem explicitly.

Completed as L223: exact integral and periodic-primitive identities proved;
1,260 rational tests pass, including 627 endpoint crossings. The aggregate
cancellation estimate remains unproved; no draft estimate was promoted.
