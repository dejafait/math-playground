# Pole-compensated identity working checkpoint — step433

Completed later in this step: the full derivation and qualifications
are canonical in C999h. The notes below preserve the unfinished
checkpoint; they are not a separate proof or a current Next action.

Approved target: review432's positive-w identity/residual on
[1,3/2] x [40,45]. This is one development attempt, not a sign test.

Use a=w/2, b(x)=x/2+log theta(exp(2x)), b0=b(0),
h_w(x)=exp(w*b(x))-2*cosh(a*x), H(w,t)=Z_Q(w,a+i*t).
Imported caseIII gives H=integral h_w(x)exp(i*t*x)dx.
Both subtractions are retained. C999g fixes the centering and branch.

Candidate algebra, to check before promoting:
partial_w h=b*h+r, r=2*b*cosh(a*x)-x*sinh(a*x).
For x>=0, r=x*exp(-a*x)+2*log(theta(exp(2x)))*cosh(a*x).
Theorem7.4/Proposition7.2 give b-b0=integral(1-cos(x*y))*M(y)/y^2 dy.
Thus H_w=b0*H+D H+Q, with D the positive symmetric difference
and Q=Fourier(r). Completion is c=-d/(2w), d=t^2+w^2/4.
G_w=(b0+w/(2d)-1/w)*G+c*D(G/c)+c*Q.

Remaining checks: uniform moments of h and its w derivative,
absolute Fubini for the paired generator, compensation conventions,
completion signs/factors, explicit Q and event residual. Use
w in [1/2,2] for a real neighborhood. Source canonical measure is
finite, even, absolutely continuous; no Gaussian atom is present.
No global positivity or event existence is assumed. Do not drop the
pairing before using G=G_t=0. Preserve stops427/429/430.
