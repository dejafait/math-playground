# Finite theta-domain diagnostic — work in progress, step143

Approved target and scope: the unchanged SPECIALIZE assessment
`literature/2026-11-08-hedenmalm-formal-inverse-domain-test.md`.
No H_finite membership or Mellin normalization is assumed.

Primary v1 (1.2.1)-(1.2.3) gives, with x=pi*n^2*t^2,
w(t)=t^(1/2) sum_{n>=1} (2*x^2-3*x) exp(-x), and w(1/t)=w(t).
Set delta=t*d/dt, D=-i*delta. The source kernel identity gives Lw=0.
For a well-defined prescription T(Lu)=-LDu on L(V), necessarily LDw=0.
At t=1 inversion gives delta*w=0, so LDw(1)=-delta^2*w(1).

Pending exact verification: the second derivative polynomial is
P2(x)=8*x^4-56*x^3+(165/2)*x^2-(75/4)*x.
Seek a rational bound delta^2*w(1)<-1/6. Bound its n=1 contribution
using 3<pi<22/7 and exp(-pi)>1/27; bound the full n>=2 upper tail
by 900*sum n^8/20^(n^2), using exp(3)>20.
At the time of this checkpoint these inequalities and differentiated
endpoint estimates still required their complete proofs; this working
note was not a certificate.

On failure retire only this V prescription. Keep positive metric,
H_finite domain, symmetry, closure and actual-Xi mixed positivity open.

Completed later in this step: canonical L906 proves the certified
failure, including every differentiated endpoint and tail estimate.
The replay script and complete certificate are under `scripts/hedenmalm/`.
This checkpoint is preserved as unfinished reasoning history;
the canonical lemma governs the completed result.
