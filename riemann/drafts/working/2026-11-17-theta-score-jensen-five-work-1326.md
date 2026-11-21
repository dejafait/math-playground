# Fixed actual-theta score Jensen test1326 — working checkpoint

Approved target: exactly the n=5 origin Jensen test in assessment1325.
Main gap remains L030-L032/C032a, actual all-degree algebraic-square positivity.
Inputs: L016/L019, with L020 only supplying transform relevance.
No RH, C031e-box or cross-notebook premise.

Plan: justify a complex series germ on |Im u|<pi/4; use
A(-u)=A(u)+sinh(u/2) and K=(2D^2-1/2)A to obtain K even.
K(0)>0 then supplies the local zero-valued logarithm.
Compute K derivatives through six by Q_0(v)=8v^2-12v,
Q_(j+1)=(1/2-2v)Q_j+2v Q_j', then sum Q_j(pi n^2)e^(-pi n^2).
Use exact rational intervals for pi and exp and a separate infinite tail.
The odd score has a1=-kappa2, a3=kappa4, a5=-kappa6.
J5=X(5a1+10a3 X^2+a5 X^4). No numerical preview is evidence.
A pass stops this fixed test and leaves global class/approximation and
all Xi signs open. A failure excludes only entire LP scores matching
these derivatives. Preserve certificate failures and don't extend degrees.

Completed: NONREAL_PAIR_CERTIFIED. Canonical proof is C019a; full exact
certificate is scripts/theta-score/jensen-five-1326.json. All seven tail
bounds are below 10^-60 and all sign/enclosure checks pass. This fixed
calculation stops here; the nominated continuation is a separate audit.
The attempted mpmath preview could not run (module unavailable); it
supplied no values or evidence. The successful computation uses only
the Python standard library and exact rational/integer bounds.
