# Constant Appell identity audit1600: saved reasoning

Approved target: assessment1599, g=1,n=1,x=1 only. Mathematical audit in
progress; no actual-F or general corrected theorem is asserted.
Independent coefficient: [z]exp(z)=1. Put theta=X+iY(X),
Y=log(sin X/X), |X|<pi, and h(X)=1-X cot X+log(X/sin X).
For X>0, h'>0, h~X^2/2 near zero and h->infinity at pi;
tau=sqrt(h), theta(-tau)=-conjugate(theta(tau)). Thus Re theta'>0.
Potential decisive comparison: the complete paired omitted tail equals
(e/pi) integral_pi^infinity exp(-tau^2) X'(tau) d tau>0.
Must still write full orientation/connector and absolute-convergence proof,
then compare the independent coefficient, not assume (3.21).
Endpoint plan: truncate at Y=-R and X=+/-a_R. The integrand
f(theta)=exp(exp(i theta)-i theta) is entire and 2pi periodic;
vertical sides cancel. For large R the remaining horizontal connectors
lie at |X|>=pi/2 and have total modulus <=2pi exp(-R).
Near X=pi, delta=pi-X, X cot X<=-pi/(4delta), while
|Y'|=O(1/delta), giving an integrable full-curve majorant.
No quadrature or finite truncation can replace these checks.

Completed: all obligations above are discharged in canonical C028l.
The full-line value is 1; the finite-range value is 1-T with
0<T<exp(1-pi^2). No numerical estimate is used. The working reasoning
is retained as saved, rather than discarded or treated as a second proof.
