# Constant-100 local count: bounded specialization2113

Completed bounded attempt under the unchanged SPECIALIZE target in
`drafts/literature/2026-11-21-local-heat-count-review-2111.md`.
Main gap: L030-L032/C032a mixed positivity. This count could reduce
C488a's transport costs; it supplies neither all-height reality nor signs.

Read L019/L020/L058, L488's strip/normalization and cited tail input,
C488a through its global-count proof and nearby-count absorption,
and L135's entire recentered-Jensen obstruction. Reused source coverage;
reopened Polymath1904.12438v2 (6)-(11), Proposition9.1 and proof,
and (105). The October30 explicit-positive-time-tail source note warns
that the numerical estimates for 0<=y<=1 cannot be copied to 3<=y<=4.
No such extension is assumed here.

Attempt: center a Cauchy disk at u+3.5i, radius0.5, fully within the
published 0.7-comparison band. Quantify its logarithmic derivative and
the positive zero kernel. Test window covering and the t=0 endpoint.
Use C488a's existing global count to test the finite-height bridge.
The source onset is still unspecified; any numerical assignment needs
a proof. Success means the full saved domain at constant100; a tail
with an existential onset is only a restriction, never completion.

Initial calculation: for Q=H_t/B_t and |Q-1|<=delta<1 on this disk,
Cauchy gives |Q'/Q|<=2delta/(1-delta). At delta=0.7 this is14/3.
The explicit M_t logarithmic derivative and the positive Hadamard
kernel can then be bounded directly. Need all constants, closed-window
coverage, and a quantitative comparison of the finite-height count
before recording any result.

Completed reasoning is canonical in
`lemmas/C488b-local-heat-count-onset-reduction.md`. It pays the closed
endpoints directly with a positive-kernel integral, obtains the
finite sector |x|<=148r from half the symmetric global count, and
reduces the rest to |H_t/B_t-1|<=0.99 from horizontal coordinate29399
on 3<=Im z<=4. That comparison is unproved. The source's0.7 estimate
gives only an existential tail. The exact failed global comparison at
(x,r)=(40000,200) is C488b(14). No mathematical script or numerical
sampling was used; none would certify the unbounded remaining domain.
